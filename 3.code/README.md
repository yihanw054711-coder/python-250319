# Python 学习笔记与练习 (python-250319)

学习代码与练习记录

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

本仓库记录我从零开始学习 Python 的完整历程，按天（day）组织，涵盖从基础语法到面向对象、异常处理、模块化的核心知识点。目标是打好编程基础，为进一步学习**数据结构与算法、机器学习、深度学习**做准备。

## 📚 学习进度

| 目录 | 主题 | 核心内容 |
|------|------|---------|
| `day01` | 环境与入门 | Python安装、第一个程序、爬虫初体验 |
| `day02` | 基础语法 | 变量、数据类型、类型转换、输入输出、运算符 |
| `day03` | 流程控制 | if/elif/else、match-case、while、三目运算符 |
| `day04` | 循环与容器(上) | for、break/continue、列表 |
| `day05` | 容器数据类型 | 字符串、元组、集合、字典 |
| `day06` | 函数 | 定义、参数、返回值、作用域 |
| `day07` | 函数进阶 | global/nonlocal、递归、匿名函数、文件操作 |
| `day08` | 面向对象基础 | 类、对象、属性、方法、特殊方法 |
| `day09` | 面向对象三大特性 | 封装、继承、多态、property |
| `day10` | 异常处理 | try-except-else-finally、raise、自定义异常 |
| `day11` | 模块与包 | import、from-import、模块搜索 |

## 🚀 运行方式

```bash
# 克隆仓库
git clone git@github.com:yihanw054711-coder/python-250319.git
cd python-250319

# 运行某个练习(以day08为例)
python3 day08/P05_Class_Demo.py
```

部分练习需要第三方库：

```bash
pip install requests pandas   # day01爬虫等用到
```

## 🗂️ 项目结构

```
python-250319/
├── day01/ ~ day11/    # 按天组织的学习代码
│   ├── PXX_*.py           # 各知识点练习
│   └── readme.txt         # 当天笔记
├── main.py            # 入口示例
├── README.md          # 本文件
├── LICENSE            # MIT 许可证
└── .gitignore
```

## 🎯 学习目标

- [x] Python 基础语法
- [x] 面向对象编程
- [x] 异常处理
- [x] 模块与包
- [ ] 数据结构与算法
- [ ] NumPy & Pandas
- [ ] 机器学习 / 深度学习

## 📖 学习资料

- 尚硅谷大模型技术之 Python 课程（教程文档因体积与版权原因未包含在仓库中）

## 🤝 贡献

这是个人学习仓库，欢迎交流建议，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源。

---

*持续学习中 · Learning in progress* 🌱
