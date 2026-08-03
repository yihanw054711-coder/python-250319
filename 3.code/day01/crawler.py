import os
import sys
import requests
import pandas as pd
import time

# -------------------------- 1. 配置参数 --------------------------
# 东方财富网 A股实时行情接口 (通过抓包分析获得)
# 参数说明: pn=页码, pz=每页数量, po=排序方式, np=是否复权, ut=用户令牌(固定值)
url = "https://68.push2.eastmoney.com/api/qt/clist/get"

params = {
    "pn": 1,
    "pz": 5000,  # 单次请求获取5000条，覆盖全部A股
    "po": 1,
    "np": 1,
    "ut": "bd1d9ddb04089700cf9c27f6f7426281c",
    "fltt": 2,
    "invt": 2,
    "fid": "f3",
    "fs": "m:0 t:6,m:0 t:13,m:0 t:80,m:1 t:2,m:1 t:23",  # A股筛选条件
    "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152",
    "_": int(time.time() * 1000)  # 时间戳，防止缓存
}

# 请求头：关键是 User-Agent，模拟 Chrome 浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://quote.eastmoney.com/"  # 来源页，部分网站会校验
}

# -------------------------- 2. 发送请求 --------------------------
# 禁用环境代理（避免系统或 CI 配置的代理导致 ProxyError）
for k in ("HTTP_PROXY","HTTPS_PROXY","http_proxy","https_proxy"):
    os.environ.pop(k, None)

try:
    print("正在从东方财富网获取实时数据...")
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    s = requests.Session()
    s.trust_env = False  # 不使用环境代理

    # 更完整的浏览器请求头，模拟真实浏览器
    headers_full = headers.copy()
    headers_full.update({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    })

    # 重试策略：对常见临时错误重试
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 502, 503, 504], allowed_methods=["GET"]) 
    adapter = HTTPAdapter(max_retries=retries)
    s.mount("https://", adapter)
    s.mount("http://", adapter)

    # 尝试原始 host，若被拒可尝试去掉前缀数字（CDN 节点）作为回退
    attempt_urls = [url]
    if "68.push2.eastmoney.com" in url:
        attempt_urls.append(url.replace("68.push2.eastmoney.com", "push2.eastmoney.com"))

    response = None
    data = None
    for u in attempt_urls:
        try:
            print(f"尝试 URL: {u}")
            response = s.get(u, params=params, headers=headers_full, timeout=10)
            print(f"HTTP {response.status_code} 返回，body 预览:\n{response.text[:500]}")
            response.raise_for_status()
            data = response.json()
            break
        except requests.exceptions.RequestException as e:
            print(f"URL {u} 请求失败: {e}")
            # 如果是 RemoteDisconnected，继续尝试下一个回退 host
            continue

    if data is None:
        # 所有尝试失败，抛出以进入上层 except 处理并退出非零码
        raise requests.exceptions.RequestException("所有尝试均失败，请检查网络、被封或接口变更")

    # -------------------------- 3. 解析数据 --------------------------
    # 提取核心数据列表
    stock_list = data["data"]["diff"]

    if not stock_list:
        print("未获取到股票数据，请检查接口是否失效。")
        exit()

    # 定义字段映射：将晦涩的 f1, f2 映射为中文列名（便于分析）
    field_map = {
        "f12": "股票代码",
        "f14": "股票名称",
        "f2": "最新价",
        "f3": "涨跌幅(%)",
        "f4": "涨跌额",
        "f5": "成交量(手)",
        "f6": "成交额(万)",
        "f7": "振幅(%)",
        "f8": "换手率(%)",
        "f9": "市盈率(TTM)",
        "f20": "总市值(万)",
        "f21": "流通市值(万)"
    }

    # 清洗数据：只保留需要的字段，并改名
    cleaned_data = []
    for stock in stock_list:
        row = {field_map.get(key, key): stock[key] for key in field_map.keys() if key in stock}
        cleaned_data.append(row)

    # -------------------------- 4. 保存与分析 --------------------------
    # 转换为 DataFrame (数据分析的标准格式)
    df = pd.DataFrame(cleaned_data)

    # 数据类型转换（将字符串转为数值型，方便后续计算）
    numeric_fields = ["最新价", "涨跌幅(%)", "成交额(万)", "市盈率(TTM)"]
    for field in numeric_fields:
        df[field] = pd.to_numeric(df[field], errors="coerce")

    # 保存为 CSV 文件
    filename = f"A股实时行情_马年春节_{time.strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")  # utf-8-sig 解决 Excel 乱码问题

    print(f"爬取成功！共获取 {len(df)} 只股票数据。")
    print(f"数据已保存至: {filename}")
    print("\n【涨幅前 5 名股票】:")
    print(df.sort_values(by="涨跌幅(%)", ascending=False).head()[["股票代码", "股票名称", "最新价", "涨跌幅(%)"]])

except requests.exceptions.RequestException as e:
    print(f"网络请求失败: {e}")
    sys.exit(1)
except KeyError as e:
    print(f"数据解析失败，可能接口已更新: {e}")
    sys.exit(1)
except Exception as e:
    print(f"程序异常: {e}")
    sys.exit(1)