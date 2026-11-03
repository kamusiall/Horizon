---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 33 items, 10 important content pieces were selected

---

1. [Astra Demonstrates Direct Neural Network Weight Editing via Weight-Space Programming](#item-1) ⭐️ 8.0/10
2. [Subvocal Smart Glasses Decode Silent Speech Using RF Signals](#item-2) ⭐️ 8.0/10
3. [Video Reveals How Background Airplane Noise Leaks Exact Locations](#item-3) ⭐️ 8.0/10
4. [SciMe Atlas Maps 10 Years of ML Papers into Per-Topic Benchmark Pages](#item-4) ⭐️ 8.0/10
5. [Nvidia Releases Open-Source Auto-Ontology Tool for Automated Knowledge Engineering](#item-5) ⭐️ 7.0/10
6. [Revolut Transitions to Self-Hosted GLM Models for Cost and Privacy](#item-6) ⭐️ 7.0/10
7. [Kyle Kingsbury Warns LLMs Erode Trust in Software Maturity Signals](#item-7) ⭐️ 7.0/10
8. [Small-scale validation of "good views beat next-token prediction" using human captions](#item-8) ⭐️ 7.0/10
9. [LightMIS: Ultra-lightweight medical image segmentation for edge devices](#item-9) ⭐️ 7.0/10
10. [U.S. Census Bureau AI Adoption Data Disrupted by Executive Order 14434](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Astra Demonstrates Direct Neural Network Weight Editing via Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 8.0/10

MIT CSAIL researchers demonstrated that OpenAI's GPT-6 Astra model can read, interpret, and directly edit the weights of another neural network without using gradient descent or a training loop. In one experiment, Astra modified only 0.016% of Qwen3.5-0.8B's 800 million parameters, boosting its MATH-500 accuracy from 7.9% to 48.1%. This introduces a fundamentally different paradigm for model improvement—using an LLM as a programmer that reasons about and directly manipulates another model's weight space, rather than relying on traditional training or fine-tuning. If scalable, it could open new paths for model editing, interpretability, and potentially recursive self-improvement. Astra touched 131,072 weight entries (about 0.016% of Qwen3.5-0.8B's parameters), using Python to calculate replacement values and submitting edited tensors for testing. The method also successfully identified what small networks were trained on and repaired a driving policy, suggesting the capability extends beyond language models.

hackernews · dbreunig · Nov 2, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50341174)

**Background**: Weight-space programming is an approach where a general-purpose LLM reads, interprets, and directly writes the weights of another neural network without gradient descent or training loops. Traditional model editing techniques typically involve lightweight expert networks or targeted fine-tuning, but this approach treats weight tensors as text artifacts that an LLM can reason about and modify. The term was introduced by MIT CSAIL researchers using OpenAI's GPT-6 Astra model, which appears to have a native ability to parse and manipulate raw weight data.

<details><summary>References</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>
<li><a href="https://kingy.ai/blog/weight-space-programming-ai-agent-model-weights/">Weight-Space Programming: GPT-6 Astra Edits Qwen - kingy.ai</a></li>
<li><a href="https://www.digit.in/features/general/mit-researchers-show-llms-can-edit-neural-network-weights-without-training-heres-what-it-means.html">MIT Researchers show LLMs can edit neural network weights ...</a></li>

</ul>
</details>

**Discussion**: The community is deeply divided: enthusiasts like vessenes call the results 'insane' and see emergent understanding of complex systems, while domain experts like yurimo caution that the blog overstates findings and that weight editing capabilities have existed for some time. Others speculate Astra may have been trained on neural weight data as an attempt at recursive self-improvement, and some note this fits a pattern of LLMs rapidly grasping complex systems that would take humans months to understand.

**Tags**: `#weight-space-programming`, `#LLM-agents`, `#model-editing`, `#Qwen`, `#interpretability`

---

<a id="item-2"></a>
## [Subvocal Smart Glasses Decode Silent Speech Using RF Signals](https://news.ycombinator.com/item?id=50340088) ⭐️ 8.0/10

The Subvocal Company, a YC F26 startup, has developed smart glasses that use radio frequency (RF) signals to decode silent subvocal speech into text. The glasses emit radio waves that pass through the face and are modulated by the tongue, lips, and soft palate during silent mouthing, which foundation models then translate into text. This technology enables discreet, hands-free human-computer interaction at the speed of speech, which is highly beneficial for accessibility and environments where speaking aloud is disruptive. It represents a significant advancement in wearable hardware by moving away from cumbersome EMG electrodes to a more practical RF-based approach integrated into everyday eyewear. The founders initially attempted to use EMG electrodes but switched to RF due to issues with signal stability, interference, and user comfort. The current prototype embeds antennas within the glasses frames, and the company is working on cross-user generalization by scaling data collection, as everyone's facial anatomy produces vastly different RF signal patterns.

hackernews · aarushyadav · Nov 2, 17:16

**Background**: Subvocal recognition (SVR) is the process of detecting internal or silent speech and converting it into digital text or commands without the need for audible vocalization. Previous approaches have often relied on electromyography (EMG) to read nerve or muscle signals, but these methods face challenges with sensor placement and environmental interference. The Subvocal Company's approach uses RF sensing, which sends radio waves through the face to detect articulator movements, combined with machine learning models to decode the resulting signal perturbations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subvocal_recognition">Subvocal recognition - Wikipedia</a></li>
<li><a href="https://www.electronicdesign.com/technologies/industrial/boards/article/21759898/subvocal-speech-capture-keeps-things-quiet-while-improving-recognition-accuracy">Subvocal Speech Capture Keeps Things Quiet... | Electronic Design</a></li>

</ul>
</details>

**Discussion**: The community is highly enthusiastic about the technology, praising its sci-fi-like nature and potential for accessibility, though some users request better hardware accommodation for larger noses and prescription lenses. Privacy concerns are a significant topic, with one commenter citing Google's previous abandonment of similar tech due to the potential for invasive data correlation, while others hope the company will eventually license the technology to broader smart glasses platforms.

**Tags**: `#subvocal-speech`, `#wearable-hardware`, `#human-computer-interaction`, `#signal-processing`, `#accessibility`

---

<a id="item-3"></a>
## [Video Reveals How Background Airplane Noise Leaks Exact Locations](https://simonwillison.net/2026/Nov/3/a-sound-that-leaks-your-exact-location/) ⭐️ 8.0/10

A video by content creator Colsto demonstrates a novel OSINT technique where imperceptible background airplane noise in a video's audio track is analyzed for Doppler curves. This audio data is then cross-referenced with historical ADS-B flight tracking data to pinpoint the exact location where the video was recorded. This technique highlights a significant privacy vulnerability, as almost any video recorded outdoors could potentially be geolocated without any visual clues. It showcases a highly creative application of signal processing and open-source intelligence that could affect journalists, activists, and everyday users who rely on the anonymity of their media. The method relies on analyzing the Doppler effect in the faint sounds of passing aircraft to determine their speed, distance, and flight paths. By identifying the specific gaps and patterns between different flights, the audio can be matched against publicly available ADS-B flight data to find a precise geographical match.

rss · Simon Willison · Nov 3, 05:32

**Background**: The Doppler effect is the change in frequency of a wave in relation to an observer who is moving relative to the wave source, commonly experienced as a change in pitch as a siren or airplane passes by. ADS-B (Automatic Dependent Surveillance-Broadcast) is a surveillance technology where aircraft determine their position via satellite navigation and periodically broadcast it, enabling them to be tracked by services like FlightAware and ADS-B Exchange.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pulse-Doppler_signal_processing">Pulse-Doppler signal processing - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/FlightAware">FlightAware - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#osint`, `#privacy`, `#signal-processing`, `#security`

---

<a id="item-4"></a>
## [SciMe Atlas Maps 10 Years of ML Papers into Per-Topic Benchmark Pages](https://www.reddit.com/r/MachineLearning/comments/1xmk8rx/we_turned_10_years_of_ml_papers_into_one_page_per/) ⭐️ 8.0/10

A new free research tool called SciMe Atlas has launched, aggregating approximately 109,000 accepted papers from ICML, NeurIPS, ICLR, CVPR, and AAAI since 2016 into roughly 1,260 topics, with results tables and ablations extracted from the full text of 79,000 papers. Each topic page displays best reported benchmark numbers over time, ablations from recent papers (including negative results), baseline comparisons, recent arXiv preprints, and a BibTeX file of key papers. This tool dramatically reduces the time researchers spend on literature review by structuring a decade of ML research into digestible, per-topic pages with extracted benchmark records and ablation tables. It provides a unique bird's-eye view of how fields evolve — for example, revealing that compact Gaussian splatting grew from 29 papers in 2023-24 to 240 in 2025-26, while some benchmark metrics like Deep Blending PSNR have barely improved. The extraction is not perfect and numbers from different papers are not always directly comparable, so the tool should be treated as a starting point rather than an authoritative leaderboard. Benchmark numbers and ablations from 2026 papers are not yet included, meaning current records mostly reflect papers up to 2025, and every extracted number links back to its source paper for verification.

reddit · r/MachineLearning · /u/latenticlabs · Nov 3, 05:09

**Background**: Gaussian splatting is a volume rendering technique for novel view synthesis that represents 3D scenes using collections of anisotropic 3D Gaussian primitives, enabling high-quality, real-time radiance field rendering. The technique was revitalized and exploded in popularity in 2023 when a research group from Inria proposed the seminal 3D Gaussian splatting method. The Deep Blending dataset, introduced at SIGGRAPH Asia 2018, consists of real-world indoor scenes with complex geometries and lighting conditions, and is commonly used as a standard benchmark to evaluate novel view synthesis methods. Metrics such as PSNR (Peak Signal-to-Noise Ratio) are used to measure reconstruction quality on these benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting</a></li>
<li><a href="https://github.com/Phog/DeepBlending">Deep Blending for Free-Viewpoint Image-Based Rendering DeepBlending Dataset Results | noodle-lab/GaussianSpa | DeepWiki NerfBaselines: Dataset Mip-NeRF 360 Deep Blending Dataset | YihangChen-ee/HAC-plus | DeepWiki Novel View Synthesis on DeepBlending (PSNR, SSIM, LPIPS)</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Literature Review`, `#Research Tools`, `#Benchmarks`, `#Data Visualization`

---

<a id="item-5"></a>
## [Nvidia Releases Open-Source Auto-Ontology Tool for Automated Knowledge Engineering](https://github.com/NVIDIA/auto-ontology) ⭐️ 7.0/10

Nvidia has released an open-source auto-ontology tool on GitHub designed to automate the construction of ontologies. The tool leverages large language models (LLMs) to generate structured knowledge representations from data. This release is significant for enterprise AI and knowledge representation, as manual ontology construction is notoriously labor-intensive and costly. By automating this process, Nvidia's tool could drastically reduce the resources required for enterprise knowledge engineering and improve the reliability of AI agents. The tool addresses the challenge of building structured knowledge bases by using LLMs, though community members note that LLMs can struggle with reliability and may prioritize learned weights over provided data. The project is available on GitHub, but some users found the documentation lacking a clear, concise summary of its goals.

hackernews · campervans · Nov 3, 07:04 · [Discussion](https://news.ycombinator.com/item?id=50348962)

**Background**: Ontology construction is a foundational knowledge engineering task that involves creating a shared conceptual structure to define concepts and their relationships. Traditionally, this process is manual, time-consuming, and difficult to sustain, prompting research into automated approaches using neural and Transformer-based models. Neuro-symbolic AI seeks to combine the pattern recognition of neural networks with the structured logic of symbolic AI to overcome individual weaknesses of each approach.

<details><summary>References</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1007/s10462-019-09782-9">Automatic ontology construction from text: a review from ...</a></li>
<li><a href="https://tdwi.org/articles/2024/04/08/adv-all-can-neuro-symbolic-ai-solve-ai-weaknesses.aspx">Q&A: Can Neuro- Symbolic AI Solve AI ’s Weaknesses? | TDWI</a></li>
<li><a href="https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/kpmg-the-knowledge-engineering-imperative.pdf">The knowledge engineering imperative</a></li>

</ul>
</details>

**Discussion**: The community discussion reflects a mix of skepticism and cautious optimism. Some users expressed concerns about the reliability of using LLMs for ontology construction, arguing that models often fail to strictly follow instructions or prioritize provided data over their internal weights. Others, particularly those in enterprise settings, noted the high cost of getting ontology right and are curious if this tool can practically assist them.

**Tags**: `#ontology`, `#knowledge-representation`, `#LLM-tools`, `#enterprise-AI`, `#open-source`

---

<a id="item-6"></a>
## [Revolut Transitions to Self-Hosted GLM Models for Cost and Privacy](https://twitter.com/guilleflorvs/status/2117379073785696395) ⭐️ 7.0/10

Revolut has transitioned from proprietary API-based LLMs to self-hosted open-source GLM models, deploying 56 Nvidia B200s to achieve a blended cost of $0.30 per million tokens. This move reportedly reduces their token expenses to roughly a tenth of what they previously paid to providers like Anthropic and OpenAI. This transition serves as a significant enterprise case study demonstrating that major fintech companies can achieve substantial cost savings and enhanced data privacy by self-hosting open-source models. It highlights a growing trend where organizations are moving away from proprietary APIs to gain better control over costs, data security, and model behavior. The infrastructure investment includes 56 Nvidia B200 GPUs with an estimated hardware cost of $2.5M-3M, plus ongoing operating expenses for electricity, cooling, and updates. The reported blended cost of $0.30 per million tokens represents a significant reduction compared to proprietary API pricing, though the exact calculation method (input vs. output averaging) remains unclear.

hackernews · pretext · Nov 3, 09:53 · [Discussion](https://news.ycombinator.com/item?id=50350004)

**Background**: GLM (General Language Model) is a series of open-weight large language models developed by Z.ai, designed to be competitive with frontier models in reasoning, coding, and agentic tasks. Self-hosting LLMs allows organizations to run these models on their own hardware, eliminating per-token API charges and providing complete control over data privacy. This approach becomes cost-effective at scale, as organizations pay for hardware upfront rather than per request.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://www.premai.io/blog/self-hosted-llm-guide-setup-tools-cost-comparison-2026/">Self - Hosted LLM Guide: Setup, Tools & Cost Comparison (2026)</a></li>

</ul>
</details>

**Discussion**: Community discussion centered on the practical benefits of self-hosting, including eliminating token rationing that stifles developer productivity and ensuring data privacy by removing trust dependencies on third-party inference providers. Commentators noted that open-source models often follow instructions more precisely than proprietary alternatives, though they may struggle with ambiguous prompts, and debated the cost-effectiveness of the hardware investment versus previous API spending.

**Tags**: `#self-hosted-llm`, `#enterprise-ai`, `#open-source-models`, `#data-privacy`, `#glm`

---

<a id="item-7"></a>
## [Kyle Kingsbury Warns LLMs Erode Trust in Software Maturity Signals](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 7.0/10

In his Jepsen analysis of ParticleDB 1.1.4, Kyle Kingsbury included a notable section on LLM tradeoffs, arguing that LLMs erode trust in documentation, software, and the organizations that produce them by making traditional markers of system maturity easier to counterfeit. He posed an open question to the community about what maintainers can do to ensure correct software and demonstrate its quality to users in the age of LLMs. This observation highlights a novel societal and technical concern: as LLMs make it trivial to generate polished documentation, test suites, and other signals of engineering rigor, engineers may begin treating all new software projects with suspicion. This could fundamentally shift how trust is established in the software ecosystem, forcing maintainers to find new ways to prove genuine quality beyond surface-level indicators. The quote appears in the context of a Jepsen analysis of ParticleDB 1.1.4, a multi-model database designed for AI workloads that claimed to be Postgres-compatible and offer "Full ACID" transactions, but which Jepsen found exhibited frequent and profound transactional anomalies. Kingsbury's LLM tradeoffs section broadens the scope from this specific failure to a systemic concern about the software industry at large.

rss · Simon Willison · Nov 1, 16:49

**Background**: Jepsen is an independent distributed-systems analysis and testing project created by Kyle Kingsbury (also known as Aphyr) that has uncovered critical correctness bugs in dozens of popular databases, becoming a practical standard for validating consistency claims. ParticleDB is a database marketed for AI agents that claimed Postgres compatibility and full ACID compliance, claims that Jepsen's rigorous testing found to be significantly overstated. The intersection of these findings with LLM-generated content raises questions about whether AI tools make it easier for projects to present a veneer of maturity without underlying substance.

<details><summary>References</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen: ParticleDB 1.1.4</a></li>
<li><a href="https://system-design.space/en/chapter/jepsen-consistency/">Jepsen and consistency models — System Design Space</a></li>
<li><a href="https://news.ycombinator.com/item?id=50316100">Jepsen: ParticleDB 1.1.4 | Hacker News</a></li>

</ul>
</details>

**Discussion**: Discussion on Hacker News around the Jepsen ParticleDB analysis highlighted the severity of the database's correctness failures, with commenters noting it was described as "a library of confusion" exhibiting transactional anomalies in essentially every test scenario. The broader concern about LLMs eroding trust signals resonated with readers familiar with the challenge of evaluating software quality in an era of AI-generated documentation and marketing materials.

**Tags**: `#llms`, `#software-engineering`, `#trust`, `#documentation`, `#generative-ai`

---

<a id="item-8"></a>
## [Small-scale validation of "good views beat next-token prediction" using human captions](https://www.reddit.com/r/MachineLearning/comments/1xlzoze/smallscale_check_of_good_views_beat_nexttoken/) ⭐️ 7.0/10

A researcher conducted a laptop-scale experiment (11M-param text encoder, 10,000 COCO photos with human captions) to test whether the Balestriero & LeCun (2026) claim about "good views" outperforming next-token prediction holds when using only human-written captions, eliminating the potential data leakage present in the original paper's use of image captioner-generated text. The results confirmed the same ranking: good views (0.320) > bad views (0.192) > next-token prediction (0.148) on mutual 10-NN retrieval between text and frozen DINOv2 image embeddings. This experiment addresses a critical methodological concern in the original LeJEPA paper — that image captioner-generated text could leak visual information into the text training data, inflating alignment scores. By replicating the core finding with strictly human-written captions, it provides independent evidence that the "good views" training paradigm genuinely produces better multimodal alignment, strengthening confidence in the approach for representation learning research. The setup used frozen DINOv2-base image embeddings and a 4-layer, width-256 text encoder (11M params) trained for 3,000 steps with a VICReg-style anti-collapse loss rather than the paper's SIGReg loss. The gap between methods was smaller when measured via R@1 retrieval with a fitted rotation (0.084 vs 0.063 vs 0.057) compared to mutual 10-NN, and the experiment was limited to a single dataset, a single image model, and parameters far smaller than the original paper's 109M model trained on 72B tokens.

reddit · r/MachineLearning · /u/Traditional_Frame763 · Nov 2, 15:08

**Background**: DINOv2 is a self-supervised visual foundation model that produces robust, transferable image features using Vision Transformer architectures. VICReg (Variance-Invariance-Covariance Regularization) is a self-supervised learning loss that prevents embedding collapse by encouraging variance across batch dimensions, invariance to augmentations, and decorrelation between embedding dimensions. SIGReg (Sketched Isotropic Gaussian Regularization), introduced by Balestriero & LeCun for the LeJEPA framework, is a newer regularization technique that encourages embeddings to follow an isotropic Gaussian distribution without requiring heuristics like stop-gradients. The "good views" concept refers to training text encoders on pairs of different captions describing the same image, creating a contrastive signal that aligns text representations with image representations without the text model ever directly seeing image data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/dinov2-model">DINOv 2 Visual Foundation Model</a></li>
<li><a href="https://imbue.com/blog/2022-04-21-vicreg">VICReg : Tutorial and lightweight PyTorch implementation - Imbue</a></li>
<li><a href="https://deepwiki.com/rbalestr-lab/lejepa/3.1-sigreg-loss">SIGReg Loss | rbalestr-lab/lejepa | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#MachineLearning`, `#Multimodal Alignment`, `#Representation Learning`, `#Empirical Study`, `#DINOv2`

---

<a id="item-9"></a>
## [LightMIS: Ultra-lightweight medical image segmentation for edge devices](https://www.reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image/) ⭐️ 7.0/10

Researchers introduced LightMIS, a 2D binary medical image segmentation model with only 131K parameters that aggregates multi-scale encoder features directly without a learned stage-wise decoder. The model achieves performance comparable to nnU-Net while using 98.14% fewer parameters and 94.58% fewer GFLOPs, and runs 10.5x faster on an Arm Mali-G52 MC2 edge GPU. This work demonstrates that high-quality medical image segmentation can be achieved with drastically reduced computational requirements, making it highly practical for deployment on resource-constrained edge devices. By maintaining near state-of-the-art accuracy with a fraction of the parameters, LightMIS enables faster, more energy-efficient medical imaging analysis in clinical and remote settings. The model was trained and evaluated under the nnU-Net v2.3.1 protocol across six datasets and five imaging modalities to ensure a fair comparison. All LightMIS variants achieved 100% GPU operator coverage without CPU fallback, avoiding the latency issues that arise when unsupported operations are offloaded to the CPU.

reddit · r/MachineLearning · /u/OkLion2068 · Nov 2, 20:22

**Background**: nnU-Net is a self-configuring framework for medical image segmentation that automatically adapts preprocessing, network architecture, and training based on dataset properties. Segmentation performance is commonly evaluated using overlap metrics such as the Dice Coefficient and Intersection over Union (IoU). In edge computing, "operator fallback" occurs when a model contains operations not supported by the hardware accelerator, forcing them to run on the CPU and causing significant latency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/nnu-net-framework">nnU - Net : Automated Medical Image Segmentation</a></li>
<li><a href="https://apxml.com/courses/cnns-for-computer-vision/chapter-4-image-segmentation-techniques/segmentation-evaluation-metrics">Image Segmentation Evaluation Metrics ( IoU , Dice )</a></li>
<li><a href="https://www.techveda.live/2026/08/18/operator-fallback-edge-inference/">Operator Fallback: Why the Accelerator Path Is Slower</a></li>

</ul>
</details>

**Tags**: `#medical-imaging`, `#model-efficiency`, `#edge-computing`, `#image-segmentation`, `#lightweight-models`

---

<a id="item-10"></a>
## [U.S. Census Bureau AI Adoption Data Disrupted by Executive Order 14434](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/) ⭐️ 6.0/10

Simon Willison updated his AI adoption analysis using October 22, 2026 data from the U.S. Census Bureau's Business Trends and Outlook Survey (BTOS), revealing that the Bureau was affected by Executive Order 14434 (dubbed the 'Super Intelligence' order), which caused a disruption including a 2025 shutdown. The survey question was also broadened in November 2025 from 'AI in producing goods or services' to 'AI in any business function,' creating a break in the time series that makes pre- and post-break data not directly comparable. The BTOS is one of the few large-scale, recurring U.S. government surveys tracking corporate AI adoption, and the disruption from Executive Order 14434 introduces a significant gap in longitudinal data that policymakers, analysts, and businesses rely on to understand AI adoption trends. The change in survey wording also complicates year-over-year comparisons, making it harder to assess whether AI adoption is genuinely accelerating or plateauing. The latest data (collected October 5–18, 2026) shows AI use in any business function at 40.7% for firms with 250+ employees, 33.5% for 100–249, 27.9% for 50–99, 23.8% for 20–49, 23.3% for 1–4, 22.1% for 10–19, and 21.1% for 5–9. The chart uses a six-survey trailing average, and the gap between the old and new question wordings includes both the 2025 shutdown and the wait for six observations under the broader question.

rss · Simon Willison · Nov 2, 13:31

**Background**: The Business Trends and Outlook Survey (BTOS) is a biweekly U.S. Census Bureau survey reaching 200,000 businesses out of 1.2 million total, with each business completing the survey every twelve weeks, and new data published on alternating Thursdays at 10am. Executive Order 14434, titled 'Inaugurating the Era of Super Intelligence,' is a White House order that appears to have disrupted the Bureau's data collection operations. Willison previously used the same Apollo Global Management chart based on Census data to demonstrate GPT-5 data analysis capabilities and Claude's Code Interpreter, a tool that runs Python and Node.js in a sandboxed environment for data manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Sep/9/claude-code-interpreter/">My review of Claude’s new Code Interpreter, released under a ...</a></li>
<li><a href="https://grokipedia.com/page/Claude_Code_Interpreter">Claude Code Interpreter — Grokipedia</a></li>

</ul>
</details>

**Tags**: `#AI adoption`, `#AI policy`, `#executive order`, `#data analysis`, `#Simon Willison`

---