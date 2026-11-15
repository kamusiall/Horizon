---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 25 items, 6 important content pieces were selected

---

1. [Lovable AI-built apps expose passport details and over 200K private messages](#item-1) ⭐️ 8.0/10
2. [ICML 2027 Introduces Two-Stage Review and Reciprocal Reviewer Requirements](#item-2) ⭐️ 7.0/10
3. [Developer Trains Encoder-Only Transformer with LoRA to Predict Blood Sugar](#item-3) ⭐️ 7.0/10
4. [SpaceX Catches Starship Booster With Mechazilla Arms After Flight 15](#item-4) ⭐️ 6.0/10
5. [Papr Memory Retrieval Achieves 96.0% on LongMemEval-S Benchmark](#item-5) ⭐️ 6.0/10
6. [Should short-horizon price forecasting papers benchmark against market-implied forecasts, not just naive baselines? (D)](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Lovable AI-built apps expose passport details and over 200K private messages](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

Security researchers at Crissy Field revealed that apps built with Lovable, an AI app builder, exposed sensitive user data including passport details and over 200,000 private messages due to insufficient Row-Level Security (RLS) in their underlying Supabase databases. This incident underscores the real-world security risks of AI-generated code, where rapid app creation can outpace proper security configuration and expose sensitive data at scale. With AI app builders producing applications in minutes, misconfigured database permissions can create thousands of vulnerable apps that require no sophisticated hacking to exploit. The root cause was insufficient Row-Level Security policies in Supabase, which exposes PostgreSQL databases directly through auto-generated Data APIs accessible from the frontend. Lovable has implemented automatic pre-publish scanning and a free deeper SAST scan with auto-fix options and publish-blocking on unresolved findings, though community reports suggest Supabase's default configurations may remain insecure for existing projects despite an October 30 fix.

hackernews · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**Background**: Lovable is an AI app builder that creates working web applications from natural language prompts, including database schemas and application logic. Many such apps use Supabase, a backend-as-a-service built on PostgreSQL that exposes the database directly through auto-generated REST APIs via PostgREST. Row-Level Security (RLS) is a PostgreSQL feature that controls which rows users can SELECT, INSERT, UPDATE, or DELETE based on authorization policies; without proper RLS configuration, any authenticated user can potentially access all rows in a table.

<details><summary>References</summary>
<ul>
<li><a href="https://supabase.com/docs/guides/database/overview">Database | Supabase Docs</a></li>
<li><a href="https://lovable.dev/">App & Website Builder | Build Software in Minutes | Lovable</a></li>

</ul>
</details>

**Discussion**: The blog author noted the post initially gained little traction two weeks prior. Discussion focused on shared responsibility between Lovable and Supabase, with one commenter linking to a Supabase GitHub discussion about insecure defaults that may persist for existing projects despite an October 30 fix. Lovable's Head of Security confirmed the root cause was insufficient RLS and described their automated scanning and auto-fix tooling, while other commenters emphasized that AI-generated apps are easy targets requiring no sophisticated hacking knowledge and are being created in large numbers daily.

**Tags**: `#ai-coding-tools`, `#security`, `#lovable`, `#supabase`, `#row-level-security`

---

<a id="item-2"></a>
## [ICML 2027 Introduces Two-Stage Review and Reciprocal Reviewer Requirements](https://www.reddit.com/r/MachineLearning/comments/1xvkxbj/icml_2027_changes_d/) ⭐️ 7.0/10

ICML 2027 has announced a two-stage review process where area chairs decide whether a paper proceeds to full review, with senior area chairs confirming any proposed first-stage rejections and authors receiving short justifications by February 23. The conference also mandates reciprocal reviewer requirements: every paper must name a reciprocal reviewer from its author list, no reviewer can be on more than 20 submissions, and authors with three or more submissions must serve on the program committee. These changes directly address the escalating crisis of submission explosion and reviewer burnout that has plagued major ML conferences in recent years as submission numbers have grown into the thousands. If successful, the policy could set a precedent for other top-tier AI conferences and significantly reshape how machine learning research is evaluated and published. Each reciprocal reviewer can handle a maximum of 6 papers, and each author is allowed on at most one paper that lacks an eligible reciprocal reviewer among its authors, effectively limiting free passes for papers whose coauthors cannot review (e.g., undergrads, interns, non-field researchers). Papers that fail to comply with these requirements may be desk rejected, and the two-stage cut introduces a risk that quick area chair reads could overlook strong papers, though the senior area chair confirmation step serves as a safeguard.

reddit · r/MachineLearning · /u/Gravitist · Nov 13, 21:53

**Background**: Major machine learning conferences like ICML, NeurIPS, and ICLR have experienced exponential growth in paper submissions over the past decade, placing enormous strain on the volunteer-based peer review system. The traditional single-stage review process requires multiple reviewers to thoroughly evaluate every submission, which has become unsustainable as submission volumes have surged. Area chairs (ACs) oversee groups of papers and synthesize reviewer feedback, while senior area chairs (SACs) supervise ACs and handle escalations, forming a hierarchical quality-control structure within the conference review pipeline.

**Discussion**: The original poster views the changes as a reasonable and fair fix for out-of-control reviewer load, particularly praising the linkage between authorship volume and reviewing duty. However, they express concern that the first-stage area chair cut could cause good papers to be missed, though they acknowledge the senior area chair confirmation helps mitigate this risk, and they invite discussion on whether the solution might simply shift the problem elsewhere.

**Tags**: `#ICML`, `#Academic Publishing`, `#Peer Review`, `#Machine Learning`, `#Conference`

---

<a id="item-3"></a>
## [Developer Trains Encoder-Only Transformer with LoRA to Predict Blood Sugar](https://www.reddit.com/r/MachineLearning/comments/1xvja5n/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 7.0/10

A developer trained a custom 31,253-parameter encoder-only transformer on approximately 19,200 CGM-years of synthetic data and fine-tuned it using LoRA on 115 days of personal continuous glucose monitor (CGM) data. The resulting model can predict blood sugar levels up to 2 hours into the future, infill missing traces, perform backcasts, and has demonstrated an emergent ability to predict time-of-day from past blood sugar data. This project demonstrates a novel cross-pollination of large language model techniques, such as large-scale synthetic pretraining and LoRA fine-tuning, to personalized time-series health data. It suggests that parameter-efficient methods can create competitive, personalized predictive models for diabetes management, potentially paving the way for more accessible and accurate automated insulin dosing or alert systems. The model accepts time series inputs along with insulin and carbohydrate action curves, outputting blood glucose in Kovatchev risk-space using a combination of DILATE, MSE, and pinball loss with learned Kendall-Gal weights. Despite its capabilities, the developer notes the model is still worse than a human at predicting hypoglycemia in the next 30 minutes, and the simulator's counterfactual reasoning capabilities lack a downstream benchmark.

reddit · r/MachineLearning · /u/0xdeadf1sh · Nov 13, 20:48

**Background**: Continuous glucose monitors (CGMs) are wearable devices that continuously track interstitial glucose levels, which are highly correlated with blood glucose. LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that allows large pre-trained models to be adapted to specific tasks by adding small trainable matrices while keeping the original model weights frozen. An encoder-only transformer is a neural network architecture that processes input sequences to generate contextualized representations, commonly used in models like BERT.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Continuous_glucose_monitor">Continuous glucose monitor</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Time Series Prediction`, `#Personalized Medicine`, `#Transformers`, `#LoRA`

---

<a id="item-4"></a>
## [SpaceX Catches Starship Booster With Mechazilla Arms After Flight 15](https://www.spacex.com/launches/starship-flight-15) ⭐️ 6.0/10

SpaceX successfully caught the Starship Super Heavy booster using the Mechazilla launch tower's mechanical arms following Flight 15, marking a major milestone in fully reusable rocket technology. This is a significant step toward rapid reusability of the booster without requiring landing legs or ocean recovery. This achievement demonstrates the viability of catching and reusing the booster, which could dramatically reduce launch costs and turnaround times, opening a new era in spaceflight. It represents a critical step toward SpaceX's goal of full and rapid reusability for the Starship system, which is designed to carry crew and cargo to Earth orbit, the Moon, Mars, and beyond. The catch was performed by the Mechazilla launch tower arms at SpaceX's Starbase facility in Texas. The heat shield performance remains a key factor for future flights, and the next steps include attempting double catches and re-flying the same vehicles to validate the reusability cycle.

hackernews · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**Background**: Starship is a two-stage, fully reusable, super heavy-lift launch vehicle under development by SpaceX, consisting of the Starship spacecraft and the Super Heavy booster. Mechazilla is the nickname given by Elon Musk to the launch tower equipped with mechanical arms designed to catch returning boosters, named after the Mechagodzilla character from the Godzilla film franchise. The system is intended as the successor to the Falcon 9 and Falcon Heavy rockets and is designed to carry more than 100 metric tonnes to orbit in a fully reusable configuration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spacex.com/vehicles/starship">Starship - SpaceX</a></li>
<li><a href="https://en.m.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://www.inverse.com/innovation/spacex-mechazilla-starships-giant-orbital">SpaceX Starship: How the Mechazilla grabbing arm will enable a Mars...</a></li>

</ul>
</details>

**Discussion**: The community is overwhelmingly enthusiastic, with commenters calling it the dawn of a new era in spaceflight and praising the SpaceX engineering team. Key points include the importance of heat shield durability for future flights, the potential for double catches and re-flight of the same vehicles, and the cost advantages of 100% reusability compared to Falcon 9's estimated 60% reusability by cost.

**Tags**: `#SpaceX`, `#Starship`, `#aerospace`, `#reusability`, `#engineering`

---

<a id="item-5"></a>
## [Papr Memory Retrieval Achieves 96.0% on LongMemEval-S Benchmark](https://www.reddit.com/r/MachineLearning/comments/1xwnloh/longmemevals_960_with_the_official_judge_and_what/) ⭐️ 6.0/10

The Papr memory retrieval system scored 96.0% on all 500 LongMemEval-S questions using the official GPT-4o judge (gpt-4o-2024-08-06), with per-question answers and judge labels made public for reproducibility. The results were achieved using the Papr-Embed 0.6B open-source embedding model, a Gemini Flash 2.5 reranker, and a single-turn answer model, with retrieval recall reaching near-saturation at 97.9% for top-5 retrieval. This result demonstrates that retrieval-based memory systems are approaching the performance ceiling on LongMemEval-S, with most remaining errors attributable to the reader model rather than retrieval failures. The findings provide valuable empirical insights for the long-context LLM community, particularly regarding the tradeoffs between top-k retrieval settings and the diminishing returns of expanding retrieval depth beyond top-5. Top-20 vs. top-5 retrieval yielded only a net gain of 3 questions (11 gained, 8 lost), indicating it is a trade rather than a free improvement. Run-to-run variance is approximately ±3 questions, meaning the 96.0% vs. 95.6% comparison with Chronos is effectively a tie, though this run was optimized for token efficiency. The authors acknowledge that top-20 was selected after reviewing top-5 misses, so the 96.0% figure should be treated as tuned on this specific benchmark set.

reddit · r/MachineLearning · /u/remoteinspace · Nov 15, 05:40

**Background**: LongMemEval-S is a benchmark evaluating long-term memory capabilities of language models, consisting of 500 questions that test retrieval and reasoning over extended conversation histories. Prior reported results include Chronos at 95.6% using full context with multi-turn agents, Hindsight at 94.6% with 43.6k tokens per question under a different judge, and gbrain at 90.6%. The benchmark distinguishes between retrieval errors (failing to find relevant evidence) and reader errors (failing to correctly reason over retrieved evidence), making it useful for diagnosing where memory systems fall short.

**Tags**: `#long-context`, `#retrieval`, `#benchmark`, `#LLM-evaluation`, `#memory`

---

<a id="item-6"></a>
## [Should short-horizon price forecasting papers benchmark against market-implied forecasts, not just naive baselines? (D)](https://www.reddit.com/r/MachineLearning/comments/1xw6fk9/should_shorthorizon_price_forecasting_papers/) ⭐️ 6.0/10

A Reddit discussion questioning why short-horizon price forecasting papers benchmark against naive baselines rather than market-implied forecasts, and why they focus on point forecasts instead of interval coverage.

reddit · r/MachineLearning · /u/happypeanut-t · Nov 14, 16:23

**Tags**: `#time-series-forecasting`, `#evaluation-methodology`, `#financial-ml`, `#benchmarking`, `#price-prediction`

---