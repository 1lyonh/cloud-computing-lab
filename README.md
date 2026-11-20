# cloud-computing-lab

云计算课程实验仓库，用于练习 Git 与 GitHub 的完整开发流程。

## 关于我

- 姓名：linyuhan
- GitHub：[@1lyonh](https://github.com/1lyonh)
- 邮箱：3246137540@qq.com
- 方向：计算机相关专业，目前正在学习云计算技术
- 兴趣：Linux 运维、云服务器、Python 自动化脚本

## 仓库内容

| 文件 | 说明 |
| --- | --- |
| `README.md` | 仓库说明与个人介绍 |
| `cloud_cost.py` | 简单的云服务器成本估算程序（Python 3） |
| `.gitignore` | 忽略 Python 运行时产生的缓存文件 |

## 程序说明

`cloud_cost.py` 是一个不需要任何第三方依赖的 Python 命令行小工具，
根据云服务器的 CPU/内存规格、实例数量和购买时长，估算需要花费的金额。

```bash
python cloud_cost.py
```

运行后会按提示输入规格编号、实例数量和购买月数，程序输出每月费用与总费用。

## 学习目标

1. 掌握 `git init / add / commit / log / status / remote / push` 等基本命令；
2. 学会在 GitHub 上创建远程仓库并关联本地仓库；
3. 体验“修改代码 → 提交更改 → 推送到远程”的完整开发流程。
