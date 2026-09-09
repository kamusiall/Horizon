---
layout: default
title: "Horizon Summary: 2026-09-09 (EN)"
date: 2026-09-09
lang: en
---

> From 29 items, 18 important content pieces were selected

---

1. [OpenAI Claims AI System Solved Navier-Stokes Millennium Prize Problem](#item-1) ⭐️ 10.0/10
2. [llm CLI version 0.35 adds support for OpenAI's GPT-6 Astra](#item-2) ⭐️ 9.0/10
3. [Meta Launches Muse, a Personal AI Agent with Layered Prompt Injection Defenses](#item-3) ⭐️ 8.0/10
4. [Google DeepMind Announces AlphaGenome Atlas for Human DNA Variant Prediction](#item-4) ⭐️ 8.0/10
5. [Terence Tao Warns AI May Non-Renewably Mine Open Math Problems](#item-5) ⭐️ 8.0/10
6. [NeurIPS Desk-Rejects 178 Papers Using Flawed AI Detector](#item-6) ⭐️ 8.0/10
7. [LLM-Guided Program Evolution Breaks 10 Circle-Packing Records for $28](#item-7) ⭐️ 8.0/10
8. [LLMs Spontaneously Develop Novel Social Biases Through Adaptive Exploration](#item-8) ⭐️ 7.0/10
9. [Qwen3.8 27B Quantization Benchmarks: 4-bit Holds Up, 1-bit Collapses](#item-9) ⭐️ 7.0/10
10. [OpenAI Introduces ChatGPT Images 2.5 with Sunburst and Flare Models](#item-10) ⭐️ 7.0/10
11. [Generating Bad Apple Autonomously with a Tiny Recurrent Dynamical System](#item-11) ⭐️ 7.0/10
12. [Embedflow: Zero-Downtime Migration Between Embedding Models](#item-12) ⭐️ 7.0/10
13. [Inception Labs Releases Mercury 2.5 Diffusion-Based LLM](#item-13) ⭐️ 6.0/10
14. [I-have-ADHD: A Skill to Stop Coding Agents from Burying Answers](#item-14) ⭐️ 6.0/10
15. [Abusive crawlers now consume more CPU than legitimate access on git.kernel.org](#item-15) ⭐️ 6.0/10
16. [OpenAI Chief Scientist Jakub Pachocki on Defensive AI and Reckless Racing](#item-16) ⭐️ 6.0/10
17. [Stanford Launches Free 'Probability for AI' Course with 1:10 Teacher Ratio](#item-17) ⭐️ 6.0/10
18. [Rustuna: High-Performance Rust Implementation of Optuna Released](#item-18) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Claims AI System Solved Navier-Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/) ⭐️ 10.0/10

On September 8, 2026, OpenAI announced that an internal AI model had produced a solution to the Navier-Stokes existence and smoothness problem, one of the seven Millennium Prize Problems in mathematics. The claimed proof demonstrates that Navier-Stokes solutions in three-dimensional Euclidean space can develop a singularity in finite time, and OpenAI shared both a writeup and a formalization in the Lean proof assistant. If verified, this would represent a monumental breakthrough in both pure mathematics and AI reasoning capabilities, as the Navier-Stokes problem has remained unsolved for decades and is central to understanding fluid turbulence. It also signals a dramatic leap in AI's ability to perform deep mathematical reasoning, with an internal model reportedly trained for less than two weeks surpassing previous publicly released systems. The claim has not been verified by external mathematicians or the Clay Mathematics Institute, and the announcement was accompanied by a priority dispute with Levent Alpöge (an Anthropic employee) and Tristan Buckmaster, who had derived closely related results on the Euler equations used in the proof. The method built upon a 2023 technique by Diego Córdoba and Luis Martínez-Zoroa for proving blowup phenomena in related fluid equations, and OpenAI stated it would not claim the $1 million Clay Millennium Prize even if offered.

hackernews · tedsanders · Sep 8, 17:13 · [Discussion](https://news.ycombinator.com/item?id=49613262)

**Background**: The Navier-Stokes equations are a system of partial differential equations that describe the motion of fluids in space and are used in countless practical applications across science and engineering. The existence and smoothness problem asks whether, in three dimensions, smooth and globally defined solutions always exist for given initial conditions, or whether a counter-example can be found where solutions break down. The Clay Mathematics Institute designated this as one of seven Millennium Prize Problems in 2000, offering $1 million for a solution; the only Millennium Prize problem solved to date is the Poincaré conjecture, resolved by Grigori Perelman in 2010.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**Discussion**: Community sentiment is a mix of awe and deep concern. Commenters highlighted the astounding technical leap of an internal model trained for less than two weeks being more than twice as capable in mathematics as the recently released Astra model, while others expressed unease about the privatization of scientific discovery and wished the work had been done under public institutions like NASA. A significant controversy centers on OpenAI's admission that it cannot rule out that de-identified data from researchers' product usage helped train the models, raising accusations of potential data spying on competitors' work, and a linked concurrent HN thread reportedly outlines aggressive behavior by specific OpenAI employees in the priority dispute.

**Tags**: `#OpenAI`, `#Mathematics`, `#Navier-Stokes`, `#Millennium Prize`, `#AI Reasoning`

---

<a id="item-2"></a>
## [llm CLI version 0.35 adds support for OpenAI's GPT-6 Astra](https://simonwillison.net/2026/Sep/7/llm/) ⭐️ 9.0/10

Simon Willison's `llm` CLI tool has been updated to version 0.35, which introduces support for OpenAI's newly released GPT-6 Astra model. The release note simply lists the new `gpt-6-astra` model as the primary addition. GPT-6 Astra is OpenAI's most capable model, designed for complex reasoning, coding, computer use, research, and document creation, making its availability in a widely used CLI tool significant for developers. The `llm` CLI is a popular unified interface for dozens of LLM providers, so adding this flagship model expands the tool's utility for command-line AI workflows. GPT-6 Astra was released as a limited preview on September 3, 2026, following a delay caused by OpenAI's Hugging Face incident in July 2026 to add more safeguards. The `llm` tool can be installed via `uv tool install llm` and supports both remote APIs and locally installed models.

rss · Simon Willison · Sep 7, 23:54

**Background**: The `llm` CLI is a Python tool and library built by Simon Willison that provides a unified command-line interface to dozens of large language models, including those from OpenAI, Anthropic, Google, and local model providers. It allows users to run prompts or start chats against arbitrary OpenAI-compatible Chat Completions endpoints. GPT-6 Astra is OpenAI's latest flagship model, optimized for structured document creation, presentations, spreadsheets, and complex end-to-end tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/ llm : Access large language models from the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**Tags**: `#openai`, `#llm`, `#gpt-6-astra`, `#cli-tool`, `#model-release`

---

<a id="item-3"></a>
## [Meta Launches Muse, a Personal AI Agent with Layered Prompt Injection Defenses](https://ai.meta.com/muse/) ⭐️ 8.0/10

Meta has announced the launch of Muse, a personal AI agent integrated across its ecosystem and targeting mass-market consumers. The agent features layered prompt injection defenses, including model training to resist attacks, harness-level marking of untrusted inputs, deterministic code checks, and an ensemble of classifiers running outside the agent's reach. This represents Meta's major push into consumer AI agents, bringing agentic AI to billions of users across Facebook, Instagram, and other Meta platforms. The layered security approach is particularly significant because prompt injection remains one of the most critical unsolved challenges in LLM-based agent deployment at scale. A basic version of the agent will be available for free, with subscriptions priced at $20 and $100 per month for heavier usage, and the product is initially available only in the U.S. Reuters reported that the rollout proceeded despite internal concerns about the technology mismanaging access to sensitive personal data, and users can opt out of certain data sharing.

hackernews · yks · Sep 8, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49615537)

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs are designed to cause unintended behavior in large language models by taking advantage of the model's inability to distinguish between developer-defined instructions and user-supplied content. Indirect prompt injection is especially dangerous for agents with web browsing or file access, as adversarial prompts can be embedded in external content the agent retrieves. A layered defense strategy—combining model hardening, input marking, deterministic checks, and independent classifiers—has emerged as a best practice, as no single mitigation fully prevents these attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html">LLM Prompt Injection Prevention - OWASP Cheat Sheet Series</a></li>
<li><a href="https://en.wikipedia.org/wiki/Personal_agent">Personal agent</a></li>

</ul>
</details>

**Discussion**: Commenters debated Meta's market strategy, with some arguing Muse targets less tech-savvy 'normie-tier' users who are oblivious to model differences, while others expressed skepticism about feeding more personal data into Meta's ecosystem. Technical discussion focused on David Singleton's thread describing the layered prompt injection defenses, and one commenter noted that the marketing examples (health, travel, kids' education) touch on anxiety-prone areas where a simple confirm button may not be sufficient.

**Tags**: `#AI Agents`, `#Meta`, `#Prompt Injection`, `#Consumer AI`, `#AI Security`

---

<a id="item-4"></a>
## [Google DeepMind Announces AlphaGenome Atlas for Human DNA Variant Prediction](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 8.0/10

Google DeepMind has released AlphaGenome Atlas, an AI-powered predictive map that catalogs the molecular effects of 9 billion possible single-nucleotide variants in the human genome. The model takes up to 1 Mb of DNA as input to predict variant impacts at an unprecedented scale. This release is significant because it provides a comprehensive resource for interpreting non-coding DNA regions, which make up 98% of the genome and are crucial for orchestrating gene activity and disease susceptibility. It could greatly accelerate research in genomics, disease risk assessment, and precision medicine by offering a new perspective on variant impact prediction. AlphaGenome is a unified DNA sequence model that overcomes previous trade-offs between input sequence length and prediction resolution. The Atlas provides molecular predictions and AVI scores for all 9 billion single-nucleotide variants, and is accessible to the public via the DeepMind website without requiring an institutional affiliation.

hackernews · utiiiD · Sep 8, 14:55 · [Discussion](https://news.ycombinator.com/item?id=49611251)

**Background**: The human genome consists of coding and non-coding regions, with the latter making up 98% of the genome and playing a critical role in regulating gene expression. Single-nucleotide variants (SNVs) are substitutions of a single nucleotide at a specific position in the genome, which can help explain differences in susceptibility to diseases. Existing methods for predicting variant impacts often involve a trade-off between input sequence length and prediction resolution, limiting their performance and modality scope.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/">AlphaGenome Atlas: Molecular predictions for 9 Billion human DNA variants — Google DeepMind</a></li>
<li><a href="https://www.nature.com/articles/s41586-025-10014-0">Advancing regulatory variant effect prediction with AlphaGenome | Nature</a></li>
<li><a href="https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/">AlphaGenome: AI for better understanding the genome — Google DeepMind</a></li>

</ul>
</details>

**Discussion**: Community members shared tutorial videos and noted that the Atlas is publicly accessible without requiring an affiliation. Discussions compared the AI's in silico predictions to real experimental mutagenesis studies on viruses, questioned the model's handling of promoter sequences in non-coding DNA, and explored practical applications such as using it with 23andMe data to identify pathogenic mutations.

**Tags**: `#genomics`, `#deepmind`, `#bioinformatics`, `#variant-prediction`, `#AI-for-science`

---

<a id="item-5"></a>
## [Terence Tao Warns AI May Non-Renewably Mine Open Math Problems](https://mathstodon.xyz/@tao/117237320796901560) ⭐️ 8.0/10

Terence Tao, one of the world's leading mathematicians, publicly argued that indiscriminate use of AI to solve open mathematical problems risks depleting the intellectual ecosystem needed for sustained mathematical progress. He framed the issue as a form of non-renewable "mining" where solution extraction without understanding undermines future research. This raises a fundamental question about the role of AI in research: whether rapid automated problem-solving could hollow out the field by removing the open problems that drive human mathematical development and insight. It challenges the assumption that more AI-generated solutions automatically translate to deeper scientific understanding. Tao's central point is that powerful solution-extraction tools can achieve short-term goals of solving problems at the cost of sustaining the ecosystem for the next wave of progress and understanding the progress already obtained. He distinguishes between merely obtaining a verified solution and developing the theory and insights that make a solution meaningful.

hackernews · _alternator_ · Sep 8, 21:00 · [Discussion](https://news.ycombinator.com/item?id=49616968)

**Background**: Terence Tao is a Fields Medal-winning mathematician known for his work across multiple areas of mathematics and his thoughtful commentary on mathematical practice. Open math problems are unsolved conjectures and questions that serve as catalysts for developing new theories, techniques, and connections between fields. The concern is that mathematics advances not just through answers but through the structures and understanding built while pursuing those answers, which a raw solution from AI might bypass.

**Discussion**: The discussion was highly engaged with several viewpoints: one commenter drew a parallel to Asimov's "Jokester," where the bottleneck became asking meaningful questions rather than finding answers. Another pushed back by noting mathematics has always been highly competitive, citing Gauss and the Newton-Leibniz controversy. Some questioned Tao's premise, arguing that a solution without insight isn't interesting to the profession anyway, while others agreed that the ecosystem of open problems matters for sustained progress.

**Tags**: `#AI`, `#mathematics`, `#Terence Tao`, `#research`, `#AI impact`

---

<a id="item-6"></a>
## [NeurIPS Desk-Rejects 178 Papers Using Flawed AI Detector](https://www.reddit.com/r/MachineLearning/comments/1wakf62/neurips_deskrejected_178_papers_for_being/) ⭐️ 8.0/10

NeurIPS Position Paper Track used the proprietary AI detector Pangram to desk-reject 178 papers (18.4% of submissions) without human review or appeal process. Independent researchers found the same detector flagged the track chairs' own papers at 24-69% AI-generated, and Pangram's default settings originally flagged 42.7% of all submissions. This incident reveals the systemic unreliability of AI-generated content detectors when applied to academic peer review, particularly highlighting disproportionate false positives for ESL researchers. It raises serious concerns about automated desk-rejection policies in academic publishing and the lack of due process for affected authors. Pangram's default setting flagged nearly half of all submissions as 90-100% AI, forcing organizers to shrink text windows to reduce the flag rate to 12.7%. A Stanford study showed 61.22% of human-written TOEFL essays are falsely flagged as AI due to structurally rigid non-native English, and NeurIPS published zero demographic calibration data for the detector.

reddit · r/MachineLearning · /u/tughanbulut · Sep 8, 10:19

**Background**: Desk rejection is a decision by academic editors to decline a manuscript immediately without sending it to peer review. Pangram is an AI detection software developed by Brooklyn-based Pangram Labs that uses natural language processing to identify text produced by large language models, but it has been criticized for contributing to "witch hunts" for AI writing. AI detectors generally work by analyzing patterns in text, but research has shown they often produce false positives, especially for non-native English speakers whose formal writing tends to be more structurally rigid.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pangram_(AI_detector)">Pangram (AI detector)</a></li>
<li><a href="https://www.aischolar.com/news/article/what-is-desk-reject">What Is a Desk Reject? 6 Common Reasons & How to Avoid It</a></li>

</ul>
</details>

**Discussion**: The Reddit post generated significant community interest, with the author (who disclosed building a competing deterministic citation checker) providing detailed analysis of the thresholds, data privacy issues, and recourse options for rejected authors. The author emphasized that rejected papers carry no misconduct mark and encouraged resubmission to ICLR or ICML.

**Tags**: `#neurips`, `#ai-detection`, `#academic-publishing`, `#peer-review`, `#ai-ethics`

---

<a id="item-7"></a>
## [LLM-Guided Program Evolution Breaks 10 Circle-Packing Records for $28](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

A researcher used an LLM to iteratively evolve an optimization algorithm for circle packing rather than directly solving the problem, starting from a simple seed solver and using a scoreboard of results plus prior attempt history to guide each proposed change. The approach improved 10 best-known solutions on the Packomania csqv benchmark (N=101–114) by 2.4–5.4% in just 15 iterations at a total LLM cost of $27.72, with results independently accepted by Packomania maintainers. This demonstrates a compelling paradigm where LLMs act as algorithm-evolution engines guided by independent verification, rather than as direct problem solvers, achieving measurable scientific progress on a recognized benchmark at extremely low cost. The approach could be broadly applied to other combinatorial optimization and scientific discovery problems where iterative code improvement with automated verification is feasible. Each candidate algorithm proposed by the LLM is evaluated against an independent verifier, so improvements are retained and failures discarded, creating a Darwinian selection process over code. The author specifically seeks feedback on the plateau-detection stopping rule used to determine when to halt the evolution loop, which is the component they consider most in need of critique.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Circle packing is a well-studied combinatorial optimization problem where the goal is to arrange circles, potentially of different sizes, within a bounded area such as a unit square to maximize some objective like the sum of radii. Packomania is a community-maintained benchmark repository that tracks the best-known solutions for various circle-packing variants, including csqv (maximize the sum of radii of N variable-radius circles in the unit square). The approach here treats the LLM as a meta-optimizer that evolves the solver code itself, analogous to how evolutionary algorithms evolve candidate solutions but operating at the level of algorithmic strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28</a></li>
<li><a href="https://arxiv.org/html/2609.05093">LLM-Guided Program Evolution for Circle Packing:Breaking 10 Packomania Records for $28</a></li>
<li><a href="http://www.packomania.com/cciuneq/">The best known solutions of benchmark instances for ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#program synthesis`, `#combinatorial optimization`, `#algorithm evolution`, `#benchmark`

---

<a id="item-8"></a>
## [LLMs Spontaneously Develop Novel Social Biases Through Adaptive Exploration](https://openreview.net/challenge?redirect=%2Fforum%3Fid%3Dpc7fqaOcAH) ⭐️ 7.0/10

A recent study demonstrates that large language models can spontaneously develop novel social biases towards artificial demographic groups, such as Tufa, Aima, Reku, and Weki, even when no inherent differences exist between them. The research shows that LLMs exhibit more stratified task allocations than human participants, with newer and larger models showing exacerbated bias due to insufficient exploration. This finding is significant because it reveals that AI bias is not just a reflection of explicit stereotypes in training data, but can emerge from the model's own decision-making processes, such as exploration-exploitation trade-offs. It highlights a dangerous trend where more capable models may lead to more unequal outcomes, posing serious challenges for deploying LLMs in fair decision-making roles. The study uses an iterative hiring experiment where LLMs act as consultants in a fictional city, assigning applicants from four unfamiliar demographic groups to various jobs. Biases emerge because the models explore too little, allowing early observations to disproportionately influence their impressions of entire groups, resulting in highly stratified task allocations.

hackernews · paimapi · Sep 8, 21:47 · [Discussion](https://news.ycombinator.com/item?id=49617581)

**Background**: The research builds on social science concepts of emergent biases resulting from exploration-exploitation trade-offs, where decision-makers rely on limited early experiences to form judgments about groups. In the context of AI, this means that even without explicit demographic data or pre-existing stereotypes about a group, an LLM can create and reinforce new biases through its adaptive learning process during multi-turn interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.06148">[2511.06148] Large Language Models Develop Novel Social Biases Through Adaptive Exploration</a></li>
<li><a href="https://arxiv.org/html/2511.06148v1">Large Language Models Develop Novel Social Biases Through Adaptive Exploration</a></li>
<li><a href="https://news.ycombinator.com/item?id=49617581">Large Language Models Develop Novel Social Biases Through Adaptive Exploration | Hacker News</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights the methodology of the study, where users shared the specific prompts used to simulate the hiring process in a fictional city. Commenters also connected the findings to broader cultural and literary theories about how bias-making machinery is embedded in texts, while others referenced real-world examples of racial bias in online marketplaces to contextualize the results.

**Tags**: `#LLMs`, `#AI Bias`, `#Machine Learning`, `#Research`, `#AI Ethics`

---

<a id="item-9"></a>
## [Qwen3.8 27B Quantization Benchmarks: 4-bit Holds Up, 1-bit Collapses](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 7.0/10

Benchmark results for Qwen3.8 27B reveal that the model maintains quality down to 4-bit quantization but degrades significantly at 1-bit. The findings provide concrete guidance for practitioners deploying this open-weight dense vision-language model locally. These results directly inform local LLM deployment decisions, helping users balance memory savings against quality loss when running Qwen3.8 27B on consumer hardware. The findings are especially relevant for users with sub-16GB VRAM cards who need to choose quantization levels carefully. The benchmark uses Wilson 95% confidence intervals to assess quality differences across quantization levels, showing minimal loss down to 4-bit but a notable drop at 2-bit and collapse at 1-bit. Community members note that Qwen3.8 27B's thinking capability may partially offset quantization degradation by reasoning longer before completing tasks.

hackernews · stared · Sep 8, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49611128)

**Background**: Quantization reduces the precision of LLM weights (e.g., from 16-bit to 4-bit or lower) to decrease memory and computational requirements, enabling models to run on consumer GPUs. Qwen3.8 27B is an open-weight dense vision-language model suited for coding, professional workflows, and multimodal interaction, available through platforms like Hugging Face and OpenRouter. Post-training quantization techniques like those used in llama.cpp and Ollama allow users to trade quality for smaller model sizes, with 4-bit being a common sweet spot for many architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/ Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-27b">Qwen 3 . 8 27 B - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://picovoice.ai/blog/sub-4-bit-llm-quantization/">Sub- 4 - Bit LLM Quantization : Enterprise Guide to Methods & Tradeoffs</a></li>

</ul>
</details>

**Discussion**: Commenters debated the statistical validity of confidence intervals, with one noting they don't measure run-to-run variation as commonly assumed. Several users requested benchmarks for KV cache quantization, noting its importance for long-context scenarios, while others observed that Qwen3.8 27B's extended thinking capability may compensate for quantization-induced quality loss. A practical concern was raised about the 'Q3 hole' for sub-16GB VRAM cards like the RTX 5080 and 5070 Ti, where users need clearer guidance on quality breakpoints.

**Tags**: `#quantization`, `#LLM`, `#benchmarking`, `#Qwen`, `#local-inference`

---

<a id="item-10"></a>
## [OpenAI Introduces ChatGPT Images 2.5 with Sunburst and Flare Models](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 7.0/10

On September 8, 2026, OpenAI released ChatGPT Images 2.5, introducing two new API model IDs: gpt-image-2.5-sunburst and gpt-image-2.5-flare. The update brings improved multi-turn instruction following, faster response times, and better preservation of subjects in reference photos. This release gives developers two specialized models to choose from based on their specific workload needs, rather than a single general-purpose model. It represents an incremental but meaningful upgrade for API users, improving editing precision and everyday image generation workflows across the OpenAI ecosystem. Sunburst is positioned as the stronger model for workflows where editing precision matters most, while Flare is optimized for fast, high-quality everyday image generation. Both models bill at the same per-token rates as the previous gpt-image-2 model and share a single entry in OpenAI's pricing calculator.

rss · Simon Willison · Sep 8, 22:46

**Background**: OpenAI's image generation models have been widely adopted, with over 3 billion images generated across ChatGPT Images and the GPT-Image models in the API. Multi-turn instruction following refers to a system's ability to handle instructions across multiple dialogue turns by retaining context and managing evolving constraints. The previous major model was gpt-image-2, and the new 2.5 models are positioned as direct successors with workload-specific optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/gpt-image-2-5-flare-sunburst">GPT- Image -2.5 Flare vs Sunburst : New OpenAI Image APIs</a></li>
<li><a href="https://apidog.com/blog/gpt-image-2-5-flare-vs-sunburst-vs-gpt-image-2/">GPT- Image -2.5 Flare vs Sunburst vs gpt- image -2: which to pick, and...</a></li>
<li><a href="https://ofox.ai/blog/gpt-image-2-5-flare-vs-sunburst/">GPT Image 2.5 Flare vs Sunburst : which should you use?</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Image Generation`, `#API`, `#ChatGPT`, `#Multimodal AI`

---

<a id="item-11"></a>
## [Generating Bad Apple Autonomously with a Tiny Recurrent Dynamical System](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 7.0/10

A developer built a 417k-parameter recurrent dynamical system that autonomously generates the full ~6,500-frame 'Bad Apple' video from a single initial latent state without timestamp inputs. The system uses an LSTM-style recurrence and a frame decoder, trained with techniques like rollout horizon curriculum and state perturbation noise to ensure long-horizon stability. This project demonstrates a novel approach to continuous temporal flow in latent space, showing that a tiny model can generate long video sequences autonomously from a single initial condition. The underlying architecture and training techniques offer valuable insights for generative models and RNNs, potentially influencing future work in autonomous video generation and dynamical systems. The model features a 64-D latent dimension for both hidden state and internal memory, using a 4-gate LSTM-style recurrence with orthogonal initialization and a 4-stage bilinear upsampling frame decoder. Despite being trained on rollouts of up to 512 frames, the model successfully unrolled the full 6,500-frame sequence, and the checkpoint with the lowest training loss was not necessarily the best at autonomous generation.

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Background**: SIREN (Sinusoidal Representation Networks) are implicit neural representations that use periodic sine activation functions to encode signals with high-frequency detail. Recurrent dynamical systems use RNNs to approximate time-evolving dynamics, and in closed-loop inference, they generate sequences autonomously by feeding their own outputs back as inputs without external timestamp inputs. This project builds on these concepts by using a recurrent system to learn temporal flow in latent space rather than mapping coordinates to pixels directly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/siren-based-architecture.md">emergentmind.com/topics/ siren -based-architecture.md</a></li>
<li><a href="https://www.emergentmind.com/topics/recurrent-dynamical-solvers">Recurrent Dynamical Solvers</a></li>

</ul>
</details>

**Tags**: `#RNN`, `#Generative Models`, `#Latent Space`, `#Video Generation`, `#Machine Learning`

---

<a id="item-12"></a>
## [Embedflow: Zero-Downtime Migration Between Embedding Models](https://www.reddit.com/r/MachineLearning/comments/1wabmm7/my_lab_found_a_way_to_migrate_between_embedding/) ⭐️ 7.0/10

A research lab introduced 'embedflow,' a method that enables zero-downtime migration between embedding models by reranking the top-K results from the old index using the new model, eliminating the need to re-embed billions of documents. The tool was tested across 63 migrations on up to 1 million documents and is available as an open-source Python package compatible with Qdrant. This approach addresses a critical infrastructure bottleneck in RAG and vector search systems, where upgrading embedding models traditionally requires massive compute costs and extended downtime. By avoiding full re-embedding, organizations can adopt newer, better-performing models without incurring prohibitive operational costs or service interruptions. In one notable test, migrating from Qwen 4B to Qwen 8B embeddings achieved retrieval quality equivalent to native retrieval using just 50 reranked documents. The main challenge identified is determining the optimal value of K (the number of documents to rerank), which varies depending on the specific models and dataset involved.

reddit · r/MachineLearning · /u/Potential_Low_1183 · Sep 8, 02:16

**Background**: Embedding models convert text into dense vector representations used for semantic search and retrieval-augmented generation (RAG). When organizations want to upgrade to a newer, better embedding model, they typically must re-embed their entire document corpus, which can take months for large datasets; for example, re-embedding one billion documents with Qwen 8B on an H100 GPU would take approximately 108 days. Embedflow sidesteps this by using the old index to retrieve candidate documents and then reranking those candidates with the new model, progressively materializing the new vectors over time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/arnsri33/embedflow">GitHub - arnsri33/ embedflow : Zero downtime embedding upgrades</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-Embedding-8B">Qwen / Qwen 3- Embedding - 8 B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#embeddings`, `#rag`, `#vector-search`, `#model-migration`, `#information-retrieval`

---

<a id="item-13"></a>
## [Inception Labs Releases Mercury 2.5 Diffusion-Based LLM](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5) ⭐️ 6.0/10

Inception Labs has released Mercury 2.5, an updated version of its diffusion-based large language model (LLM) that offers improved performance over its predecessor. This release represents an incremental advancement in the niche architecture of diffusion-based LLMs, which offer potential speed advantages for specific tasks like reranking, though the model remains closed-weights. While the model shows improved creative writing capabilities with reasoning disabled, enabling reasoning mode can paradoxically lead to hallucinations and degraded performance in certain tasks.

hackernews · Topfi · Sep 8, 20:14 · [Discussion](https://news.ycombinator.com/item?id=49616354)

**Background**: Diffusion-based LLMs are a novel architecture that generate text through a diffusion process rather than the traditional autoregressive approach, potentially offering faster inference speeds. Unlike open-weight models that can be downloaded and self-hosted, closed-weight models like Mercury 2.5 keep their core parameters proprietary and accessible only via API.

<details><summary>References</summary>
<ul>
<li><a href="https://aipapersacademy.com/large-language-diffusion-models/">Large Language Diffusion Models: The Era Of Diffusion LLMs?</a></li>
<li><a href="https://www.agentshows.ai/watch/open-weight-vs-closed-weight-frontier-ai-and-the-high-stakes-batt.html">Open-Weight vs Closed - Weight Frontier AI — and the... | AgentShows</a></li>

</ul>
</details>

**Discussion**: Community members highlighted the model's blazing speed for tasks like reranking vector store results, but noted that enabling reasoning mode degraded creative writing performance and caused hallucinations. There was also disappointment that the model remains closed-weights despite running on widely available GPUs, and users shared practical tips like opting out of data training.

**Tags**: `#diffusion-llm`, `#inception-labs`, `#mercury`, `#llm-inference`, `#model-release`

---

<a id="item-14"></a>
## [I-have-ADHD: A Skill to Stop Coding Agents from Burying Answers](https://github.com/ayghri/i-have-adhd) ⭐️ 6.0/10

A new skill/plugin called 'I-have-ADHD' has been released on GitHub for coding agents like Claude, designed to enforce concise, direct responses and prevent the model from burying key information in verbose output. The tool acts as a persistent reminder injected into agent sessions to curb excessive verbosity. Excessive verbosity is a widely reported pain point with LLM coding agents, leading to wasted tokens, higher costs, and reduced developer productivity as users struggle to find the actual answer or change buried in lengthy explanations. This community-validated utility addresses a real workflow problem, though it highlights a deeper limitation in model behavior that prompt-level fixes only partially solve. The skill must be asserted at every turn in a session to maintain its effect, as Claude models tend to revert to verbose behavior after a few turns even when instructed in global CLAUDE.md files. Users note that while the token cost of the reminder is negligible, the underlying issue is not simply an output style flag but a deeper model behavior that persists across iterations.

hackernews · domhudson · Sep 8, 14:13 · [Discussion](https://news.ycombinator.com/item?id=49610631)

**Background**: Coding agents like Claude Code are agentic tools that understand codebases, edit files, and run commands to assist developers. 'Skills' are plugins or instruction sets that can be installed to modify agent behavior, and the community has built a large ecosystem of such skills for tools including Claude, OpenAI Codex, Gemini CLI, and Cursor. Prompt engineering techniques, including concise prompting, are commonly used to control LLM output length and structure, but model-level tendencies toward verbosity often resist persistent correction.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alirezarezvani/claude-skills">alirezarezvani/ claude - skills : 380 Claude Code skills & agent skills ...</a></li>
<li><a href="https://portkey.ai/blog/optimize-token-efficiency-in-prompts/">How to Optimize Token Efficiency When Prompting</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent , Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: Community sentiment is strongly positive about the tool's effectiveness but frustrated with the underlying model behavior it addresses. Users like ryandrake and jp57 highlight specific 'Claudisms' such as excessive use of 'not-this-but-that' constructions and burying the lede, while sleazebreeze notes the conciseness only lasts a few turns before the model reverts, suggesting the problem requires deeper fixes from Anthropic rather than prompt-level workarounds.

**Tags**: `#LLM-tooling`, `#coding-agents`, `#prompt-engineering`, `#Claude`, `#developer-experience`

---

<a id="item-15"></a>
## [Abusive crawlers now consume more CPU than legitimate access on git.kernel.org](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 6.0/10

Konstantin Ryabitsev reports that abusive crawlers now consume more CPU cycles on git.kernel.org than all legitimate access combined, including git clones. At any given time, across five geo-distributed nodes, 14 CPU cores are dedicated solely to rendering git commits as HTML for scrapers. This highlights a growing operational crisis for public infrastructure as AI-driven crawlers increasingly scrape content for training data, imposing unsustainable costs on maintainers of open-source projects. Simon Willison echoes the concern for his own Datasette project, which serves a large number of crawlable web pages and faces similar exposure. The 14 CPU cores continuously rendering commits as HTML represent pure overhead with no benefit to the kernel community, effectively a form of involuntary resource subsidization by abusive bots. The problem is distributed across five geo-distributed nodes, indicating it is not localized but systemic.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository hosting site for the Linux kernel source code, maintained by the kernel community and serving developers worldwide. Datasette is an open-source tool by Simon Willison for exploring and publishing data, which generates many crawlable web pages. As AI companies ramp up data collection for model training, aggressive and often poorly-behaved crawlers have become a significant burden on public infrastructure, raising both cost and ethical concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kernel.org">kernel . org - Wikipedia</a></li>
<li><a href="https://pypi.org/project/datasette/">datasette · PyPI</a></li>

</ul>
</details>

**Tags**: `#web-crawling`, `#infrastructure`, `#scraping`, `#git`, `#ai-training-data`

---

<a id="item-16"></a>
## [OpenAI Chief Scientist Jakub Pachocki on Defensive AI and Reckless Racing](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 6.0/10

Simon Willison shared a quote from OpenAI Chief Scientist Jakub Pachocki, who argues that building smarter AI models is necessary to create defensive systems against rogue AI agents. Pachocki also emphasizes that despite the need for defensive capabilities, the AI industry must avoid reckless racing due to the serious stakes involved. This statement highlights a critical tension within the AI industry: the need to rapidly develop advanced AI for defensive purposes versus the risks of racing toward AGI without adequate safety measures. It reflects an ongoing debate among AI leaders about whether accelerating model development is the best way to ensure safety or if it inherently increases existential risks. Pachocki notes that powerful, aligned AI will be required to secure infrastructure, protect against rogue agents in real time, and invent new protective measures, making it a primary focus of OpenAI’s deployment efforts. He explicitly warns that the necessity of building defensive systems should not be used as an excuse for recklessness.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment is a subfield of AI safety focused on ensuring that AI systems reliably pursue objectives consistent with human intentions and values. As AI systems become more capable, concerns about rogue agents—autonomous AI that deviates from its intended function or acts harmfully—have increased. Many prominent AI researchers and executives have warned that advanced AI could endanger human civilization if not properly aligned, leading to debates over the pace of AI development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://grokipedia.com/page/AI_Agents_Gone_Rogue">AI Agents Gone Rogue</a></li>

</ul>
</details>

**Tags**: `#ai-safety`, `#ai-ethics`, `#openai`, `#alignment`, `#ai-defense`

---

<a id="item-17"></a>
## [Stanford Launches Free 'Probability for AI' Course with 1:10 Teacher Ratio](https://www.reddit.com/r/MachineLearning/comments/1wbf3ox/teach_ml_community_service_project_from_stanford_n/) ⭐️ 6.0/10

Stanford professor Chris Piech announced a free online course called 'Probability for AI' starting October 9th, featuring a unique model where one volunteer teacher is assigned for every 10 students. The course includes interactive tools and a free coding agent that allows students to build AI applications, such as an AI text detection app, after just one hour of learning. This initiative democratizes access to high-quality AI education by providing a free, community-driven learning experience with an unusually low teacher-to-student ratio, which could significantly improve learning outcomes. It also leverages AI coding agents as educational partners, reflecting a broader trend of integrating AI tools into the learning process to make complex subjects more accessible. The course is funded by a kind alum, keeping it free for all participants, and has already attracted over 1,000 volunteer teacher applications. The curriculum is designed to be accessible to individuals with only a light math background, and volunteer teachers receive training, including practice with teachable agents.

reddit · r/MachineLearning · /u/chrispiech · Sep 9, 07:54

**Background**: Probability is a foundational mathematical concept for artificial intelligence and machine learning, underpinning algorithms for inference, prediction, and decision-making. AI coding agents are systems designed to autonomously assist with software development tasks, and their use in education can help students bridge the gap between theoretical concepts and practical application. Teachable agents are AI systems designed to learn from users, creating a collaborative learning environment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_coding_agent">AI coding agent</a></li>
<li><a href="https://www.emergentmind.com/topics/instructional-agents">Instructional Agents</a></li>

</ul>
</details>

**Tags**: `#education`, `#machine-learning`, `#community`, `#stanford`, `#probability`

---

<a id="item-18"></a>
## [Rustuna: High-Performance Rust Implementation of Optuna Released](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 6.0/10

The Optuna team has released Rustuna, a Rust-based reimplementation of the popular Optuna hyperparameter optimization framework that maintains API compatibility while eliminating all Python dependencies. The project offers improved memory efficiency and native performance through Rust's memory management. This release matters because Optuna is widely used across the ML community for hyperparameter tuning, and a Rust implementation addresses growing concerns about Python supply chain security and memory overhead in large-scale optimization workflows. ML practitioners who need to run many trials in resource-constrained or security-sensitive environments now have a viable alternative that preserves the familiar Optuna API. Rustuna keeps the familiar Optuna API and concepts, meaning existing users can transition without learning a new interface. The zero-Python-dependency design specifically mitigates supply chain attack risks that have become a significant concern in the Python ecosystem, while Rust's native memory management reduces the memory footprint compared to the Python version.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is an open-source hyperparameter optimization framework originally introduced in 2018 by Preferred Networks, with its first stable release in January 2020. Hyperparameter optimization is the process of systematically selecting optimal hyperparameters for a machine learning algorithm to maximize model performance, which is critical for achieving the best results from ML models. Optuna supports a define-by-run API, pruning of unpromising trials, and distributed parallel optimization, making it one of the most popular HPO tools in the ML ecosystem. Rustuna reimagines this framework in Rust, a systems programming language known for memory safety and performance without garbage collection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optuna">Optuna</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperparameter_optimization">Hyperparameter optimization</a></li>
<li><a href="https://optuna.org/">Optuna - A hyperparameter optimization framework</a></li>

</ul>
</details>

**Tags**: `#hyperparameter-optimization`, `#rust`, `#optuna`, `#ml-tooling`, `#performance`

---