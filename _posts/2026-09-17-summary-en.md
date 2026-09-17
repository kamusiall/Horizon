---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17
lang: en
---

> From 29 items, 9 important content pieces were selected

---

1. [Nvidia Announces Native CUDA GPU Programming Support in Rust](#item-1) ⭐️ 8.0/10
2. [TMLR Investigates Authors of Papers Slated for Desk Rejection](#item-2) ⭐️ 8.0/10
3. [GoBench: A New Benchmark Evaluating LLMs on the Game of Go](#item-3) ⭐️ 8.0/10
4. [SHADOW-50M: A 19.8 MB Ternary LLM with Built-in Calculation Circuits](#item-4) ⭐️ 8.0/10
5. [TabPFN-3.5 Released as New SOTA Tabular Foundation Model](#item-5) ⭐️ 8.0/10
6. [4B Parameter Model Trained to Generate 81% Faster Postgres Query Plans](#item-6) ⭐️ 7.0/10
7. [Xiaomi MiMo 2.6 Live Post-Training Dashboard Released](#item-7) ⭐️ 7.0/10
8. [Google Releases Gemini 3.8 Live Speech-to-Speech Models with New Web UI Tool](#item-8) ⭐️ 7.0/10
9. [LARA: Lightweight Composable Residual Adapters for Frozen LLMs](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Nvidia Announces Native CUDA GPU Programming Support in Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

Nvidia has officially announced native GPU programming support in Rust, providing two distinct tracks for developers to write GPU kernels directly in the Rust programming language. This marks a significant shift from the traditional C/C++-centric CUDA development model. This development brings Rust's memory safety guarantees and modern language features to GPU programming, potentially reducing bugs in high-performance computing and AI/ML workloads. It also signals Nvidia's recognition of Rust's growing importance in systems programming and could influence the broader GPU programming ecosystem by attracting Rust developers to CUDA. The announcement outlines two tracks for writing GPU kernels in Rust, though the specific technical implementation details are available in the full blog post. The support integrates with Nvidia's CUDA platform, which dominates the GPU computing market but raises concerns about vendor lock-in and portability to other GPU architectures.

hackernews · nonmaskable · Sep 16, 11:15 · [Discussion](https://news.ycombinator.com/item?id=49724881)

**Background**: CUDA is Nvidia's proprietary parallel computing platform that allows developers to use GPUs for general-purpose processing, traditionally accessed through C/C++. Rust is a systems programming language known for memory safety without garbage collection, increasingly adopted in performance-critical applications. GPU kernels are functions that execute on the GPU, and writing them has typically required either CUDA C++ or higher-level domain-specific languages like Triton.

**Discussion**: The community discussion centers on concerns about vendor lock-in, with several commenters worried that native CUDA support in Rust will tie code to Nvidia hardware and create the same #ifdef hell as C++ CUDA. Others see potential benefits, noting that Hugging Face's Candle Rust crate could integrate well with this new capability, while some commenters compare the approach to alternatives like Triton and Slang, and one commenter questions the writing style of the blog post itself.

**Tags**: `#Nvidia`, `#CUDA`, `#Rust`, `#GPU Programming`, `#AI/ML Tooling`

---

<a id="item-2"></a>
## [TMLR Investigates Authors of Papers Slated for Desk Rejection](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/) ⭐️ 8.0/10

TMLR's Co-Editor-in-Chief interviewed the authors of 10 papers slated for desk rejection to assess their understanding of their own submissions. The investigation revealed that only one author could adequately answer all questions, while the vast majority either could not explain basic concepts or struggled with technical details. This investigation exposes a serious integrity problem in machine learning research, likely driven by AI-generated or ghostwritten papers. It raises concerns about the vulnerability of peer review systems to fraudulent submissions and the potential erosion of trust in academic publishing. Of the ten submissions, one was withdrawn, one author was unavailable, one did not show up for a scheduled meeting, three could not answer basic questions, three struggled with technical details, and only one answered all questions but had a major flaw identified by the interviewer.

reddit · r/MachineLearning · /u/hihey54 · Sep 16, 23:20

**Background**: TMLR (Transactions on Machine Learning Research) is a journal that complements JMLR by focusing on shorter manuscripts with fast turnarounds and double-blind reviewing. Desk rejection occurs when an editor rejects a paper before sending it to peer reviewers, typically due to poor quality or scope mismatch. The proliferation of large language models has made it easier to produce convincing but potentially fraudulent research papers, challenging traditional academic integrity safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://jmlr-org.nproxy.org/tmlr/">Transactions on Machine Learning Research</a></li>
<li><a href="https://www.aischolar.com/news/article/is-desk-rejection-common">Is Desk Rejection Common?</a></li>

</ul>
</details>

**Tags**: `#academic-integrity`, `#peer-review`, `#machine-learning`, `#TMLR`, `#AI-generated-content`

---

<a id="item-3"></a>
## [GoBench: A New Benchmark Evaluating LLMs on the Game of Go](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 8.0/10

GoBench is a newly released benchmark that evaluates LLMs' reasoning ability through 9x9 Go games against a ladder of KataGo opponents ranging from random to superhuman levels. The benchmark shows that top LLMs achieve 2500-3560 Elo, significantly below superhuman KataGo at 4400 Elo, and demonstrates a strong correlation with ARC-AGI 2 (r=0.83). GoBench provides a novel and unsaturated measure of general reasoning ability for LLMs, addressing the need for benchmarks that can track progress as models continue to improve. Its strong correlation with ARC-AGI 2 suggests it captures similar reasoning skills while offering a different evaluation modality through strategic gameplay. The benchmark allows LLMs to use coding tools and two hours of preparation before evaluation, with Codex with Astra reaching 3560 Elo under these conditions compared to 2500 Elo for GPT-6 Astra max without such tools. The creator plans to maintain a live leaderboard as long as the benchmark remains unsaturated.

reddit · r/MachineLearning · /u/Roland31415 · Sep 16, 18:54

**Background**: KataGo is a widely used, open-source Go engine trained through self-play that achieves superhuman performance and is utilized by strong human Go players. ARC-AGI 2 is a challenging reasoning benchmark that emphasizes compositional rules and contextual rule use, designed to be difficult for AI while remaining relatively easy for humans. The game of Go has historically served as a prominent testbed for AI capabilities due to its strategic complexity and enormous search space.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KataGo">KataGo - Wikipedia</a></li>
<li><a href="https://arcprize.org/blog/announcing-arc-agi-2-and-arc-prize-2025">Announcing ARC - AGI - 2 and ARC Prize 2025 | ARC Prize</a></li>

</ul>
</details>

**Tags**: `#LLM-benchmarks`, `#reasoning`, `#game-of-go`, `#evaluation`, `#ARC-AGI`

---

<a id="item-4"></a>
## [SHADOW-50M: A 19.8 MB Ternary LLM with Built-in Calculation Circuits](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 8.0/10

A developer trained SHADOW-50M, a 44M parameter language model from scratch on 45B tokens, using ternary {-1,0,+1} weights and fixed 512-bit fingerprints for its 73,880-token vocabulary. The model ships in just 19.8 MB, runs at ~1,900 tok/s on a laptop CPU, and features a built-in fixed circuit for arithmetic and reasoning tasks without requiring external tool calls. This proof-of-concept demonstrates that extreme model quantization and novel architectural choices can enable highly capable, ultra-fast edge AI inference on standard CPUs and browsers. By integrating fixed calculation circuits and a memory-mapped attention state retrieval system, it offers a new approach to building tiny LLMs that can reliably compute and retrieve information offline without relying on vector databases. The model uses a 159 KB compiled kernel and consumes about 41 MB of RAM, with a WebAssembly version running at 500 tok/s in a browser. While it underperforms a similarly sized bf16 model (Supra-50M) on standard benchmarks like ARC-Easy and PIQA, it excels at specific reasoning, math, and retrieval tasks due to its specialized circuits and disk-based attention state index.

reddit · r/MachineLearning · /u/Final-Data-1410 · Sep 15, 12:59

**Background**: Ternary quantization restricts neural network weights to {-1, 0, +1}, drastically reducing memory footprint and eliminating most floating-point multiplications. Traditional language models use trained embeddings to represent tokens, but SHADOW-50M instead uses fixed 512-bit fingerprints for its vocabulary. The model also replaces external tool calls for math with a fixed circuit at the readout that directly fills in calculation results in the token stream.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ternaryllm">TernaryLLM: Low-Bit Language Models</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Quantization`, `#Edge AI`, `#CPU Inference`, `#Small Models`

---

<a id="item-5"></a>
## [TabPFN-3.5 Released as New SOTA Tabular Foundation Model](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs released TabPFN-3.5, a new state-of-the-art tabular foundation model that tops both the TabArena and BeyondArena benchmarks. The release introduces multiple variants, including a 6x faster "Fast" model and a "Thinking" model that trades additional compute for improved accuracy. This release represents a significant leap in tabular machine learning, demonstrating that foundation models can outperform traditional methods on complex datasets with up to 1 million rows and 20,000 features. The ability to handle text-rich, high-cardinality, and high-dimensional data with substantial Elo improvements signals a major shift towards pre-trained models for structured data tasks. TabPFN-3.5 achieves +250 Elo points over the strongest previous baseline on BeyondArena, while the "Thinking" variant adds +20 Elo on BeyondArena and +44 Elo on TabArena compared to the base model. The "Thinking" variant is accessible via API, and the "Fast" variant is currently in alpha.

reddit · r/MachineLearning · /u/tuanacelik · Sep 15, 16:18

**Background**: TabPFN (Tabular Prior-data Fitted Network) is a transformer-based machine learning model designed for tabular datasets, originally proposed in 2022. It operates as a foundation model by using in-context learning, trained on synthetic tasks sampled from a prior distribution, allowing it to make predictions on new datasets without retraining. TabArena serves as a living benchmarking system designed to reliably evaluate and compare the performance of tabular machine learning models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TabPFN">TabPFN - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">[2506.16791] TabArena: A Living Benchmark for Machine Learning on Tabular Data</a></li>

</ul>
</details>

**Tags**: `#Tabular Data`, `#Foundation Models`, `#Machine Learning`, `#SOTA`, `#TabPFN`

---

<a id="item-6"></a>
## [4B Parameter Model Trained to Generate 81% Faster Postgres Query Plans](https://rohanbansal.com/qorl) ⭐️ 7.0/10

A developer trained a 4-billion parameter language model using reinforcement learning to generate database query plans that are reportedly 81% faster than PostgreSQL's default planner on a constrained benchmark. The model was distilled from frontier model trajectories and evaluated on an 8 GB in-memory dataset using read-only SELECT queries. This demonstrates a novel application of LLMs to database query optimization, a domain traditionally dominated by cost-based heuristic algorithms. If generalizable, such approaches could complement or enhance traditional query planners, though significant questions remain about reliability, scalability, and practical deployment in production database systems. The benchmark used a small 8 GB dataset that fit entirely in memory, with shared_buffers constrained, queries warmed before measurement, and only read-only SELECT statements tested. The model regularly used non-default PostgreSQL settings such as enable_sort=off and random_page_cost=1.1, which commenters note could artificially disadvantage PostgreSQL's default planner and explain the performance gap by itself.

hackernews · polyphilz · Sep 16, 18:50 · [Discussion](https://news.ycombinator.com/item?id=49731285)

**Background**: A query plan is the sequence of steps a database engine uses to execute a SQL query, and since SQL is declarative, there are typically many alternative ways to execute a given query with widely varying performance. Traditional query optimizers use cost-based heuristics to estimate and select the most efficient execution plan based on statistics about the data. Recent research has explored using large language models for query optimization, including training-free approaches using LLM embeddings for plan similarity matching and semantic-aware join reordering.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Query_plan">Query plan - Wikipedia</a></li>
<li><a href="https://www.together.ai/blog/using-llms-to-optimize-database-query-execution">AI for Systems: Using LLMs to Optimize Database Query Execution</a></li>

</ul>
</details>

**Discussion**: Community sentiment is predominantly skeptical, with commenters raising concerns about overfitting to unrealistic benchmark conditions and questioning whether the results would hold at scale or with realistic OLTP workloads. Multiple commenters point out that the model's use of non-default PostgreSQL settings like random_page_cost=1.1 could explain the performance difference rather than genuine planning improvements. Others highlight the fundamental unsuitability of LLMs for the math-heavy nature of query optimization, noting hallucination risks in production and expressing preference for AlphaGo-style neural network heuristics instead.

**Tags**: `#LLM applications`, `#database optimization`, `#query planning`, `#reinforcement learning`, `#benchmarking`

---

<a id="item-7"></a>
## [Xiaomi MiMo 2.6 Live Post-Training Dashboard Released](https://mimo.xiaomi.com/rl/) ⭐️ 7.0/10

Xiaomi has publicly released a live dashboard streaming real-time reinforcement learning (RL) training metrics for its upcoming MiMo-V2.6-Pro and MiMo-V2.6-Flash models, with team lead Luo Fuli revealing the training progress on September 17. This marks a rare instance of a major AI lab exposing its post-training process to the public in real time. This unprecedented transparency in LLM post-training allows the community to observe the RL training process as it happens, a practice rarely seen among frontier model providers. Combined with community reports of frontier-level coding performance at extremely low cost, it positions Xiaomi as a serious competitor in the open-source AI space that could disrupt incumbent providers. The dashboard streams live training metrics directly from the trainer's logs for both the Pro and Flash variants of MiMo-V2.6. The previous generation, MiMo-V2-Pro, features over 1 trillion total parameters with 42 billion active parameters and a 1-million-token context window.

hackernews · krackers · Sep 16, 20:09 · [Discussion](https://news.ycombinator.com/item?id=49732270)

**Background**: Xiaomi's MiMo series is the company's line of large language models, with the V2-Pro variant having been introduced in March 2026 under the codename "Hunter Alpha" on OpenRouter before its official release. The MiMo team is led by Luo Fuli, a former DeepSeek researcher, and the models have gained attention for strong coding performance at low cost. Reinforcement learning post-training is a technique used to improve model capabilities through reward-based learning after initial pretraining.

<details><summary>References</summary>
<ul>
<li><a href="https://news.aibase.com/news/31131">Xiaomi Publicly Reveals the RL Training Process of MiMo -V 2 . 6 Large...</a></li>
<li><a href="https://mimo.xiaomi.com/rl/">mimo -v 2 . 6 RL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members praise MiMo's cost-to-performance ratio, with one software engineer reporting quality comparable to Anthropic models at a fraction of the cost, despite occasional hallucination loops. Benchmark comparisons show MiMo-V2.5-Pro scoring 19% on DeepSWE 1.1, lagging behind competitors like Fable (70%) and Astra (74%), though commenters note the newer version shows improvement. Several users questioned why other major model providers don't offer similar training transparency.

**Tags**: `#open-source-ai`, `#LLM`, `#coding-agent`, `#model-evaluation`, `#xiaomi`

---

<a id="item-8"></a>
## [Google Releases Gemini 3.8 Live Speech-to-Speech Models with New Web UI Tool](https://simonwillison.net/2026/Sep/15/gemini-live/) ⭐️ 7.0/10

Google has released Gemini 3.8 Live and 3.8 Live Extended Thinking, two new speech-to-speech models designed for real-time voice interaction. Simon Willison has also built a lightweight, library-free web UI tool that allows users to test and interact with these models directly through a browser. These new models represent a significant advancement in real-time voice AI, with the Extended Thinking variant achieving the top spot on Artificial Analysis' Speech to Speech Quality Index. The availability of a simple web UI tool lowers the barrier for developers and users to experiment with and integrate these advanced conversational capabilities into their own applications. The web UI tool connects directly to the `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent` WebSocket endpoint and uses the Web Audio API for audio capture and playback without relying on any external libraries. The Extended Thinking model is specifically recommended for complex, multi-step problem solving during real-time voice interactions.

rss · Simon Willison · Sep 15, 22:47

**Background**: Speech-to-speech AI models process audio input directly and generate audio output without intermediate text conversion, enabling more natural and lower-latency voice interactions. Google's Gemini 3.8 Live models are part of a new generation of dialogue models, similar to OpenAI's GPT-Live family, that support real-time reasoning and task completion. The Extended Thinking variant is optimized for scenarios requiring higher background reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3 . 8 Live Extended Thinking | Gemini API | Google AI for...</a></li>

</ul>
</details>

**Tags**: `#Gemini`, `#speech-to-speech`, `#AI models`, `#Google`, `#voice AI`

---

<a id="item-9"></a>
## [LARA: Lightweight Composable Residual Adapters for Frozen LLMs](https://www.reddit.com/r/MachineLearning/comments/1whx9tr/lara_small_composable_behaviours_for_frozen_llms_p/) ⭐️ 6.0/10

A new research project called LARA (Lightweight Additive Residual Adaptation) introduces a PyTorch library for training low-rank residual adapters on frozen language models. These adapters can be independently trained, blended, or routed at inference time using a Mixture of Behaviors (MoBs) approach to enable multiple capabilities like coding, math, and summarization in a single model. This approach offers a modular alternative to traditional fine-tuning methods like LoRA, allowing a single frozen LLM to exhibit multiple behaviors without maintaining separate adapted models. It could significantly reduce the computational and storage costs of deploying specialized LLMs while enabling dynamic behavior composition at inference time. LARA trains low-rank residual adapters at selected layers rather than modifying the model's weights directly, and includes a soft router that selects or combines behaviors on a token-by-token basis. The repository provides comparisons with LoRA and includes demos for both task-specific behaviors and writing style emulation based on authors like Hemingway and Fitzgerald.

reddit · r/MachineLearning · /u/kertara · Sep 16, 13:28

**Background**: LoRA (Low-Rank Adaptation) is a popular technique that freezes pre-trained model weights and injects trainable rank decomposition matrices into Transformer layers to reduce the number of trainable parameters for fine-tuning. LARA builds on similar principles of parameter-efficient fine-tuning but focuses on additive residual corrections that can be composed and routed dynamically, similar to Mixture-of-Experts architectures where a soft router directs tokens to different specialized components.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2106.09685">[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models</a></li>
<li><a href="https://www.ibm.com/think/topics/lora">What is LoRA (Low-Rank Adaption)? | IBM</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Post-Training`, `#LoRA`, `#Modular AI`, `#PyTorch`

---