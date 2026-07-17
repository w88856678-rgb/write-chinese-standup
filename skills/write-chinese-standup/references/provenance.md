# 来源与授权审计

本 Skill 的提示词、模板和脚本均为重新设计的原创实现，没有复制下列项目的代码、示例段子或成段文案。外部项目只用于验证高层工作流、Agent 分工和公开技术标准。

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
