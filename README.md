# write-chinese-standup

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validate](https://github.com/w88856678-rgb/write-chinese-standup/actions/workflows/validate.yml/badge.svg)](https://github.com/w88856678-rgb/write-chinese-standup/actions/workflows/validate.yml)

这是一个给 Codex 用的中文脱口秀创作工具。你可以交给它一段真实经历、一个生活观察，或者一份还不满意的稿子。它会帮你找到更好笑的讲法，整理段子结构，修改笑点和节奏，最后写成能直接开口排练的逐字稿。

它会尊重你的真实经历和说话方式，不替你编故事，也不模仿某位演员。目标很简单：让段子更像你、更好懂，也更适合站在台上讲。

## 能做什么

- 从日常生活里找到值得讲的冲突、尴尬、误会和反差
- 通过提问补齐人物、场景、原话和动作，找到真正好笑的细节
- 把一个想法写成有铺垫、有笑点、有结尾的完整段子
- 修改现有稿件，指出哪里拖沓、哪里不好懂、哪里还能更好笑
- 把多个段子整理成 3–10 分钟演出稿，写好开场、转场、结尾和前后呼应
- 添加停顿、重读、人物切换、动作和等笑提示
- 根据开放麦的笑声、冷场和听不懂的位置，告诉你哪些保留、哪些重写、下次重点改哪里

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
使用 $write-chinese-standup，根据这次开放麦记录，告诉我哪些地方有效、哪些地方没讲清楚，以及下次最该改哪一处。
```

更多入门示例见 [examples/quick-start.md](examples/quick-start.md)。

## 它怎么帮你写

它通常会按下面的顺序陪你完成一段稿子：

1. **把事情问清楚**：找出人物、地点、原话、动作，以及你当时真正想要什么。
2. **寻找最好笑的讲法**：从反差、误会、夸张、类比和人物表演等方向里选择最适合你的角度。
3. **写成完整段子**：安排必要的铺垫，把笑点放到最有力的位置，并继续往后发展。
4. **像主编一样改稿**：删掉多余解释，缩短绕口的句子，让每一段都更清楚、更像你的口吻。
5. **准备上台**：补上停顿、重读、人物切换、动作和等笑提示。
6. **演完继续改**：根据真正的笑声、冷场和听众反应，判断哪里保留、哪里重写。

## 输出内容

你通常会拿到：

- 这一段最值得讲的冲突和角度
- 一版自然、顺口、可以直接排练的完整逐字稿
- 最多三个可以替换的备用笑点
- 一个明确的改稿建议，告诉你下次最值得先改哪里

## 要不要准备 API Key

在 Codex 里直接使用，不需要额外申请 API Key。只有当你想把它做成独立网站、机器人或自动语音应用时，才需要另外选择模型和申请 API。

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
