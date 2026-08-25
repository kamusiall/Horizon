---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 32 items, 7 important content pieces were selected

---

1. [MS Paint and Photos silently watermark AI images with server-issued GUIDs](#item-1) ⭐️ 8.0/10
2. [Anthropic’s best AI model struggles to attract users as cheaper tools thrive](#item-2) ⭐️ 7.0/10
3. [Using AI as a Spatial Software Generator for Programmable 3D Objects](#item-3) ⭐️ 7.0/10
4. [CCPL: Delay-Corrected Bellman Operator for Constrained RL](#item-4) ⭐️ 7.0/10
5. [The entire city of San Francisco as a video game](#item-5) ⭐️ 6.0/10
6. [XMPP Celebrates 25 Years of Digital Independence](#item-6) ⭐️ 6.0/10
7. [SQLite Database File Doubles as Executable Linux Binary](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [MS Paint and Photos silently watermark AI images with server-issued GUIDs](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Microsoft Paint and Photos have been found to silently embed invisible, GUID-based watermarks into images manipulated using AI features, even when users utilize local models for generation. The watermark GUID is issued from a remote server during prompt moderation, meaning the process is not fully local and creates a traceable identifier linked to the user's session. This discovery raises significant privacy concerns because users may believe local AI processing is private and offline, yet the watermarking system contacts Microsoft's servers to obtain a unique identifier. The silent, non-disableable watermark could enable traceability of AI-generated or AI-edited images back to specific users, potentially undermining internet anonymity and creating risks of identification through legal subpoenas. The invisible watermark is embedded at the pixel level and is referenced by a GUID stored in the C2PA manifest, which is a content provenance standard. Even when using local AI models, Paint's local generation path contacts a remote server for prompt moderation and receives the watermark GUID, meaning the process is not truly offline.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: C2PA (Coalition for Content Provenance and Authenticity) is a standard for certifying the source and history of media content, often used to combat misinformation by embedding provenance metadata. Digital watermarking embeds information into media files in ways that are difficult to perceive or remove, and has been increasingly adopted by AI companies to mark AI-generated content. Local AI models run on a user's own hardware rather than cloud servers, which users typically assume provides greater privacy and autonomy.

<details><summary>References</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible Watermarks in Locally-Generated Images :: Xusheng Li</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock that MS Paint has evolved beyond a simple pixel-coloring app and concern that silent watermarking represents a threat to internet anonymity. Several users noted that the GUID watermark could be weaponized through copyright subpoenas to identify anonymous creators, while others pointed out Microsoft's history of sloppy AI feature implementations, such as the Copilot watermark incident in Azure DevOps. The consensus was that this is less about AI provenance and more about secret user tracking.

**Tags**: `#AI`, `#Privacy`, `#Watermarking`, `#Microsoft`, `#Security`

---

<a id="item-2"></a>
## [Anthropic’s best AI model struggles to attract users as cheaper tools thrive](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 7.0/10

An FT report reveals Anthropic's annualized revenue reached $65bn in July with expected Q3 profitability, while OpenAI's revenue surpassed $40bn following the GPT 5.6 launch.

rss · Simon Willison · Aug 23, 20:24

**Tags**: `#Anthropic`, `#OpenAI`, `#AI Industry`, `#Revenue`, `#Market Analysis`

---

<a id="item-3"></a>
## [Using AI as a Spatial Software Generator for Programmable 3D Objects](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

A new paper explores using Large Language Models (LLMs) as spatial software generators to create 3D objects that are inherently programmable, animation-ready, and structurally articulated from inception. Unlike traditional AI 3D generators that produce monolithic meshes, this approach generates 3D objects as software code with built-in hierarchical structures and articulation logic. This approach could significantly disrupt industries like industrial design, game development, simulations, and AR/VR/XR by producing 3D assets that are immediately usable in animations and adaptable to different compute environments. It represents a paradigm shift from mesh-based 3D generation toward procedural, code-driven 3D creation that leverages the improving spatial coding capabilities of LLMs. The generated 3D objects contain logic at creation time to adapt their appearance based on compute power, appearing differently on mobile devices versus sophisticated game engines. The approach currently lags behind traditional AI 3D generators in creating complex organic shapes, but the authors argue that as LLMs improve at spatial coding, code will eventually dominate 3D generation.

reddit · r/MachineLearning · /u/mhb_11 · Aug 24, 19:10

**Background**: Traditional AI 3D generators typically produce monolithic textured meshes—single geometric blobs without internal structure or articulation. Procedural modeling, by contrast, uses rule-based or node-based systems to generate geometry through linked relationships, allowing for more structured and editable outputs. Articulated 3D models consist of rigid bodies connected by joints, enabling natural movements and animations, which is a key advantage of the spatial programming approach described in this work.

<details><summary>References</summary>
<ul>
<li><a href="https://www.maxon.net/it/article/3d-modeling-vs-3d-rendering">3 D Modeling vs . 3 D Rendering: What is the Difference?</a></li>
<li><a href="https://www.mold7.com/what-articulated-3d-model">What Is an Articulated 3D Model and How Can You Use It? mold7.com</a></li>
<li><a href="https://www.automatic3d.com/compare/meshy">Automatic 3 D vs Meshy — AI Text-to- 3 D Comparison (2026)</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#3D-generation`, `#spatial-programming`, `#procedural-modeling`, `#AI-research`

---

<a id="item-4"></a>
## [CCPL: Delay-Corrected Bellman Operator for Constrained RL](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 7.0/10

The post introduces CCPL (Causal Consequence-Penalized Learning), a method for constrained reinforcement learning that uses a delay-corrected Bellman operator with an adaptive effective discount learned from the consequence-delay distribution, along with an Interventional Consequence Net (ICN) for causal attribution of consequences to actions. Standard constrained RL assumes immediate and attributable consequences, which breaks down in real-world settings where violations are delayed and stochastic, leading to incorrect penalization of actions. CCPL addresses this fundamental problem by providing a theoretically grounded approach (with a contraction proof under unknown stochastic delay) that could significantly improve the reliability of safe RL in complex, real-world environments. The delay-corrected Bellman operator's contraction proof holds under unknown stochastic delay, and the ICN is pretrained on structural-causal-model labels to estimate marginal causal contribution per action rather than relying on temporal proximity. A notable limitation is that the ICN currently requires access to the environment's structural causal model to generate pretraining labels, which restricts applicability to benchmark settings where the SCM is known or can be reasonably specified.

reddit · r/MachineLearning · /u/No_Cauliflower7923 · Aug 24, 12:11

**Background**: In reinforcement learning, the Bellman operator is a mathematical tool used to update value functions, and its contraction property guarantees convergence to a unique optimal solution under certain conditions. Constrained RL extends standard RL by adding constraints (such as safety limits) that the agent must respect while maximizing rewards. A structural causal model (SCM) is a formal framework representing the causal mechanisms of a system, often using directed acyclic graphs to describe relationships among variables and guide causal inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baeldung.com/cs/bellman-operator-reinforcement-learning">What Is the Bellman Operator in Reinforcement Learning? | Baeldung on Computer Science</a></li>
<li><a href="https://en.wikipedia.org/wiki/Structural_causal_model">Structural causal model</a></li>
<li><a href="http://mitliagkas.github.io/ift6085-2020/ift-6085-lecture-19-notes.pdf">IFT 6085 - Lecture 19 Basic results on reinforcement learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#causal inference`, `#constrained RL`, `#bellman operator`, `#attribution`

---

<a id="item-5"></a>
## [The entire city of San Francisco as a video game](https://sf.thijs.gg/) ⭐️ 6.0/10

A web-based interactive 3D model of San Francisco that users can explore like a video game, sparking community discussion about potential expansions and procedural generation.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Tags**: `#3D graphics`, `#procedural generation`, `#interactive maps`, `#game development`, `#digital twins`

---

<a id="item-6"></a>
## [XMPP Celebrates 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 6.0/10

The XMPP protocol, originally known as Jabber, marked its 25th anniversary, prompting reflection on its enduring role as an open, federated communication standard. The milestone highlights the protocol's continued relevance in an era of increasing platform centralization. XMPP represents a foundational model for decentralized, vendor-independent digital communication, offering an alternative to proprietary messaging silos. Its flexibility is further evidenced by modern, unconventional use cases such as serving as a communication layer for AI agents. The protocol supports federated messaging, allowing users on different servers to communicate seamlessly, much like email. Community members continue to actively develop and use clients like Movim, Conversations, and Fluux, alongside server software such as ejabberd and Prosody.

hackernews · inputmice · Aug 24, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49421536)

**Background**: XMPP (Extensible Messaging and Presence Protocol) is an open XML-based protocol for real-time communication, originally created in 1999 under the name Jabber. In its early days, major platforms like Google and Facebook adopted XMPP for their chat services, enabling interoperability where users could chat across different networks using a single client. Over time, many of these platforms moved to proprietary protocols, but XMPP has maintained a dedicated community and continues to be used for instant messaging, presence, and specialized applications.

**Discussion**: The community discussion reflects a mix of nostalgia and ongoing practical use, with some users noting XMPP's past interoperability with services like Google and Facebook. A notable portion of the debate centers on the XMPP vs. Matrix rivalry, with some commenters arguing that Matrix duplicated efforts and received disproportionate funding that could have strengthened the XMPP ecosystem. Interestingly, one user highlighted a modern AI use case, employing XMPP as a communication layer for AI agents, while others shared practical experiences with telephony bridges like jmp.chat.

**Tags**: `#XMPP`, `#Communication Protocols`, `#AI Agents`, `#Open Source`, `#Digital Independence`

---

<a id="item-7"></a>
## [SQLite Database File Doubles as Executable Linux Binary](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 6.0/10

Farid Zakaria demonstrated a method for creating a SQLite database file that also functions as a directly executable Linux binary by mapping ELF (Executable and Linkable Format) components into SQLite tables. The technique sets the SQLite file's 4-byte application ID to 'SELF' (Structured Executable & Linkable Format) and uses a custom C interpreter called 'self-exec' to extract and run the executable pieces. This is a clever systems programming pattern that creatively combines two ubiquitous file formats, demonstrating the flexibility of both SQLite and Linux's executable handling mechanisms. While more of a technical curiosity than a major breakthrough, it showcases novel approaches to binary packaging and could inspire new methods for bundling data and executables together. The SQLite application ID is set at byte 68 of the file to the value 'SELF', and the ELF components are arranged according to a defined SQL schema. Execution relies on Linux's binfmt_misc kernel mechanism, which can be configured to recognize the 'SELF' pattern and route it to the self-exec interpreter, allowing the kernel to directly execute the database file.

rss · Simon Willison · Aug 24, 11:38

**Background**: The Executable and Linkable Format (ELF) is the standard file format for executables, object code, and shared libraries on Linux and Unix-like systems. SQLite is a widely used embedded relational database that stores an entire database in a single file, which includes a configurable 4-byte application ID field for application identification. The Linux kernel's binfmt_misc capability allows arbitrary executable file formats to be recognized and passed to user space applications, such as emulators or custom interpreters, enabling non-native files to be executed directly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Binfmt_misc">binfmt_misc - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/35557487/where-can-i-register-a-sqlite-application-id">registration - Where can I register a sqlite application ID ?</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#Systems Programming`, `#Executable Formats`

---