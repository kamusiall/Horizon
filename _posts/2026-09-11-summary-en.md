---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 32 items, 10 important content pieces were selected

---

1. [Quoting Calif Research](#item-1) ⭐️ 9.0/10
2. [OpenAI Releases New Agents API for Managed AI Agent Infrastructure](#item-2) ⭐️ 8.0/10
3. [More questions about whether researchers can trust OpenAI with unpublished math](#item-3) ⭐️ 8.0/10
4. [Native is now the future of mobile at Shopify](#item-4) ⭐️ 8.0/10
5. [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](#item-5) ⭐️ 7.0/10
6. [Forgejo <=16.0.3 Critical RCE](#item-6) ⭐️ 7.0/10
7. [ACL Sustainable Reviewing Policy (D)](#item-7) ⭐️ 7.0/10
8. [Shopify Moves Mobile Apps from React Native Back to Swift and Kotlin](#item-8) ⭐️ 6.0/10
9. [trynix.dev: Boot Any Nix Package in Your Browser](#item-9) ⭐️ 6.0/10
10. [Solo 348M Model Outperforms GPT-3 on Arithmetic via Step-by-Step Reasoning](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Quoting Calif Research](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research demonstrates WeWorm, a zero-click worm spreading through WeChat calls on iOS and Android, developed in just two days using AI to find the bug and write the RCE exploit.

rss · Simon Willison · Sep 10, 00:56

**Tags**: `#ai-security`, `#cybersecurity`, `#zero-click-exploit`, `#ai-assisted-research`, `#vulnerability`

---

<a id="item-2"></a>
## [OpenAI Releases New Agents API for Managed AI Agent Infrastructure](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI has introduced the Agents API, a managed service that runs the Codex harness and handles underlying agent infrastructure, enabling developers to create production-ready agents in a single API call by specifying a task, model, tools, and environment. The API includes features such as automatic context compaction, multi-agent orchestration, programmatic tool calling, and support for MCP (Model Context Protocol). This release represents a significant shift in the agentic AI landscape by offering agent-as-a-service, removing the burden of building and maintaining agent harnesses, sandboxes, and reliability infrastructure from developers. It could accelerate adoption of agentic AI across products by making it trivial to integrate autonomous agent capabilities without deep infrastructure expertise, though it also raises concerns about vendor lock-in. Notably, the API allows developers to opt for self-hosted sandboxes, which could ease transitions between providers and reduce lock-in concerns. The service also supports the Agents SDK for managed workflows while allowing direct calls to the Responses API for lower-level control, giving developers flexibility in how they interact with the system.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: An AI agent is a program that can pursue goals, use external tools, and take actions with some level of autonomy, typically driven by large language models. Building an agent 'harness'—the orchestration layer that manages tool calls, state, memory, and multi-step execution—is complex and infrastructure-heavy, which is why managed services like this are emerging. Agentic AI represents an evolution beyond simple chatbot interactions toward systems that can perceive, reason, and act autonomously across multi-step workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents SDK | OpenAI API</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>

</ul>
</details>

**Discussion**: The community is divided on the merits of agent-as-a-service versus self-hosted solutions: some appreciate the abstraction and ease of use it provides, especially for serverless environments where state persistence is challenging, while others see it as vendor lock-in and advocate for running agents in self-managed VMs. The ability to self-host sandboxes is highlighted as a particularly enticing feature that may ease provider transitions, though some users express frustration with the push toward managed services and demand more transparency around reasoning tokens they pay for.

**Tags**: `#OpenAI`, `#Agents`, `#API`, `#LLM`, `#Agentic AI`

---

<a id="item-3"></a>
## [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

Mathematicians and researchers are raising concerns about whether OpenAI can be trusted with unpublished research, given that the company may train on researcher interactions and publish related results without attribution.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Tags**: `#OpenAI`, `#AI Ethics`, `#Research Integrity`, `#Data Privacy`, `#Intellectual Property`

---

<a id="item-4"></a>
## [Native is now the future of mobile at Shopify](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify is moving from React Native back to native Swift and Kotlin, citing that AI agents can now handle enough of the dual-platform implementation work to make it cost-effective.

rss · Simon Willison · Sep 10, 21:11

**Tags**: `#AI agents`, `#software engineering`, `#React Native`, `#mobile development`, `#industry trends`

---

<a id="item-5"></a>
## [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 7.0/10

Cognition announces its new SWE-2 coding model, claiming performance rivaling other leading models, but the community raises concerns about benchmark generalization, closed-weights, and the company's past credibility.

hackernews · seelos · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645443)

**Tags**: `#AI models`, `#software engineering`, `#benchmarks`, `#LLM`, `#coding agents`

---

<a id="item-6"></a>
## [Forgejo <=16.0.3 Critical RCE](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 7.0/10

Forgejo versions 16.0.3 and below contain a critical remote code execution vulnerability caused by template variable expansion interfering with git repository initialization.

hackernews · weierstass · Sep 10, 15:57 · [Discussion](https://news.ycombinator.com/item?id=49645907)

**Tags**: `#security`, `#vulnerability`, `#forgejo`, `#rce`, `#git-hosting`

---

<a id="item-7"></a>
## [ACL Sustainable Reviewing Policy (D)](https://www.reddit.com/r/MachineLearning/comments/1wd7b83/acl_sustainable_reviewing_policy_d/) ⭐️ 7.0/10

ACL announces a proposed 'Sustainable Reviewing Policy' that would cap total submissions at 20 per author and 5 per first-author per cycle, require each submission to come with a qualified reviewer, and use a lottery system when submissions exceed reviewer capacity.

reddit · r/MachineLearning · /u/S4M22 · Sep 11, 05:38

**Tags**: `#academic-publishing`, `#peer-review`, `#NLP`, `#ACL`, `#research-policy`

---

<a id="item-8"></a>
## [Shopify Moves Mobile Apps from React Native Back to Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 6.0/10

Shopify has announced a major architectural shift away from React Native, returning to native development using Swift for iOS and Kotlin for Android for their mobile applications. This reverses their earlier adoption of React Native as a cross-platform solution. This decision is a high-profile reversal that could influence other large companies evaluating whether cross-platform frameworks like React Native are worth the trade-offs at scale. It signals that for complex, high-traffic mobile applications, native development may still offer advantages in performance, developer experience, and maintainability that outweigh the benefits of a shared codebase. The migration involves rewriting significant portions of the mobile app stack in platform-native languages, which is a resource-intensive process for a company of Shopify's scale. Some community members note that LLM-assisted tooling such as Codex has made large-scale rewrites more feasible, though others dispute whether AI tooling was a decisive factor in Shopify's decision.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is a popular cross-platform framework developed by Meta (formerly Facebook) that allows developers to write mobile apps using JavaScript and React, sharing much of the codebase between iOS and Android. Native development using Swift (for iOS) and Kotlin (for Android) involves writing separate codebases for each platform but typically yields better performance, smoother UI, and easier access to platform-specific APIs. Shopify originally adopted React Native to accelerate mobile development and share code across platforms, but has now concluded that the trade-offs no longer favor that approach for their use case.

**Discussion**: Community discussion is highly active, with many commenters expressing astonishment that Shopify employs 3,000 engineers for what they perceive as a relatively straightforward e-commerce app, questioning the company's engineering credibility. Several commenters share their own experiences migrating from React Native to native, with some noting that AI tools like Codex can accelerate such rewrites for smaller apps, while others argue that LLM assistance was not a decisive factor in pre-2026 migrations. There is broad agreement that moving off React Native can be the right call, but debate over the narrative that AI tooling made Shopify's migration economically viable.

**Tags**: `#mobile-development`, `#react-native`, `#swift`, `#kotlin`, `#software-architecture`

---

<a id="item-9"></a>
## [trynix.dev: Boot Any Nix Package in Your Browser](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 6.0/10

trynix.dev is a new platform that lets users boot any Nix package from the past 13 years directly in a browser-based WebAssembly VM. A complementary GitHub Action, trynix-preview, was also released to allow reviewers to boot a pull request's build in the browser without needing servers. This project makes historical and reproducible software environments instantly accessible for debugging, testing, and education without requiring local installations or remote servers. It also pioneers a new interactive code review workflow where changes can be tested live in the browser before merging. The platform uses qemu-wasm to run an x86_64 Linux virtual machine entirely through WebAssembly in the browser. Packages are URL-addressable, allowing users to directly link to specific historical versions, such as Python 3.6.2 from 2017.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a declarative package manager known for its reproducible builds and ability to maintain multiple versions of software side-by-side. WebAssembly (Wasm) is a portable compilation target that allows high-performance code to run securely in web browsers. qemu-wasm is a port of the QEMU emulator to WebAssembly, enabling full virtual machines to run client-side.

**Tags**: `#nix`, `#webassembly`, `#reproducibility`, `#developer-tools`, `#virtualization`

---

<a id="item-10"></a>
## [Solo 348M Model Outperforms GPT-3 on Arithmetic via Step-by-Step Reasoning](https://www.reddit.com/r/MachineLearning/comments/1wc7hmu/i_trained_a_348m_model_trained_from_scratch_on/) ⭐️ 6.0/10

A solo developer trained a 348M parameter language model from scratch on 22.7B tokens, fine-tuning it to solve arithmetic by explicitly showing step-by-step work like carries and borrow chains. The model achieves a 99.4% average across nine GPT-3 arithmetic sub-tasks, outperforming GPT-3 175B, and can add up to 14 digits after the developer expanded the place-value vocabulary from 6 to 19 entries. This project demonstrates that a very small model can dramatically outperform massive models on specific reasoning tasks when trained to use explicit, structured chain-of-thought reasoning. It highlights that model scale is not always the bottleneck for arithmetic; instead, the training methodology and vocabulary design are critical factors for success. The model achieves 98% on 3x3 multiplication and 85% on negative results, but struggles significantly with word problems (4% on GSM8K) due to operation selection errors rather than arithmetic errors. It requires greedy decoding, as sampling corrupts the column routine, and it currently has no division capability.

reddit · r/MachineLearning · /u/nkthebass · Sep 10, 03:28

**Background**: Chain-of-thought prompting is a technique where language models are encouraged to generate intermediate reasoning steps before arriving at a final answer, which has been shown to improve performance on arithmetic and logic tasks. While large models often exhibit this emergent ability, this project explicitly trains a small model to perform structured, step-by-step arithmetic operations, mimicking how humans calculate using columns and carries.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in ...</a></li>
<li><a href="https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/">Language Models Perform Reasoning via Chain of Thought</a></li>

</ul>
</details>

**Tags**: `#small-models`, `#arithmetic`, `#chain-of-thought`, `#training`, `#benchmarks`

---