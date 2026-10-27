---
layout: default
title: "Horizon Summary: 2026-10-27 (EN)"
date: 2026-10-27
lang: en
---

> From 33 items, 8 important content pieces were selected

---

1. [OpenAI Announces AI-Assisted Discoveries Including Claim That ETH is False](#item-1) ⭐️ 9.0/10
2. [OpenAI Claims to Disprove the Exponential Time Hypothesis](#item-2) ⭐️ 9.0/10
3. [Cloudflare Discloses Cross-Request KV Cache Exposure in GLM-5.3 Workers AI](#item-3) ⭐️ 8.0/10
4. [Hugging Face Open-Sources Revived Papers with Code Platform](#item-4) ⭐️ 8.0/10
5. [Applying Brooks's Law to AI-Assisted Coding and Autonomous Agents](#item-5) ⭐️ 7.0/10
6. [Sebastian Raschka Releases From-Scratch Video Course on Building Reasoning Models](#item-6) ⭐️ 7.0/10
7. [Deepity: Hand-Tuned C++/CUDA Predictive Coding Library Outperforms JAX on MNIST](#item-7) ⭐️ 7.0/10
8. [PBT Escapes Hyperparameter Dead Zones in Grokking but Doesn't Speed It Up](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Announces AI-Assisted Discoveries Including Claim That ETH is False](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ⭐️ 9.0/10

OpenAI has announced three new AI-assisted discoveries in harmonic analysis, complexity theory, and quantum field theory. Most notably, the announcement claims that the Exponential Time Hypothesis (ETH) is false, providing a deterministic algorithm for counting satisfying assignments of k-CNF formulas that runs in sub-exponential time. Disproving ETH would represent a monumental breakthrough in computational complexity theory, fundamentally altering our understanding of algorithmic limits for NP-complete problems. Additionally, OpenAI's improved approach to academic collaboration—by involving mathematicians like Terence Tao prior to public release—demonstrates a shift toward more responsible AI-driven scientific discovery. The proposed algorithm for k-CNF counting uses poly_k(n, m) space and runs in time dominated by 2^(n/(log n)^(0.5 + o(1))), which is superpolynomial but sub-exponential. OpenAI states they involved relevant academic experts before releasing these findings to alleviate concerns in the scientific community.

hackernews · jonluca · Oct 26, 21:35 · [Discussion](https://news.ycombinator.com/item?id=50251344)

**Background**: The Exponential Time Hypothesis (ETH) is a foundational conjecture in computational complexity theory positing that 3-SAT cannot be solved in sub-exponential time in the worst case. Harmonic analysis is a field of mathematical analysis that decomposes functions into basic wave components, closely related to Fourier analysis. Quantum field theory is a framework in physics combining classical field theory, special relativity, and quantum mechanics to construct physical models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Harmonic_analysis">Harmonic analysis - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Exponential_function">Exponential function - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community response is highly polarized; some users are amazed by the sub-exponential algorithm for k-CNF and OpenAI's improved academic collaboration, while others dismiss it as propaganda or express concerns about data contamination. Commenters particularly praised the involvement of mathematicians like Terence Tao in the review process, though skepticism remains about the ultimate validity of the claims.

**Tags**: `#complexity-theory`, `#AI-for-science`, `#exponential-time-hypothesis`, `#OpenAI`, `#scientific-discovery`

---

<a id="item-2"></a>
## [OpenAI Claims to Disprove the Exponential Time Hypothesis](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) ⭐️ 9.0/10

A paper from OpenAI's math research, dated October 25, 2026, claims to prove that the Exponential Time Hypothesis (ETH) is false by demonstrating that subexponential-time algorithms exist for certain NP-complete problems. Anthropic reportedly released a concurrent proof achieving the same bounds but using a different approach. A disproof of ETH would represent a paradigm shift in computational complexity theory, a field where major separation and collapse results are extraordinarily rare. The result has broad implications for complexity theory, as ETH underpins many known lower bounds and optimality results for algorithms across NP-complete problems and beyond. The result does not imply that all NP problems admit subexponential-time algorithms, because runtime bounds of the form 2^o(n) do not transfer under general polynomial-time reductions. The paper specifically notes that 2^(n^o(1)) would be needed for such transfers, so the finding is narrower than a full collapse of NP to subexponential time. The proof remains subject to expert verification, with a team reportedly collaborating to examine the work.

hackernews · vok · Oct 26, 21:59 · [Discussion](https://news.ycombinator.com/item?id=50251661)

**Background**: The Exponential Time Hypothesis (ETH), formulated by Impagliazzo and Paturi in 1999, asserts that 3-SAT (satisfiability of 3-CNF Boolean formulas) cannot be solved in subexponential time in the worst case—meaning no algorithm can solve it faster than 2^(c*n) for some constant c > 0. ETH is stronger than P ≠ NP and implies numerous lower bounds for algorithms across computational complexity theory. If ETH were false, many assumed-optimal algorithms and hardness results that depend on it would need to be reconsidered.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exponential_time_hypothesis">Exponential time hypothesis</a></li>
<li><a href="https://elsolitario.org/en/2026/10/26/openai-refutes-exponential-time-hypothesis/">Exponential Time Hypothesis : What It Is and Why It Fell</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights that the result does not imply P = NP or that NP is subexponential, since subexponential bounds of the form 2^o(n) do not transfer under general polynomial-time reductions. Commenters noted the rarity of complexity class separations and questioned whether the theoretical algorithm has immediate practical applications for SAT solving. One commenter raised the intriguing implication that if ETH (and its stronger variant SETH) is false, previously proven quadratic lower bounds for self-attention in transformers might no longer hold, potentially opening the door to sub-quadratic attention implementations.

**Tags**: `#complexity-theory`, `#ETH`, `#SAT-solving`, `#theoretical-CS`, `#AI-math-research`

---

<a id="item-3"></a>
## [Cloudflare Discloses Cross-Request KV Cache Exposure in GLM-5.3 Workers AI](https://blog.cloudflare.com/kv-cache-exposure-remediation/) ⭐️ 8.0/10

Cloudflare disclosed a cross-request KV cache exposure bug in their GLM-5.3 Workers AI deployment, caused by insufficient session isolation in the SGLANG serving framework, which could allow data leakage between different users' requests. The company published a root cause analysis, pulled the affected model offline, and implemented remediation measures. This incident highlights a real-world security vulnerability in serverless LLM infrastructure, where shared KV cache memory between users can lead to cross-tenant data leakage if isolation is not properly enforced. It raises broader concerns about the security of multi-tenant LLM serving systems, as other serverless providers likely face similar but undisclosed risks. The bug stemmed from a mismatch between the advertised 1,048,576-token context window and the actual KV cache pool capacity of only 681,280 tokens on prefill GPUs, which Cloudflare was aware of before launch. The root cause was an isolation and bookkeeping failure in SGLANG's cache management rather than a flaw in the GLM-5.3 model itself.

hackernews · wondersky · Oct 26, 22:41 · [Discussion](https://news.ycombinator.com/item?id=50252159)

**Background**: KV cache is a memory structure used in LLM serving to store intermediate attention computations, enabling faster token generation by avoiding redundant recomputation. In multi-tenant serverless deployments, multiple users share the same GPU resources, making proper isolation of KV cache between requests critical to prevent data leakage. SGLANG is an LLM serving framework that provides efficient cache management and inference orchestration, similar to other frameworks like vLLM. GLM-5.3 is Zhipu AI's flagship open-weights language model, known for strong coding performance and a large context window.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.3">zai-org/ GLM - 5 . 3 · Hugging Face</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2026/08/pagedattention-radixattention-llm-kv-cache/">KV Cache Management: PagedAttention & RadixAttention</a></li>

</ul>
</details>

**Discussion**: Commenters agreed the bug was an isolation and bookkeeping failure in SGLANG and Cloudflare's infrastructure, not a flaw in the GLM-5.3 model itself. Many praised Cloudflare's transparent root cause analysis and swift remediation, while some questioned whether advertising a 1M token context window while only having capacity for ~681K tokens was misleading. Several commenters noted that other serverless LLM providers likely have similar undisclosed issues or may not even be aware such problems exist.

**Tags**: `#llm-serving`, `#kv-cache`, `#security`, `#cloudflare`, `#sglang`

---

<a id="item-4"></a>
## [Hugging Face Open-Sources Revived Papers with Code Platform](https://www.reddit.com/r/MachineLearning/comments/1xgoadu/papers_with_code_is_now_opensource_p/) ⭐️ 8.0/10

Hugging Face has open-sourced a revived version of the Papers with Code platform under an Apache 2.0 license, with the codebase available on GitHub at github.com/huggingface/paperswithcode. The platform tracks trending AI research, benchmarks, and state-of-the-art (SOTA) models, and was rebuilt using a Python FastAPI backend with a React frontend, hosted on a Hetzner VPS as a single monorepo. The original Papers with Code was a widely-used resource for the AI/ML community that was acquired by Meta and subsequently shut down, leaving a significant gap in the research ecosystem. By reviving and open-sourcing the platform, Hugging Face is restoring an essential tool for tracking research progress and enabling community-driven contributions to keep the resource up to date. The platform exposes a publicly available API as well as an accompanying MCP (Model Context Protocol) server, allowing large language models to securely access the platform's data and tools. The developer noted that the decision to open-source came after receiving numerous feature requests, making collaborative development more practical than solo maintenance.

reddit · r/MachineLearning · /u/NielsRogge · Oct 27, 09:54

**Background**: Papers with Code was originally a platform that aggregated open-access research papers in computer science and machine learning, linking them to code implementations, datasets, and benchmark evaluation tables. It served as a one-stop shop for researchers to find state-of-the-art results across various tasks. Meta acquired the platform and later shut it down, prompting community efforts to recreate the resource. The Model Context Protocol (MCP) is a standard introduced by Anthropic that enables AI applications to securely connect to external data sources and tools through server implementations.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Papers_with_Code">Papers with Code</a></li>
<li><a href="https://www.kdnuggets.com/2022/04/brief-introduction-papers-code.html">A Brief Introduction to Papers With Code - KDnuggets</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#Papers with Code`, `#Hugging Face`, `#Open Source`, `#Machine Learning`, `#Research Tools`

---

<a id="item-5"></a>
## [Applying Brooks's Law to AI-Assisted Coding and Autonomous Agents](https://j11g.com/the-mythical-man-month-in-the-age-of-ai) ⭐️ 7.0/10

An article examines how the classic software engineering principles from "The Mythical Man-Month" apply to modern AI-assisted coding and autonomous agents. It specifically debates whether deploying multiple AI agents on a project with unclear requirements accelerates failure or helps discover the right path. As AI coding tools and autonomous agents become more prevalent, understanding how traditional software engineering laws apply to them is crucial for project management. This analysis helps developers and managers avoid common pitfalls when scaling AI-assisted development, ensuring that adding more AI power actually improves productivity rather than causing coordination overhead. The article suggests that throwing multiple autonomous agents at a single codebase without clear orchestration can lead to them rewriting each other's work in a high-speed loop. However, the drastically reduced cost and time of generating code with AI may change the fundamental trade-offs of Brooks's Law, making rapid iteration a viable strategy for requirement discovery.

hackernews · ilreb · Oct 27, 06:25 · [Discussion](https://news.ycombinator.com/item?id=50255298)

**Background**: "The Mythical Man-Month" is a foundational 1975 book by Fred Brooks that introduced Brooks's Law, which states that adding manpower to a late software project makes it later. This occurs because new team members require training and communication overhead increases quadratically with the number of people. The article applies this decades-old principle to the emerging paradigm of AI agents acting as software developers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/The_Mythical_Man-Month">The Mythical Man-Month</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brooks's_law">Brooks's law</a></li>

</ul>
</details>

**Discussion**: The community is divided on whether Brooks's Law applies to AI, with some arguing that the speed of AI makes generating wrong answers fast a useful tool for discovering correct requirements. Others counter that the law only applies to software creation, not idea generation, and that modern agent orchestrators can easily solve coordination issues like agents rewriting each other's work. A notable concern raised is that LLMs are currently poor at writing instructions for themselves, often over-constraining subagents.

**Tags**: `#AI agents`, `#software engineering`, `#LLM coding`, `#Brooks's Law`, `#autonomous development`

---

<a id="item-6"></a>
## [Sebastian Raschka Releases From-Scratch Video Course on Building Reasoning Models](https://magazine.sebastianraschka.com/p/building-reasoning-models) ⭐️ 7.0/10

Sebastian Raschka has released a new from-scratch video course focused on building reasoning models, covering the fundamentals of how LLMs develop reasoning capabilities. The course follows his well-known intuitive teaching style and builds on his previous educational content, including the popular book "Build Your Own LLM From Scratch." Reasoning capabilities are one of the most active frontiers in LLM research, with techniques like chain-of-thought prompting driving advances in complex applications such as autonomous agents and robotics. Raschka is a highly respected ML educator, and this course provides accessible, high-quality instruction on a cutting-edge topic at a time when interest in reasoning LLMs is surging across the industry. The course emphasizes conceptual understanding over practical deployment, as building a useful LLM from scratch requires significant compute resources, specialized datasets, and operational expertise that tutorials cannot realistically provide. Community members note that Raschka's materials are known for being readable and approachable, though hands-on experimentation may require either cloud GPUs or a reasonably powerful local machine.

hackernews · sgiannopoulos · Oct 26, 15:11 · [Discussion](https://news.ycombinator.com/item?id=50245138)

**Background**: Reasoning models are LLMs designed to perform logical deduction and multi-step problem-solving, often using techniques like chain-of-thought reasoning to break down complex tasks into intermediate steps. Building such models from scratch involves understanding neural network architecture, training procedures, and the specific mechanisms that enable reasoning behavior. Sebastian Raschka is widely recognized for his accessible educational materials that guide learners through implementing ML systems from fundamental components.

<details><summary>References</summary>
<ul>
<li><a href="https://kili-technology.com/blog/llm-reasoning-guide">The Ultimate Guide to LLM Reasoning (2025)</a></li>
<li><a href="https://www.promptingguide.ai/research/llm-reasoning">LLM Reasoning | Prompt Engineering Guide</a></li>
<li><a href="https://github.com/atfortes/Awesome-LLM-Reasoning">GitHub - atfortes/Awesome- LLM - Reasoning : From Chain-of-Thought...</a></li>

</ul>
</details>

**Discussion**: The community discussion reflects strong appreciation for Raschka's teaching style, with several commenters praising his ability to explain complex AI topics intuitively and noting the readability of his book. A notable thread addresses the misconception that from-scratch tutorials should enable training of production-quality LLMs, with one commenter clarifying that these resources serve understanding rather than practical deployment given the compute and data requirements involved. There is also discussion about computing requirements for hands-on learning, with uncertainty about whether local hardware suffices or cloud GPUs are necessary.

**Tags**: `#LLMs`, `#reasoning-models`, `#education`, `#machine-learning`, `#from-scratch`

---

<a id="item-7"></a>
## [Deepity: Hand-Tuned C++/CUDA Predictive Coding Library Outperforms JAX on MNIST](https://www.reddit.com/r/MachineLearning/comments/1xg6sqa/deepity_a_handtuned_ccuda_predictive_coding/) ⭐️ 7.0/10

A new open-source predictive coding library named Deepity has been released, featuring a hand-tuned C++20 core with AVX2/AVX-512 SIMD kernels and a CUDA backend. In CPU benchmarks on MNIST, Deepity achieved 98.21% accuracy in 487.5 seconds, outperforming the JAX-based jpc (97.55% in 531.4s) and ngc-learn (98% in 1707.7s). This library provides a highly optimized, from-scratch implementation of predictive coding, an alternative to backpropagation that uses local error minimization and requires no backward graph in memory. It demonstrates that predictive coding networks can be competitive with traditional backpropagation in both speed and accuracy when optimized at the kernel level, offering a valuable tool for researchers exploring biologically plausible learning algorithms. The library includes several predictive coding network variants, such as classic-settling and Direct Kolen-Pollack feedback, with Python bindings via nanobind. While the CPU path is mature and benchmarked, the CUDA backend is still being optimized for large-scale training, and the software is currently in alpha (version 0.1.0a3) under solo maintenance.

reddit · r/MachineLearning · /u/Important-Home4431 · Oct 26, 19:34

**Background**: Predictive coding is a framework where neural networks perform inference through iterative energy minimization, with each layer holding a local belief about its state and comparing it against top-down predictions. Unlike backpropagation, which uses a single global error signal flowing backward, predictive coding relies on local error minimization, making it a biologically plausible alternative. Deepity leverages SIMD vectorization techniques like AVX-512 and the SLEEF library for transcendental functions to achieve high performance on CPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10561268/">Local minimization of prediction errors drives learning of invariant...</a></li>
<li><a href="https://paperswithcode.co/paper/2506.23800">Towards the Training of Deeper Predictive Coding Neural Networks ...</a></li>

</ul>
</details>

**Tags**: `#Predictive Coding`, `#C++`, `#CUDA`, `#Machine Learning`, `#Optimization`

---

<a id="item-8"></a>
## [PBT Escapes Hyperparameter Dead Zones in Grokking but Doesn't Speed It Up](https://www.reddit.com/r/MachineLearning/comments/1xfqhfc/pbt_doesnt_make_grokking_faster_but_it_can_escape/) ⭐️ 7.0/10

An empirical study demonstrates that while Population Based Training (PBT) is slower than grid search for grokking in favorable hyperparameter regions, it can escape "dead zones" where no fixed hyperparameter configuration groks. The author found that PBT escapes by following a specific learning rate and weight decay trajectory where the validation loss reward signal flips sign. This research provides nuanced, mechanistic insights into how PBT interacts with grokking dynamics, challenging the assumption that PBT universally accelerates training. It suggests PBT is better suited as a rescue tool for bad hyperparameter ranges rather than a general speed-up mechanism. The study used modular addition mod 97 with a 35% train split and a small MLP, comparing PBT against grid search and random search. A key finding is that the winning learning rate/weight decay schedule carries the result, not the weight copying, as replaying the schedule on fresh initializations achieved 95% accuracy in 55/60 cases.

reddit · r/MachineLearning · /u/Virtual-Message-9739 · Oct 26, 07:48

**Background**: Grokking is a phenomenon where a neural network suddenly generalizes to a task long after achieving zero training loss, often studied in algorithmic tasks like modular arithmetic. Population Based Training (PBT) is a hyperparameter optimization method that evolves a population of models by copying weights and mutating hyperparameters during training based on performance. This study explores whether PBT's dynamic hyperparameter adjustments can accelerate or facilitate the grokking process.

**Tags**: `#grokking`, `#population-based-training`, `#hyperparameter-optimization`, `#training-dynamics`, `#deep-learning`

---