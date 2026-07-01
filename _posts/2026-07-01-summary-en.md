---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 36 items, 12 important content pieces were selected

---

1. [Anthropic Announces Claude Sonnet 5, Its Most Agentic Sonnet Model Yet](#item-1) ⭐️ 9.0/10
2. [Claude Code Found Steganographically Marking Customer Requests](#item-2) ⭐️ 8.0/10
3. [Anthropic Launches Claude Science, an AI Workbench for Scientists](#item-3) ⭐️ 8.0/10
4. [DeepReinforce Releases Ornith-1.0 Open-Weights LLMs for Agentic Coding](#item-4) ⭐️ 8.0/10
5. [Google's Agentic AI Peer-Reviewer Formally Documented for ICML/STOC](#item-5) ⭐️ 8.0/10
6. [U.S. Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](#item-6) ⭐️ 7.0/10
7. [Google Releases Gemini Image Flash-Lite, a Distilled Faster Image Model](#item-7) ⭐️ 7.0/10
8. [Meta's Brain2Qwerty Decodes Brain Waves into Text Non-Invasively](#item-8) ⭐️ 7.0/10
9. [REAP: Automatic Curation of Coding Agent Benchmarks from Production Usage](#item-9) ⭐️ 7.0/10
10. [shot-scraper 1.10 adds video recording for agent demos](#item-10) ⭐️ 6.0/10
11. [Interactive 2D Map Visualizes 11 Million Academic Papers by Semantic Similarity](#item-11) ⭐️ 6.0/10
12. [New Tool Enables Crossmatching 80TB+ of Astronomical Data on Low-Spec Hardware](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic Announces Claude Sonnet 5, Its Most Agentic Sonnet Model Yet](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 9.0/10

Anthropic has released Claude Sonnet 5, a new model designed to be the most agentic Sonnet to date, capable of planning, using tools like browsers and terminals, and running autonomously across long tasks. Sonnet 5 is now the default model for Free and Pro plans, with Max, Team, and Enterprise users able to select it, and its effort parameter defaults to high on the Claude API and Claude Code. This release pushes agentic capabilities—previously requiring larger, more expensive models like Opus—into the more affordable Sonnet tier, potentially democratizing autonomous AI agent workflows for a broader user base. However, community discussion reveals significant concerns about price-to-performance tradeoffs, with multiple users noting that Opus outperforms Sonnet 5 at equivalent cost when effort levels are raised above medium. Independent benchmarking by community members indicates Sonnet 5 performs at roughly GLM-5.2 level at 2x cost but 2x speed, with notable weak spots in trivia, combined tool-calling tasks, and puzzle solving. According to the system card, Sonnet 5 is less capable than Sonnet 4.6 on CyberGym vulnerability discovery, and when run with default mitigations, it scored a 0 on CyberGym.

hackernews · marinesebastian · Jun 30, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48736605)

**Background**: Anthropic's Claude model family includes multiple tiers—Sonnet (mid-tier) and Opus (premium)—with Sonnet historically offering a balance of cost and capability while Opus targets maximum performance. 'Agentic AI' refers to models that can autonomously plan, use external tools, and complete multi-step tasks with minimal human intervention, as opposed to generative AI which primarily creates content from prompts. The 'effort' parameter controls how many hidden reasoning tokens a model generates before answering, with higher effort generally producing better results at greater computational cost. This creates a cost-performance tradeoff that users must navigate when selecting models and effort levels.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/06/30/anthropic-claude-sonnet-5-vs-sonnet-4-6-vs-opus-4-8-agentic-coding-benchmarks-api-pricing-and-cost-performance-tradeoffs-compared/">Anthropic Claude Sonnet 5 vs Sonnet 4.6 vs Opus ... - MarkTechPost</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The dominant sentiment is skepticism about Sonnet 5's value proposition, with multiple commenters observing that Opus consistently outperforms Sonnet 5 at equivalent cost when effort levels exceed medium, making it unclear why users would choose higher effort Sonnet 5 over simply using Opus at a lower effort setting. One user noted that the model's optimization for fully agentic development may actually make it less suitable for agent-assisted development workflows, while another pointed out that its price-performance ratio appears worse than competing models like GLM-5.2, raising questions about its competitive positioning.

**Tags**: `#anthropic`, `#claude`, `#llm-release`, `#agents`, `#benchmarks`

---

<a id="item-2"></a>
## [Claude Code Found Steganographically Marking Customer Requests](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

A blog post revealed that Anthropic's Claude Code tool steganographically embeds hidden markers in requests sent from customer machines, a practice not openly disclosed to users. The discovery sparked significant community debate about transparency and trust in AI providers, generating nearly 2,000 upvotes and over 500 comments. This finding raises serious trust and transparency concerns because it demonstrates that AI providers may ship tooling that performs undisclosed actions on customer machines, potentially without informed consent. It also highlights the tension between providers' business interests—such as detecting unauthorized model distillation—and users' expectations of honest disclosure, which is critical for maintaining trust in the rapidly growing AI ecosystem. The steganographic markers are believed to be intended for identifying usage patterns, possibly to detect firms conducting model distillation by routing large volumes of requests through Claude Code. Some commenters noted the implementation was surprisingly easy to detect through reverse engineering, suggesting it was not crafted with the sophistication typical of 'underhanded code' techniques.

hackernews · kirushik · Jun 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48734373)

**Background**: Claude Code is Anthropic's agentic coding system that operates across entire projects to understand codebases, execute multi-file changes, and complete development tasks autonomously. Steganography is the practice of concealing information within another message or object in a way that the presence of the hidden information is not evident to an unsuspecting observer. In the context of AI tooling, steganographic markers could be used to trace or identify the source of requests without the user's knowledge. Model distillation is a technique where one AI model is trained using outputs from another, more capable model, which frontier AI labs often seek to detect and prevent.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Steganography">Steganography</a></li>

</ul>
</details>

**Discussion**: The community was divided, with some commenters arguing that the lack of transparent disclosure about steganographic marking is unacceptable regardless of the provider's business justification, while others felt the blog post's conclusion was overblown given the clear intent of identifying model distillation. Several commenters expressed broader distrust of major AI labs, advocating for local AI as a privacy-preserving alternative. One commenter noted the implementation was surprisingly sloppy and could have been far harder to detect using established 'underhanded code' techniques.

**Tags**: `#Anthropic`, `#Claude Code`, `#Steganography`, `#AI Ethics`, `#Trust`

---

<a id="item-3"></a>
## [Anthropic Launches Claude Science, an AI Workbench for Scientists](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic has launched Claude Science, a product that integrates large language model capabilities with scientific research tools, databases, and high-performance computing (HPC) clusters for data science applications. The product runs a local server with a web-based UI that connects to institutional clusters and computational tools, generating reproducible scientific artifacts including figures, manuscripts, and the code that created them. This launch targets scientific research workflows directly, potentially transforming how scientists conduct data analysis, write papers, and interact with computational infrastructure much like Claude Code transformed software development. Anthropic's CEO reportedly expects Claude Code-level impact in the scientific community, with early users reporting real-world successes in genomics analysis and bioinformatics problem-solving. Claude Science distinguishes itself from Claude Code and Cowork by running a local server with a browser-based UI rather than being tightly coupled to the host machine, a design choice likely motivated by the strict security lockdowns common in pharmaceutical and research environments. The product integrates with institutional HPC clusters and various databases, enabling researchers to execute computational workflows directly through the interface.

hackernews · lebovic · Jun 30, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48735770)

**Background**: High-performance computing (HPC) clusters are widely used in scientific research for computationally intensive tasks such as genomics, molecular dynamics, climate modeling, and materials science. Anthropic's Claude Code product previously demonstrated how an AI-powered coding tool could fundamentally change developer workflows, and the company is now applying a similar approach to scientific research. The product also launched alongside NVIDIA's BioNeMo Agent Toolkit, indicating a broader industry push toward AI-assisted life sciences research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science , an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://www.statnews.com/2026/06/30/anthropic-release-claude-science-ceo-dario-amodei/">Anthropic releases Claude Science , sees Claude Code level impact</a></li>

</ul>
</details>

**Discussion**: Community sentiment is highly positive, with a biophysicist reporting significant workflow acceleration but noting the challenge of keeping mental models aligned with AI-generated code. A parent shared a compelling use case where Claude Science solved a bioinformatics question about their son's rare genetic condition in about a minute, a question that human bioinformaticians had been unable to satisfactorily answer. One commenter who helped build the Biomni HPC integration emphasized that the product is capable of far more than making plots and writing papers, while another highlighted the local-server architecture as a strategic choice for locked-down pharma environments.

**Tags**: `#anthropic`, `#scientific-research`, `#data-science`, `#llm-applications`, `#bioinformatics`

---

<a id="item-4"></a>
## [DeepReinforce Releases Ornith-1.0 Open-Weights LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce has released Ornith-1.0, a new MIT-licensed open-weights LLM family designed for agentic coding, available in variants ranging from 9B to 397B parameters. The models are built on top of pretrained Gemma 4 and Qwen 3.5 and claim state-of-the-art coding performance among open-source models of comparable size. This release introduces a novel "self-scaffolding" training framework where the model jointly learns to solve tasks and construct the scaffolds that guide those solutions, potentially advancing how LLMs orchestrate multi-step coding workflows. The open MIT licensing and strong local performance demonstrated by early testers could make it a highly attractive option for developers running agentic coding harnesses locally. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, with the 35B MoE running at 103 tokens/second on a standard local setup using a 20GB Q4_K_M GGUF file. The underlying base models, Gemma 4 and Qwen 3.5, are both Apache 2.0 licensed, ensuring compatibility with the MIT license applied to Ornith-1.0.

rss · Simon Willison · Jun 29, 16:17

**Background**: "Self-scaffolding" refers to a training approach where the model continuously improves not only its code generation but also the orchestration strategy used to solve software engineering problems, effectively building its own scaffolding before tackling a task. Mixture of Experts (MoE) is an architecture that increases model parameters while keeping inference compute constant by routing inputs to specialized sub-networks. GGUF is a standard file format for distributing quantized large language models for local inference, supported by tools like LM Studio.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc">Ornith 1.0 : Self Learning LLM for Coding | by Mehul Gupta | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#coding`, `#open-weights`, `#model-release`, `#agentic`

---

<a id="item-5"></a>
## [Google's Agentic AI Peer-Reviewer Formally Documented for ICML/STOC](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 8.0/10

Google has released a formal research paper documenting an agentic AI peer-reviewer that was deployed to review approximately 10,000 papers at the ICML and STOC computer science conferences. The system achieved a 30-minute turnaround time per paper and caught 34% more mathematical errors compared to standard zero-shot prompting. This deployment establishes a strong precedent for AI-automated scientific peer review at a massive conference scale, potentially transforming how academic papers are vetted for quality and accuracy. The demonstrated improvement in catching mathematical errors highlights the system's technical depth and its potential to augment the reliability of published research. The agentic system's performance was formally documented in a paper and showed a 34% improvement in detecting mathematical errors over zero-shot prompting methods. It successfully handled around 10,000 papers with a rapid 30-minute turnaround time, showcasing its ability to operate effectively at scale.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Agentic AI refers to artificial intelligence systems that act autonomously, executing workflows, self-correcting, and utilizing tools to complete tasks rather than merely suggesting responses. Zero-shot prompting is a technique used to elicit reasoning from large language models by asking a question or giving an instruction without providing any prior examples of the desired output.

<details><summary>References</summary>
<ul>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>
<li><a href="https://medium.com/@albert_88839/zero-in-on-the-right-responses-with-zero-shot-and-few-shot-prompting-f50fb154af4d">Zero in on the Right Responses with Zero - Shot and... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#peer review`, `#automated research`, `#scientific review`, `#Google AI`

---

<a id="item-6"></a>
## [U.S. Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 7.0/10

The U.S. Department of Commerce has withdrawn export controls on Anthropic's Claude Fable 5 and Mythos 5 models, as confirmed by a letter from Commerce Secretary Howard Lutnick to Anthropic's Chief Compute Officer Tom Brown dated June 30, 2026. Anthropic is redeploying Fable 5 with new classifiers to block cybersecurity tasks, with routine coding and debugging falling back to Opus 4.8. This represents a significant regulatory reversal for frontier AI models that were previously blocked on national security grounds, signaling how rapidly U.S. AI export policy can shift. The decision impacts businesses relying on American frontier models, as the back-and-forth nature of these controls raises questions about the reliability of building critical functions on top of U.S. AI infrastructure. Fable 5 is the consumer-facing version of Anthropic's Mythos-class model, capable of deep reasoning and autonomous complex tasks, while Mythos 5 is the more powerful variant that was previously available publicly for only about 96 hours before government intervention. The redeployed Fable 5 includes enhanced safeguards and classifiers specifically targeting cybersecurity use cases, meaning some coding capabilities are restricted compared to the original release.

hackernews · Pragmata · Jun 30, 23:55 · [Discussion](https://news.ycombinator.com/item?id=48740771)

**Background**: Anthropic launched Mythos 5 as its most powerful publicly available model, but the U.S. government imposed export controls shortly after launch citing national security concerns, making the model inaccessible for several weeks. The U.S. has been progressively tightening export controls on advanced AI technology since October 2022, primarily targeting China but increasingly extending to frontier AI models themselves. The Bureau of Industry and Security (BIS) formalized a flexible license review policy for AI-related transactions in January 2026, creating the framework under which these controls were applied and subsequently lifted.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jul/01/anthropic-fable-mythos-ai-models-us-export-controls-lifted">Anthropic: US has lifted export controls on Fable and Mythos AI models after security risk fears | AI (artificial intelligence) | The Guardian</a></li>
<li><a href="https://www.anthropic.com/news/redeploying-fable-5">Redeploying Claude Fable 5 \ Anthropic</a></li>
<li><a href="https://www.bbc.com/news/articles/cdr42623e1do">Fable and Mythos : Anthropic says US lifts export ban on its advanced...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely critical, with users expressing concern that unpredictable regulatory whiplash makes it impossible to build business-critical functions on American frontier models. Multiple commenters called for actual legislation rather than ad hoc executive decisions, arguing that the lack of a clear, predictable process deters investment in U.S. AI companies. There is also notable discussion about Fable 5's restricted coding capabilities, with some users questioning the practical utility of a model that cannot be used for software development tasks.

**Tags**: `#AI-regulation`, `#export-controls`, `#Anthropic`, `#frontier-models`, `#policy`

---

<a id="item-7"></a>
## [Google Releases Gemini Image Flash-Lite, a Distilled Faster Image Model](https://deepmind.google/models/gemini-image/flash-lite/) ⭐️ 7.0/10

Google has released Gemini Image Flash-Lite, a distilled and faster version of its Gemini image generation model, colloquially known as "Nano Banana 2 Lite." The new model generates images in under 5 seconds compared to approximately 30 seconds for the base model while retaining strong text rendering capabilities. This release enables real-time and interactive AI image generation use cases where low latency is critical, such as illustrated story apps and news article illustration. It reflects the broader industry trend of distilling large generative models into lighter variants that trade some nuance for dramatic speed improvements. Early access users report that Flash-Lite behaves like a distilled version of the base Nano Banana 2 model, maintaining good text rendering but falling short on highly nuanced prompts. A notable limitation is the inability to programmatically force aspect ratios, and users have reported friction accessing the model via Google AI Studio due to Google One account requirements that exclude Workspace users.

hackernews · minimaxir · Jun 30, 16:48 · [Discussion](https://news.ycombinator.com/item?id=48735444)

**Background**: Model distillation is a machine learning technique where knowledge from a large, capable model is transferred to a smaller, faster one, sacrificing some performance for efficiency. Google's Gemini image models, informally dubbed "Nano Banana" by the community, are part of the company's broader Gemini multimodal AI family. The "Flash-Lite" branding is used across Google's model lineup to denote variants optimized for low latency and cost-effectiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite">Gemini 2.5 Flash-Lite | Gemini Enterprise Agent Platform | Google Cloud Documentation</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: users praise the model's speed and text rendering, with one developer noting it generates images in under 5 seconds and maintains character likeness better than competitors. However, significant frustration exists around Google's access friction, particularly the requirement for a Google One account that excludes Workspace users. One commenter also expressed concern about AI-generated images being used deceptively in real estate listings.

**Tags**: `#image-generation`, `#google-gemini`, `#ai-models`, `#generative-ai`

---

<a id="item-8"></a>
## [Meta's Brain2Qwerty Decodes Brain Waves into Text Non-Invasively](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/?_fb_noscript=1) ⭐️ 7.0/10

Meta's Brain2Qwerty paper introduces a non-invasive brain-computer interface that decodes MEG and EEG signals into typed text. The research provides a statistically significant improvement over existing techniques and includes open-source code and datasets. This development represents a notable advancement in non-invasive brain-computer interfaces, potentially paving the way for new communication methods without surgical implants. It also demonstrates how AI and deep learning models can be applied to neural decoding, though it raises valid privacy concerns about neural tracking. The Brain2Qwerty model combines three hierarchical modules to generate sentences directly from continuous recordings of brain activity. While it offers an incremental improvement, the underlying model is currently not multimodal, and some suggest that joint embeddings of EEG and MEG data could further enhance performance.

hackernews · alok-g · Jun 30, 21:29 · [Discussion](https://news.ycombinator.com/item?id=48739466)

**Background**: Brain-computer interfaces (BCIs) aim to translate brain activity into commands for external devices, often requiring invasive surgical implants for high fidelity. Non-invasive methods like magnetoencephalography (MEG) and electroencephalography (EEG) measure magnetic fields and electrical activity in the brain, respectively, but typically produce noisier signals. Neural decoding is the process of reconstructing stimuli or intended actions from these recorded brain signals using computational models.

<details><summary>References</summary>
<ul>
<li><a href="https://facebookresearch.github.io/brain2qwerty/">Brain 2 Qwerty — Decoding typed sentences from non-invasive brain...</a></li>
<li><a href="https://dallasexpress.com/health/mind-reading-ai-by-meta-types-your-thoughts/">Typing Without Touch: Brain 2 Qwerty Decodes Your Thoughts — No...</a></li>
<li><a href="https://www.oxcin.ox.ac.uk/research/research-groups/basic-neuroscience-groups/physiological-neuroimaging-group/techniques-we-use/magnetoencephalography-meg">Magnetoencephalography ( MEG ) — Oxford University Centre for...</a></li>

</ul>
</details>

**Discussion**: The community notes that while the technology is not entirely new, the open release of code and datasets is highly commendable. Commenters also raised significant privacy concerns about the potential for neural tracking, while others discussed technical improvements, such as using joint multimodal embeddings of EEG and MEG data to boost performance.

**Tags**: `#BCI`, `#brain-computer-interface`, `#neural-decoding`, `#MEG`, `#Meta-Research`

---

<a id="item-9"></a>
## [REAP: Automatic Curation of Coding Agent Benchmarks from Production Usage](https://www.reddit.com/r/MachineLearning/comments/1uk713d/reap_automatic_curation_of_coding_agent/) ⭐️ 7.0/10

REAP (Relevance and Execution-Audited Pipeline) introduces an automated curation pipeline that constructs coding agent benchmarks from real developer-agent sessions without requiring manual labeling. This approach derives evaluation data directly from interactive production usage rather than relying on manually crafted benchmark tasks. This addresses a critical gap in AI agent evaluation, where most public benchmarks are designed for static model outputs rather than interactive agent performance in real-world scenarios. By automating benchmark creation from production sessions, REAP could make coding agent evaluation more scalable, relevant, and reflective of actual developer needs. The pipeline audits both relevance and execution of developer-agent interactions to filter and curate benchmark-quality tasks automatically. The method eliminates manual labeling effort, which is typically a bottleneck in benchmark construction, though specific technical details about the filtering criteria and quality assurance mechanisms are available in the full paper.

reddit · r/MachineLearning · /u/julian88888888 · Jul 1, 00:50

**Background**: Coding agents are AI systems that assist developers by performing coding tasks through interactive sessions, and their evaluation has traditionally relied on benchmarks designed for measuring static model output quality rather than dynamic agent behavior. Most existing benchmarks fail to capture the complexities of real-world agent interactions, such as planning, tool use, and multi-step decision-making. REAP bridges this gap by sourcing benchmark tasks from actual production developer-agent sessions, aligning with the broader industry trend toward application-specific and real-world reliability evaluations for LLM agents.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.01527">[2604.01527] REAP : Automatic Curation of Coding Agent ...</a></li>
<li><a href="https://github.com/gudo7208/awesome-coding-agent-eval">GitHub - gudo7208/awesome- coding - agent -eval: A curated collection...</a></li>

</ul>
</details>

**Tags**: `#coding agents`, `#benchmarks`, `#evaluation`, `#LLMs`, `#agent evaluation`

---

<a id="item-10"></a>
## [shot-scraper 1.10 adds video recording for agent demos](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 6.0/10

Simon Willison released shot-scraper 1.10, introducing a new `shot-scraper video` command that accepts a `storyboard.yml` file defining a routine to run against a web application and uses Playwright to record a video of that routine. The feature is specifically designed to help AI coding agents produce visual demonstrations of their work. This addresses a growing need in the AI agent ecosystem for verification and evaluation — having agents produce video demos of their work provides a tangible way to confirm that code actually functions as intended. It represents a novel approach to agent output validation, moving beyond text-based summaries to visual proof of functionality. The storyboard YAML format supports defining a server startup command, target URL, viewport dimensions, cursor visibility, wait conditions, custom JavaScript injection (such as mocking the clipboard API), and a sequence of scenes with actions like pauses and clicks. The tool can output both WebM and MP4 formats, and supports authentication via cookie-based JSON files.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line utility built on Playwright, Microsoft's browser automation library, originally designed for taking automated screenshots of web pages for documentation purposes. Playwright enables programmatic control of Chromium, Firefox, and WebKit browsers, allowing developers to simulate user interactions like clicks, typing, and navigation. Simon Willison has previously advocated for the importance of having coding agents produce demos of their work, and this tool represents his latest effort to enable that capability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/ shot - scraper : A command-line utility for taking...</a></li>
<li><a href="https://simonwillison.net/2022/Mar/10/shot-scraper/">shot - scraper : automated screenshots for documentation, built on...</a></li>

</ul>
</details>

**Tags**: `#ai-agents`, `#tooling`, `#playwright`, `#agent-evaluation`, `#automation`

---

<a id="item-11"></a>
## [Interactive 2D Map Visualizes 11 Million Academic Papers by Semantic Similarity](https://www.reddit.com/r/MachineLearning/comments/1ujn3u5/a_map_of_the_latest_11_million_papers_split_by/) ⭐️ 6.0/10

A free web tool called The Global Research Space was released, visualizing 11 million academic papers from OpenAlex and arXiv in a 2D semantic map. The tool uses SPECTER2 embeddings and UMAP dimensionality reduction to enable keyword search, semantic queries, time-slice navigation, and analytics. This tool provides researchers with a macroscopic view of scientific literature trends, making it easier to navigate the massive volume of papers published daily. It offers an alternative approach to literature exploration by combining semantic search with interactive visualization and institutional analytics. The creator encoded paper titles and abstracts using the SPECTER2 model, then projected the embeddings into 2D space using UMAP, applying Voronoi diagrams to label high-density regions. The tool also features a daily auto-ingestion script to keep the map up-to-date with new publications.

reddit · r/MachineLearning · /u/icannotchangethename · Jun 30, 11:55

**Background**: SPECTER2 is a scientific document embedding model developed by the Allen Institute for AI that outperforms previous models by using a two-step training process with format-specific adapters. UMAP (Uniform Manifold Approximation and Projection) is a dimensionality reduction algorithm commonly used to visualize high-dimensional data in lower-dimensional space. OpenAlex is an open-access bibliographic catalog of scientific papers, authors, and institutions that succeeded the Microsoft Academic Graph.

<details><summary>References</summary>
<ul>
<li><a href="https://itinai.com/benchmarking-large-language-models-in-biomedical-classification-and-named-entity-recognition-evaluating-the-impact-of-prompting-techniques-and-domain-knowledge/">Benchmarking Large Language Models in Biomedical Classification...</a></li>
<li><a href="https://umap-learn.readthedocs.io/">UMAP : Uniform Manifold Approximation and Projection for Dimension...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAlex">OpenAlex - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#literature-mining`, `#visualization`, `#embeddings`, `#research-tools`, `#UMAP`

---

<a id="item-12"></a>
## [New Tool Enables Crossmatching 80TB+ of Astronomical Data on Low-Spec Hardware](https://www.reddit.com/r/MachineLearning/comments/1uk7ec6/80tb_of_astronomy_for_the_hddpoor_crossmatch_the/) ⭐️ 6.0/10

A new tool released on Hugging Face allows researchers to crossmatch over 80TB of data from more than 30 astronomical surveys using as little as 4GB of RAM. This eliminates the need to download massive datasets to local disk, making large-scale astronomical analysis accessible from a standard laptop. This development significantly lowers the hardware barrier for researchers and machine learning practitioners working with large scientific datasets, democratizing access to comprehensive astronomical data. It enables broader participation in multi-survey analysis without requiring expensive storage infrastructure. The tool's killer feature is crossmatching, which links observations of the same object across different surveys, a process that previously required downloading hefty chunks of data. Tutorials are available on Hugging Face and Asciinema to guide users through the crossmatching process.

reddit · r/MachineLearning · /u/Smith4242 · Jul 1, 01:07

**Background**: Crossmatching in astronomy involves linking observations of the same celestial object across different surveys to create a comprehensive view of that object. The Gaia mission, referenced for its massive scale, is a European Space Agency observatory that created the largest 3D map of the Milky Way by surveying about 1% of its 100 billion stars.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/hugging-science/multimodal-universe-hats">80TB+ of astronomy for the HDD-poor: crossmatch the Multimodal...</a></li>
<li><a href="https://science.nasa.gov/mission/gaia/">Gaia - NASA Science</a></li>

</ul>
</details>

**Tags**: `#astronomy`, `#data-accessibility`, `#large-scale-data`, `#scientific-data`, `#tooling`

---