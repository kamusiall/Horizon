---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07
lang: en
---

> From 27 items, 9 important content pieces were selected

---

1. [Boson AI Releases Higgs Realtime Duplex, a 45B MoE Full-Duplex Multimodal Model](#item-1) ⭐️ 8.0/10
2. [Ant Ling Releases Ling-3.2-flash: 560B/25B Native Multimodal MoE with 1M Context](#item-2) ⭐️ 8.0/10
3. [Smaller Decision Model Routes to Claude Opus for 4x Cost Savings](#item-3) ⭐️ 7.0/10
4. [RealPage Rent-Pricing Lawsuit Settles for Nearly $360M](#item-4) ⭐️ 7.0/10
5. [The Shifting Dynamics Between ML Academia and Industry in 2026](#item-5) ⭐️ 7.0/10
6. [Libghostty 1.0: Stable C ABI Terminal Emulation Library Released](#item-6) ⭐️ 6.0/10
7. [Firecracker VM Escape: Practical Exploitation of PwnEscape Vulnerability](#item-7) ⭐️ 6.0/10
8. [Nilay Patel Critiques AI Industry: Products Not Worth the Costs](#item-8) ⭐️ 6.0/10
9. [ICLR 2027's New 1-4 Review Scale: A 2,2,3 is Above Average](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Boson AI Releases Higgs Realtime Duplex, a 45B MoE Full-Duplex Multimodal Model](https://www.reddit.com/r/MachineLearning/comments/1xpn5pv/higgs_realtime_duplex_a_45b_moe_fullduplex_model/) ⭐️ 8.0/10

Boson AI has released Higgs Realtime Duplex, a 45B Mixture-of-Experts model that processes audio, video, and text concurrently in 160ms chunks while performing background thinking, tool calls, and delegation to a larger backend model. Unlike turn-based voice models, Duplex runs all streams simultaneously and can backchannel, interrupt, or stay quiet based on silence tokens, enabling true full-duplex multimodal interaction. This represents a significant architectural departure from the dominant turn-based voice assistant paradigm, where models must listen, wait for end of turn, think, and then speak. By enabling simultaneous listening, speaking, and background reasoning at a cost target of one-tenth of human time per hour, the approach could reshape real-time AI interaction design and make scalable, natural multimodal assistants more economically viable. The model processes audio at 6.25 tokens/s input and 12.5 tokens/s output, with video frames every 6 chunks, totaling roughly 2.6K tokens per minute for audio and video and up to 5K with thinking and tool traces. Harder problems are delegated to a much larger backend model with shared context, and the front model is deliberately mid-sized to control cost; benchmarks show OpenAI leading on five of seven tasks, with Duplex furthest behind on turn-taking in Full-Duplex-Bench.

reddit · r/MachineLearning · /u/Cali_Cobarde · Nov 6, 20:23

**Background**: Mixture of Experts (MoE) is a machine learning architecture that divides a model into specialized sub-networks, allowing larger models to be trained with less compute by activating only relevant experts per input. Full-duplex multimodal interaction is an emerging research area where AI models simultaneously listen, see, and speak—mimicking human face-to-face conversation—rather than following the traditional turn-based listen-then-respond pattern. Recent academic work such as DuplexOmni and ELLSA 2 has explored separating interaction and thinking layers or jointly optimizing speech with gestures and expressions. Boson AI's Higgs Realtime is a speech-to-speech realtime API compatible with the OpenAI Realtime API, and the new Duplex variant extends this toward concurrent multimodal streaming.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.boson.ai/higgs-realtime">Higgs Realtime – Boson AI</a></li>
<li><a href="https://arxiv.org/abs/2606.09186">[2606.09186] DuplexOmni: Real-Time Listening, Seeing ...</a></li>

</ul>
</details>

**Tags**: `#multimodal-ai`, `#real-time-inference`, `#voice-ai`, `#mixture-of-experts`, `#full-duplex`

---

<a id="item-2"></a>
## [Ant Ling Releases Ling-3.2-flash: 560B/25B Native Multimodal MoE with 1M Context](https://www.reddit.com/r/MachineLearning/comments/1xpye7g/ant_ling_introduces_ling32flash_560b25b_native/) ⭐️ 8.0/10

Ant Ling has released Ling-3.2-flash, a native multimodal mixture-of-experts (MoE) model with 560B total parameters and 25B activated parameters per token, supporting text, image, and video inputs with a maximum context window of 1M tokens. The model demonstrates strong benchmark performance across vision, math, and agentic tasks, including a 96.80 on MathVision (with CI), 30.12 on Humanity's Last Exam (multimodal subset), 85.63 on AndroidWorld, and 67.77 on BlenderBench. This release positions Ling-3.2-flash among the frontier of large-scale multimodal models that combine long-context reasoning with agentic capabilities like GUI operation and multi-agent collaboration. The strong scores on challenging benchmarks like Humanity's Last Exam and ZEROBench, which were designed to be difficult for frontier models, signal meaningful progress in multimodal reasoning and document understanding. Notable benchmark results include 96.80 on MathVision (with CI), 30.12 on HLE-MM, 18.00/43.71 on ZEROBench main/sub, 92.21 on OmniDocBench 1.5, 85.15 on CharXiv_RQ, 79.93 on MedXpertQA-MM, 85.86 on Vision2Web, and 85.63 on AndroidWorld. The model supports both OpenAI-compatible and Anthropic-compatible API access, and demonstrates capabilities in PDF-to-code implementation, GUI operation, 3D reconstruction, and multi-agent collaboration workflows.

reddit · r/MachineLearning · /u/the-hollow-soul · Nov 7, 05:21

**Background**: Mixture-of-Experts (MoE) is an architecture where only a subset of a model's parameters (the 'activated parameters') are used per token, allowing large total parameter counts while maintaining computational efficiency. Humanity's Last Exam (HLE) is a benchmark of 2,500 challenging questions across over 100 subjects, created by the Center for AI Safety and Scale AI to probe frontier knowledge. ZEROBench is a deliberately difficult visual reasoning benchmark of 100 curated questions where frontier models initially scored 0% at release, leaving significant headroom for future progress. OmniDocBench evaluates models on diverse document parsing tasks across academic papers, textbooks, and other sources.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Humanity's_Last_Exam">Humanity's Last Exam - Wikipedia</a></li>
<li><a href="https://zerobench.github.io/">ZeroBench: An Impossible Visual Benchmark</a></li>
<li><a href="https://arxiv.org/abs/2412.07626">[2412.07626] OmniDocBench : Benchmarking Diverse PDF...</a></li>

</ul>
</details>

**Tags**: `#multimodal-models`, `#mixture-of-experts`, `#long-context`, `#LLM-release`, `#agentic-AI`

---

<a id="item-3"></a>
## [Smaller Decision Model Routes to Claude Opus for 4x Cost Savings](https://hightouch.com/blog/llm-judges-identity-resolution) ⭐️ 7.0/10

A blog post from Hightouch describes using a smaller decision model called Jev, developed by TypeSafe AI, to selectively invoke Claude Opus for identity resolution tasks. By having Jev act as a gatekeeper that only escalates to the more expensive Opus model when needed, the system achieves Opus-level accuracy at approximately one-quarter of the cost. This approach demonstrates a practical model orchestration pattern where a cheap, fast decision model routes queries to a frontier LLM only when necessary, dramatically reducing inference costs without sacrificing output quality. As LLM costs remain a major barrier to production deployment, this routing strategy could become a standard architectural pattern for cost-sensitive applications across the industry. Jev is a specialized model from TypeSafe AI that returns choices, scores, or yes/no probabilities rather than chat completions, making it well-suited for decision and routing tasks at roughly $0.042 per million tokens. A notable limitation discussed is that if the decision model must also provide reasoning for every case, the cost savings can evaporate since an extra inference step is added, highlighting the importance of use-case-specific tuning.

hackernews · theanomaly · Nov 6, 19:48 · [Discussion](https://news.ycombinator.com/item?id=50397429)

**Background**: Identity resolution is the process of reconciling disparate data records to determine whether they belong to the same real-world person, commonly used in customer data platforms and marketing analytics. Claude Opus is Anthropic's most capable and expensive LLM family, while Jev is a lightweight transformer-based model optimized for fast, efficient decision-making rather than open-ended text generation. The routing pattern described here falls under the broader category of LLM orchestration, where multiple models with different cost and capability profiles are combined to optimize for both accuracy and expense.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://jevmodel.org/">Jev Model — TypeSafe Jev AI API, Playground & Pricing</a></li>
<li><a href="https://www.twilio.com/en-us/blog/insights/identity-resolution">Identity resolution: what it is and how it works - Twilio</a></li>

</ul>
</details>

**Discussion**: Commenters discussed practical implementations of similar routing patterns, with one user noting that Qwen 27B can effectively orchestrate queries to Claude models and another pointing to swival.dev as a platform that uses Cloudflare's Clef for automatic model selection with confidence scoring. A significant ethical concern was raised about the application domain, with one commenter warning that AI-assisted identity resolution effectively makes privacy violations cheaper and urging developers to consider the societal implications of what they build. Technical tradeoffs were also debated, particularly the challenge of finding decision models that can both route and provide reasoning without negating the cost savings.

**Tags**: `#LLM-routing`, `#cost-optimization`, `#model-orchestration`, `#decision-models`, `#identity-resolution`

---

<a id="item-4"></a>
## [RealPage Rent-Pricing Lawsuit Settles for Nearly $360M](https://www.multifamilydive.com/news/realpage-rent-pricing-case-360m-renters/873553/) ⭐️ 7.0/10

A class-action lawsuit against RealPage and several rental companies has concluded with nearly $360 million in settlements, with the defendants agreeing to stop sharing non-public data for use in RealPage's algorithmic revenue management pricing system. The companies did not admit fault or liability as part of the settlement. This settlement is a landmark case in the emerging legal landscape around algorithmic price-fixing, signaling that regulators and courts are scrutinizing AI-driven pricing systems that may facilitate collusion without explicit coordination. It could reshape how property management companies and other industries use shared data in algorithmic pricing tools, potentially affecting millions of renters and setting precedents for similar cases in other sectors. The settling companies agreed to stop providing RealPage with their non-public data and to stop using RealPage's revenue management system in ways that use competitors' non-public data to inform pricing recommendations. However, RealPage retains a decade of historical pricing data, which could still be used to inform recommendations unless stricter boundaries are enforced.

hackernews · raybb · Nov 6, 23:37 · [Discussion](https://news.ycombinator.com/item?id=50399991)

**Background**: RealPage's AI Revenue Management system, formerly known as YieldStar, is a dynamic pricing engine that processes supply and demand signals, competitive market data, lease expiration patterns, and property-level performance to generate rent pricing recommendations for apartment units. The lawsuit alleged that RealPage collected competitively sensitive, real-time information from participating landlords—including occupancy rates, lease terms, and rent rolls—and used that information to generate pricing recommendations that effectively coordinated rent prices across competitors. The U.S. Department of Justice was also involved in litigation over the software's alleged role in rent price-fixing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aboutlawsuits.com/realpage-rent-pricing-lawsuit-damages-tenants-inflated-rents/">RealPage Rent Pricing Lawsuit Seeks... - AboutLawsuits.com</a></li>
<li><a href="https://www.classyaction.app/blog/realpage-rent-price-fixing-settlement">RealPage Rent Price -Fixing Lawsuit : What Renters N | ClassyAction</a></li>
<li><a href="https://bestcre.com/realpage-ai-revenue-management-review-cre-ai/">RealPage AI Revenue Management Review: Dynamic Pricing ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the settlement's effectiveness, noting that RealPage retains a decade of historical pricing data that could continue to inform recommendations. Some advocated for a public rental registry to address information asymmetry, while others proposed more radical solutions like banning corporate ownership of rental properties. The discussion reflected broader concerns about whether algorithmic collusion can be meaningfully addressed through incremental legal settlements or requires systemic regulatory reform.

**Tags**: `#algorithmic-pricing`, `#legal-settlement`, `#real-estate`, `#data-privacy`, `#ai-regulation`

---

<a id="item-5"></a>
## [The Shifting Dynamics Between ML Academia and Industry in 2026](https://www.reddit.com/r/MachineLearning/comments/1xponb2/what_exactly_is_the_relationship_between_ml/) ⭐️ 7.0/10

A Reddit user has sparked a discussion questioning whether industry is still adopting ideas from academia in 2026, observing a significant shift where industry now drives frontier research while academia follows up with derivative work. The user notes that while academia once paved the way for industry applications, it now appears that industry is impassive to academic follow-up research. This observation highlights a major meta-trend in the machine learning ecosystem where the center of gravity for fundamental innovation has moved from universities to big tech companies. It raises important questions about the relevance and impact of academic research in highly applied fields if industry no longer adopts or acknowledges these external contributions. The user points out that while algorithms like ADAM and TRPO from academia were widely adopted by industry in the past, today's academic proposals for new optimization routines or neural network architectures often face low to no adoption. This suggests that academia and industry are diverging into separate worlds, with industry taking on the role of the primary idea generator.

reddit · r/MachineLearning · /u/Strong_Boy_757 · Nov 6, 21:25

**Background**: ADAM (Adaptive Moment Estimation) is a widely used optimization algorithm that combines the advantages of Momentum and RMSprop, becoming the default optimizer for training large-parameter AI models. TRPO (Trust Region Policy Optimization) is a model-free, on-policy reinforcement learning algorithm known for its stability and efficiency in optimizing policies for complex tasks. Both were examples of academic innovations that successfully transitioned to industry standards during the 2012-2018 era.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Adam_(optimization_algorithm)">Adam (optimization algorithm)</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Academia`, `#Industry`, `#Research`, `#Meta-discussion`

---

<a id="item-6"></a>
## [Libghostty 1.0: Stable C ABI Terminal Emulation Library Released](https://mitchellh.com/writing/libghostty-1-0) ⭐️ 6.0/10

Mitchell Hashimoto has released libghostty-vt 1.0, a portable, high-performance C library for terminal emulation extracted from the core of the Ghostty terminal emulator. The library features a stable C ABI designed to let developers build new terminals and agentic coding tools without reimplementing terminal emulation logic from scratch. This release provides a foundational building block for the terminal ecosystem, enabling developers to create new terminal applications and AI-driven coding tools without the significant effort of writing a terminal emulator. The stable C ABI ensures cross-language compatibility and long-term reliability, which is particularly valuable as agentic coding tools increasingly need robust terminal integration. The API design uses opaque handles for objects and enum-keyed getters and setters to avoid leaking implementation details to callers, following patterns from well-regarded C libraries. Projects already built on libghostty include herdr, cmux, and mobile embedders like expo-libghostty for React Native and flutter_ghostty for Flutter, demonstrating cross-platform adoption.

hackernews · mfiguiere · Nov 6, 23:30 · [Discussion](https://news.ycombinator.com/item?id=50399933)

**Background**: Ghostty is a terminal emulator written in Zig by Mitchell Hashimoto, known for its performance and modern features like the Kitty graphics protocol for inline images. A C ABI (Application Binary Interface) defines how compiled code interacts with a library at the machine level, and maintaining ABI stability means downstream consumers can upgrade the library without recompiling their own code. Terminal emulation involves interpreting escape sequences and rendering text-based interfaces, which is complex enough that most projects prefer to reuse an existing library rather than implement their own.

<details><summary>References</summary>
<ul>
<li><a href="https://mitchellh.com/writing/libghostty-1-0">Libghostty 1.0 – Mitchell Hashimoto</a></li>
<li><a href="https://lib.ghostty.org/vt/">libghostty-vt: libghostty-vt</a></li>
<li><a href="https://github.com/Uzaaft/awesome-libghostty">GitHub - Uzaaft/awesome-libghostty</a></li>

</ul>
</details>

**Discussion**: Community sentiment is overwhelmingly positive, with users praising the project's design and Hashimoto's restraint in not promoting his own competing product Rex in the announcement. Several commenters highlighted the API design as instructive for their own projects, noting the value of opaque handles and stable ABI patterns, while one user shared their experience using libghostty in an Android project. Some discussion touched on comparisons with the Kitty terminal's rendering performance, and users noted Ghostty's strengths with fancy TUI programs and inline image support.

**Tags**: `#terminal-emulator`, `#zig`, `#c-api`, `#developer-tools`, `#libghostty`

---

<a id="item-7"></a>
## [Firecracker VM Escape: Practical Exploitation of PwnEscape Vulnerability](https://pwn.ai/blog/firecracker-escape) ⭐️ 6.0/10

A technical deep-dive writeup demonstrates practical exploitation of the PwnEscape vulnerability (CVE-2026-99999) to escape Firecracker microVMs, showing how a guest VM can achieve code execution on the host. The exploit specifically targets Firecracker configurations that do not use the jailer, which is the production-recommended isolation mechanism. Firecracker microVMs are widely used in cloud and serverless infrastructure (notably by AWS for Lambda and Fargate), so demonstrating a practical guest-to-host escape has significant implications for multi-tenant cloud security. The writeup highlights that while the underlying Linux kernel networking vulnerability is the root cause, the security posture of the virtualization layer (jailer vs. non-jailer) determines whether exploitation leads to full host compromise. The PwnEscape vulnerability (CVE-2026-99999) resides in the Linux kernel's networking subsystem and allows a guest VM to read and write host memory by sending crafted network packets. The demonstrated exploit requires Firecracker to run without the jailer binary, which in production setups would drop privileges, apply seccomp filters, and use namespace isolation to constrain the VMM process.

hackernews · SerCe · Nov 6, 19:33 · [Discussion](https://news.ycombinator.com/item?id=50397219)

**Background**: Firecracker is an open-source virtualization technology developed by AWS that creates lightweight microVMs using Linux KVM, designed for fast startup and low memory overhead with a minimal attack surface. The jailer is a companion binary that isolates the Firecracker VMM process by dropping to an unprivileged UID, setting up a chroot, and applying seccomp and namespace restrictions. PwnEscape (CVE-2026-99999) is a critical Linux kernel vulnerability disclosed in October 2026 that enables guest-to-host VM escapes through the networking subsystem, affecting any KVM-based virtualization stack including Firecracker.

<details><summary>References</summary>
<ul>
<li><a href="https://pwn.ai/blog/pwnescape">PwnEscape: Guest-to-Host KVM Escape (CVE-2026-99999)</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker/blob/main/docs/jailer.md">firecracker /docs/ jailer .md at main · firecracker -microvm/ firecracker</a></li>
<li><a href="https://cybernews.com/security/critical-linux-bug-pwnescape-allows-vm-escape/">PwnEscape Linux Vulnerability Lets VM Guests Escape to Hosts ...</a></li>

</ul>
</details>

**Discussion**: Commenters emphasized that this is not a new vulnerability but a practical exploitation guide for the previously disclosed PwnEscape bug, and noted that properly jailed Firecracker instances would significantly limit the impact of such an escape. One commenter advocated for the Nova Microhypervisor approach using a formally verified microkernel instead of relying on a complex Linux kernel at the hypervisor layer. Another commenter pointed out that their production ClickBench service running hundreds of Firecracker VMs could potentially be used to PoC the escape, highlighting real-world exposure.

**Tags**: `#security`, `#virtualization`, `#firecracker`, `#vm-escape`, `#vulnerability`

---

<a id="item-8"></a>
## [Nilay Patel Critiques AI Industry: Products Not Worth the Costs](https://simonwillison.net/2026/Nov/6/nilay-patel/) ⭐️ 6.0/10

Nilay Patel, editor-in-chief of The Verge, argued on The Vergecast that current AI products are not good enough to justify their high costs, environmental impact, and the political corruption surrounding the industry's push for adoption. He specifically called out AI overviews, deepfake slop, and the fact that AI companies are spending more than they are making, while also noting that AI agents are not yet real or being used as intended. This critique from a prominent tech journalist captures a growing sentiment that the AI industry's massive investments have not yet translated into products that deliver clear, tangible value to ordinary users. It highlights a potential turning point in public perception, where the gap between hype and reality may drive demand for better products rather than more marketing. Patel links the AI industry's cost imposition to political corruption, citing CEOs visiting the White House and what he describes as obvious crypto-corruption. He also references real-world harms such as hacked blood-storage refrigerators in Europe, arguing that the societal costs of AI infrastructure are concrete while the benefits remain unrealized for most people.

rss · Simon Willison · Nov 6, 17:13

**Background**: AI Overviews is a generative AI feature integrated into Google Search that displays AI-generated responses at the top of search results, which has been a source of controversy over accuracy and quality. AI slop refers to low-effort, mass-produced digital content created with generative AI that is perceived as lacking quality or meaning, often flooding social media and search results. AI agents are autonomous or semi-autonomous AI systems designed to perform tasks on behalf of users, but experts have cautioned against letting hype about their capabilities get ahead of reality, as the technology is still maturing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://www.technologyreview.com/2025/07/03/1119545/dont-let-hype-about-ai-agents-get-ahead-of-reality/">Don’t let hype about AI agents get ahead of... | MIT Technology Review</a></li>

</ul>
</details>

**Tags**: `#AI-industry-criticism`, `#AI-costs`, `#tech-commentary`, `#AI-agents`

---

<a id="item-9"></a>
## [ICLR 2027's New 1-4 Review Scale: A 2,2,3 is Above Average](https://www.reddit.com/r/MachineLearning/comments/1xps7xu/iclr_2027s_new_14_scale_a_2_2_3_is_better_than_it/) ⭐️ 6.0/10

An analysis of over 73,000 public reviews on OpenReview reveals that ICLR 2027's new 4-point review scale is heavily skewed, with 57% of reviews giving a score of 2 and the median paper averaging exactly 2.0. Consequently, a paper receiving scores of 2, 2, and 3 is already above the majority of submissions. This statistical breakdown helps researchers calibrate their expectations for the new review scale, which lacks historical intuition for the academic community. Understanding the score distribution is crucial for authors and reviewers to accurately gauge paper acceptance odds at one of the most prestigious machine learning conferences. The analysis covers the first 25,000 of approximately 40,800 submissions, ordered by OpenReview's listing rather than a random sample. The interactive tool built by the authors only displays aggregate counts and does not reveal paper titles, authors, or review text.

reddit · r/MachineLearning · /u/latenticlabs · Nov 7, 00:03

**Background**: ICLR (International Conference on Learning Representations) is one of the top three most prestigious conferences in machine learning and AI research. The conference recently transitioned to a 4-point review scale (1: clear reject, 2: weak reject, 3: weak accept, 4: clear accept), leaving reviewers without an established baseline for score distributions. OpenReview is a transparent peer review platform that hosts these submissions and their public reviews.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations">International Conference on Learning Representations</a></li>
<li><a href="https://openreview.net/about">About | OpenReview</a></li>

</ul>
</details>

**Tags**: `#ICLR`, `#peer-review`, `#academic-publishing`, `#machine-learning`, `#data-analysis`

---