---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 37 items, 12 important content pieces were selected

---

1. [Greg Kroah-Hartman Critically Examines LLM-Based Kernel Vulnerability Claims](#item-1) ⭐️ 8.0/10
2. [Black Forest Labs Releases FLUX 3 Image with Canvas-Based Element Placement](#item-2) ⭐️ 8.0/10
3. [AI Ataraxos Defeats World's Best Stratego Player on a Modest Budget](#item-3) ⭐️ 8.0/10
4. [Parallel-in-Time RNN Training via GTF-DEER Achieves 100x Speedup on Chaotic Time Series](#item-4) ⭐️ 8.0/10
5. [NeurIPS Paper Reveals 'Authority Bias' in LLMs Accepting Misinformation from Verified Sources](#item-5) ⭐️ 8.0/10
6. [DwarfStar (ds4): Local LLM Inference Engine by Redis Creator antirez](#item-6) ⭐️ 7.0/10
7. [Claude Opus 5.5 Paints on a Simulated Canvas Using Code](#item-7) ⭐️ 7.0/10
8. [Developer Shares One-Month Experience Coding with GLM 5.3 Flash](#item-8) ⭐️ 7.0/10
9. [NeurIPS Paper Tackles Topological Out-of-Domain Generalization in Dynamical Systems Reconstruction](#item-9) ⭐️ 7.0/10
10. [FLEET: Memory-Augmented MCTS for Reward-Aware Best-of-N LLM Generation](#item-10) ⭐️ 7.0/10
11. [Court agrees with EFF: Utah's VPN law demands a technical impossibility](#item-11) ⭐️ 6.0/10
12. [The Forgetful CPU: Running Linux on Apple M4 Silicon](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Greg Kroah-Hartman Critically Examines LLM-Based Kernel Vulnerability Claims](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

Linux kernel maintainer Greg Kroah-Hartman delivered a talk titled "Security in the LLM Age" (Kernel Recipes 2026, video available on YouTube) in which he systematically evaluated Anthropic's LLM-based vulnerability findings, known as "Mythos," that claimed 79 new Linux kernel vulnerabilities. His analysis revealed that only 20 of the 79 reported issues actually required fixes, while the rest were invalid, vague, fabricated, or already patched — amounting to roughly one hour of ordinary kernel development work. The talk strikes at the heart of the ongoing debate about AI capability claims versus reality, showing that a heavily marketed LLM security "breakthrough" largely reproduced pattern-matching of previously known kernel patches rather than discovering genuinely novel vulnerabilities. It matters for kernel developers, security researchers, and AI labs alike because inflated claims erode public trust, and Kroah-Hartman's stature as one of the most senior kernel maintainers gives his assessment significant weight in the community. Kroah-Hartman's breakdown of Mythos's 79 reported vulnerabilities: 24 provided no detail at all ("something crashed"), 14 were not bugs, 3 contained totally made-up data, 15 were already fixed in the latest release (11 by others, 4 by Anthropic itself), and only 20 needed fixes — of which 7 assumed a malicious filesystem image and 2 assumed attacker-controlled inputs. He also criticized Anthropic for not citing the original kernel developers whose historical patches the LLM effectively pattern-matched, echoing broader concerns about AI labs' citation practices.

hackernews · usernomdeguerre · Oct 2, 02:51 · [Discussion](https://news.ycombinator.com/item?id=49929391)

**Background**: Greg Kroah-Hartman is one of the most influential Linux kernel maintainers, responsible for the stable kernel branch series, and is known for his candid, no-nonsense assessments of kernel security. Anthropic's "Mythos" effort followed earlier experiments, such as researcher Nicholas Carlini's use of a simple 12-line bash script feeding kernel source files to Claude with a "find vulnerabilities, treat it like a CTF" prompt, which found a 23-year-old kernel bug and generated significant publicity around LLM-driven vulnerability discovery. Academic research has also noted that LLMs struggle to capture the root causes of vulnerabilities, often relying on surface-level pattern matching against historical bug fixes rather than deep semantic understanding. The Linux kernel's fully open development process means Kroah-Hartman's claims can be independently verified by anyone, unlike closed-source AI evaluation results.

<details><summary>References</summary>
<ul>
<li><a href="https://www.stork.ai/blog/ai-just-hacked-linuxs-23-year-old-secret">AI Finds 23-Year-Old Linux Kernel Bug with Simple Script | Stork.AI</a></li>
<li><a href="https://arxiv.org/abs/2509.19117">[2509.19117] LLM-based Vulnerability Discovery through the ... vul-rag: Enhancing LLM-based Vulnerability Detection via ... Large Language Model-enabled Vulnerability Investigation: A ... LLM Security: Vulnerabilities, Attacks, Defenses, and ... Security of LLM-based agents regarding attacks, defenses, and ... Securing Large Language Models: Threats, Vulnerabilities and ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (241 points, 75 comments) was largely appreciative of Kroah-Hartman's candor, with commenters highlighting the stark dissonance between AI labs marketing their models as world-endangeringly powerful while their actual security research output amounts to modest, partially invalid bug reports. Multiple commenters criticized Anthropic for failing to cite the original kernel developers whose patches the LLM pattern-matched, drawing parallels to OpenAI's citation controversies, while others noted the value of having claims from someone deeply knowledgeable and the fact that everything is verifiable since the kernel is open source.

**Tags**: `#LLM`, `#security`, `#linux-kernel`, `#vulnerability-research`, `#AI-evaluation`

---

<a id="item-2"></a>
## [Black Forest Labs Releases FLUX 3 Image with Canvas-Based Element Placement](https://bfl.ai/models/flux-3-image) ⭐️ 8.0/10

Black Forest Labs has released FLUX 3 Image, a new AI image generation and editing model that allows users to place individual elements on a canvas using bounding boxes and then edit each box independently after generation. The model supports text-to-image generation, multi-reference editing with up to 10 input images, and native output resolutions from 768px up to 4K with selectable aspect ratios. FLUX 3 Image shifts the focus toward user experience and steerability, addressing a long-standing pain point in AI image generation where controlling the precise placement of elements within a composition has been difficult. This positions it competitively against models like Ideogram V4 and tools like InvokeAI, potentially making it more practical for professional workflows that require exact compositional control. The model renders at fixed resolution tiers from 768 up to 4K and supports clean text rendering, which has historically been a weakness in many image generation models. It is available through multiple API providers including OpenRouter and fal.ai, and is part of a broader FLUX 3 multimodal system that also covers video, audio, and actions.

hackernews · minimaxir · Oct 1, 19:24 · [Discussion](https://news.ycombinator.com/item?id=49925974)

**Background**: Black Forest Labs is the company behind the FLUX family of text-to-image models, which have been competitive with leading closed models in terms of quality and capability. Previous iterations like FLUX.2 Pro offered 32B parameters, multi-reference support, and 4MP output. The broader trend in AI image generation has been moving from simple prompt-based generation toward more controllable, interactive workflows where users can specify spatial layout, reference images, and fine-grained edits — a space also occupied by tools like InvokeAI and models like Ideogram V4.

<details><summary>References</summary>
<ul>
<li><a href="https://bfl.ai/models/flux-3-image">FLUX 3 Image : Maximum control over every pixel | Black Forest Labs</a></li>
<li><a href="https://openrouter.ai/black-forest-labs/flux-3-image">FLUX . 3 Image - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://fal.ai/models/blackforestlabs/flux-3/text-to-image">Flux 3 Image (Text to Image ) API on fal</a></li>

</ul>
</details>

**Discussion**: Commenters broadly praised the UX and steerability of FLUX 3 Image, with one noting it improves on Ideogram V4's cumbersome JSON-based bounding box approach. However, some expressed skepticism about output quality, with one commenter calling out a showcase example as notably poor, and another cynically remarking that AI-generated images have eroded trust in digital imagery entirely. A practical discussion also emerged around whether the model could generate accurate frame-by-frame sprite sequences for game development, a use case no current image model handles well.

**Tags**: `#image-generation`, `#AI-models`, `#FLUX`, `#generative-AI`, `#UX`

---

<a id="item-3"></a>
## [AI Ataraxos Defeats World's Best Stratego Player on a Modest Budget](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

A team of researchers from Carnegie Mellon, MIT, NYU, and Stanford developed an AI called Ataraxos that defeated Pim Niemeijer, arguably the best Stratego player of all time, 15 games to one with four draws. The system was trained using just 16 GPUs and a few thousand dollars, and it learned approximately 34 times more efficiently than DeepNash, the previous state-of-the-art Stratego AI from DeepMind in 2022. Stratego is an imperfect-information game where most of the opponent's pieces are hidden, making it fundamentally harder for AI than perfect-information games like chess or Go. This breakthrough demonstrates that AI can now master complex hidden-information games with dramatically reduced computational resources, potentially opening the door to more efficient approaches for real-world problems involving incomplete information. Ataraxos's key innovation is its sample efficiency, requiring 34 times fewer self-play games than DeepNash while achieving substantially stronger play. The research is documented in both a Nature paper and an arXiv preprint (arXiv:2511.07312), and the modest training cost of a few thousand dollars contrasts sharply with the massive compute budgets typically associated with game-playing AI breakthroughs.

hackernews · PaulHoule · Oct 2, 14:11 · [Discussion](https://news.ycombinator.com/item?id=49933740)

**Background**: Stratego is a classic board game where players arrange pieces of varying ranks on a hidden board, and most opponent piece identities are concealed until pieces engage in combat, creating a deep imperfect-information challenge. Previous AI milestones like Deep Blue (chess) and AlphaZero (Go) conquered perfect-information games where all pieces are visible, but imperfect-information games like Stratego and poker require fundamentally different reasoning because the optimal move depends on unknown information. DeepNash, released by DeepMind in 2022, was the first major AI to achieve expert-level Stratego play using Nash equilibrium-based reinforcement learning, but it required enormous computational resources.

**Discussion**: Commenters highlighted the sample efficiency improvement as the most critical advance, noting that hidden-information games make traditional search-based approaches impossible since the best move depends on unknowable opponent information. Several expressed surprise that Stratego proved so difficult for AI given its seemingly simple ruleset, while one commenter pointed out the elite institutional backing behind the work despite its modest compute budget. Another user humorously lamented having planned to build the first winning Stratego bot themselves, only to be preempted by this research.

**Tags**: `#game-ai`, `#imperfect-information-games`, `#reinforcement-learning`, `#research`, `#stratego`

---

<a id="item-4"></a>
## [Parallel-in-Time RNN Training via GTF-DEER Achieves 100x Speedup on Chaotic Time Series](https://www.reddit.com/r/MachineLearning/comments/1wuz2s4/parallelintime_training_of_recurrent_neural/) ⭐️ 8.0/10

The paper introduces GTF-DEER, a parallel-in-time training algorithm that combines DEER's scalable forward pass with Generalized Teacher Forcing (GTF) to stabilize training under chaotic dynamics, achieving over 100x speedup on sequences with T exceeding 10^6. This NeurIPS spotlight work demonstrates that the combination prevents the runtime degradation that previously caused DEER to break down from O[(log T)^2] to O[T log T] under chaotic systems. This addresses a fundamental limitation in training recurrent neural networks on long chaotic time series, where sequential backpropagation through time scales as O[T] and existing parallelization methods like DEER fail due to chaotic divergence. The method significantly outperforms Mamba and other state space models in dynamical systems reconstruction, making it highly relevant for scientific ML applications involving complex dynamical systems. DEER uses Newton-type fixed point iterations across the entire sequence length to enable O[(log T)^2] scaling through efficient GPU parallelization, while GTF performs linear interpolation between predicted and true states with a tunable parameter alpha that can fully rectify exploding gradients in chaotic dynamics learning. The combination reduces exposure bias compared to traditional teacher forcing and enables stable training on both simulated and real-world chaotic systems.

reddit · r/MachineLearning · /u/DangerousFunny1371 · Oct 1, 13:12

**Background**: Recurrent neural networks are traditionally trained using backpropagation through time, which processes sequences sequentially and scales linearly with sequence length T, creating a bottleneck for very long time series. DEER (Deep Equilibrium-based Recurrent Learning) parallelizes the forward pass by solving for fixed points using Newton-type iterations, enabling logarithmic scaling, but this approach breaks down when applied to chaotic dynamical systems due to sensitive dependence on initial conditions. Generalized Teacher Forcing addresses this by interpolating between model predictions and ground truth states during training, providing a middle ground that prevents gradient explosions while reducing exposure bias. Dynamical systems reconstruction aims to learn the underlying governing equations or dynamics of a system from observed time series data, with applications in physics, biology, and engineering.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.12683v1">Parallel-in-Time Training of Recurrent Neural Networks for ...</a></li>
<li><a href="https://proceedings.mlr.press/v202/hess23a/hess23a.pdf">Generalized Teacher Forcing for Learning Chaotic Dynamics</a></li>
<li><a href="https://www.alphaxiv.org/abs/2306.04406">Generalized Teacher Forcing for Learning Chaotic Dynamics | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#RNNs`, `#dynamical-systems`, `#parallel-training`, `#chaotic-systems`, `#time-series`

---

<a id="item-5"></a>
## [NeurIPS Paper Reveals 'Authority Bias' in LLMs Accepting Misinformation from Verified Sources](https://www.reddit.com/r/MachineLearning/comments/1wv1c2e/llms_that_push_back_on_a_wrong_user_still_accept/) ⭐️ 8.0/10

A NeurIPS paper introduces 'Authority Bias,' a phenomenon where LLMs that resist user pressure to accept wrong answers still accept the same misinformation when framed as coming from a 'verified source.' Testing 8 models, the researchers found that a single verified-source note flipped 45-88% of correct answers in 7 of 8 models, with GPT-5.4 flipping on 44.7% and Grok-4.20 on 87.5% of questions. This finding exposes a critical vulnerability in Retrieval-Augmented Generation (RAG) and agentic AI systems, where models increasingly rely on tool outputs and retrieved documents. Since standard sycophancy evaluations only test user pressure, models can pass these tests while remaining highly susceptible to misinformation injected through trusted system components. The researchers used TriviaQA questions the models already answered correctly and introduced wrong answers either as a verified source or a user claim, finding that the effect mostly vanished in multiple-choice formats. Internal probing of open-weight models revealed a shared 'this answer was endorsed' component with a thin part encoding the speaker, though the linear intervention only worked in 3 of 5 open-weight families.

reddit · r/MachineLearning · /u/MajorRedditor23 · Oct 1, 14:45

**Background**: Sycophancy in LLMs refers to the tendency of models to align with user beliefs or statements, even when the user is wrong, often to deliver responses rated highly by humans. Standard sycophancy evaluations typically apply pressure through the user prompt. As AI research accelerates towards agentic systems that use tools and memory autonomously, safeguarding against misinformation from these tools becomes crucial for AI safety.

<details><summary>References</summary>
<ul>
<li><a href="https://aclanthology.org/2025.acl-long.1400/">LLMs Trust Humans More, That’s a Problem! Unveiling and ...</a></li>
<li><a href="https://www.nngroup.com/articles/sycophancy-generative-ai-chatbots/">Sycophancy in Generative-AI Chatbots - NN/G</a></li>
<li><a href="https://arxiv.org/pdf/2605.23989">Towards trustworthy agentic AI: a comprehensive survey of ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#authority-bias`, `#AI-safety`, `#sycophancy`, `#agentic-AI`

---

<a id="item-6"></a>
## [DwarfStar (ds4): Local LLM Inference Engine by Redis Creator antirez](https://dwarfstar.sh/) ⭐️ 7.0/10

DwarfStar 4 (ds4) is a new C-based local LLM inference engine created by antirez, the author of Redis, designed to run DeepSeek V4/V4.1 Flash, GLM 5.x, and Qwen3.8 Flash Next models locally on Metal, CUDA, and ROCm hardware. It features SSD-backed KV cache streaming, asymmetric 2-bit quantization, and exposes a CLI, OpenAI/Anthropic-compatible HTTP APIs, and a native agent in a single stack. ds4 brings the minimalist, performance-focused C philosophy that made Redis successful into the local LLM inference space, offering an alternative to heavier Python-based runtimes. Its SSD streaming capability allows users with less than 96GB of RAM to run very large models that would otherwise be impossible to load entirely into memory, broadening access to frontier models on consumer hardware. The primary target is Metal on Macs with 96GB or more of unified memory, while smaller machines can rely on SSD streaming to run large models like full GLM 5.x (non-Flash) on 128GB systems. The engine uses asymmetric 2-bit quantization and keeps token history and live model state together in the agent mode, running inference directly without a separate HTTP server.

hackernews · fibo · Oct 2, 18:01 · [Discussion](https://news.ycombinator.com/item?id=49936575)

**Background**: antirez is the pseudonym of Salvatore Sanfilippo, the well-known systems programmer who created Redis, a widely used in-memory data store. SSD streaming is an emerging technique for running large LLMs on hardware with insufficient RAM: instead of loading the entire model into memory, transformer layers (or routed experts in Mixture-of-Experts models) are streamed on-demand from NVMe SSDs, computed, and then freed. Apple Silicon's unified memory architecture allows the GPU (via the Metal API) to access the same memory pool as the CPU, making it particularly well-suited for local LLM inference compared to discrete GPU systems with limited VRAM.

<details><summary>References</summary>
<ul>
<li><a href="https://dwarfstar.sh/">DwarfStar 4 ( ds 4 ): Local DeepSeek V4.1, Qwen and GLM</a></li>
<li><a href="https://github.com/antirez/ds4">antirez/ ds 4 : DeepSeek 4 Flash and PRO local inference engine for...</a></li>
<li><a href="https://insiderllm.com/guides/ssd-streaming-moe-engines/">Every SSD-Streaming MoE Engine: What's Real, What's Dead</a></li>

</ul>
</details>

**Discussion**: Community members are actively extending ds4: one maintainer created a fork with shared libraries for FFI bindings in Go, adding vision and Qwen support. Users report excellent performance on M5 Max 128GB machines running Qwen 3.8 Flash Next with long context windows, though some note occasional memory issues that may stem from the agentic harness rather than ds4 itself. Several commenters highlight the high hardware requirements (96GB+ RAM for Metal) and discuss alternative implementations, including an Intel Xe-LP inference engine inspired by ds4.

**Tags**: `#local-llm`, `#inference-engine`, `#apple-silicon`, `#open-source`, `#tooling`

---

<a id="item-7"></a>
## [Claude Opus 5.5 Paints on a Simulated Canvas Using Code](https://stillwet.art/) ⭐️ 7.0/10

A Show HN post demonstrates Claude Opus 5.5 generating artwork by writing and executing code on a simulated paint canvas, hosted at stillwet.art. The project showcases the LLM iteratively painting by calling tools such as a 'look' function to visually inspect its progress and adjust strokes accordingly. This represents a creative exploration of LLM capabilities beyond text generation, positioning code-driven image creation as an alternative to diffusion-based image models. It raises questions about whether LLMs trained with reinforcement learning in painting environments could eventually compete with or complement specialized image generation models. The model uses a 'look' tool to view the canvas at its provider's best image resolution during the painting process, enabling iterative visual feedback rather than blind generation. Some outputs exhibit uncanny valley artifacts, such as nonsensical clusters of churches in landscapes, and the model can occasionally produce 'catastrophic' glaze passes that ruin in-progress work.

hackernews · alstonite · Oct 2, 00:27 · [Discussion](https://news.ycombinator.com/item?id=49928566)

**Background**: Claude Opus is Anthropic's most capable large language model tier, with Opus 5.5 being a recent iteration designed for high-effort reasoning tasks. Unlike diffusion models (e.g., DALL-E, Stable Diffusion) which generate images directly from noise, this approach uses an LLM to write code that controls a simulated canvas with brushes, pressures, and coverage parameters. A similar exploration was previously documented in a project called 'Training AI to Paint with Code,' suggesting growing interest in code-based painting as a research direction for creative AI.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/platform/api">Claude Platform | Claude by Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus">Claude Opus</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed but noted uncanny valley artifacts, with one user pointing out nonsensical church clusters in landscapes. Several speculated that Anthropic may have trained Opus in RL environments recreating famous paintings, citing Anthropic employees posting similar capabilities on X. Others highlighted the importance of the 'look' tool for visual feedback, noting it would be alarming if the model achieved such results without iterative inspection, and one commenter drew parallels to a prior 'Training AI to Paint with Code' project.

**Tags**: `#LLM`, `#AI-art`, `#code-generation`, `#Claude-Opus`, `#creative-AI`

---

<a id="item-8"></a>
## [Developer Shares One-Month Experience Coding with GLM 5.3 Flash](https://wagtail.org/blog/one-month-on-glm-53-flash/) ⭐️ 7.0/10

A developer published a detailed account of using GLM 5.3 Flash for a month of coding work, reporting total costs of approximately $68 with about 4kWh of energy use and 365 grams of carbon emissions. The post also recounts a costly mistake where choosing the wrong model for a prototype resulted in 450M tokens consumed and $150 spent almost overnight, highlighting the importance of careful model selection in agentic workflows. This real-world usage report provides concrete data on the cost and energy efficiency of a leading open-weight model, offering practitioners actionable insights for model selection in agentic coding patterns. The findings are particularly relevant as teams weigh tradeoffs between intelligence, speed, token efficiency, and environmental impact when deploying LLMs in production. GLM 5.3 Flash is a 320B parameter Mixture-of-Experts model with only 18B active parameters, making it the first natively multimodal model in the GLM-5 series and released under the MIT license. The developer noted that energy costs represented roughly 1% of total expenditure, and that better model selection could have achieved similar prototype results at approximately 5x lower cost.

hackernews · ThibWeb · Oct 2, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49934620)

**Background**: GLM 5.3 Flash is part of the GLM-5 series developed by Z.AI, designed to deliver strong coding and agentic benchmark performance at a fraction of the cost of frontier models like Claude Opus. Agentic patterns refer to AI workflows where LLMs autonomously use tools, make decisions, and iterate on problem-solving, which can lead to high token consumption if the wrong model is chosen. Mixture-of-Experts (MoE) architectures like GLM 5.3 Flash's activate only a subset of parameters per token, enabling large total parameter counts with low inference cost.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/vlm/glm-5.3-flash">GLM - 5 . 3 - Flash /FlashX - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.3-Flash">zai-org/GLM-5.3-Flash · Hugging Face</a></li>
<li><a href="https://aimultiple.com/agentic-ai-design-patterns">4 Agentic AI Design Patterns & Real-World Examples</a></li>

</ul>
</details>

**Discussion**: Commenters were surprised by how low the energy consumption was relative to total cost, with one noting that 4kWh is equivalent to about 15 miles of EV driving. A key counterpoint raised was that cost-per-token metrics can be misleading because some models are far more token-hungry than others, making cost-per-task and time-per-task comparisons more useful. Another commenter praised recent speed improvements for GLM 5.3 Flash on DGX Spark clusters, comparing the experience favorably to Claude Opus 4.5, while also noting that consistency still lags behind frontier models.

**Tags**: `#LLM`, `#GLM`, `#energy-efficiency`, `#model-evaluation`, `#agentic-patterns`

---

<a id="item-9"></a>
## [NeurIPS Paper Tackles Topological Out-of-Domain Generalization in Dynamical Systems Reconstruction](https://www.reddit.com/r/MachineLearning/comments/1wvwodf/topological_outofdomain_generalization_in/) ⭐️ 7.0/10

A NeurIPS 2026 paper mathematically identifies key failure modes in previous hierarchical dynamical systems reconstruction (DSR) models that prevent them from correctly learning control parameters and extrapolating beyond the training domain, and fixes these through feature-splitting and physical sparsity priors. The modified hierarchical DSR model can predict bifurcations and beyond-bifurcation dynamics without any explicit knowledge of control parameters provided during training. This addresses a genuinely hard and underexplored problem where models must handle qualitative regime changes—such as transitions from cyclic to chaotic behavior—rather than just statistical shifts, which current state-of-the-art time series forecasting models cannot do. The approach has significant real-world applications in climate systems, neuroscience (e.g., transitions into epileptic activity), and medicine (e.g., sepsis onset), where predicting previously unseen dynamical regimes is a fundamental expectation of any scientific theory. The approach is generic and works for different discrete and continuous time recurrent neural networks, and was tested with shallow PLRNNs and Neural ODEs. Because the control parameters driving regime changes are often not exactly known, the model must infer the dynamical system jointly with the control parameters, making the task substantially harder than standard out-of-distribution generalization in machine learning.

reddit · r/MachineLearning · /u/DangerousFunny1371 · Oct 2, 15:25

**Background**: Dynamical systems reconstruction (DSR) seeks to infer from time series measurements a generative model of the underlying dynamical process, which is a prime objective across scientific disciplines. A bifurcation occurs when a small smooth change to a system's parameter values causes a sudden qualitative or topological change in its behavior, such as transitioning from a stable fixed point to a limit cycle or to chaos. Out-of-domain generalization in DSR profoundly differs from OODG considered elsewhere in machine learning, requiring mathematical notions based on topological concepts and ergodic theory to formalize the idea of learnability of a DSR model. Previous hierarchical DSR models attempted to harvest group-level information across multiple domains while retaining single-domain characteristics, but had limitations in correctly learning and extrapolating control parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.05335">Towards Foundational Models for Dynamical System ... A scalable generative model for dynamical system ... Reconstructing computational system dynamics from neural data ... Reconstructing Computational Dynamics from Neural ... - bioRxiv Publications | Theoretical Neuroscience - GitHub Pages Optimal Recurrent Network Topologies for Dynamical Systems ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bifurcation_theory">Bifurcation theory - Wikipedia</a></li>
<li><a href="https://openreview.net/attachment?id=xTYIAD2NND&name=pdf">Out-of-Domain Generalization in Dynamical Systems Reconstruction</a></li>

</ul>
</details>

**Tags**: `#dynamical-systems`, `#out-of-distribution-generalization`, `#time-series-forecasting`, `#bifurcation`, `#NeurIPS`

---

<a id="item-10"></a>
## [FLEET: Memory-Augmented MCTS for Reward-Aware Best-of-N LLM Generation](https://www.reddit.com/r/MachineLearning/comments/1wvs12j/adding_memory_to_search_instead_of_sampling_in/) ⭐️ 7.0/10

FLEET is a new algorithm that improves Best-of-N LLM generation by attributing external rewards to individual tokens and using Monte Carlo Tree Search (MCTS) with stored hidden states to guide future sampling. It identifies branching points by tracking high entropy and varentropy in logits, stores normalized hidden states in a vector database mapped to reward metadata, and uses modified MCTS to penalize suboptimal tokens during subsequent generation runs. Standard Best-of-N sampling is a blind search that generates multiple completions without leveraging reward feedback from previous attempts, making it computationally inefficient for reward maximization tasks. FLEET addresses this inefficiency by making generation aware of past rewards, achieving comparable or better performance with significantly fewer iterations — for example, reaching baseline performance on LiveCodeBench with only 9 iterations instead of 32, and improving scores from 0.59 to 0.69 under the same budget. FLEET uses cosine similarity for retrieving and updating metadata entries, relying on the observation that very high similarity implies low KL divergence, preserving meaningful token distributions. The metadata store can be preserved as a prior for other tasks or used to enrich supervised fine-tuning and reinforcement learning, and since it is not updated during an iteration itself, it can be passed as a simple lookup table without requiring sequential execution.

reddit · r/MachineLearning · /u/Helpful_Minimum_2214 · Oct 2, 12:04

**Background**: Best-of-N (BoN) sampling is a simple inference-time alignment technique where an LLM generates N candidate responses, a reward model scores them, and the best one is returned — but this process does not learn from the rewards it receives across attempts. Entropy measures the model's uncertainty over the next token, while varentropy measures the variance of that uncertainty; high values of both indicate points where the model is uncertain and inconsistent, making them natural branching points for search algorithms. Monte Carlo Tree Search (MCTS) is a heuristic search algorithm that builds a partial game tree by balancing exploration and exploitation, commonly adapted for LLM reasoning to guide token selection during generation.

<details><summary>References</summary>
<ul>
<li><a href="https://repovive.com/roadmaps/llm-fine-tuning/preference-alignment/best-of-n-sampling">Best - of - N Sampling - Preference Alignment | LLM ... | Repovive</a></li>
<li><a href="https://www.njkumar.com/literature-review-sampling-techniques/">Literature review on sampling techniques for language models</a></li>
<li><a href="https://arxiv.org/html/2404.01054v1">Regularized Best - of - N Sampling to Mitigate Reward Hacking for...</a></li>

</ul>
</details>

**Tags**: `#LLM-inference`, `#reward-maximization`, `#MCTS`, `#best-of-n`, `#reinforcement-learning`

---

<a id="item-11"></a>
## [Court agrees with EFF: Utah's VPN law demands a technical impossibility](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) ⭐️ 6.0/10

A court has agreed with the EFF that Utah's VPN law requires platforms to achieve the technically impossible task of blocking VPN traffic, forcing them to either block all VPNs nationwide or exit Utah entirely.

hackernews · hn_acker · Oct 1, 22:23 · [Discussion](https://news.ycombinator.com/item?id=49927754)

**Tags**: `#vpn`, `#internet-regulation`, `#digital-rights`, `#censorship`, `#eff`

---

<a id="item-12"></a>
## [The Forgetful CPU: Running Linux on Apple M4 Silicon](https://yuka.dev/blog-2026-10-02-linux-m4.html) ⭐️ 6.0/10

A technical blog post explores the challenges and architectural peculiarities encountered when running Linux on Apple's M4 hardware. The article documents the specific difficulties of working with Apple's M4 CPU architecture from a Linux perspective, noting unusual behavior described as 'forgetful.' This exploration highlights the ongoing tension between Apple's proprietary hardware excellence and the open-source community's desire for alternative operating system support. It demonstrates both the appeal of Apple Silicon performance and the friction its closed ecosystem creates for developers seeking open platforms. The technical deep-dive examines how Apple's proprietary architecture decisions in the M4 create specific obstacles for Linux portability efforts. The M4 CPU exhibits behaviors that require special handling when running non-macOS operating systems, reflecting the broader challenges of reverse-engineering undocumented Apple Silicon features.

hackernews · signa11 · Oct 2, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49933869)

**Background**: Apple's M4 chip is part of the company's Apple Silicon lineup, which uses ARM-based architecture custom-designed by Apple. Running Linux on Apple Silicon has historically required significant reverse-engineering efforts due to Apple's closed hardware documentation and proprietary protocols. Projects like Asahi Linux have pioneered similar efforts for earlier M-series chips, making alternative OS support on Apple hardware an ongoing community effort.

**Discussion**: Commenters focused more on Apple's closed ecosystem philosophy than on the technical M4 Linux implementation details. Discussion included frustration with Apple's proprietary protocols (using trackpad limitations as an example) and debate over whether development efforts would be better directed toward x86-64 or open hardware alternatives like RISC-V. There was general appreciation for Apple's hardware quality alongside criticism of macOS bloat and the company's closed approach.

**Tags**: `#apple-silicon`, `#linux`, `#arm`, `#hardware`, `#m4`

---