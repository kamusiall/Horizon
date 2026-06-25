---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 36 items, 10 important content pieces were selected

---

1. [OpenAI Unveils First Custom AI Inference Chip 'Jalapeño' Built with Broadcom](#item-1) ⭐️ 9.0/10
2. [Anthropic Accuses Alibaba of Illicitly Extracting Claude AI Model Capabilities](#item-2) ⭐️ 8.0/10
3. [Qualcomm to Acquire Modular in ~$4 Billion Deal](#item-3) ⭐️ 8.0/10
4. [Superhuman Generals.io Agent Built with Self-Play RL and JAX](#item-4) ⭐️ 8.0/10
5. [MuJoFil: GPU-Native Simulator for High-Fidelity Vision RL Training](#item-5) ⭐️ 7.0/10
6. [DeepSWE: A New Contamination-Free Benchmark for LLM Coding Agents](#item-6) ⭐️ 7.0/10
7. [Cloudflare launched self-managed OAuth for all](#item-7) ⭐️ 6.0/10
8. [RubyLLM: A Unified Ruby Framework for Major AI Providers](#item-8) ⭐️ 6.0/10
9. [Simon Willison converts MDN browser-compat-data into a SQLite database for LLMs and MCP](#item-9) ⭐️ 6.0/10
10. [LLM Inference Pricing Comparison Across 7 Providers Reveals Caching Impact](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils First Custom AI Inference Chip 'Jalapeño' Built with Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI has unveiled Jalapeño, its first custom AI inference chip, designed in collaboration with Broadcom and manufactured by TSMC, with the entire design-to-production cycle completed in just nine months using AI-assisted optimization. The chip is a massive reticle-sized ASIC purpose-built for large language model inference rather than general-purpose GPU compute. This announcement marks OpenAI's deepest move yet into vertical integration of AI infrastructure, extending its control from models and software down to custom silicon, which could significantly reduce inference costs for ChatGPT, Codex, and API products. It also signals a broader industry trend where leading AI companies are building their own chips to break free from dependence on NVIDIA GPUs for inference workloads. Jalapeño is specifically optimized for LLM inference bottlenecks including data movement costs, compute-memory balance, and networking efficiency, rather than being a general-purpose accelerator. OpenAI claims its own AI models were used to accelerate parts of the chip design and optimization process, though specifics on this AI-assisted design workflow remain limited.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: Inference is the computing phase where a trained AI model processes user requests and generates responses, and it represents the dominant ongoing operational cost for AI companies serving millions of users. While NVIDIA GPUs like the H100 and B200 are currently the industry standard for both training and inference, they are general-purpose processors, meaning purpose-built ASICs can potentially achieve much better efficiency for specific workloads. Broadcom has established itself as a key partner for custom AI silicon, having previously collaborated with Google on its TPU chips. The nine-month development cycle is notably fast for a chip of this scale, as traditional custom silicon projects typically take 18-24 months from design to production.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models">OpenAI unveils first custom AI inference chip, Jalapeño, with Broadcom — and its development was sped-up with OpenAI's own models | VentureBeat</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle">Broadcom and OpenAI unveil custom-built Jalapeño inference processor — OpenAI's first chip is a massive reticle-sized ASIC built in an ultra-fast nine-month development cycle | Tom's Hardware</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about OpenAI's claims of AI-accelerated chip design, with one noting that without more specifics it reads like marketing hype. Several users questioned why OpenAI would publicly unveil the chip at all, suggesting it amounts to giving away competitive intelligence for stock hype. Technical discussion included speculation about novel inference architectures, with one commenter proposing chips with weights baked into ROM for massive throughput, and another pointing to startup Taalas which is literally burning LLM models into silicon for claimed cost and latency wins.

**Tags**: `#OpenAI`, `#custom-silicon`, `#AI-chips`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [Anthropic Accuses Alibaba of Illicitly Extracting Claude AI Model Capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 8.0/10

Anthropic has publicly accused Alibaba of illicitly extracting capabilities from its Claude AI model, likely through techniques such as model distillation or model extraction attacks. The accusation suggests that Alibaba queried the Claude API extensively to reconstruct or transfer knowledge from the proprietary model into its own systems. This dispute highlights the growing tension between closed and open AI model providers over intellectual property enforcement, as distillation practices become a common industry shortcut for building competitive models cheaply. The outcome could set precedents for how AI companies legally protect model outputs and whether API-based access can be policed against unauthorized training. Model extraction attacks can theoretically clone a proprietary LLM for as little as $50 in API costs by systematically querying the model and using its responses to train a replica. Knowledge distillation, the more targeted method, involves using a large 'teacher' model to directly inform or fine-tune a smaller 'student' model, a practice thousands of businesses already perform daily.

hackernews · htrp · Jun 24, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48664814)

**Background**: Knowledge distillation is a machine learning technique where a larger, more computationally expensive model (the teacher) transfers knowledge to a smaller, more efficient model (the student) without significant loss of validity. Model extraction attacks are a related confidentiality threat where an adversary queries a deployed model through its normal inference surface to reconstruct the model itself or extract confidential properties of its training data. These techniques have become central to industry debates as companies use outputs from proprietary models like GPT-4 or Claude to train their own competing models at a fraction of the original training cost.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation</a></li>
<li><a href="https://beyondscale.tech/blog/ai-model-extraction-attacks-defense-guide">AI Model Extraction Attacks : Stop LLM Theft | BeyondScale</a></li>
<li><a href="https://secportal.io/vulnerabilities/model-extraction-attack">Model Extraction Attack Guide | SecPortal</a></li>

</ul>
</details>

**Discussion**: Community sentiment is highly skeptical of Anthropic's motives, with commenters quick to point out that Anthropic itself was recently ruled to have infringed copyright by downloading millions of books from pirate sites. Several users noted that distillation is a widespread industry practice and framed the accusation as a defensive move to protect IPO valuations from the threat of open-source models becoming 'good enough.' Others highlighted the irony of companies that crawled the entire internet to build their models now complaining about being copied.

**Tags**: `#AI`, `#distillation`, `#intellectual-property`, `#anthropic`, `#alibaba`

---

<a id="item-3"></a>
## [Qualcomm to Acquire Modular in ~$4 Billion Deal](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm announced its acquisition of Modular, the AI startup behind the Mojo programming language and the MAX AI serving platform, in a deal reportedly valued at around $4 billion. The acquisition brings Modular's compiler technology and AI infrastructure stack under Qualcomm's hardware-focused umbrella. This acquisition signals Qualcomm's aggressive push into AI infrastructure and compiler technology, positioning the company to compete more broadly in AI compute beyond its traditional mobile chip business. The deal also raises questions about the future of Mojo as a cross-platform language, since Modular's founder had previously criticized hardware companies for failing to build effective AI stacks. Modular's MAX platform is a high-performance AI inference and serving framework with advanced optimizations like speculative decoding and graph compiler optimizations, while Mojo is a Python-like systems programming language built on the MLIR compiler framework that targets CPUs, GPUs, TPUs, and other accelerators. Mojo had committed to open-sourcing the language in fall 2026, and as of June 2026 the compiler remains closed source with an open standard library.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: Modular was founded by Chris Lattner, the creator of LLVM and Swift, to build AI infrastructure that addresses the fragmentation of AI compute across different hardware backends. Mojo was designed to combine Python's usability with the performance of systems languages like C++ and Rust, leveraging MLIR (Multi-Level Intermediate Representation) to compile code for heterogeneous accelerators. The MAX platform provides production-grade AI serving with optimized kernels for CPUs and GPUs, and Modular's GitHub repository includes over 450,000 lines of code from more than 6,000 contributors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://docs.modular.com/max/intro/">What is Modular | Modular</a></li>
<li><a href="https://github.com/modular/modular">GitHub - modular/modular: The Modular Platform (includes MAX & Mojo) · GitHub</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed, with some expressing disappointment that Mojo may join the list of cross-platform AI languages that never truly became cross-platform, while others note that Qualcomm appears to be assembling a broad portfolio of technologies aimed at moving beyond ARM to RISC-V and becoming competitive in AI compute. One commenter pointed out the irony that Modular's founder had repeatedly criticized hardware companies for failing to build effective AI stacks, yet Modular is now being acquired by one.

**Tags**: `#qualcomm`, `#modular`, `#mojo`, `#ai-compilers`, `#acquisition`

---

<a id="item-4"></a>
## [Superhuman Generals.io Agent Built with Self-Play RL and JAX](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

A developer trained a self-play reinforcement learning agent for Generals.io that achieved superhuman performance and ranked #1 on the human 1v1 leaderboard. The project reimplemented the entire pipeline in JAX and replaced the CNN with a Vision Transformer, with the full codebase including a fast JAX simulator open-sourced. This demonstrates that scaling compute and architecture—rather than relying on human priors and ad-hoc patches—can produce superhuman agents in complex, imperfect-information real-time strategy games. The open-source release of both the agent and the JAX simulator provides a valuable resource for RL researchers and practitioners working on similar environments. The pipeline was migrated from NumPy/Torch to JAX for faster simulation and training, and the architecture was switched from a CNN to a Vision Transformer to leverage higher model capacity. The developer's blog is written as a detailed guide covering dead ends, design decisions, and practical intuitions for building similar systems.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Generals.io is a complex, imperfect-information real-time strategy game where players compete for territory on a grid. Self-play reinforcement learning is a technique where agents improve by playing against copies of themselves, famously used in systems like AlphaZero. JAX is a Python library developed by Google for high-performance numerical computing and large-scale machine learning, optimized for GPU/TPU acceleration. Vision Transformers (ViT) are transformer-based architectures for computer vision that process images as sequences of patches, offering higher capacity than traditional CNNs at the cost of data efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://en.wikipedia.org/wiki/JAX_(software)">JAX (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#self-play`, `#JAX`, `#game-AI`, `#open-source`

---

<a id="item-5"></a>
## [MuJoFil: GPU-Native Simulator for High-Fidelity Vision RL Training](https://www.reddit.com/r/MachineLearning/comments/1uemrch/mujoco_derived_simulator_for_high_fidelity_vision/) ⭐️ 7.0/10

A new open-source simulator called MuJoFil has been introduced, combining Nvidia's GPU-native Newton Physics Engine with a modified version of Google's Filament render engine. It is designed to enable highly parallelized, high-fidelity vision-based reinforcement learning training and is currently available for installation via PyPI. This project addresses a key bottleneck in vision-based reinforcement learning by providing a free, GPU-native alternative to MuJoCo's CPU-bound limitations and Nvidia Isaac Sim's high hardware and licensing requirements. By supporting realistic environments with physically based rendering (PBR) textures and common formats like GLB and OpenUSD, it could significantly improve accessibility and sim-to-real transfer for robotic policies. MuJoFil leverages Nvidia's Newton engine, which is built on NVIDIA Warp and integrates MuJoCo Warp as its primary backend, alongside a heavily modified Google Filament engine optimized for parallel GPU rendering. Users can install the CPU variant using `pip install mujofil` or the CUDA-supporting GPU variant using `pip install mujofil-warp`, though the author notes the project is still in active development and may contain bugs.

reddit · r/MachineLearning · /u/MT1699 · Jun 24, 19:07

**Background**: MuJoCo is a widely used physics simulator for robotics and reinforcement learning, but its traditional CPU-bound nature limits parallelization for vision-based tasks. Nvidia's Newton Physics Engine is a newer, open-source, GPU-accelerated engine built on NVIDIA Warp—developed with Google DeepMind and Disney Research—that integrates MuJoCo Warp as its primary backend. Google's Filament is a real-time physically based rendering (PBR) engine designed for high-quality 2D and 3D graphics across multiple platforms, which MuJoFil modifies to render multiple simulations in parallel natively on the GPU.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>
<li><a href="https://github.com/google/filament">GitHub - google/filament: Filament is a real-time physically ...</a></li>
<li><a href="https://mujoco.org/">MuJoCo — Advanced Physics Simulation</a></li>

</ul>
</details>

**Tags**: `#Reinforcement Learning`, `#Simulation`, `#Robotics`, `#Computer Vision`, `#Open Source`

---

<a id="item-6"></a>
## [DeepSWE: A New Contamination-Free Benchmark for LLM Coding Agents](https://www.reddit.com/r/MachineLearning/comments/1ue0hlp/deepswe_new_benchmark_looking_at_how_well_todays/) ⭐️ 7.0/10

DeepSWE is a new open-source benchmark that evaluates frontier LLM coding agents on original, long-horizon software engineering tasks written from scratch across 91 repositories and 5 programming languages. Unlike existing benchmarks, its tasks are contamination-free—meaning no model has seen the solutions during pretraining—and solutions require 5.5x more code than SWE-bench Pro despite prompts being roughly half the length. This benchmark addresses critical limitations of existing coding benchmarks like SWE-bench Pro by testing real-world complexity and preventing data contamination, which has become a growing concern as benchmarks saturate and models may have memorized solutions. It provides a more reliable signal for how well today's frontier coding agents actually perform in genuine software engineering work, which is essential for researchers, model developers, and enterprises adopting AI coding tools. DeepSWE uses hand-written verifiers that test software behavior rather than implementation details, ensuring that solutions are evaluated on correctness rather than code style. The benchmark is open-source and available on GitHub, with results tracked across multiple frontier models including GPT and Claude variants.

reddit · r/MachineLearning · /u/we_are_mammals · Jun 24, 02:03

**Background**: SWE-bench and its variants (SWE-bench Verified, SWE-bench Pro) have been the dominant benchmarks for evaluating LLM-based coding agents on real-world software engineering tasks, typically drawn from GitHub issues and pull requests. As models have improved, these benchmarks have begun to saturate, prompting concerns that models may have seen solutions during pretraining (data contamination) and that tasks may not reflect the full complexity of real engineering work. DeepSWE, created by Datacurve, aims to address these gaps by introducing original tasks that require significantly more complex, long-horizon solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://deepswe.datacurve.ai/">DeepSWE</a></li>
<li><a href="https://www.linkedin.com/posts/xiang-d_github-scaleapiswe-benchpro-os-swe-bench-activity-7375744754174771200-WMSV">Introducing SWE - Bench Pro : A New Benchmark for Coding... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#code-generation`, `#LLM-agents`, `#software-engineering`, `#evaluation`

---

<a id="item-7"></a>
## [Cloudflare launched self-managed OAuth for all](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 6.0/10

Cloudflare launched self-managed OAuth for all accounts, enabling users to create and manage their own OAuth clients that integrate with Cloudflare as a more secure and user-friendly alternative to API tokens. Opening up OAuth to all customers is an important step toward a broader Cloudflare app ecosystem, allowing developers to build integrations with delegated access and scoped permissions rather than relying solely on static API keys. The feature allows developers to create self-managed OAuth clients that integrate with Cloudflare, providing a more secure, user-friendly, and manageable alternative to API tokens. The underlying implementation appears to use Ory Hydra, with the author noting that CPU usage is remarkably small even at Cloudflare's scale.

hackernews · terryds · Jun 25, 02:18 · [Discussion](https://news.ycombinator.com/item?id=48668033)

**Background**: OAuth 2.0 is an authorization framework that allows third-party applications to obtain limited access to a user's account without exposing credentials, typically through scoped access tokens. Self-managed OAuth clients let developers register and control their own OAuth applications rather than relying on a provider-managed flow. Cloudflare already exposes its API as an MCP server supporting OAuth and dynamic client registration, which some community members note makes the lack of DCR support in this new offering somewhat ironic.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/oauth-for-all/">Unlocking the Cloudflare app ecosystem with OAuth for all</a></li>
<li><a href="https://cloudflare-docs.cloudflare-docs.workers.dev/changelog/post/2026-06-03-public-oauth-clients/">Introducing self - managed OAuth clients · Changelog</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some praise the technical achievement and the use of Ory Hydra at scale, while others argue OAuth is overly complex for simple server-to-server use cases where scoped API keys with rotation and audit logs suffice. The Ory Hydra author chimed in to express excitement, and several commenters clarified that this is specifically about OAuth for accessing Cloudflare accounts rather than a generic login solution for custom apps.

**Tags**: `#oauth`, `#cloudflare`, `#authentication`, `#developer-tools`, `#infrastructure`

---

<a id="item-8"></a>
## [RubyLLM: A Unified Ruby Framework for Major AI Providers](https://rubyllm.com/) ⭐️ 6.0/10

RubyLLM is a Ruby framework that provides a unified API for interacting with all major AI providers, allowing developers to build chatbots, AI agents, and RAG applications. The framework aims to offer a delightful and expressive developer experience for integrating various AI models into Ruby applications. This framework simplifies the integration of multiple AI providers for Ruby developers, reducing the complexity of switching between different APIs and enabling faster development of AI-powered features. It provides a native Ruby-like experience for AI workflows, which is valuable for the Ruby ecosystem as AI adoption grows. While the API design is highly praised, users have reported edge-case bugs such as caching issues with certain providers like xAI. There are also concerns regarding maintainer responsiveness to pull requests and the merging of low-quality contributions.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: RubyLLM acts as an abstraction layer over different Large Language Model (LLM) APIs, similar to frameworks like Vercel's AI SDK but tailored for the Ruby programming language. It allows developers to use a single interface to access models from various providers, supporting features like chat completions, tool use, and Retrieval-Augmented Generation (RAG).

<details><summary>References</summary>
<ul>
<li><a href="https://rubyllm.com/">RubyLLM | One beautiful Ruby framework for all major AI ...</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ruby_llm: One delightful Ruby framework for ...</a></li>

</ul>
</details>

**Discussion**: The community generally praises RubyLLM's API design and usability, comparing it favorably to Vercel's AI framework. However, some users express frustration with maintainer engagement, noting unmerged pull requests and edge-case bugs like caching failures with specific providers, while others highlight ecosystem projects building on top of it.

**Tags**: `#ruby`, `#llm-framework`, `#ai-providers`, `#developer-tools`, `#api-design`

---

<a id="item-9"></a>
## [Simon Willison converts MDN browser-compat-data into a SQLite database for LLMs and MCP](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 6.0/10

Simon Willison created a GitHub repository called simonw/browser-compat-db that converts Mozilla's mdn/browser-compat-data into a ~66MB SQLite database, with build scripts generated by Claude Code for web (Opus 4.8) and a GitHub Actions workflow built by Codex Desktop (GPT-5.5). The database is hosted on a GitHub orphan branch to enable open CORS headers, making it accessible via the GitHub CDN and explorable through Datasette Lite. This project makes MDN's comprehensive browser compatibility data readily available to LLMs and MCP servers in a queryable SQLite format, bridging authoritative web platform documentation with the emerging AI tooling ecosystem. It also demonstrates a practical pattern for hosting CORS-enabled SQLite databases on GitHub and showcases AI-assisted programming for building data pipelines. The build script uses sqlite-utils to convert the browser-compat-data into SQLite, and the GitHub Actions workflow force-pushes the resulting database to a `db` orphan branch because regular repository files (unlike GitHub releases) provide open CORS headers. The database can be downloaded directly or explored interactively via Datasette Lite at lite.datasette.io.

rss · Simon Willison · Jun 24, 23:59

**Background**: The Model Context Protocol (MCP) is an open standard announced by Anthropic in November 2024 for connecting AI assistants to external data sources, tools, and development environments, and has been adopted by major AI providers including OpenAI and Google DeepMind. Mozilla's mdn/browser-compat-data repository contains machine-readable browser compatibility data for web technologies such as Web APIs, JavaScript features, and CSS properties. sqlite-utils is a Python CLI utility and library for manipulating SQLite databases, enabling easy conversion of JSON and CSV data into queryable SQLite tables.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://github.com/mdn/browser-compat-data">GitHub - mdn/browser-compat-data: Browser compatibility data for Web technologies as displayed on MDN · GitHub</a></li>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library ...</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#SQLite`, `#browser-compat-data`, `#LLM-tooling`, `#developer-tools`

---

<a id="item-10"></a>
## [LLM Inference Pricing Comparison Across 7 Providers Reveals Caching Impact](https://www.reddit.com/r/MachineLearning/comments/1ueavxn/i_compiled_llm_inference_pricing_across_7/) ⭐️ 6.0/10

A Reddit user compiled a public spreadsheet comparing LLM inference pricing across seven providers including OpenRouter, DeepSeek, Together AI, Fireworks, and Groq. The comparison reveals that cached input costs vary dramatically between providers, with cache hits sometimes being tens of times cheaper than cache misses. This comparison highlights that for workloads involving agents with large system prompts, RAG pipelines, or multi-turn conversations, the caching policy can be more important than the headline token price. It also shows that the same model can vary significantly in cost depending on the provider, making provider choice a critical factor for cost optimization. The spreadsheet tracks input/output token pricing, context windows, cached input pricing, supported models, and provider-specific differences, but does not include benchmark data on latency or throughput. The author notes that comparing real throughput, cold-start times, model precision variants, egress costs, and reliability remains difficult.

reddit · r/MachineLearning · /u/Technomadlyf · Jun 24, 11:28

**Background**: Prompt caching allows LLM providers to store and reuse the results of processing long, stable prefixes in prompts, such as system instructions or retrieved documents, reducing both cost and latency for subsequent requests. This is particularly relevant for Retrieval-Augmented Generation (RAG) pipelines and agent frameworks that repeatedly send similar context. DeepSeek V4 Pro, one of the models mentioned in the comparison, is a Mixture-of-Experts model with 1.6 trillion parameters and a one-million-token context window.

<details><summary>References</summary>
<ul>
<li><a href="https://www.truefoundry.com/blog/provider-agnostic-prompt-caching-llm-gateway">Provider-Agnostic Prompt Caching : How an LLM Gateway Normalizes...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#pricing`, `#caching`, `#providers`, `#cost optimization`

---