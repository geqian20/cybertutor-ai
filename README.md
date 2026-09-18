# CyberTutor AI

基于 Claude API 的轻量级命令行网络安全 AI 助手。

使用 Python 和 Anthropic SDK，将终端输入的问题发送给模型，再显示文本回答。系统提示词将模型设定为网络安全助教，适合学习大模型 API 调用与基础命令行交互。

## 当前功能

- 终端交互式问答。
- 使用 `.env` 配置 API Key、API 地址和模型名称。
- 网络安全助教系统提示词，可在 `test2.py` 中修改。
- 捕获请求异常并显示错误提示。
- 输入 `exit` 退出，支持大小写及首尾空格。

目前每次请求只发送当前问题，不保留多轮上下文；尚未实现工具调用、自动执行任务或知识库检索。每次响应最多生成 1024 tokens，目前仅显示首个文本内容块。

## 文件结构

```text
cybertutor-ai/
├── test2.py          # 命令行程序
├── README.md        # 项目说明
├── requirements.txt # Python 依赖
├── .gitignore       # 排除密钥、虚拟环境和缓存
└── .env.example     # 配置模板，不含真实密钥
```

## 快速开始（macOS / Linux）

在项目目录中执行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

用文本编辑器打开 `.env`，填写：

| 配置 | 说明 |
| --- | --- |
| `AI_API_KEY` | 你自己的 API 密钥 |
| `AI_BASE_URL` | Anthropic API 地址，或服务商提供的 Anthropic Messages 兼容地址 |
| `AI_MODEL_NAME` | 你的账户可调用的模型名称；模板值需要替换 |

然后启动：

```bash
python test2.py
```

示例：

```text
你: 什么是 SQL 注入？如何防范？
正在思考中...
AI: （模型返回的回答）
你: exit
再见！
```

## 配置与常见问题

- `.env` 仅保存在本地，已被 `.gitignore` 排除。仓库只提供占位配置 `.env.example`。
- `python-dotenv` 默认不会覆盖已存在的同名环境变量；修改 `.env` 后仍使用旧配置时，请检查终端环境变量。
- 启动时提示缺少密钥：确认已创建 `.env` 并填写 `AI_API_KEY`。客户端在请求异常处理之前初始化，配置错误可能直接中止启动。
- 身份验证、模型不存在或连接失败：检查密钥、账户可用模型及 API 地址。API 调用可能产生服务商费用。
- 程序会显示异常详情，分享错误截图或日志前请检查是否包含敏感信息。

## 原文件与发布调整

本项目来自本地 `test2.py`，保留原文件名及主要实现。发布副本将退出判断 `question.lower == "exit"` 修复为 `question.strip().lower() == "exit"`，解决漏调用方法导致无法退出的问题。

原始本地文件未修改，同目录的真实 `.env` 未复制、未提交。新增本说明、依赖清单、忽略规则及配置模板。

## 后续可扩展方向

多轮对话、流式输出、配置校验以及工具调用。
