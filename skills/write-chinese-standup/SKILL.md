---
name: write-chinese-standup
description: Create, expand, edit, assemble, rehearse, and retrospect Chinese stand-up comedy material. Use when Codex is asked to capture a comedy premise, turn a real-life observation into a bit, punch up jokes, review comedic structure, write a 3–10 minute Chinese stand-up script, add performance or TTS cues, build callbacks, or analyze open-mic feedback.
---

# 中文脱口秀写作

## Operating contract

- Treat the user as the author and preserve their lived experience, vocabulary, boundaries, and stage persona.
- Prefer specific events, actions, dialogue, and sensory details over abstract opinions or motivational conclusions.
- Never invent autobiographical facts. Mark hypothetical material explicitly and ask for confirmation before presenting it as the user's experience.
- In guided mode, ask exactly one high-leverage question at a time. In quick-draft mode, state compact assumptions and produce a usable draft immediately.
- Default to Chinese. Keep spoken lines natural enough to say aloud in one breath.
- Do not imitate a named comedian's distinctive voice. Translate references into high-level traits such as restrained, absurd, observational, aggressive, or self-deprecating.
- Use the current host model. Do not request a separate model API key unless the user explicitly asks for a standalone app or deployment.
- Keep this skill license-clean. Before importing or adapting external material, read [references/provenance.md](references/provenance.md) and verify that the source has an explicit compatible license.

## Route the request

- **记点子**: Capture the incident, attitude, surprising detail, and possible comic tension. Do not force a finished joke.
- **展开段子**: Run the guided development workflow and create a complete bit.
- **快速成稿**: Draft from available facts with clearly stated assumptions and minimal questions.
- **审稿/加强笑点**: Diagnose first, then patch weak lines while preserving the author's voice.
- **出逐字稿/拼专场**: Arrange several bits into a coherent set with an opening, transitions, callbacks, and ending.
- **加表演标记/TTS**: Add human-readable performance cues; generate SSML only when a target TTS provider is known to support it.
- **复盘开放麦**: Separate observed audience response from guesses, then propose one-variable tests for the next performance.

## Use role-separated passes

Run distinct passes even when one host model performs all roles. Do not pretend they are statistically independent agents; the separation exists to reduce premature convergence.

1. **素材采访员** extracts real events, exact wording, stakes, and boundaries without trying to be funny.
2. **角度写手组** creates at least three materially different approaches using different comic engines, not three paraphrases.
3. **主编** selects or combines candidates using clarity, surprise, author voice, and stageability; it must be allowed to reject all candidates.
4. **表演导演** edits breath length, role changes, physical action, emphasis, and laugh holds after the text works on the page.
5. **模拟观众** predicts confusion, offense, and likely laugh points only as hypotheses. Never present simulated reaction as evidence; replace it with real rehearsal or open-mic data as soon as available.

Hide discarded drafts by default. Show role outputs only when the user asks to compare approaches or audit the process.

## Develop a bit

1. **Set the brief.** Establish the intended audience, target duration, real incident, stage persona, and off-limit areas. Ask only for the missing fact that most changes the material.
2. **Find the truth anchor.** Identify what the user wanted, what blocked them, what they actually did, and the most emotionally charged or embarrassing detail.
3. **State the comic premise.** Write one internal sentence in the form “我原以为 X，结果 Y；最荒唐的是 Z.” Use it as a compass, not necessarily as a spoken line.
4. **Generate angles.** Read [references/craft.md](references/craft.md). Explore at least three distinct engines before choosing: contrast, misdirection, escalation, analogy, status reversal, act-out, rule of three, specificity, or callback.
5. **Scene the material.** Reconstruct who was present, what was said, what the body did, and what changed beat by beat. Make the audience see the event before explaining it.
6. **Run the writer pass.** Draft freely with setup, reveal, punchline, and optional tags. Keep only lines that advance context, tension, character, or laughs.
7. **Run the editor pass.** Score truth, clarity, surprise, voice, stageability, and joke density using the rubric in [references/craft.md](references/craft.md). Fix the lowest dimension first.
8. **Run the performance pass.** Read [references/performance-markup.md](references/performance-markup.md). Use its defined cue vocabulary to mark pauses, emphasis, role changes, movements, states, and laugh holds without cluttering every sentence.
9. **Offer a testable next version.** When alternatives matter, give at most three punchline or delivery variants and explain the intended audience effect in one short phrase each.

## Assemble a set

1. Open with a short, reliable line that establishes persona and earns attention quickly.
2. Group bits by emotional or narrative connection, not merely by topic labels.
3. Write transitions that introduce new information or reframe the previous laugh; avoid presenter-style transitions.
4. Seed one or two reusable details early and call them back later only when the second context changes their meaning.
5. Place the most emotionally honest or memorable bit near the end, then finish on a clear laugh rather than a summary.
6. Estimate duration with `scripts/estimate_duration.py`. Treat the estimate as a starting point and replace it with rehearsal timing when available.

## Output contracts

For a developed bit, return:

1. `创作判断`: premise, persona attitude, and selected comic engines.
2. `可表演逐字稿`: clean spoken script, with sparse performance cues when useful.
3. `备用笑点`: zero to three replaceable punchlines or tags.
4. `下一次测试`: one concrete question or performance variable.

For a critique, return:

1. `诊断`: what works and the biggest bottleneck.
2. `逐段修改`: preserve strong original lines and show only meaningful changes.
3. `修改后逐字稿`: a complete performable version.
4. `验证方法`: what reaction or timing to observe live.

Do not expose hidden reasoning or dump a large framework on the user. Keep process labels brief and make the script the main artifact.

## Persist material

Keep work in chat unless the user asks to save, organize, or maintain a writing workspace.

When persistence is requested:

1. Run `scripts/init_standup_workspace.py <target-directory>` using the script path relative to this skill.
2. Store raw observations in `ideas/`, developed pieces in `bits/`, assembled scripts in `sets/`, and performance notes in `open-mics/`.
3. Use the templates copied into `_templates/`; never overwrite existing material unless the user explicitly asks.
4. Prefer filenames like `YYYY-MM-DD-short-topic.md`.

## Guardrails

- Distinguish stage exaggeration from factual allegations about identifiable people.
- For roasts, confirm the target and context are appropriate; prefer behavior, status, and self-implication over immutable traits or humiliation.
- Avoid lazy stereotypes and slurs. If sensitive identity is central to the author's own material, preserve agency and aim the joke at power, contradiction, or the speaker's predicament.
- Never claim that a line is funny merely because it follows a template. Use rehearsal and audience response as the final judge.
