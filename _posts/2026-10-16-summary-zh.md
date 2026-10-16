---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 45 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [Citizen Lab 报告：定向广告被指用作零点击间谍软件投放通道](#item-tech-news-1) ⭐️ 8.0/10
2. [Libreboot 26.10 发布：加入 UEFI/EDK 支持与 233 款 Chromebook 移植](#item-tech-news-2) ⭐️ 8.0/10
3. [Meta 发布 816B 开放权重模型 Muse Spark Open](#item-tech-news-3) ⭐️ 7.0/10
4. [Nick Cammarata 称神经网络“干净”，引发可解释性争论](#item-tech-news-4) ⭐️ 7.0/10
5. [AI 数学进展为何令数学家感到不安](#item-tech-news-5) ⭐️ 7.0/10
6. [Anthropic IPO 前披露季度营收 168 亿美元，环比增近 50%](#item-tech-news-6) ⭐️ 7.0/10
7. [LPC 2026：Android 内核约 800 个厂商钩子，维护者寻求减少](#item-tech-news-7) ⭐️ 7.0/10
8. [Linux 发布七个稳定版内核，修复 skb\_checksum\_help\(\) 严重漏洞](#item-tech-news-8) ⭐️ 7.0/10
9. [库克称 Apple 智能 10 月底在华发测试版，不含 Siri AI](#item-tech-news-9) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Citizen Lab 报告：定向广告被指用作零点击间谍软件投放通道](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 8.0/10

公民实验室（Citizen Lab）的报告指控以色列公司 Discover Tech 将定向广告变成投放通道，用于向目标设备安装“零点击”雇佣兵间谍软件；该报告经 Hacker News 讨论及《卫报》《The Verge》报道扩散。报告对广告分发与命令控制（C2）环节有较具体描述，但没有清楚说明广告究竟通过何种机制触发恶意代码安装，因此“零点击”这一定性目前仍属研究方说法，缺乏可供独立核验的技术细节。对受影响用户与平台来说，触发机制与可问责主体这两个关键问题都尚未解决。

hackernews · jcomp · 10月15日 10:43 · [社区讨论](https://news.ycombinator.com/item?id=50101813)

**「背景」** 零点击攻击指不需要受害者点击链接或打开文件即可触发利用的攻击方式。Horizon 在 5 月 16 日的日报中曾报道 Google Project Zero 对 Pixel 10 一条零点击利用链的详细分析，其中指出 AI 功能会在用户交互前预处理消息与媒体，从而扩大攻击面，并强调即便修补速度很快，这类攻击仍是持续威胁。此次 Citizen Lab 的报告把这种攻击类型与广告投放环节联系起来，指控定向广告被用作了向目标设备投递雇佣间谍软件的通道，但报告对具体激活机制的说明仍不充分。

**「影响」** 由于报告未公开触发安装的具体机制，平台与安全团队目前难以据此制定针对性的检测或缓解措施；而讨论中一位广告技术从业者指出，广告技术生态里并不存在单一的“广告提供方”，这让事后追责与切断投放链路都更加困难。

**「社区讨论」** Hacker News 讨论中，一位自称从业 13 年的广告技术工程师认为报告在“零点击”这一点上相当耸动：它描述了分发与 C2，却对以零点击方式激活恶意代码的机制语焉不详，并反驳“应由广告提供方负责”的说法，称广告技术生态中并不存在单一的“广告提供方”。另有评论者主张干脆禁止整个在线广告行业，也有人据此质疑以色列网络安全公司是否可被视为独立可信的实体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">2026-05-16 — Pixel 10 0-click exploit chain detailed by Project Zero</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#spyware`, `#adtech`, `#privacy`, `#zero-click-exploit`

---

<a id="item-tech-news-2"></a>
### [Libreboot 26.10 发布：加入 UEFI/EDK 支持与 233 款 Chromebook 移植](https://libreboot.org/news/libreboot2610.html) ⭐️ 8.0/10

Libreboot 26.10（代号 “Ominous Olive”）发布，新增 UEFI/EDK 支持，并从 MrChromebox 的 coreboot 发行版导入 233 款当前受支持的 Chromebook 移植。据社区评论引述的发布说明，其中 Baytrail（Kip）已完成测试，其余设备仍需测试；本次 Chromebook 支持为 source-only，即必须从源码构建，发布时不提供二进制文件。发布中还包含一项针对 LLM 辅助贡献的严格政策，部分讨论者认为这是本次发布最重要的部分。

hackernews · iamnothere · 10月15日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=50102923)

**「背景」** Libreboot 是基于 coreboot 的自由开源引导固件，目标是在特定 Intel/AMD x86 与 ARM 主板上替换专有的 BIOS/UEFI 固件（tool-2-1）。coreboot 通过不同载荷提供启动环境：SeaBIOS 提供传统 PC BIOS 服务，edk2 提供 UEFI 服务，而 Chromebook 则使用定制引导器 depthcharge（tool-2-2、tool-2-3）。因此，Libreboot 引入 UEFI/EDK 与 Chromebook 支持，意味着它的固件栈开始覆盖此前由这些其他载荷和 Chromebook 引导路径所对应的设备类型。

**「影响」** 对 Chromebook 用户来说，此版本新增的 233 个机型支持目前仅有源码、不提供现成固件，必须自行从源码构建，且只有 Baytrail（Kip）经过测试，其余机型是否可用尚待验证，因此想刷机的人应预期自行承担构建与调试成本。UEFI/EDK 载荷的引入方式与 MrChromebox 用 edk2 充当现代 UEFI 引导载荷的做法一致，这意味着后续 Chromebook 机型移植可能更直接。

**「社区讨论」** 评论者 iamnothere 认为真正重要的是 UEFI/EDK 集成与 Chromebook 支持，称这让 Libreboot 可用设备数量成倍增加、未来移植更容易，而讨论热度却被 AI 政策占据。AdmiralAsshat 提醒这些 Chromebook 支持目前仅为源码形式且多数未测试，cwiggs 则报告 Heads 项目中已合入首个基于 MrChromebox 代码的 ChromeOS 移植 PR，第二、第三个移植正在进行；另有评论者对项目限制 LLM 辅助贡献的严格政策表示支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://libreboot.org/">Libreboot – Free and Open Source BIOS/ UEFI boot firmware</a></li>
<li><a href="https://doc.coreboot.org/">Welcome to the coreboot documentation — coreboot ...</a></li>
<li><a href="https://deepwiki.com/coreboot/coreboot/16-payloads-and-external-firmware">Payloads and External Firmware | coreboot / coreboot | DeepWiki</a></li>
<li><a href="https://mrchromebox.tech/">MrChromebox .tech</a></li>
<li><a href="https://doc.coreboot.org/distributions.html">Distributions — coreboot 26.06-1170-gb34a744391b documentation</a></li>

</ul>
</details>

**标签**: `#open-source firmware`, `#Libreboot`, `#UEFI`, `#Chromebooks`, `#coreboot`

---

<a id="item-tech-news-3"></a>
### [Meta 发布 816B 开放权重模型 Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) ⭐️ 7.0/10

Meta 发布了 Muse Spark Open，这是一个 816B 参数（模型名标注为 A42B）的开放权重模型，官方称其针对 Mac Studio 运行做了优化，并提供从 Unsloth 到 MLX 的多种推理器部署支持，模型权重与部署文档已上线 Hugging Face 和 dev.meta.ai。社区用户核对许可证后指出，该许可基本允许自由使用，但含 Model-as-a-Service 条款：若被许可方及其关联方通过 API 或类似接口向第三方提供模型输出，且合计毛收入超过两千万美元，则超出授权范围。性能评价并非来自 Meta 的宣称，而是社区引用的 Artificial Analysis 对比结果，称其落后于可在单张 B300 上运行的 Qwen3.8 Flash Next 与 GLM 5.3 Flash；有评论者提醒，这类榜单通常只覆盖最高推理档位，未必反映高并发生产场景。

hackernews · bigwheels · 10月15日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=50107379)

**「背景」** Muse Spark Open 属于开放权重（open-weight）模型：权重可下载后自行部署，但使用受许可证约束——其 Hugging Face 模型卡标注为 816B 总参数／42B 激活参数、100 万 token 上下文，采用 Meta 自有的 Muse Model License，而非 Apache 等标准开源许可。Horizon 2026 年 8 月 16 日的日报曾报道，阿里开放权重模型半年内下载量超过 30 亿次，同期 Meta 为 2.27 亿次、谷歌为 4.18 亿次，显示 Meta 在开放权重生态的采用度上此前落后于竞争对手。

**「对转售方与自托管者的实际约束」** 对想把该模型包装成 API 对外提供的团队来说，真正的门槛在许可而非权重：社区引用的条款显示，当使用方及其关联公司合计毛收入超过 2000 万美元时，以 API 或类似接口向第三方提供模型输出（Model-as-a-Service）将受到限制，这类厂商要么改为内部自用部署，要么继续选用其他开放模型。Meta 同时给出了从 Unsloth 到 MLX 的多运行器部署路径，自托管因而更容易落地，但 816B 参数规模仍要求 Mac Studio 级别的大显存硬件，且社区评论认为其表现不及 Qwen3.8 Flash Next、GLM 5.3 Flash 等可单机运行的竞品。

**「社区讨论」** 争论最集中的是许可性质：有评论者逐条核对后认为除 Model-as-a-Service 收入条款外基本可自由使用，而社区中另一部分观点认为这仍不算完全开源；a11r 引用 Artificial Analysis 认为 Muse Spark Open 不及 Qwen3.8 Flash Next 和 GLM 5.3 Flash，并抱怨该榜单只提供最高推理档位的比较。armcat 强调 Meta 在推理器适配上投入很大（从 Unsloth 到 MLX 皆可运行），simonw 则表示自己没有能承载该规模模型的机器，只能通过 OpenRouter 调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-15/alibaba-ai-models-hit-3-billion-downloads-passing-meta-google">2026-08-16 — 阿里开放权重模型下载量超 30 亿，超越 Meta 与谷歌</a></li>
<li><a href="https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B">meta- models / Muse - Spark - Open -816B-A42B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#open-weight LLM`, `#Meta`, `#model licensing`, `#Mac Studio inference`, `#AI community debate`

---

<a id="item-tech-news-4"></a>
### [Nick Cammarata 称神经网络“干净”，引发可解释性争论](https://already-clean.goodfire.com/) ⭐️ 7.0/10

Nick Cammarata 在 X 上发布并推广一项论证，主张神经网络比此前假设的更“干净”、更容易解释；他称自己曾在 OpenAI 参与机械可解释性早期研究，当时因网络看似混乱而持悲观态度，如今认为有好消息。该条目本身只提供指向这条推文的链接，未包含底层博客正文，因此其技术主张无法在现有材料中核实。Hacker News 上的讨论随即展开，核心争议在于这些结论是否超出了已有证据所能支持的范围。

hackernews · themgt · 10月15日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=50105647)

**「背景」** 在机制可解释性（mechanistic interpretability）领域，长期的主流悲观判断是：神经元之所以「多义」（polysemanticity），是因为模型以叠加（superposition）方式在有限维度中编码远超维度数量的特征，因此单个神经元很难对应单一可解释概念。Goodfire 的 Nick Cammarata 于 2026 年 10 月 15 日发表《Neural Networks Are Already Clean》，主张早期模型生物中多义性的成因并非叠加，而是若干普通且大多可修复的问题，并称现在已能理解参数量达万亿级模型中的大多数神经元。

**「影响」** 对机械可解释性研究者而言，这场争论的实际分歧在于：若多义性更多源于现有分析工具的失败而非网络的固有属性，研究方向就应从接受多义性转向改进工具；但现有材料未给出可核实的实验结果来支撑这一转向。

**「社区讨论」** 评论者 bluejay2387 认为该主张超出现有证明，指出渐进式特征复杂性和早期训练结构对后续训练的影响早已为人所知（如 CNN、彩票假说），且这些现象与参数重载并不互斥；aesthesia 则将其语气比作 Anthropic 机械可解释性团队在首批大规模 SAE 结果时期那种“轻躁狂”式的热情。antics 把这篇论述概括为一份旨在论证“给 AI 基因组测序”比想象中更容易的证据汇编。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/goodfire-neural-networks-are-already-clean-cammarata-neurons-interpretable-90-percent-qwen3-32b-2026">&quot;Neural Networks Are Already Clean&quot;: Goodfire&#x27;s Cammarata ...</a></li>
<li><a href="https://www.goodfire.com/research/already-clean">Neural Networks Are Already Clean - Goodfire</a></li>

</ul>
</details>

**标签**: `#mechanistic interpretability`, `#neural networks`, `#AI alignment`, `#polysemanticity`, `#AI safety`

---

<a id="item-tech-news-5"></a>
### [AI 数学进展为何令数学家感到不安](https://www.derekthompson.org/p/i-know-why-the-mathematicians-weep) ⭐️ 7.0/10

Derek Thompson 发表文章《I know why the mathematicians weep》，主张 AI 在数学领域的进展触动数学家的存在性与职业焦虑，因为其地位、声望和收入所依赖的能力可能被商品化。该文在 Hacker News 引发广泛辩论；现有材料表明这是一篇评论/分析，而非已验证的技术突破、模型发布或工程成果。由于源内容未提供，文中具体论证、案例和技术细节无法独立核对。

hackernews · RickJWagner · 10月15日 13:44 · [社区讨论](https://news.ycombinator.com/item?id=50103630)

**「背景」** Horizon 10 月 7 日的日报曾报道，OpenAI 发布“Sharing AI Progress in Mathematics”并公开 GitHub 仓库，其中包含声称证明 Barnette 猜想、以及解决 proofatlas.ai 前 500 个开放问题中 90 个的预印本，但这些均属未经独立验证的宣称（tool-1-1）。8 月 13 日的日报则记录了菲尔兹奖得主 Timothy Gowers 的判断：当前 LLM 更擅长采样式数学，而非人类式定理证明，更适合用作辅助工具（tool-1-2）；厂商宣称的快速进展与专家对能力边界的保留，构成了这篇随笔及其 Hacker News 讨论的直接背景。

**「影响」** 对数学研究者而言，最直接的后果是验证负担前移：已有论述指出 AI 已能以形式化与非形式化两种方式证明研究级定理，并据此建议数学家持续跟进该技术、正视其对数学实践方式的扰动（tool-3-1），这意味着从业者需要把更多精力投入校对、形式化与判定证明是否成立，而不能仅因结果被发布就予以接受。对外部宣称也应保持同样的核验标准：目前已有资料专门区分“已被证明”与“仅被声称”的 2026 年数学成果（tool-3-2），而个别报道所称 OpenAI 一夜解决 722 道数学题、证明“准黎曼假设”之类的说法（tool-3-3）尚属未经独立验证的声明，不宜直接当作已确立的能力结论使用。

**「社区讨论」** 有评论者认为，真正令人哀悼的不是岗位被替代，而是寻求真理的欲望与验证机制被削弱：AI 生成的论文和结论未经阅读、验证就被当作已解决。也有评论者借 Robert Brandom 的规范性实践理论指出，LLM 编码了语言中的规范规律，却可能在理由交换和概念系统的社会维持上有根本缺陷；另有评论者以中世纪织工行会衰落为类比，提醒被技术抛下的人未必得到历史善待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/sharing-ai-progress-in-mathematics/">2026-10-07 — OpenAI 发布数学 AI 进展，宣称证明多个开放问题</a></li>
<li><a href="https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/">2026-08-13 — 高尔斯：LLM 擅长采样式数学，而非人类式定理证明</a></li>
<li><a href="https://arxiv.org/html/2603.03684">Mathematicians in the Age of AI 1footnote 11footnote 1I am grateful to...</a></li>
<li><a href="https://felloai.com/ai-solved-math-problems/">AI Solved Math Problems: What Is Proven in 2026</a></li>
<li><a href="https://eu.36kr.com/en/p/4015128916676736">Mathematics Big Bang: OpenAI Solved 722 Complex Math Problems...</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#LLMs`, `#epistemology`, `#future of work`

---

<a id="item-tech-news-6"></a>
### [Anthropic IPO 前披露季度营收 168 亿美元，环比增近 50%](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 7.0/10

据英国《金融时报》报道，Anthropic 在周三面向投资者的活动中表示，其季度收入增长近 50% 至 168 亿美元，并给出逐季数据：第一季度约 48 亿美元、第二季度 115 亿美元、第三季度 168 亿美元。公司还称第三季度每在“算力”上花费 1 美元对应 1.70 美元收入，调整后营业利润率（不含股权激励）为 11%。Anthropic 同时告知投资者，“蒸馏”（竞争对手用其模型输出训练自家模型）占收入 5% 至 7%，并已在第三季度“大幅”削减相关用量。上述数字均来自 FT 援引的匿名知情人士，属二手信息，Anthropic 并未公开确认。

rss · Simon Willison · 10月15日 13:04

**「背景」** Horizon 5 月 30 日的日报曾报道，Anthropic 在 5 月披露其年化 run-rate 收入超过 470 亿美元（此前到 2025 年底为 90 亿美元），当时公司仍以年化口径对外沟通；而本次向投资者披露则改用季度实际收入（约 48 亿、115 亿、168 亿美元），Simon Willison 也注意到 Anthropic 似乎不再使用年化 run-rate 的说法。Horizon 5 月 29 日的日报还报道了该公司 650 亿美元 Series H 融资与 9650 亿美元投后估值，这为当前披露 IPO 意向提供了前情。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/29/anthropic/#atom-everything">2026-05-30 — Anthropic run-rate revenue reaches $47 billion</a></li>
<li><a href="https://www.anthropic.com/news/series-h">2026-05-29 — Anthropic raises $65B in Series H at $965B valuation</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#Anthropic`, `#business/financials`, `#IPO`, `#model distillation`

---

<a id="item-tech-news-7"></a>
### [LPC 2026：Android 内核约 800 个厂商钩子，维护者寻求减少](https://lwn.net/Articles/1098493/) ⭐️ 7.0/10

在 2026 年 Linux Plumbers Conference 的 Android 专场中，Todd Kjos 介绍了 Android 内核的 vendor hook（厂商钩子）机制：它本质上是加在 Android 内核里的专用 tracepoint，厂商设备加载内核模块挂接到该 tracepoint，即可拦截控制流、修改数据结构甚至短路主线代码。他给出的数字是，当前使用最广的 Android 6.6 内核带有 3,100 多个树外补丁，其中 1,531 个是新内核特性的回移、287 个是已在邮件列表讨论但尚未进入主线的改动，剩余 1,306 个（约 42%）为“纯 Android”改动，其中三分之一以上是厂商钩子；内核中厂商钩子总数约 800 个，近一半位于内存管理子系统与 CPU 调度器。Kjos 说采用厂商钩子的主要原因是紧迫性——上游流程太慢——加上有些硬件没有上游驱动，而 Android 维护者自认缺乏判断所有改动是否必要的专业能力，因此对新增钩子采取宽松政策，同时表示希望减少这一数量。这是会议演讲的总结，并非内核功能发布或已生效的代码变更。

rss · LWN.net · 10月15日 15:09

**「背景：GKI 与 vendor hook 机制」** Android 设备使用的内核长期与 Linux 主线存在大量分叉，Google 推出的通用内核镜像（GKI）试图统一内核核心，让厂商的差异化代码只能以 vendor hook 的形式加入。vendor hook 本质上是加进 Android 内核的特殊 tracepoint（形如 trace\_android\_vh\_…），厂商设备加载相应的内核模块挂载到该 tracepoint 上，即可修改数据结构、注入代码或短路主线逻辑，因此厂商可以在不干扰他人的前提下加入自己的改动。正因如此，Todd Kjos 在 2026 年 Linux Plumbers Conference 上讨论的正是这套机制的使用现状与管理难题，包括内核中约 800 个 vendor hook 该如何削减。

**「影响」** 对内核与 Android 平台开发者来说，最直接的技术约束是：Android 试图为这些钩子维持稳定 ABI，Kjos 明确表示这经常限制钩子所在代码路径能做的改动，意味着在被大量钩子覆盖的调度器和内存管理区域，主线与小版本变更都需考虑厂商模块的兼容性。现场讨论也显示这一局面短期难解：Kjos 一方面说 sched\_ext 现已在 Android 内核中得到支持，另一方面承认 sched\_ext 基础设施又被加上了厂商钩子，他宁可保留现有钩子也不愿转向完全树外的调度器实现。

**标签**: `#Android kernel`, `#Linux kernel`, `#vendor hooks`, `#Linux Plumbers Conference`, `#open source`

---

<a id="item-tech-news-8"></a>
### [Linux 发布七个稳定版内核，修复 skb\_checksum\_help\(\) 严重漏洞](https://lwn.net/Articles/1100611/) ⭐️ 7.0/10

Greg Kroah-Hartman 发布了 7.2.11、6.18.57、6.12.113、6.6.159、6.1.190、5.15.223 和 5.10.272 七个稳定版内核，均包含对 CVE-2026-99999 的修复。该漏洞位于 skb\_checksum\_help\(\)，补丁作者 Michael S. Tsirkin 称，带有错误校验和元数据的 IPv4 数据包可能“破坏网络头并造成一系列麻烦”。LWN 表示这一系列发布还包含其他改动，并按惯例建议所有用户升级。目前可确认的只是该修复已进入这些稳定版内核，来源摘要未提供更多技术细节，也没有独立的漏洞验证结果。

rss · LWN.net · 10月15日 13:01

**「背景」** Linux 稳定内核由 Greg Kroah-Hartman 维护，安全修复通常在同一天回合并发到多条长期维护分支（5.10、5.15、6.1、6.6、6.12、6.18、7.2）。Horizon 8 月 29 日的日报曾报道同一模式：八个稳定内核（最高到 7.2.2、5.10.268）各自包含对 CVE-2026-80590 的修复，该漏洞允许非特权用户把 IPv4/IPv6 分片标记为 GSO 而触发内核崩溃；本次则是同一组分支的版本号继续推进，修复对象换成 CVE-2026-99999。Horizon 8 月 17 日的日报还记录了 7.2 主线版本本身的发布，本次的 7.2.11 属于该分支的后续稳定更新。

**「受影响用户需要做什么」** 对运行受影响分支的运维者而言，修复已同时落入 7.2.11、6.18.57、6.12.113、6.6.159、6.1.190、5.15.223 和 5.10.272，因此仍停留在 5.10、5.15 等长期支持线上的系统无需跳到 7.2.x 即可获得 CVE-2026-99999 的补丁。CVE 记录确认进入 IPv4 栈的畸形校验和元数据会让 skb\_checksum\_help\(\) 破坏网络头，所以早于上述版本的内核仍然暴露，升级应及时执行而非推迟到常规维护窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1091118/">2026-08-29 — 八个稳定内核版本修复可致内核崩溃的漏洞</a></li>
<li><a href="https://lwn.net/Articles/1088991/">2026-08-17 — Linux 内核 7.2 发布：引入 BPF、调度器及文件系统多项改进</a></li>
<li>CVE-2026-99999 - CVE Record</li>
<li>CVE-2026-99999: In the Linux kernel, the following vulnerability has been resolved: ipv4: validate checksum_start before completing… - Rapid7</li>

</ul>
</details>

**标签**: `#linux-kernel`, `#security`, `#cve`, `#stable-releases`, `#networking`

---

<a id="item-tech-news-9"></a>
### [库克称 Apple 智能 10 月底在华发测试版，不含 Siri AI](https://jiemian.com/article/15194723.html) ⭐️ 7.0/10

10 月 15 日，苹果董事会执行主席蒂姆·库克在上海受访时称，Apple 智能（Apple Intelligence）与阿里千问大模型已获批准，将于 10 月晚些时候在中国发布测试版。首批功能包括实时翻译、书写工具和照片清除工具，但 Siri AI 此次不在其中。这一说法来自界面新闻经 Telegram 频道转述的报道，属库克的公开宣布而非已落地的正式版能力，具体上线日期、覆盖机型范围、审批主体及后续功能排期在现有材料中均未给出。

telegram · zaihuapd · 10月15日 08:59

**「背景」** 8 月 15 日的 Horizon 日报曾报道，苹果已专门为中国市场训练大语言模型并获阿里巴巴支持，中国网信办也已备案其生成式 AI 服务，若落地苹果将成为首家获准在华提供自有 AI 模型的外企，但当时消息基于未具名消息源、缺乏技术细节。TechCrunch 7 月 16 日的报道同样称 Apple Intelligence 已获批与阿里、百度一同在中国上线。相比之下，此次由库克亲自确认审批通过并给出 10 月底测试版的时间表，且明确首批功能不含 Siri AI。

**「对中国用户的影响」** 对国行用户而言，10 月底上线的只是测试版且不含 Siri AI，苹果 9 月发布、随 iPhone Duo 一同提供的 Apple Intelligence 2 与 Siri AI 暂无法在中国大陆使用，想获得完整体验需等待后续版本。另有报道称中国版采用“千问直接接入系统、再共建中国定制模型”的两层方案（tool-3-1），这意味着其模型栈与海外版并不一致，参与测试的用户应对功能与回答表现的差异有所预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/">2026-08-15 — 苹果联手阿里为中国训练专属 AI 大模型，有望成首个获批外企</a></li>
<li>Apple Intelligence approved for launch in China with Alibaba and Baidu - TechCrunch</li>
<li><a href="https://post.smzdm.com/p/agg4knn6/">等了两年， 国 行 Apple Intelligence ...</a></li>
<li><a href="https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/">Apple today introduced iPhone Duo, the first foldable iPhone.</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#阿里千问`, `#AI 在中国`, `#Siri`, `#科技监管`

---