# write-chinese-standup

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validate](https://github.com/w88856678-rgb/write-chinese-standup/actions/workflows/validate.yml/badge.svg)](https://github.com/w88856678-rgb/write-chinese-standup/actions/workflows/validate.yml)

一个给 Codex 用的通用中文脱口秀创作助手。你可以交给它一段经历、一个生活观察或一份旧稿，让它陪你找角度、改笑点、组场、排练，再根据实际演出继续修改。

它也能根据你的稿子和表达特点推荐值得学习的演员，说明**哪里相似、哪里不同、看什么、练什么**。目标是帮你形成自己的表达，写出更自然、更能讲出口的作品。

## 能做什么

| 你现在遇到的问题 | 它会帮你做什么 |
|---|---|
| 有件事想说，但不知道哪里好笑 | 找出真实动作、欲望、反常细节与个人矛盾 |
| 有稿子，但像吐槽文章 | 修铺垫、落点、口语、人物对话和后续发展 |
| 不知道自己的风格，也不知道该看谁 | 从样本分析表达特点，推荐相似与互补的学习对象 |
| 同一段要上开放麦、年会或拍短视频 | 调整共同背景、开场、节奏和时长，保留素材核心 |
| 想从几个段子拼成一场 | 安排段落、转场、情绪与回扣，标出缺素材的部分 |
| 演完不知道怎么改 | 区分真实反应与猜测，为下一场设计一个可比较的变化 |
| 想长期积累 | 保存作者档案、点子、段子版本、演员研究和演出记录 |

一句改稿就改一句，不必先做长问卷。普通写稿不需要联网或额外 API Key；查询当前市场、最新作品与近期演出时才核实新资料。

## 相似演员推荐怎么用

直接给一段自己的稿，或者说明喜欢哪位演员的哪种表达：

```text
使用 $write-chinese-standup，根据下面这段稿子的视角、喜剧机制和语言特点，推荐两位相似演员和一位适合补短板的演员。给作品或访谈入口、相似点、差异和一项原创练习；没有表演视频就不要猜我的台风。
```

初始库有 **12 位演员**：鸟鸟、周奇墨、呼兰、徐志胜、何广智、付航、小鹿、刘旸、唐香玉、于祥宇、漆漆、房主任。库外演员可按需研究，初始名单不代表排名。

推荐会区分“这段稿有相近机制”“你喜欢的观看方向”和“适合练某项能力”。同样的职业、性别、地域或性格标签不等于风格相近；不会给出没有测量依据的相似度百分比。

资料核查日期为 **2026-10-02**，演员样本主要来自 2021–2025 年可核查的官方目录与访谈。仅有目录的条目是探索入口，不能冒充已看完表演后的分析；旧作品也不会被说成最新热度。详细依据见[演员种子库](skills/write-chinese-standup/references/comedian-library.md)。

## 面向不同中文演出场景

工作流覆盖开放麦、俱乐部拼盘、售票专场、综艺短 set、商演年会、短视频及地域语言适配。比如同一件职场小事，年会需要处理同事共享背景，公开拼盘需要让陌生观众听懂，短视频则要重新安排入口与停顿。

[市场与场景参考](skills/write-chinese-standup/references/market-and-scenes.md)纳入 2026 年 8 月的小剧场市场报道，保留来源、统计时间与适用范围，把事实和创作建议分开。初始资料偏大陆普通话市场；粤语、台湾或海外华语内容会另外查目标地区的样本。

## 安装

### 让 Codex 安装

在 Codex 中发送：

```text
请使用 $skill-installer 安装这个 GitHub 仓库中的 Skill：
https://github.com/w88856678-rgb/write-chinese-standup/tree/main/skills/write-chinese-standup
```

### 下载当前仓库包

下载 [dist/write-chinese-standup.zip](dist/write-chinese-standup.zip)，解压后把 `write-chinese-standup` 文件夹放到 `~/.codex/skills/`，然后重新打开 Codex 任务。最终路径为 `~/.codex/skills/write-chinese-standup/SKILL.md`。

更新已有安装时，先保留你对技能做的个人修改，再合并或替换。GitHub Releases 中的旧版本不会随仓库更新；需要当前内容请使用上面的仓库包。

## 快速使用

```text
使用 $write-chinese-standup，帮我记录一个生活观察，不急着写笑话。一次只问一个问题。
```

```text
使用 $write-chinese-standup，把下面的真实经历写成 3 分钟开放麦稿。直接给稿，新增设定集中说明。
```

```text
使用 $write-chinese-standup，找这份稿最影响效果的两个问题，保留我原来有效的句子，再给完整修改版。
```

```text
使用 $write-chinese-standup，把这段 5 分钟俱乐部稿改成 90 秒口播，保留前提和结尾，说明删了哪些支线。
```

```text
使用 $write-chinese-standup，根据这次演出记录做复盘，下次只改一个变量，告诉我应该观察什么。
```

更多完整任务见[使用示例](examples/quick-start.md)。

## 创作与训练如何衔接

先从已有素材识别作者视角与目标场景，再找到喜剧前提，选择适合的机制，完成逐字稿和朗读修改。用户需要找风格时才进入演员研究；有真实演出反馈后，再更新段子版本和作者档案。

通常交付一版完整可排练稿、必要的设定说明、最多三个备用笑点，以及下一次最值得测试的变化。不会因为套用了某种结构就承诺“炸场”。

用户要求保存时，可初始化写作工作区：

```bash
python3 skills/write-chinese-standup/scripts/init_standup_workspace.py ./my-standup
```

生成 `profile/`、`ideas/`、`bits/`、`sets/`、`open-mics/`、`studies/` 和 `_templates/`。重复运行保留已有模板和作品。跨聊天积累依靠这些真实文件，技能本身不会自动记住未保存的内容。

## 维护与验证

```bash
python3 scripts/build_distribution.py
python3 scripts/validate_repository.py
```

验证涵盖技能入口、内部链接、工作区模板及重复初始化的数据保留，并检查 ZIP 与当前源码逐字节一致。行为试用场景见[examples/behavior-checks.md](examples/behavior-checks.md)；自动验证不证明段子一定好笑。

## 授权与来源

原创指令、模板、练习和代码采用 [MIT License](LICENSE)。研究外部作品时保留链接与必要的事实说明，不复制演员段子、整场字幕或付费课程。外部作品仍归原权利人，仓库许可不覆盖外链内容。

历史工作流来源及新增研究资料的使用边界见[来源与授权](skills/write-chinese-standup/references/provenance.md)。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
