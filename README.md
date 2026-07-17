# write-chinese-standup

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validate](https://github.com/w88856678-rgb/write-chinese-standup/actions/workflows/validate.yml/badge.svg)](https://github.com/w88856678-rgb/write-chinese-standup/actions/workflows/validate.yml)

一个面向 Codex 的中文脱口秀写作 Skill：把真实生活素材逐步打磨成可表演、可排练、可持续迭代的中文脱口秀逐字稿。

它不是“随机生成几个段子”的提示词，而是一套完整创作流程：素材采访、角度发散、主编筛选、笑点加强、表演标记、整场编排和开放麦复盘。

## 能做什么

- 记录尚未成形的生活观察和喜剧点子
- 把真实事件展开成完整段子
- 对已有稿件做结构诊断和 punch-up
- 组合 3–10 分钟逐字稿，补转场与 callback
- 添加停顿、重读、角色切换、动作和等笑标记
- 估算稿件时长，建立长期创作工作区
- 根据真实开放麦记录提出下一轮单变量测试

## 安装

### 方法一：让 Codex 帮你安装

在 Codex 里新建一个任务，然后发送：

```text
请使用 $skill-installer 安装这个 GitHub 仓库中的 Skill：
https://github.com/w88856678-rgb/write-chinese-standup/tree/main/skills/write-chinese-standup
```

安装完成后，重新打开一个 Codex 任务即可使用。

### 方法二：下载发布包

1. 打开仓库右侧的 **Releases**。
2. 下载最新版的 `write-chinese-standup.zip`。
3. 解压后，把整个 `write-chinese-standup` 文件夹放进 `~/.codex/skills/`。
4. 重新启动 Codex。

最终路径应为：

```text
~/.codex/skills/write-chinese-standup/SKILL.md
```

## 快速使用

安装后可以直接说：

```text
使用 $write-chinese-standup，把我今天被外卖员反向安慰的经历写成一个 3 分钟段子。一次只问我一个问题。
```

也可以使用这些指令：

```text
使用 $write-chinese-standup，先帮我记录这个点子，不要急着写笑话。
```

```text
使用 $write-chinese-standup，诊断这份逐字稿最影响笑声的一个问题，然后给我可直接上台的修改版。
```

```text
使用 $write-chinese-standup，为这份稿子添加稀疏的停顿、重读、角色切换和等笑标记。
```

```text
使用 $write-chinese-standup，根据这次开放麦记录，区分观察、假设和下一场实验。
```

更多入门示例见 [examples/quick-start.md](examples/quick-start.md)。

## 创作流程

Skill 会用同一个宿主模型执行分工明确的多轮处理，不会伪装成多个相互独立的模型：

1. **素材采访员**：只找真实事件、原话、欲望、阻碍和边界。
2. **角度写手组**：使用不同喜剧机制生成至少三个方向。
3. **主编**：按真实、清晰、惊奇、作者声音、可演性和密度筛选。
4. **表演导演**：处理呼吸、停顿、角色、动作、重读和等笑。
5. **模拟观众**：只提出风险假设，不能代替真实观众反馈。

## 输出内容

完整段子通常包括：

- `创作判断`：核心前提、人物态度和选中的喜剧机制
- `可表演逐字稿`：自然口语化的完整脚本
- `备用笑点`：最多三个可替换 punchline 或 tag
- `下一次测试`：一个能在朗读或开放麦中验证的变量

## 是否需要大模型 API

在 Codex 内使用时不需要额外 API Key，Skill 会直接使用当前宿主模型。只有当你要把它做成独立网站、机器人、自动语音应用或批量生产工具时，才需要另外选择模型和申请 API。

请不要把 API Key、密码、Token 或真实隐私信息提交到本仓库。

## 目录结构

```text
skills/write-chinese-standup/
├── SKILL.md                    # 主工作流
├── agents/openai.yaml          # Codex 展示信息
├── assets/                     # 点子、段子、整场稿和复盘模板
├── references/                 # 创作方法、表演标记与授权审计
└── scripts/                    # 工作区初始化与时长估算工具
```

## 授权与来源

本项目采用 [MIT License](LICENSE)。Skill 的提示词、模板和脚本是重新设计的原创实现，没有复制参考仓库中的代码、示例段子或成段文案。

项目只吸收了明确许可来源的高层工作流思想和公开技术标准。`Rinko-O9/rinko-talkshow-skill` 因未检测到明确许可证，已明确排除，不复制、不改写、不打包其内容。完整记录见 [来源与授权审计](skills/write-chinese-standup/references/provenance.md)。

## 贡献

欢迎提交问题和改进建议。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，特别是其中的许可证清洁和原创性要求。
