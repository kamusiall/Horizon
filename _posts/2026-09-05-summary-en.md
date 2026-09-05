---
layout: default
title: "Horizon Summary: 2026-09-05 (EN)"
date: 2026-09-05
lang: en
---

> From 30 items, 7 important content pieces were selected

---

1. [OpenAI Announces GPT-6 Astra with 99.9% ARC-AGI 3 Score and Competitive Pricing](#item-1) ⭐️ 10.0/10
2. [Anthropic Formalizes Fermat's Last Theorem in Lean](#item-2) ⭐️ 9.0/10
3. [GPT-6 Astra Released on OpenRouter with Superior Vision Capabilities](#item-3) ⭐️ 9.0/10
4. [Actively exploited sandbox RCE in all Chromium versions](#item-4) ⭐️ 8.0/10
5. [Can AI design circuit boards yet?](#item-5) ⭐️ 7.0/10
6. [Portal by Spotify cut my Claude Code token usage by 90%](#item-6) ⭐️ 6.0/10
7. [The Ghost Productivity Question: Why GPT-5-Class Models Haven't Shocked the Economy](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Announces GPT-6 Astra with 99.9% ARC-AGI 3 Score and Competitive Pricing](https://simonwillison.net/2026/Sep/3/gpt6-astra/) ⭐️ 10.0/10

OpenAI announced the rollout of GPT-6 Astra, its new flagship LLM, to ChatGPT Plus, Pro, Business, and Enterprise users as well as through the OpenAI API and AWS, with API pricing set at $10 per million input tokens and $50 per million output tokens, matching Anthropic's Claude Fable 5 and 5.1. The model reportedly scores 99.9% on the ARC-AGI 3 benchmark and demonstrates strong improvements on security tasks and long-context processing compared to its predecessor GPT-5.6 Sol. This release positions GPT-6 Astra as a direct competitor to Anthropic's Claude Fable 5, potentially reshaping the competitive landscape among frontier LLM providers including OpenAI, Anthropic, and Meta. The benchmark results, particularly on security tasks and long-context handling, suggest meaningful advances in capabilities that matter for enterprise and developer use cases, while the matching API pricing intensifies the price-performance rivalry in the market. The 99.9% ARC-AGI 3 score was achieved using OpenAI's custom 'Provider Adapter harness,' which preserves opaque reasoning state between requests and uses compaction for longer conversations; notably, the default ARC-AGI harness scored only 62.7% for $26K, compared to $19K for the custom harness run. On the Artificial Analysis Intelligence Index, Astra scores 61, equal to GPT-5.6 Sol but 5 points lower than Claude Fable 5.1, while it leads the Coding Agent Index cost efficiency frontier at roughly half the per-task cost of Claude Fable 5.

rss · Simon Willison · Sep 3, 20:18

**Background**: The ARC-AGI benchmark is designed to evaluate general intelligence in AI systems through abstract reasoning tasks that require novel problem-solving, with higher scores indicating stronger generalization capabilities. A 'harness' in benchmarking refers to a software wrapper that manages how a model processes and responds to test inputs, and different harness configurations can significantly affect measured performance, making cross-model comparisons complex. The frontier LLM market is currently dominated by OpenAI, Anthropic, and Meta, with each company frequently releasing new models and competing on both benchmark scores and API pricing to attract developers and enterprise customers.

**Discussion**: Community members on Reddit and Hacker News flagged that GPT-6 Astra's headline 99.9% ARC-AGI 3 score was achieved using a custom harness, and that without it the model scores approximately 60%, raising questions about the comparability of benchmark results across different harness configurations. Some commenters also noted that Claude Fable 5 does not yet have a published ARC-AGI 3 result, making direct comparisons premature.

**Tags**: `#GPT-6`, `#OpenAI`, `#LLM Release`, `#ARC-AGI`, `#Benchmarks`

---

<a id="item-2"></a>
## [Anthropic Formalizes Fermat's Last Theorem in Lean](https://www.anthropic.com/research/formalizing-fermats-last-theorem) ⭐️ 9.0/10

Anthropic has successfully formalized Fermat's Last Theorem in the Lean proof assistant, producing 13 million lines of code and proving 29,500 intermediate theorems along the way. The formalization follows the Darmon–Diamond–Taylor exposition from 1995 of the Wiles–Taylor–Wiles argument, rather than the more modern proof approaches. This demonstrates that AI can now formalize large swaths of advanced mathematics, potentially catching errors in the existing body of mathematical proofs and significantly reducing the burden of refereeing new mathematical work. The scale and speed of the formalization suggest that AI-assisted proof verification could become a transformative tool for the mathematical community. The formalization develops Fontaine theory to study flat deformations of Galois representations and builds on enough of Mazur's work on the Eisenstein ideal to conclude that no Frey curve can have a point of order p greater than certain bounds. The proof route uses the Langlands–Tunnell theorem and Ribet's level-lowering theorem, and Kevin Buzzard — who has been independently working on formalizing the modern proof — notes this is not the modern approach he has been pursuing.

hackernews · jlebar · Sep 4, 18:42 · [Discussion](https://news.ycombinator.com/item?id=49568506)

**Background**: Fermat's Last Theorem states that no three positive integers a, b, and c satisfy a^n + b^n = c^n for any integer n greater than 2, and was famously proved by Andrew Wiles in 1995 using sophisticated tools from algebraic geometry and number theory. Lean is a proof assistant and programming language that allows mathematicians to write proofs in a formal, machine-checkable format, ensuring every logical step is rigorously verified against foundational axioms. Formalizing a theorem in Lean means translating the entire proof — including all prerequisite results and infrastructure — into a form that the computer can independently verify, which can be an enormous undertaking for proofs as deep as Wiles'.

**Discussion**: Community members recommended Kevin Buzzard's blog post for important context on what the achievement does and does not mean, while a software engineering-minded commenter questioned whether 13 million lines of Lean can truly be considered bug-free. Others noted the sheer scale of proving 29,500 intermediate theorems and observed that it lends credence to the idea that AI can prove anything that is in principle provable.

**Tags**: `#formal-verification`, `#lean`, `#mathematics`, `#anthropic`, `#ai-research`

---

<a id="item-3"></a>
## [GPT-6 Astra Released on OpenRouter with Superior Vision Capabilities](https://openrouter.ai/openai/gpt-6-astra) ⭐️ 9.0/10

OpenAI's GPT-6 Astra model is now available on OpenRouter, offering advanced vision-based web development and SVG generation capabilities. Early benchmarks highlight its ability to accurately handle non-90-degree cutouts and shapes compared to competing models like Opus 5. This release provides developers with a significantly more capable vision model for web development tasks, potentially reducing overall token usage despite a higher per-token cost. It intensifies competition in the LLM space by setting a new standard for visual accuracy and code generation from design sources. The model is accessible to Pro users on OpenRouter and offers different tiers, such as "Astra low" and "Astra high," which affect output quality and cost. While it is more expensive per token than alternatives, users report it requires fewer tokens to achieve superior results, making it cost-effective for specific budgets.

hackernews · Topfi · Sep 4, 21:39 · [Discussion](https://news.ycombinator.com/item?id=49570545)

**Background**: OpenRouter is an API platform that aggregates access to various large language models (LLMs) from different providers, allowing developers to easily switch between them. Vision models like GPT-6 Astra are designed to interpret images and generate corresponding code or text, a crucial feature for automating web development from visual designs. Competing models mentioned include Anthropic's Opus 5 and Google's offerings, which are frequently benchmarked against OpenAI's latest releases.

**Discussion**: Community sentiment is highly positive regarding the model's vision and SVG generation capabilities, with users demonstrating its superior handling of complex shapes compared to Opus 5. However, there is a shared concern that the model's efficiency and pricing might degrade over time, a common practice among major AI providers. Others noted initial availability issues on OpenRouter that have since been resolved for Pro users.

**Tags**: `#GPT-6`, `#OpenAI`, `#OpenRouter`, `#vision-models`, `#LLM-release`

---

<a id="item-4"></a>
## [Actively exploited sandbox RCE in all Chromium versions](https://nvd.nist.gov/vuln/detail/cve-2026-85046) ⭐️ 8.0/10

A critical sandbox escape RCE vulnerability (CVE-2026-85046) caused by a type confusion bug in V8 is being actively exploited in Chromium, with a patch available in the latest stable release.

hackernews · negura · Sep 4, 21:52 · [Discussion](https://news.ycombinator.com/item?id=49570669)

**Tags**: `#security`, `#chromium`, `#vulnerability`, `#v8`, `#rce`

---

<a id="item-5"></a>
## [Can AI design circuit boards yet?](https://eebench.org/blog/can-ai-design-circuit-boards-yet/) ⭐️ 7.0/10

A benchmark-driven exploration of whether AI can currently design circuit boards, with experienced engineers in the comments sharing mixed-but-encouraging real-world results using LLMs for PCB design tasks.

hackernews · iopapa · Sep 4, 19:48 · [Discussion](https://news.ycombinator.com/item?id=49569366)

**Tags**: `#AI hardware design`, `#PCB design`, `#LLM agents`, `#eebench`, `#AI applications`

---

<a id="item-6"></a>
## [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90) ⭐️ 6.0/10

Spotify's Portal tool claims to reduce Claude Code token usage by 90% by delegating certain tasks to cheaper models like Gemini Flash, though commenters note this is essentially a model-routing approach with mixed tradeoffs.

hackernews · cebert · Sep 4, 23:38 · [Discussion](https://news.ycombinator.com/item?id=49571465)

**Tags**: `#LLM tooling`, `#token optimization`, `#Claude Code`, `#model delegation`, `#Spotify engineering`

---

<a id="item-7"></a>
## [The Ghost Productivity Question: Why GPT-5-Class Models Haven't Shocked the Economy](https://www.reddit.com/r/MachineLearning/comments/1w7f6kq/gpt_567_does_it_even_matter_the_ghost/) ⭐️ 6.0/10

A Reddit discussion post raises the question of why current GPT-5-class models, despite being genuinely capable of performing a substantial fraction of knowledge work, have not produced a noticeable productivity shock in the real economy. The author argues that the bottleneck likely lies in organizational, regulatory, and institutional constraints rather than in model intelligence itself. This question strikes at the heart of the ongoing debate about AI's economic impact, challenging the common assumption that model capability directly translates to economic substitution and job displacement. It has significant implications for how organizations, policymakers, and workers should think about AI adoption timelines and the true nature of productivity gains from LLMs. The author distinguishes between technical capability and economic substitution, noting that in professions like law, medicine, and research, AI can accelerate specific tasks but the surrounding workflow—verification, compliance, communication, institutional processes—remains a bottleneck. Coding is cited as the clearest exception where productivity gains are visible, though even there the bottleneck often shifts rather than disappears.

reddit · r/MachineLearning · /u/Same-Club4925 · Sep 4, 20:02

**Background**: The post echoes the classic 'productivity paradox'—a phenomenon where technological advances don't immediately show up in productivity statistics, similar to the Solow Paradox observed during the early computing era. The author draws an analogy to the internet, which could transmit information essentially for free but did not instantly eliminate newspapers, universities, or offices, suggesting that institutional change lags significantly behind technological change. The discussion also touches on the distinction between benchmark performance and real-world economic output, a gap that has been observed across multiple technology revolutions.

**Tags**: `#LLMs`, `#productivity`, `#economics`, `#AI impact`, `#discussion`

---