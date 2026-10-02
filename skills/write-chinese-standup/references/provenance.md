# 来源与授权审计

本 Skill 的提示词、模板、练习和脚本均为原创实现，没有复制参考项目的代码、演员段子或成段文案。外部项目用于高层工作流与技术标准参考；公开节目目录、报道和采访只用于作品定位、事实核查与方法研究。

## 可采用的明确授权来源

| 来源 | 许可证/性质 | 本 Skill 采用的高层思想 |
|---|---|---|
| [SpencerRaw/hermes-comedy-writing](https://github.com/SpencerRaw/hermes-comedy-writing) | MIT | 从真实点子到段子、整场稿和开放麦复盘的生命周期 |
| [s-hong46/multi_agent_comedy_club](https://github.com/s-hong46/multi_agent_comedy_club) | MIT | 写手、评论家、观众反馈和跨轮记忆的角色分离 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | 独立应用版本可选的有状态 Agent 流程编排 |
| [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) | Apache-2.0（代码） | 可选中文 TTS、情绪和语速控制；模型权重需单独检查 |
| [W3C SSML 1.1](https://www.w3.org/TR/speech-synthesis11/) | W3C Recommendation | `break`、`emphasis`、`prosody` 等语音标记的标准语义 |
| [Multi-Agent Comedy Club paper](https://aclanthology.org/2026.findings-acl.145/) | ACL 论文 | 将模拟反馈视为假设、用真实观众评价验证改稿方向 |

## 明确排除

- `Rinko-O9/rinko-talkshow-skill`：仓库未检测到明确许可证，不复制、不改写、不打包其中的 `SKILL.md`、示例或专有表述。
- `Looking4OffSwitch/brads-show`：README 声称 MIT，但仓库根目录的 `LICENSE` 链接不存在；在许可证文件补齐前不作为可复用来源。

## 后续修改规则

1. 在引入任何外部文件、代码或成段文案前检查根目录许可证及具体文件头。
2. 区分代码许可证、模型权重许可证、数据集许可证和声音/肖像授权；一个开放不代表其余全部开放。
3. 复制 MIT 或 Apache-2.0 代码时保留所要求的版权与许可声明。
4. 对无许可证、仅公开可见或许可证冲突的来源，只允许独立实现通用概念，不保留表达、结构化示例或代码细节。

## 公开研究来源与代码复用分开处理

- 演员与市场来源分别保存在 [演员种子库](comedian-library.md) 和 [市场底稿](market-and-scenes.md)，逐条记录年份、入口、核查日期及访问限度。
- 链接官方目录、摘要事实并撰写原创分析，不要求新闻或作品采用开源许可证；但公开可访问不等于可复制、转载、下载或重新打包。
- 本仓库 MIT 许可证只适用于本仓库原创内容，不为外链作品、演员肖像、字幕、录音和报道授予任何权利。
- 不收集整场字幕、付费课程内容、盗录专场或未授权素材库。练习迁移一般机制，不复制原作品的独有场景与反转组合。
- 旧版技术参考记录不是本次市场研究的证据。后续实际采用任何外部代码或模型时，重新核验对应版本许可证。
