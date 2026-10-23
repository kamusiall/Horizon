---
layout: default
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23
lang: en
---

> From 34 items, 12 important content pieces were selected

---

1. [NVIDIA OpenShell: Secure Runtime for Autonomous AI Agent Fleets](#item-1) ⭐️ 8.0/10
2. [Anthropic Shows LLMs Scale Formal Software Verification](#item-2) ⭐️ 8.0/10
3. [Anthropic Donates Agent Skills Standard to the Agentic AI Foundation](#item-3) ⭐️ 8.0/10
4. [Dijkstra's 1978 Essay Against Natural Language Programming Resurfaces Amid LLM Era](#item-4) ⭐️ 7.0/10
5. [Project Runs Full iOS 16.5 Firmware on Android Devices via XNU Kernel](#item-5) ⭐️ 7.0/10
6. [WorldTUI: A 360M Parameter Model Simulating a Terminal UI](#item-6) ⭐️ 7.0/10
7. [Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](#item-7) ⭐️ 7.0/10
8. [Carbon-X: Open 14.8B Model Trained Jointly on DNA and Text](#item-8) ⭐️ 7.0/10
9. [Open-XTTS-Trainer Enables 1-Click Training for All XTTS v2 Components](#item-9) ⭐️ 7.0/10
10. [WhissleAI Shrinks SteerTTS to 11.84 MB with int4 Quantization](#item-10) ⭐️ 7.0/10
11. [Frontier Models Struggle with ASMR Audio Classification: 8-Judge Evaluation on 480 Clips](#item-11) ⭐️ 6.0/10
12. [Few-Read Fault Localization in Simulated Analog Crossbars Using Sparse Recovery](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [NVIDIA OpenShell: Secure Runtime for Autonomous AI Agent Fleets](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA has released OpenShell, an open-source sandbox runtime that provides kernel-level isolation and declarative YAML-based security policies for executing fleets of autonomous AI agents. The tool was publicly previewed for Ubuntu at Computex in June 2026, with version 0.1.0 adding policy verification, credential-protected service access, multi-tenant deployment support, and CPU/GPU execution capabilities. As organizations deploy fleets of autonomous AI agents that need to coordinate tasks, a novel security problem emerges: agents can collude to exceed their collective permissions by delegating tasks to other agents with different access levels. OpenShell addresses this by managing both individual agent sandboxing and collective permission boundaries, making it a significant step toward safe production deployment of multi-agent systems. OpenShell uses a policy.yaml file to define sandbox security policies controlling agents' access to files, processes, networks, external services, and credentials through kernel-level isolation. The runtime was developed in collaboration with Canonical and targets Ubuntu, though it supports multi-tenant deployments with both CPU and GPU execution modes.

hackernews · niemandhier · Oct 22, 17:44 · [Discussion](https://news.ycombinator.com/item?id=50198675)

**Background**: AI agent sandboxing combines isolation, policy enforcement, and monitoring to limit what an autonomous agent can execute, access, and transmit during a task. As AI agents have evolved from simple LLM-based chatbots to autonomous systems that can read files, install packages, call APIs, and use credentials, the security challenges have grown correspondingly. In multi-agent fleets, agents must communicate and coordinate, which creates opportunities for collusion where agents collectively exceed their intended permissions by delegating tasks to peers with different access rights. Traditional container-based isolation addresses some risks but does not handle the collective permission escalation problem that emerges in coordinated agent fleets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_OpenShell">Nvidia OpenShell</a></li>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>
<li><a href="https://dev.to/imversion_tech/ai-agent-sandboxing-practical-guide-for-production-safety-58p8">AI Agent Sandboxing: Practical Guide for Production Safety</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the novelty of the collusion problem, noting that agents can delegate tasks to peers with different permissions to bypass individual sandbox restrictions. Several users pointed out the inherent tension between agent capability and security, with one observing that the more access you give an agent the more capable it becomes, making the promise of 'full capability but now secure' an oxymoron. Others discussed alternative approaches like network proxies (e.g., iron proxy) for domain-level restrictions, while some noted that anyone not already running agents in containers is taking unnecessary risks, though OpenShell appears to be a useful tool for managing those containers.

**Tags**: `#AI agents`, `#security`, `#sandboxing`, `#NVIDIA`, `#agent fleets`

---

<a id="item-2"></a>
## [Anthropic Shows LLMs Scale Formal Software Verification](https://www.anthropic.com/research/formal-verification) ⭐️ 8.0/10

Anthropic published research demonstrating that large language models can automate proof generation for formal software verification, making it practical at a much larger scale than previously possible. The approach uses LLMs to generate proofs that code satisfies formal specifications, dramatically reducing the manual effort traditionally required for deductive verification. Formal verification has historically been too labor-intensive and expensive for widespread use, limiting it to niche critical systems like aerospace and cryptography. If LLMs can automate much of the proof generation, mathematical guarantees of code correctness could become accessible to mainstream software development, significantly improving software reliability and security across the industry. The research notes that the Rocq proof checker mechanically ensures the specification is correctly satisfied by the proof, meaning developers only need to trust the formal models, the theorem statements, and the proof checker itself rather than manually reviewing all generated proof code. Community practitioners report concrete success translating Rust and C code into Lean for LLM-assisted equivalence proofs, with one developer verifying approximately 70,000 lines of C code and finding subtle behavioral differences such as floating-point handling discrepancies.

hackernews · johnbender · Oct 22, 22:54 · [Discussion](https://news.ycombinator.com/item?id=50202217)

**Background**: Formal verification is the process of using mathematical proofs to show that a program satisfies a formal specification of its behavior, as opposed to testing which only checks specific execution cases. Proof assistants like Rocq (formerly Coq) and Lean can mechanically check proofs, but writing these proofs manually is extremely time-consuming and requires deep expertise in both the target domain and proof theory. A key distinction in this field is between verification ("Are we building the product right?") and validation ("Are we building the right product?") — even perfectly verified code only proves correctness relative to a specification, not that the specification itself captures the right problem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/formal-verification">LLMs are making formal software verification feasible at a ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The discussion highlights the important distinction between verification and validation, with commenters emphasizing that formally verified code can still solve the wrong problem if the specification is incorrect. One practitioner shared concrete success translating Rust and C into Lean for LLM-assisted equivalence proofs, covering about 70,000 lines of C code and finding subtle behavioral differences. Another commenter raised the key trust question, which the research addresses by noting that only the formal models, theorem statements, and proof checker need to be trusted, not the generated proofs themselves.

**Tags**: `#formal-verification`, `#LLMs`, `#software-reliability`, `#automated-proving`, `#Anthropic`

---

<a id="item-3"></a>
## [Anthropic Donates Agent Skills Standard to the Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 8.0/10

Anthropic is donating the Agent Skills open standard, including its name, logo, GitHub organization, and the agentskills.io domain, to the Agentic AI Foundation (AAIF) under the Linux Foundation. This ensures the standard remains open, community-driven, and vendor-neutral. This donation reinforces the industry's shift toward collaborative, vendor-neutral standards for agentic AI, promoting interoperability among major players like Anthropic, OpenAI, and Block. It allows developers to build and extend AI agent capabilities using a shared, open format without being locked into a single ecosystem. Agent Skills provide a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. Developers can continue to use the standard or contribute to it on GitHub without needing to join the AAIF.

rss · Simon Willison · Oct 22, 18:09

**Background**: The Agentic AI Foundation (AAIF) is a directed fund under the Linux Foundation co-founded in December 2025 by Anthropic, OpenAI, and Block to govern open standards for autonomous AI agents. Previously, Anthropic donated the Model Context Protocol (MCP), an open-source standard for connecting AI applications to external data sources and tools, to the same foundation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation">Donating Agent Skills to the Agentic AI Foundation \ Anthropic</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://amquesteducation.com/blog/agentic-ai-foundation-aaif/">Agentic AI Foundation ( AAIF ): Open Standards Guide</a></li>

</ul>
</details>

**Discussion**: Simon Willison highlighted that he accurately predicted this donation last December when Anthropic first declared Agent Skills an open standard. He also amusingly noted that he found his old prediction by prompting Claude to search his own website using the Model Context Protocol (MCP).

**Tags**: `#agentic-ai`, `#anthropic`, `#open-standards`, `#agent-skills`, `#linux-foundation`

---

<a id="item-4"></a>
## [Dijkstra's 1978 Essay Against Natural Language Programming Resurfaces Amid LLM Era](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html) ⭐️ 7.0/10

Edsger W. Dijkstra's 1978 essay "On the foolishness of 'natural language programming'" has resurfaced on Hacker News, sparking renewed debate about its relevance in the era of Large Language Models (LLMs) and AI agents. The essay argues that natural language is inherently unsuitable for programming due to its ambiguity and lack of formal precision. This resurgence is significant because modern AI tools increasingly use natural language prompts to generate code, leading some to claim English has become a new programming abstraction layer. Dijkstra's arguments challenge this notion, forcing developers to critically examine whether natural language can reliably serve as a foundation for software development or if it merely shifts the complexity to AI intermediaries. Dijkstra specifically warned of "The New Illiteracy," arguing that natural language lacks the technical precision required for deterministic computation. The essay distinguishes between formal programming languages, which eliminate ambiguity, and natural language, which relies on context and interpretation.

hackernews · xiaoyu2006 · Oct 23, 00:52 · [Discussion](https://news.ycombinator.com/item?id=50203161)

**Background**: Edsger W. Dijkstra was a pioneering computer scientist known for his rigorous approach to programming and his influential essays (designated as "EWD" manuscripts). Natural language programming refers to the concept of writing computer programs using everyday human languages like English, rather than formal syntax. Historically, this concept has been explored in niche applications like Inform 7, but the rise of LLMs has brought it back into mainstream discussion as a potential paradigm for software development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html">E.W.Dijkstra Archive: On the foolishness of " natural language ..."</a></li>
<li><a href="https://en.wikipedia.org/wiki/Natural_language_programming">Natural language programming</a></li>

</ul>
</details>

**Discussion**: The community largely agrees with Dijkstra's premise, with many arguing that in the context of AI agents, the agent itself is the programmer using deterministic languages, not the human using natural language. Commenters highlight the distinction between communicating with mechanical systems versus intelligent entities, noting that while LLMs can interpret vague instructions, the resulting code quality often reflects the user's underlying understanding of the codebase.

**Tags**: `#natural-language-programming`, `#dijkstra`, `#llms`, `#agents`, `#programming-abstraction`

---

<a id="item-5"></a>
## [Project Runs Full iOS 16.5 Firmware on Android Devices via XNU Kernel](https://github.com/oosexgang/hackios-xnu-kernel) ⭐️ 7.0/10

A project called hackios-xnu-kernel by the group oosexgang demonstrates the ability to run full iOS 16.5 firmware on Android devices using Apple's XNU kernel, functioning as a research bench that runs timed sessions on QEMU and certain Xiaomi devices such as the POCO X5 Pro 5G. This is a notable technical achievement in cross-platform OS kernel execution, showing that iOS firmware can be booted on non-Apple hardware, which could have implications for security research, reverse engineering, and the broader emulation community. It also raises practical concerns about the potential for counterfeit devices that could run genuine iOS firmware on Android hardware, making it harder for consumers to distinguish authentic iPhones from replicas. The project is explicitly described as a research bench rather than a ROM: each session lasts a given number of seconds, after which the kernel returns to the loader and hands over its log, meaning it is not yet a practical daily-use system. The project works on QEMU as well as select Xiaomi devices, and the source code is available on GitHub.

hackernews · aghuang · Oct 22, 15:26 · [Discussion](https://news.ycombinator.com/item?id=50196718)

**Background**: XNU ('X is Not Unix') is the hybrid operating system kernel developed by Apple, originally created by NeXT for NeXTSTEP and later acquired by Apple for use in macOS, iOS, iPadOS, watchOS, and tvOS. It combines components from the Mach microkernel, BSD, and IOKit for device drivers. QEMU is a generic, open-source machine emulator and virtualizer capable of emulating many different hardware architectures, making it a popular tool for firmware research and OS porting experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XNU_kernel">XNU kernel</a></li>
<li><a href="https://www.qemu.org/docs/master/about/index.html">About QEMU — QEMU documentation</a></li>

</ul>
</details>

**Discussion**: Community members expressed admiration for the technical achievement while noting practical concerns, such as the risk that counterfeit phone makers could leverage this technology to create more convincing fake iPhones. One commenter speculated that the timed-session design might be a safeguard to prevent misuse, while others praised the project's novelty and humorously anticipated similar efforts for other locked-down firmware ecosystems like Garmin devices.

**Tags**: `#iOS`, `#XNU-kernel`, `#Android`, `#emulation`, `#reverse-engineering`

---

<a id="item-6"></a>
## [WorldTUI: A 360M Parameter Model Simulating a Terminal UI](https://simedw.com/2026/10/21/world-model-terminal/) ⭐️ 7.0/10

The author fine-tuned a 360M parameter model based on Qwen2.5-Coder-0.5B to simulate a terminal UI by predicting screen updates from user keypresses. Unlike previous LLM terminal tricks, this model is specifically trained on keypresses and screen updates, enabling it to simulate full-screen applications like vim and tmux without an actual shell or file system. This project demonstrates a novel application of small language models as generative 'world models' that can simulate complex software environments without an underlying operating system. It showcases the potential for creating interactive 'Neural Computers' where the entire user interface is generated on the fly, blurring the line between simulated and real software. The model was trained using Qwen2.5-Coder-0.5B as a starting point to achieve near real-time performance, leveraging its prior exposure to CLI usage. Fine-tuning significantly improved the model's memory and ability to maintain state across simulated terminal interactions.

hackernews · alphax314 · Oct 22, 02:18 · [Discussion](https://news.ycombinator.com/item?id=50190363)

**Background**: A 'world model' in machine learning refers to a model that learns a simulation of an environment, allowing it to predict future states based on actions. In this context, the terminal environment is treated as the 'world,' and the model predicts the next screen state based on the user's keystrokes. This concept is related to the idea of a 'Neural Computer,' where the entire UI is generative rather than backed by a traditional operating system.

<details><summary>References</summary>
<ul>
<li><a href="https://simedw.com/2026/10/21/world-model-terminal/">WorldTUI : I trained a 360M model to pretend to be... - SimEdw's Blog</a></li>
<li><a href="https://ai-manual.ru/article/worldtui-kak-model-na-360m-parametrov-izobrazhaet-terminal-bez-shella-i-fajlovoj-sistemyi/">WorldTUI : как модель на 360M параметров изображает... | AiManual</a></li>

</ul>
</details>

**Discussion**: The community expressed excitement about the project, with commenters drawing parallels to the early ChatGPT 'pretend to be a terminal' prompt and discussing the theoretical concept of a 'Neural Computer.' Users also noted the interesting choice of base model and shared related projects like a 'lossy git' version control system powered by neural networks.

**Tags**: `#LLMs`, `#Fine-tuning`, `#World Models`, `#Generative UI`, `#Terminal`

---

<a id="item-7"></a>
## [Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://www.reddit.com/r/MachineLearning/comments/1xd7bsu/i_just_came_across_nextconcept_modeling_and_the/) ⭐️ 7.0/10

Researchers introduced Next-Concept Modeling (NCM), a two-stage coarse-to-fine framework that uses a multiscale residual VQ-VAE to encode text into a hierarchy of discrete codes, which are then generated level by level in parallel by a transformer. This approach reportedly achieves up to 31x faster generation compared to diffusion language model baselines on specific benchmarks. As inference becomes a dominant computational workload, NCM offers a promising alternative to both autoregressive and diffusion language models by enabling parallel generation without the quality degradation associated with fewer sampling steps in DLMs. This could significantly reduce the latency and cost of generating text at scale. The NCM architecture consists of a multiscale residual VQ-VAE that compresses text into discrete codes, followed by a transformer that predicts all codes within a single level simultaneously. Unlike diffusion models that process the full sequence at every denoising step, NCM generates text one hierarchical level at a time, reducing the number of passes required.

reddit · r/MachineLearning · /u/PanelReader · Oct 23, 07:24

**Background**: Traditional language models generate text autoregressively, predicting one token at a time, which is slow for long sequences. Diffusion Language Models (DLMs) attempt to solve this by generating text through iterative denoising, allowing parallel refinement, but they often require many passes and degrade with fewer steps. VQ-VAE (Vector-Quantized Variational Autoencoder) is a generative model that maps continuous latent representations into discrete embeddings using a codebook, commonly used for hierarchical or discrete representation learning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.14162">[2610.14162] Next-Concept Modeling: Fast, Parallel Coarse-to ...</a></li>
<li><a href="https://hazyresearch.stanford.edu/blog/2026-10-12-ncm">Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text ...</a></li>
<li><a href="https://huggingface.co/blog/ariG23498/understand-vq">Understanding Vector Quantization in VQ-VAE - Hugging Face</a></li>

</ul>
</details>

**Discussion**: The Reddit post is from a beginner sharing their fascination with the NCM paper and asking if others have explored the approach, but no community comments were provided in the news item.

**Tags**: `#Next-Concept Modeling`, `#Language Models`, `#VQ-VAE`, `#Inference Optimization`, `#Machine Learning`

---

<a id="item-8"></a>
## [Carbon-X: Open 14.8B Model Trained Jointly on DNA and Text](https://www.reddit.com/r/MachineLearning/comments/1xchayq/carbonx_is_an_open_148b_model_trained_jointly_on/) ⭐️ 7.0/10

Carbon-X is a newly released open-source 14.8B parameter decoder-only model that can analyze raw DNA sequences and answer in English. It was mid-trained on 302B tokens and achieves a 66.7% average across five DNA benchmarks, closely matching the 67.5% score of the proprietary GPT-6.1 Sol model. This model bridges genomics and natural language processing, allowing researchers to analyze sensitive genomic datasets locally without relying on proprietary APIs. Its open-weight release under the Apache 2.0 license democratizes access to advanced DNA analysis tools while fitting on a single 80GB GPU. The model uses a shared token stream for text and DNA, utilizing 6-mer tokens, and its weights fit on one 80GB GPU in bfloat16 precision. It has not been clinically validated, and the model card notes that exact sequence operations should still be handled by code rather than the model.

reddit · r/MachineLearning · /u/jatingargiitk · Oct 22, 12:32

**Background**: DNA sequences can be tokenized into k-mers (subsequences of length k) to be processed by transformer-based language models, similar to how text is tokenized into words or subwords. Bfloat16 is a 16-bit floating-point format that offers a larger dynamic range than standard FP16, making it suitable for training and running deep learning models efficiently on modern GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/414863299_What_Can_Language_Models_Learn_from_DNA_A_Critical_Survey_of_Genomic_Foundation_Models">(PDF) What Can Language Models Learn from DNA ? A Critical Survey...</a></li>
<li><a href="https://arxiv.org/abs/1905.12322">[1905.12322] A Study of BFLOAT16 for Deep Learning Training A Study of BFLOAT16 for Deep Learning Training - arXiv.org What is bfloat16 and Why Deep Learning Uses It - binary REVISITINGBFLOAT16 TRAINING - OpenReview DLFloat: A 16-b Floating Point Format Designed for Deep ... A Study of BFLOAT16 for Deep Learning Training - NASA/ADS A Study of BFLOAT16 for Deep Learning Training - ResearchGate</a></li>

</ul>
</details>

**Tags**: `#genomics`, `#bioinformatics`, `#open-source-models`, `#multimodal`, `#LLMs`

---

<a id="item-9"></a>
## [Open-XTTS-Trainer Enables 1-Click Training for All XTTS v2 Components](https://www.reddit.com/r/MachineLearning/comments/1xcurgj/i_built_openxttstrainer_now_you_can_add_new/) ⭐️ 7.0/10

A new open-source training suite called Open-XTTS-Trainer allows users to train all three components of XTTS v2 (DVAE, GPT, and Latent HiFi-GAN) in a single click. It also introduces a text and vocabulary extender that dynamically resizes the GPT embedding matrix to support new language scripts like Arabic and Indic languages. This tool fills a significant gap in the open-source text-to-speech ecosystem by restoring the missing training pipelines left behind after Coqui AI shut down. It enables researchers and developers to adapt the powerful XTTS v2 model to new languages and scripts that were previously blocked by hardcoded vocabularies. The suite is licensed under MPL-2.0, runs out-of-the-box on modern PyTorch (Python 3.10–3.13) without dependency rot, and includes verified GPU loss convergence benchmarks on real human speech. It features a 1-click Google Colab demo and dynamically appends unique Unicode glyphs to the tokenizer without corrupting existing weights.

reddit · r/MachineLearning · /u/yashubhakt · Oct 22, 21:03

**Background**: XTTS v2 is a highly regarded local zero-shot text-to-speech model, but its development stalled when Coqui AI shut down, leaving the training code for its DVAE audio tokenizer and Latent HiFi-GAN vocoder unreleased. A DVAE (Discrete Variational Autoencoder) converts audio codes to mel spectrograms, while HiFi-GAN is a generative adversarial network-based vocoder that turns mel-spectrograms into high-quality raw audio waveforms. The original XTTS v2 was also hardcoded for only 17 languages, causing crashes when fed text with new Unicode scripts.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/coqui/XTTS-v2">coqui / XTTS - v 2 · Hugging Face</a></li>
<li><a href="https://github.com/jik876/hifi-gan">GitHub - jik876/hifi-gan: HiFi-GAN: Generative Adversarial ... HiFi-GAN and GAN Vocoders Guide | AI Understanding amitbhakt/open-xtts-trainer · Hugging Face Vocoder: HiFi-GAN and HiFT | xxyyboy/CosyVoice | DeepWiki HiFi GAN - PyTorch High-Fidelity Music Vocoder usingNeural Audio Codecs</a></li>
<li><a href="https://deepwiki.com/2noise/ChatTTS/3.2-dvae-and-audio-processing">DVAE and Audio Processing | 2noise/ChatTTS | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#XTTS-v2`, `#open-source`, `#speech-synthesis`, `#multilingual`

---

<a id="item-10"></a>
## [WhissleAI Shrinks SteerTTS to 11.84 MB with int4 Quantization](https://www.reddit.com/r/MachineLearning/comments/1xcum4s/we_shrank_our_steerable_small_tts_to_1184_mb_wer/) ⭐️ 7.0/10

WhissleAI released an edge variant of SteerTTS compressed to a total of 11.84 MB using int4 quantization-aware training (QAT) on both the 9.25M-parameter acoustic model (attention + bidirectional Mamba-3) and a 6.2M-parameter Vocos-style vocoder distilled from charactr/vocos-mel-24khz. The edge model maintains unchanged word error rate (0.96%) with only a ~0.1 UTMOS drop, preserves all 12 steering controls at 95%+ of their fp32 effect, and replaces heavy text-processing dependencies with a pure-numpy front end. This demonstrates that a fully steerable, high-quality English TTS system can fit into under 12 MB including all runtime dependencies, making it viable for on-device and edge deployment scenarios where bandwidth, storage, and latency are constrained. The preservation of intelligibility and controllability through aggressive int4 quantization provides a practical blueprint for compressing Mamba-based generative audio models without sacrificing their core functionality. The acoustic model uses attention combined with bidirectional Mamba-3 blocks, while the vocoder is a Vocos-style spectral vocoder distilled to 6.2M parameters and quantized to int4; nearly all of the ~0.1 UTMOS degradation comes from the small int4 vocoder rather than the acoustic model. On a 2018 Threadripper, the system achieves RTF 0.053 (~19x realtime) with ~120 ms time-to-first-audio and sentence-level streaming, but weights are dequantized to fp32 at load so the benefit is size rather than inference speed unless custom edge kernels are written. Limitations include English-only support, 200 voices (vs. 2,825 in the full model), no on-device voice cloning or free-text prompts, and weaker emotion tags for fast and anger styles.

reddit · r/MachineLearning · /u/Working_Hat5120 · Oct 22, 20:57

**Background**: Quantization-aware training (QAT) emulates lower-precision inference during training so the final model retains higher accuracy than naive post-training quantization, and int4 (4-bit integer) quantization is an aggressive form that dramatically reduces model size at the risk of quality loss. Vocos is a fast neural vocoder that generates spectral coefficients rather than time-domain samples, enabling rapid audio reconstruction via inverse Fourier transform in a single forward pass. Mamba-3 is a recent architecture variant that improves upon earlier state-space model designs for more efficient sequence modeling. SteerTTS is a controllable TTS system where prosodic parameters such as rate, pitch, loudness, and breathiness are adjusted via numerical steering controls and inline markup tags.

<details><summary>References</summary>
<ul>
<li><a href="https://pytorch.org/blog/quantization-aware-training/">Quantization-Aware Training for Large Language Models with ...</a></li>
<li><a href="https://github.com/gemelo-ai/vocos">GitHub - gemelo-ai/vocos: Vocos: Closing the gap between time ...</a></li>
<li><a href="https://arxiv.org/abs/2306.00814">[2306.00814] Vocos: Closing the gap between time-domain and ... GitHub - LqNoob/vocos: Vocos: Closing the gap between time ... Vocos: Closing the gap between time-domain and Fourier-based ... BSC-LT/vocos-mel-22khz · Hugging Face charactr/vocos-mel-24khz · Hugging Face vocos · PyPI</a></li>

</ul>
</details>

**Tags**: `#text-to-speech`, `#model-compression`, `#quantization`, `#edge-deployment`, `#mamba`

---

<a id="item-11"></a>
## [Frontier Models Struggle with ASMR Audio Classification: 8-Judge Evaluation on 480 Clips](https://www.reddit.com/r/MachineLearning/comments/1xcbqdm/frontier_models_are_bad_at_hearing_asmr_8_judges/) ⭐️ 6.0/10

An evaluation of 8 frontier multimodal models as audio labellers for ASMR sounds found they perform surprisingly poorly, with F1 scores ranging from 0.11 to 0.33 against human labels on 480 clips. Gemini 3.1 Pro led at 0.325 F1, while spectrogram-image-based approaches (Claude Opus 5.5 at 0.121 and Grok 4.7 at 0.110) performed worst. This reveals a significant gap in the audio understanding capabilities of frontier multimodal models, particularly for fine-grained physical trigger sounds like paper rustling, brushing, and sticky sounds. Anyone building audio data pipelines or relying on LLMs for audio annotation should be aware that current models cannot reliably label subtle foley sounds, and human-in-the-loop labelling remains essential for these categories. The evaluation used 20 labels across 480 clips, with external clips from FSD50K and ESC-50 datasets measuring recall and 6-second ASMR clips labelled by humans measuring F1. Physical triggers (paper, brushing, cutting, sticky, spraying) were nearly invisible to all judges — on 40 paper/page-turning clips, Gemini 3.1 Pro and 2.5 Pro each named paper rustling only 4 times. Whispering F1 was 0.70–0.79 for Gemini and MiMo judges, showing voices are handled well. The author uses Dawid-Skene fusion with per-class reliability weighting, routing uncertain clips to human labellers, and notes that adding 2,400 Freesound clips improved test mAP from 0.516 to 0.549 but brushing and paper detection remained at 0% on external clips at p > 0.5.

reddit · r/MachineLearning · /u/MissAppleby · Oct 22, 07:10

**Background**: ASMR (Autonomous Sensory Meridian Response) content features whispering and trigger sounds like tapping, crinkling, and brushing. FSD50K is a dataset of 51,197 human-labeled Freesound clips across 200 AudioSet classes, while ESC-50 contains 2,000 5-second environmental sound recordings across 50 semantical classes. CLAP (Contrastive Language-Audio Pretraining) is an audio embedding model used for sound classification, and Dawid-Skene is a probabilistic method for aggregating noisy labels from multiple annotators by estimating each annotator's reliability per class.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/datasets/Fhrozen/FSD50k">Fhrozen/FSD50k · Datasets at Hugging Face</a></li>
<li><a href="https://github.com/karolpiczak/ESC-50">GitHub - karolpiczak/ESC-50: ESC-50: Dataset for ...</a></li>

</ul>
</details>

**Discussion**: The post invites community input, asking whether others have had better luck getting audio LLMs to hear fine-grained foley sounds and welcoming suggestions for sound-event models worth adding as judges. No detailed comment responses were available to assess broader community sentiment.

**Tags**: `#multimodal-models`, `#audio-classification`, `#data-labeling`, `#model-evaluation`, `#frontier-models`

---

<a id="item-12"></a>
## [Few-Read Fault Localization in Simulated Analog Crossbars Using Sparse Recovery](https://www.reddit.com/r/MachineLearning/comments/1xbj6nj/fewread_fault_localization_in_simulated_analog/) ⭐️ 6.0/10

A simulation-based study demonstrates that a sparse-recovery decoder can localize up to 64 stuck-at faults in a 256x256 analog crossbar tile using only 4 to 12 random probe reads, compared to the 256 reads required for a full readout. The study also transparently reports several pre-registered claims that failed during testing. This approach significantly reduces the number of reads needed for fault localization in analog in-memory computing hardware, potentially lowering testing overhead and improving maintenance efficiency. The transparent reporting of failed hypotheses sets a strong example for rigorous, reproducible research in hardware-ML intersections. The method assumes a sparse fault model and uses random +/-1 probe vectors, achieving 1.9 to 6.4 times fewer reads than a hybrid baseline built on a published multi-outlier code. However, the study is simulation-only, relies on stored digital weights, and has limitations including unverified bidirectional periphery costs and overly tight confidence bounds due to clustered sampling.

reddit · r/MachineLearning · /u/Connect_Agency_3975 · Oct 21, 10:09

**Background**: Analog crossbar tiles perform matrix-vector multiplications directly within memory arrays, offering high efficiency for machine learning workloads but suffering from device defects like stuck-at faults where a cell remains at a fixed value. Sparse recovery is a signal processing technique that identifies a small number of anomalous elements (in this case, faulty cells) from a limited number of measurements. Fault localization in these systems typically requires reading every cell, making a few-read approach highly desirable for scalable maintenance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/330491353_Handling_stuck-at-faults_in_memristor_crossbar_arrays_using_matrix_transformations">Handling stuck - at - faults in memristor crossbar arrays using matrix...</a></li>
<li><a href="https://analogcomputesystems.com/">Analog Compute Systems ONNX to Analog Compiler for RRAM...</a></li>

</ul>
</details>

**Tags**: `#analog-computing`, `#fault-localization`, `#sparse-recovery`, `#hardware-ml`, `#crossbars`

---