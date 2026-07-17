---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 39 items, 15 important content pieces were selected

---

1. [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Multimodal Model](#item-1) ⭐️ 9.0/10
2. [Moonshot AI Releases Kimi K3, a 2.8T Parameter Open Model](#item-2) ⭐️ 8.0/10
3. [Linus Torvalds Firmly Endorses AI as a Useful Tool for Linux Kernel Development](#item-3) ⭐️ 8.0/10
4. [xAI open-sources Grok Build CLI after directory upload privacy backlash](#item-4) ⭐️ 8.0/10
5. [Claude web_fetch tool data exfiltration vulnerability disclosed](#item-5) ⭐️ 8.0/10
6. [LM Studio Introduces Bionic, an AI Agent Harness for Open Models](#item-6) ⭐️ 7.0/10
7. [Puter Compiles Firefox to WebAssembly Using Claude Opus](#item-7) ⭐️ 7.0/10
8. [ExTernD: Expanded-Rank Ternary Decomposition for LLM Post-Training Quantization](#item-8) ⭐️ 7.0/10
9. [AI Music Video Generation Compared: Claude Fable 5 vs. GPT-5.6 Sol](#item-9) ⭐️ 6.0/10
10. [Detecting LLM-Generated Text with Classical Machine Learning](#item-10) ⭐️ 6.0/10
11. [GPT-5.6 Codex Bug Deletes $HOME Directory Without Sandboxing](#item-11) ⭐️ 6.0/10
12. [Independent Researcher Shares DABSN Recurrent Architecture, Seeks Scaling Collaborators](#item-12) ⭐️ 6.0/10
13. [Call for Papers: Inaugural Real-Time Conversational Agents Workshop at NeurIPS 2026](#item-13) ⭐️ 6.0/10
14. [Researcher Seeks Devil's Advocates on Yann LeCun's JEPA Models](#item-14) ⭐️ 6.0/10
15. [PnP-CoSMo: Multi-Contrast MRI Reconstruction via Content/Style Modeling](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Multimodal Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

Thinking Machines Lab, founded by former OpenAI CTO Mira Murati, released Inkling, its first open-weights model — a 975B total parameter (41B active) Mixture-of-Experts multimodal transformer trained on 45 trillion tokens of text, images, audio, and video, released under the Apache-2.0 license. A smaller variant called Inkling-Small (276B total, 12B active) is also promised but not yet available. This release introduces a significant new US-based contender in the frontier open-weights ecosystem, joining the ranks of NVIDIA Nemotron and Gemma 4 as alternatives to Chinese open-weight models. However, Simon Willison notes that the model card and training data documentation are notably sparse, raising transparency concerns despite the model's competitive capabilities and permissive licensing. Thinking Machines explicitly states Inkling is not a frontier model but rather a strong base model intended for fine-tuning via their Tinker training platform. The training data documentation is remarkably vague, stating only that datasets include public domain content, publicly available internet data, and third-party datasets, without disclosing specific sources or composition.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) is an architecture that divides a model into multiple specialized sub-networks, allowing large total parameter counts while only activating a fraction during inference, which dramatically improves compute efficiency. Open-weights models publish their trained parameters publicly, enabling anyone to use, modify, and fine-tune them without restriction, as opposed to closed models accessible only via API. Thinking Machines Lab was founded in February 2025 by Mira Murati and raised $2 billion at a $12 billion valuation from investors including Nvidia, AMD, and Andreessen Horowitz.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thinking_Machines_Lab">Thinking Machines Lab</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://promptmetheus.com/resources/llm-knowledge-base/open-weights-model">Open - weights Model | LLM Knowledge Base</a></li>

</ul>
</details>

**Tags**: `#Open-weights`, `#Multimodal Models`, `#Thinking Machines Lab`, `#Mixture-of-Experts`, `#AI Releases`

---

<a id="item-2"></a>
## [Moonshot AI Releases Kimi K3, a 2.8T Parameter Open Model](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI launched Kimi K3 on July 16, 2026, a 2.8 trillion parameter open-weight model with a 1 million token context window, claiming the top spot as the world's largest open AI model. The model is positioned for long-horizon coding and end-to-end knowledge work, with performance reportedly approaching U.S. frontier models. This release intensifies the competition between Chinese and U.S. AI labs, as Moonshot pushes the boundary of open-weight model scale and signals a broader strategy of commoditizing AI intelligence. The availability of such a large open model could reshape market dynamics by pressuring proprietary providers on both performance and pricing. Kimi K3 is priced at $3 per 1M input tokens and $15 per 1M output tokens, with cached input at $0.3, matching Anthropic's Sonnet series pricing and considered high for a Chinese open-weight model. The model's 2.8T parameter count significantly exceeds other large open models like DeepSeek-V4-Pro (1.6T) and GLM-5.2 (754B), and running it will likely require substantial compute resources given Moonshot's reported $500 million in funding.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Moonshot AI is a Chinese AI startup that has developed the Kimi series of large language models, with earlier versions including K2.6 and K2.7 Code. Open-weight models are AI models whose parameters are publicly available, allowing developers to run, study, and modify them, in contrast to proprietary models accessed only via APIs. The release of increasingly large open models from Chinese labs has fueled debate about whether these companies are deliberately commoditizing AI intelligence to erode the moats of U.S. frontier labs. This trend echoes historical patterns where infrastructure and hardware become the primary value drivers as software capabilities become ubiquitous.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://felloai.com/kimi-k3/">Kimi K3: Moonshot's 2.8T Open-Weight Model Explained</a></li>
<li><a href="https://www.reuters.com/world/china/chinas-moonshot-unveils-worlds-largest-open-ai-model-closing-us-rivals-2026-07-17/">China's Moonshot unveils world's largest open AI model ...</a></li>

</ul>
</details>

**Discussion**: Community discussion centered on whether Chinese labs are strategically commoditizing AI intelligence, with some commenters suggesting this mirrors a 'commoditize your complement' approach to shift value toward hardware and infrastructure. Others noted the high pricing relative to typical Chinese open-weight models, with one user reporting a single pelican SVG render costing 25 cents due to extensive reasoning tokens. Concerns were also raised about the massive compute costs required to run a 2.8T parameter model despite Moonshot's substantial funding.

**Tags**: `#LLM`, `#open-models`, `#Moonshot-AI`, `#large-scale-models`, `#AI-market`

---

<a id="item-3"></a>
## [Linus Torvalds Firmly Endorses AI as a Useful Tool for Linux Kernel Development](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the top-level maintainer of the Linux kernel, made a definitive statement on the Linux Media Mailing List endorsing AI as a useful tool for kernel development. He explicitly stated that Linux is not an anti-AI project and told those who disagree to fork the project or walk away. As one of the most influential figures in open-source software, Torvalds' forceful endorsement of AI tools signals a major shift in attitudes toward AI-assisted development within the Linux community. His willingness to draw a hard line as maintainer carries significant weight and sets a clear direction for the project's culture going forward. Torvalds acknowledged that while there are open questions about the long-term economic impact of AI, the question of whether AI is useful is no longer in doubt. He attributed skepticism to a lack of actual hands-on experience with the technology, stating that anyone who doubts its utility "clearly hasn't actually used it."

rss · Simon Willison · Jul 16, 13:26

**Background**: The Linux kernel is developed through a decentralized but structured maintainer hierarchy, where changes are submitted as patches to mailing lists, reviewed, and eventually applied by maintainers before reaching Linus Torvalds' repository. As the top-level maintainer, Torvalds has final authority over what is accepted into the mainline kernel. In open-source software, forking a project means creating an independent copy to pursue a different development path, which Torvalds offered as the alternative for those who fundamentally disagree with his stance on AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fork_(software_development)">Fork (software development) - Wikipedia</a></li>
<li><a href="https://deepwiki.com/cxl-micron-reskit/famfs-linux/2-project-organization-and-maintainership">Project Organization and Maintainership | cxl-micron-reskit/famfs- linux</a></li>

</ul>
</details>

**Tags**: `#linus-torvalds`, `#linux`, `#ai-tools`, `#open-source`, `#ai-adoption`

---

<a id="item-4"></a>
## [xAI open-sources Grok Build CLI after directory upload privacy backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 8.0/10

xAI released its entire Grok Build CLI codebase under the Apache 2.0 license following severe community backlash over a feature that uploaded users' entire directories to xAI's Google Cloud buckets. The company also deleted all previously retained user data and disabled default data retention for all users starting July 12th. This incident underscores the significant privacy risks posed by AI coding assistants that handle sensitive developer files, and the open-source release represents a notable attempt to rebuild trust through transparency. The 844,530-line Rust codebase also provides rare insight into how a major AI company constructs coding agent infrastructure. The codebase contains 844,530 lines of Rust with only about 3% vendored code, and includes tool implementations borrowed from other coding agents such as Codex's apply_patch, grep_files, list_dir, and read_dir tools, as well as OpenCode's bash, edit, and glob tools. The repository was released as a single commit with no development history, and includes system prompts for both the main agent and a subagent, with the subagent prompt notably instructing it not to reveal its contents to the user.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok Build is xAI's command-line interface (CLI) tool for AI-assisted coding, comparable to tools like Anthropic's Claude Code or OpenAI's Codex CLI. These tools typically run in a user's local directory, read files, and execute commands to assist with software development tasks. The privacy backlash occurred because the tool's default behavior in early beta uploaded entire directory contents—including potentially sensitive files like SSH keys and password databases—to xAI's cloud infrastructure without clear user consent.

**Discussion**: The community reacted with alarm to the directory upload behavior, with one user reporting that running the command in their home directory uploaded SSH keys, password manager databases, documents, photos, and videos. Elon Musk responded by promising that all previously uploaded user data would be completely deleted, and xAI subsequently disabled the feature, changed default retention settings, and open-sourced the codebase to address privacy concerns.

**Tags**: `#xAI`, `#Grok`, `#open-source`, `#privacy`, `#CLI tools`

---

<a id="item-5"></a>
## [Claude web_fetch tool data exfiltration vulnerability disclosed](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Security researcher Ayush Paul discovered a bypass in Anthropic's Claude web_fetch tool that allowed attackers to exfiltrate private user memories by luring the agent through a honeypot site with nested generated links. Anthropic has since closed the hole by removing the ability for web_fetch to navigate to additional links returned within its own fetched content, though they did not pay a bug bounty, claiming they had identified it internally already. This demonstrates a real-world bypass of Anthropic's deterministic protections against prompt injection and data exfiltration, a critical concern for LLM agents that combine private data access with web tools. It highlights that even carefully designed guardrails can have subtle loopholes, reinforcing the broader industry risk known as the 'lethal trifecta' where untrusted input, private data, and external communication combine to create data breach risk. The attack used a honeypot site that instructed the AI to authenticate by specifying the user's name and navigate letter-by-letter through nested generated links, extracting the user's name, home city, and employer. The malicious payload was only shown to clients with Claude-User in their user-agent to evade detection.

rss · Simon Willison · Jul 15, 14:21

**Background**: The 'lethal trifecta' is a security concept coined by Simon Willison describing the danger when an LLM agent has access to private data, processes untrusted input, and can communicate externally, enabling prompt injection attacks to exfiltrate secrets. Anthropic's web_fetch tool was designed to mitigate this by only allowing navigation to exact URLs entered by the user or returned from the companion web_search tool, deterministically blocking attempts to concatenate private data into URLs. The vulnerability arose because web_fetch also permitted following URLs embedded in previously fetched pages, creating an indirect exfiltration path.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted ...</a></li>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool</a></li>

</ul>
</details>

**Tags**: `#LLM-security`, `#prompt-injection`, `#data-exfiltration`, `#Claude`, `#vulnerability`

---

<a id="item-6"></a>
## [LM Studio Introduces Bionic, an AI Agent Harness for Open Models](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 7.0/10

LM Studio has launched Bionic, a new AI agent application for open models that enables coding, research, and complex document workflows. It features flexible model execution, voice input, and automatic checkpointing for document changes. This release represents a significant step in the local AI tooling ecosystem by providing a dedicated agentic harness for open-source models, potentially shifting how developers and enterprises manage cost and data security. It signals a broader trend where LLMs become a primary computing interface for complex, multi-step tasks. Bionic supports flexible execution environments, allowing users to run models locally, connect via LM Link, or use frontier open-source models through LM Studio Secure Cloud. The application currently restricts agents to a single directory, lacks local web search and SSH capabilities, and offers automatic checkpointing specifically within "Work" projects.

hackernews · minimaxir · Jul 16, 20:18 · [Discussion](https://news.ycombinator.com/item?id=48939662)

**Background**: An agent harness is the software scaffolding surrounding a large language model that enables it to operate as an AI agent by managing tools, memory, and state persistence. Because LLMs are inherently stateless, the harness allows the model to perform multi-step tasks, use external tools, and maintain context over long-running sessions. Automatic checkpointing is a key feature of such harnesses, saving the agent's state and file outputs at intervals to allow workflows to pause, resume, or recover after a crash.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for ... - 9to5Mac</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>

</ul>
</details>

**Discussion**: The community response was largely positive, with users praising the familiar UI and immediate functionality with existing local models like Qwen3.6 35B, while also noting rough edges such as the lack of SSH, local web search, and directory restrictions. The founder actively engaged by offering credits for testing and soliciting feedback, and broader discussions emerged about whether LLMs will eventually become a standard interface for computing, particularly if major companies like Apple integrate similar local capabilities.

**Tags**: `#local-llm`, `#ai-agents`, `#lm-studio`, `#open-models`, `#developer-tools`

---

<a id="item-7"></a>
## [Puter Compiles Firefox to WebAssembly Using Claude Opus](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 7.0/10

Puter has successfully compiled the Firefox browser to WebAssembly, allowing a full browser instance to run inside another browser tab. The project leveraged Claude Opus and Fable tokens to accomplish the complex compilation, with an estimated token cost of $25,000. This project demonstrates the impressive capability of AI-assisted development in tackling complex software engineering tasks like porting a full browser engine to WebAssembly. It also showcases the potential for running isolated browser environments within existing browsers, which could have implications for web-based virtualization and sandboxing. The team chose Firefox/Gecko due to its strong single-process support, and the demo funnels all network traffic over a WebSocket connection using the Wisp protocol through Puter's servers. Puter claims the setup supports end-to-end encryption, and the project required significant server scaling to handle traffic from its Hacker News debut.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (WASM) is a binary instruction format that allows code written in languages like C, C++, and Rust to run at near-native speed in web browsers. Puter is an open-source, self-hostable internet computer platform that provides a backend for AI-generated apps. The Wisp protocol is a low-overhead protocol designed for proxying multiple TCP and UDP sockets over a single WebSocket connection, which is necessary because browser-based code cannot open arbitrary network connections directly.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HeyPuter/puter">GitHub - HeyPuter/puter: The Internet Computer! Free, Open ...</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>
<li><a href="https://developer.puter.com/">Puter Developer - The Backend for AI-Generated Apps</a></li>

</ul>
</details>

**Discussion**: The news item mentions that the project generated significant community interest on Hacker News, requiring the team to scale up their servers to handle the traffic. Simon Willison noted the project was "absurdly cool" and verified the end-to-end encryption claims by inspecting WebSocket messages.

**Tags**: `#WebAssembly`, `#Firefox`, `#AI-assisted development`, `#browser`, `#Puter`

---

<a id="item-8"></a>
## [ExTernD: Expanded-Rank Ternary Decomposition for LLM Post-Training Quantization](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 7.0/10

ExTernD is a novel post-training quantization (PTQ) method for large language models that decomposes weight matrices into two ternary matrices and an inner diagonal scaling matrix. This expanded-rank decomposition allows the inner rank to be arbitrarily large, enabling accuracy to approach bf16 levels with only slightly more VRAM overhead than current quantization methods. This method addresses a fundamental limitation of fixed-size ternary quantization, which the author argues is a dead end for achieving high accuracy. By allowing continuous control over the memory/compute trade-off, ExTernD offers a way to run LLMs efficiently on resource-constrained hardware while maintaining near-full-precision performance, which is highly relevant to the broader trend of optimizing LLM inference. The method factorizes weight matrices into ternary components (weights constrained to {-1, 0, +1}) with an expanded rank, correcting quantization errors using higher-rank components. The accuracy target is hit exactly rather than rounded to the next bit-width, and memory and compute scale continuously with a parameter μ, while factor sparsity scales with a threshold τ.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Post-Training Quantization (PTQ) is a technique used to compress large language models by reducing the precision of their weights after training, which lowers computational and memory requirements for inference. Ternary Weight Networks (TWNs) are a specific type of quantization where weights are constrained to three values: -1, 0, and +1, enabling multiplication-free inference and significant model compression. Traditional ternary quantization uses fixed-size matrices, which limits the achievable accuracy; ExTernD overcomes this by expanding the rank of the decomposition.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13511v1">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ ...</a></li>
<li><a href="https://www.emergentmind.com/topics/ternary-weight-networks-twns">Ternary Weight Networks Overview</a></li>
<li><a href="https://arxiv.org/abs/2502.13178">Benchmarking Post-Training Quantization in LLMs ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Quantization`, `#Post-Training Quantization`, `#Model Compression`, `#Inference Optimization`

---

<a id="item-9"></a>
## [AI Music Video Generation Compared: Claude Fable 5 vs. GPT-5.6 Sol](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6) ⭐️ 6.0/10

A blog post on tryai.dev compares AI-generated music videos created using Anthropic's Claude Fable 5 and OpenAI's GPT-5.6 Sol models for around $100. The comparison sparked a substantial discussion on Hacker News regarding the quality and implications of AI-generated creative content. This comparison highlights the growing capability of frontier AI models to generate multimedia content, raising important questions about the economic impact on working artists and the philosophical nature of art. As these tools become more accessible, they threaten the middle class of artists who previously sustained themselves through commercial aesthetic work. The blog post evaluates the output of two advanced models in the specific context of generating a music video, demonstrating impressive technological progress compared to previous years. However, the generated content currently suffers from being overly literal and lacking the narrative depth characteristic of human-directed music videos.

hackernews · hershyb_ · Jul 16, 20:03 · [Discussion](https://news.ycombinator.com/item?id=48939524)

**Background**: Claude Fable 5 is a publicly available Mythos-class model from Anthropic known for strong reasoning and coding capabilities. GPT-5.6 Sol is a frontier flagship model from OpenAI that emphasizes advanced reasoning and planning for extended, multi-step problem solving. Both models represent the latest generation of large language models that are increasingly being tested for complex creative tasks rather than just text generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://hix.ai/c/gpt-5-6-sol">GPT - 5 . 6 Sol | Try for Free | No Signup | HIX AI</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion expresses skepticism about the artistic value of the AI-generated videos, with commenters describing them as "grey goo" that lacks the narrative arc and depth of human-created art. Many users are concerned about the economic impact on middle-class artists who rely on commercial aesthetic work to fund their true creative ambitions, while others argue that true art is inherently tied to human experience and struggle.

**Tags**: `#AI-generated-content`, `#music-video`, `#AI-art`, `#creative-industries`, `#AI-economics`

---

<a id="item-10"></a>
## [Detecting LLM-Generated Text with Classical Machine Learning](https://blog.lyc8503.net/en/post/llm-classifier/) ⭐️ 6.0/10

A blog post by lyc8503 explores using classical machine learning techniques, rather than large neural networks, to classify text as LLM-generated or human-written. The approach frames LLM text detection as a binary classification problem and demonstrates that simpler, traditional ML methods can achieve meaningful results on this task. As LLM-generated content floods the internet, reliable detection tools are increasingly critical for maintaining trust in online information, academic integrity, and content quality. The use of classical ML methods is notable because they are lightweight, interpretable, and potentially deployable in resource-constrained environments like browser extensions, unlike heavy transformer-based detectors. The classifier described is relatively small, which raises the possibility of running it locally in a browser against displayed text. However, research indicates that detectors trained on one LLM's output often fail to generalize to other models, and as LLMs improve, distinguishing signals in text may diminish over time.

hackernews · uneven9434 · Jul 16, 16:41 · [Discussion](https://news.ycombinator.com/item?id=48936880)

**Background**: LLM-generated text detection is typically framed as a binary classification task and has been approached through watermarking, statistical methods, and neural-based detectors. Classical machine learning for text classification predates the deep learning era and includes techniques like TF-IDF features, logistic regression, and support vector machines. Recent surveys highlight a shift from traditional NLP techniques to modern deep learning architectures, but also note significant challenges such as cross-LLM detection failure, where a model trained to detect one LLM's output performs poorly on another's.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2310.14724">[2310.14724] A Survey on LLM-Generated Text Detection ... A Survey on LLM-Generated Text Detection: Necessity, Methods ... A Survey on LLM-Generated Text Detection: Necessity, Methods ... AI-generated text detection: A comprehensive review of ... The State of the Art in Detecting LLM-Generated Text in ... The Science of Detecting LLM-Generated Text</a></li>
<li><a href="https://aclanthology.org/2025.cl-1.8/">A Survey on LLM-Generated Text Detection: Necessity, Methods ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is heavily skeptical about the long-term feasibility of AI text detection, with one commenter arguing that text is simply not information-dense enough to reliably encode provenance signals, likening current detectors to tarot card reading. Others propose reframing the problem toward measuring writing effort rather than authorship, or building browser-based detection tools analogous to adblockers. Several commenters note that humans remain the best detectors and that models tend toward predictable, 'accent-like' patterns while human writing exhibits richer randomness.

**Tags**: `#LLM detection`, `#machine learning`, `#text classification`, `#AI-generated content`, `#classical ML`

---

<a id="item-11"></a>
## [GPT-5.6 Codex Bug Deletes $HOME Directory Without Sandboxing](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 6.0/10

Thibault Sottiaux disclosed that GPT-5.6's Codex has been found to unexpectedly delete files, most commonly the entire $HOME directory, when running in full access mode without sandboxing protections. The bug occurs when the model attempts to override the $HOME environment variable to set a temporary directory but mistakenly deletes $HOME instead. This bug highlights a critical safety risk with autonomous coding agents that operate with broad filesystem access, where a single model mistake can result in catastrophic data loss for users. It underscores why sandboxing and execution-level guardrails are essential infrastructure for any agentic AI system, rather than optional conveniences. The issue specifically arises when three conditions are met simultaneously: full access mode is enabled, Codex runs without sandboxing or auto-review, and the model attempts to manipulate the $HOME environment variable. The deletion is described as an 'honest mistake' by the model rather than adversarial behavior, pointing to reliability limitations in autonomous file operations.

rss · Simon Willison · Jul 16, 17:45

**Background**: Codex CLI is OpenAI's lightweight coding agent that runs locally on a user's computer and can execute commands with varying levels of filesystem access. Sandboxing is the practice of isolating agent processes in containers, microVMs, or similar isolation technologies so that a misbehaving or mistaken agent cannot cause damage to the host system. When agents run without sandboxing in 'full access' mode, they have unrestricted ability to execute commands, which means any error in judgment by the model can directly impact the user's filesystem.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/ codex : Lightweight coding agent that runs in your...</a></li>
<li><a href="https://beyondscale.tech/blog/ai-agent-sandboxing-enterprise-security-guide">AI Agent Sandboxing: Enterprise Security Guide 2026</a></li>
<li><a href="https://www.openlegion.ai/en/learn/ai-agent-sandboxing">AI Agent Sandboxing: Container Isolation, Escape CVEs, and ...</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#ai-safety`, `#generative-ai`, `#gpt-5`

---

<a id="item-12"></a>
## [Independent Researcher Shares DABSN Recurrent Architecture, Seeks Scaling Collaborators](https://www.reddit.com/r/MachineLearning/comments/1uycffg/seeking_collaborators_for_scaling_and_independent/) ⭐️ 6.0/10

An independent researcher has released a preprint and open-source code for DABSN (Dynamic Adaptive Bias State Network), a novel recurrent language model architecture, with implementations in PyTorch, C++, and Triton. The initial language model experiment uses 24M parameters trained on 1B tokens with a GPT-2 tokenizer, and the researcher is actively seeking collaborators for independent reproduction, stronger baselines, and access to larger GPU clusters for scaling. Recurrent architectures are receiving renewed attention as potential alternatives to Transformers for long-context modeling, since they offer constant memory during inference regardless of sequence length. An open, reproducible architecture with multiple implementations lowers the barrier for community validation and could contribute to the broader search for efficient sequence models beyond the Transformer paradigm. The architecture has been evaluated on reasoning, memory, and long-sequence benchmarks including MQAR, Copy, Key-Value retrieval, and A5/60, with a second paper planned focused on language modeling and scaling. The current scale is very small (24M parameters, 1B tokens) and the results have not yet been independently validated, so claims about the architecture's competitiveness remain preliminary.

reddit · r/MachineLearning · /u/BleedingXiko · Jul 16, 19:17

**Background**: MQAR (Multi-Query Associative Recall) is a synthetic benchmark developed by HazyResearch that tests a model's ability to perform multiple associative key-value lookups from in-context cues, and has been shown to correlate with downstream language modeling recall quality. Recurrent neural networks maintain an internal state across sequence positions, potentially offering linear-time inference and constant memory usage compared to Transformers' quadratic attention, but have historically struggled with long-range dependencies and training stability. Recent interest in alternatives like state-space models and linear attention has revived exploration of recurrent architectures for language modeling.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HazyResearch/zoology">GitHub - HazyResearch/zoology: Understand and test language ... Zoology: Measuring and Improving Recall in Efficient Language ... GitHub - howard-hou/Visual-MQAR: Understand and test multi ... MQAR: Multi-Query Associative Recall - emergentmind.com AI Benchmarks 2026: Compare 300+ LLM Benchmarks & Tests Zoology (Blogpost 1): Measuring and Improving Recall in ...</a></li>
<li><a href="https://arxiv.org/html/2312.04927v1">Zoology: Measuring and Improving Recall in Efficient Language ...</a></li>
<li><a href="https://github.com/zorino96/Adaptive-Bias-Networks">GitHub - zorino96/Adaptive-Bias-Networks: Beyond Static Bias ...</a></li>

</ul>
</details>

**Tags**: `#recurrent-neural-networks`, `#language-models`, `#architecture`, `#open-source`, `#long-context`

---

<a id="item-13"></a>
## [Call for Papers: Inaugural Real-Time Conversational Agents Workshop at NeurIPS 2026](https://www.reddit.com/r/MachineLearning/comments/1uy8e0v/cfp_rtca_neurips_2026_r/) ⭐️ 6.0/10

The Call for Papers and Demos has been announced for the inaugural Real-Time Conversational Agents (RTCA) Workshop at NeurIPS 2026, scheduled for December 11 or 12 in Sydney, Australia. The workshop invites original contributions on streaming multimodal interaction, real-time generation under latency budgets, and the evaluation of live conversational systems. As conversational AI transitions from text-based chat to real-time, multimodal interactions in the physical world, it faces fundamental challenges like latency, turn-taking, and cross-modal alignment that offline generation paradigms avoid. This workshop aims to establish shared benchmarks, vocabulary, and methodology for interactional naturalness by bringing together researchers across speech, vision, language, and HCI. Submissions can be full papers (up to 8 pages), short papers (up to 4 pages), or demo papers (up to 2 pages), and must be formatted for double-blind review using the NeurIPS 2026 style file. The submission deadline is August 29, 2026, and the workshop is non-archival, allowing authors to retain the right to publish their work elsewhere.

reddit · r/MachineLearning · /u/Few-Ferret9700 · Jul 16, 16:51

**Background**: Real-time conversational agents require full-duplex capabilities, meaning the AI can listen and speak simultaneously, allowing for natural interruptions and backchannels. Cross-modal alignment is a critical component in these systems, ensuring that speech, video, and language inputs are semantically synchronized despite latency and partial observations. Backchanneling, such as verbal and non-verbal cues from the listener, is essential for embodied conversational agents to indicate engagement and understanding during an interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://venturebeat.com/technology/openai-launches-gpt-live-a-full-duplex-voice-upgrade-that-lets-chatgpt-talk-more-like-a-person">OpenAI launches GPT-Live, a full-duplex voice upgrade that ...</a></li>
<li><a href="https://arxiv.org/abs/2411.17040">[2411.17040] Multimodal Alignment and Fusion: A Survey Cross-modal feature alignment and fusion with contrastive ... Cross-modal Alignment Algorithm and Dynamic Semantic ... AlignMamba: Enhancing Multimodal Mamba with Local and Global ... Multimodal Alignment and Fusion: A Survey - Springer Images</a></li>
<li><a href="https://www.retellai.com/blog/how-backchanneling-improves-user-experience-in-ai-powered-voice-agents">What is Backchanneling? And Why It Matters for Conversational AI</a></li>

</ul>
</details>

**Tags**: `#Conversational AI`, `#Multimodal`, `#NeurIPS 2026`, `#Real-Time Systems`, `#Call for Papers`

---

<a id="item-14"></a>
## [Researcher Seeks Devil's Advocates on Yann LeCun's JEPA Models](https://www.reddit.com/r/MachineLearning/comments/1uxcryc/looking_for_jepa_devil_advocates_r/) ⭐️ 6.0/10

A researcher working on world models for robot learning has publicly solicited critical counterarguments against Yann LeCun's Joint-Embedding Predictive Architecture (JEPA), expressing concern that LeCun's claims may be overly optimistic relative to competing approaches like LLMs and reinforcement learning. The post specifically asks the community to identify the biggest downsides of JEPA compared to other world model paradigms. JEPA is increasingly cited as a promising direction for building predictive world models in robotics and embodied AI, but rigorous critical evaluation is essential to separate genuine potential from hype. This discussion touches on a fundamental tension in the field: whether representation-prediction architectures like JEPA can truly outperform established paradigms such as large language models and reinforcement learning for real-world robotic control. The researcher has read the main recent JEPA papers from LeCun and other groups and finds the approach promising, but is troubled by LeCun's rhetorical style of dismissing LLMs and RL while positioning JEPA as the dominant path forward. The request is specifically for identification of red flags and comparative weaknesses that may not be immediately apparent from the primary literature.

reddit · r/MachineLearning · /u/Amazing-Coat5160 · Jul 15, 17:34

**Background**: JEPA (Joint-Embedding Predictive Architecture) is a self-supervised learning paradigm introduced by Yann LeCun and Meta AI in which a model encodes pairs of related inputs (such as consecutive video frames) into abstract representations and learns to predict one representation from the other, rather than predicting raw pixels. This design is intended to avoid the limitations of generative models that must reconstruct every detail of the input. World models more broadly are AI systems that learn the dynamics of physical environments and can predict future sensory observations given current inputs and actions, making them especially relevant for robotics and autonomous systems. LeCun has been a vocal critic of autoregressive LLMs and some forms of reinforcement learning, arguing that JEPA-style architectures are necessary for achieving human-level intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/">Deep Dive into Yann LeCun’s JEPA | Rohit Bandaru</a></li>
<li><a href="https://github.com/AI-in-Transportation-Lab/awesome-jepa">Awesome JEPA - Joint Embedding Predictive Architecture</a></li>

</ul>
</details>

**Tags**: `#JEPA`, `#World Models`, `#Yann LeCun`, `#Machine Learning`, `#Discussion`

---

<a id="item-15"></a>
## [PnP-CoSMo: Multi-Contrast MRI Reconstruction via Content/Style Modeling](https://www.reddit.com/r/MachineLearning/comments/1uy2h66/pnpcosmo_a_multicontrast_mri_reconstruction/) ⭐️ 6.0/10

Researchers introduced PnP-CoSMo, a plug-and-play framework for multi-contrast MRI reconstruction that separates contrast-invariant content from style. The framework learns from purely image-domain data and requires no raw k-space training data while remaining competitive with state-of-the-art unrolled networks. This approach addresses a serious data bottleneck in the ML-based MRI world by eliminating the need for raw k-space training data, which is often difficult to obtain. It also offers a built-in explanatory framework and is generalizable across different MR contrasts and forward operators by design. The framework operates in two stages: first, it learns the content/style model from purely image-domain data, and second, it freezes this model to apply it as a powerful prior in iterative reconstruction. The research was recently published in the journal Medical Image Analysis.

reddit · r/MachineLearning · /u/void_gear · Jul 16, 13:10

**Background**: In MRI, k-space is the temporary image space where data from digitized MR signals are stored, and reconstructing images from undersampled k-space data is a common inverse imaging problem. Plug-and-play (PnP) algorithms solve these problems by using a deep neural network denoiser as a proximal operator within an iterative reconstruction algorithm. Unrolled networks are currently state-of-the-art for accelerated MRI reconstruction but typically require large amounts of raw k-space data for training.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/K-space_in_magnetic_resonance_imaging">k-space in magnetic resonance imaging - Wikipedia</a></li>
<li><a href="https://researchportal.hw.ac.uk/en/publications/the-airi-plug-and-play-algorithm-for-image-reconstruction-in-radi/">The AIRI plug - and - play algorithm for image reconstruction in...</a></li>
<li><a href="https://arxiv.org/abs/2101.01570">[2101.01570] Density Compensated Unrolled Networks for...</a></li>

</ul>
</details>

**Tags**: `#MRI reconstruction`, `#medical imaging`, `#plug-and-play`, `#content-style modeling`, `#deep learning`

---