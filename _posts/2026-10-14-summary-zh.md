---
layout: default
title: "Horizon Summary: 2026-10-14 (ZH)"
date: 2026-10-14
lang: zh
---

> 从 51 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [谷歌 DeepMind 发布 Gemini 4 Argon 大模型](#item-tech-news-1) ⭐️ 8.0/10
2. [Anthropic 重新设计 monorepo 源代码控制](#item-tech-news-2) ⭐️ 8.0/10
3. [Google 发布 Gemini 4 Argon 机器人模型](#item-tech-news-3) ⭐️ 8.0/10
4. [长鑫存储称年底前推出 4F² 数据中心内存，或领先三星与海力士](#item-tech-news-4) ⭐️ 8.0/10
5. [Apple 推出 HomeView 家用设备，主打 A18 Secure Exclaves](#item-tech-news-5) ⭐️ 7.0/10
6. [Rust 借用检查器曝出 11 年前的不健全性缺陷](#item-tech-news-6) ⭐️ 7.0/10
7. [将 EmbeddingGemma 2 改造成语音转文字模型](#item-tech-news-7) ⭐️ 7.0/10
8. [Character.ai 申请第 11 章破产并拟向迪士尼出售部分资产](#item-tech-news-8) ⭐️ 7.0/10
9. [Nix 与 Lix 披露本地提权漏洞并发布修复版本](#item-tech-news-9) ⭐️ 7.0/10
10. [Rust for Linux 提出 Ownable trait 管理 C 分配对象](#item-tech-news-10) ⭐️ 7.0/10
11. [PostgreSQL 19 测试期多项功能被撤回，核心成员归因于 LLM 辅助审查](#item-tech-news-11) ⭐️ 7.0/10
12. [Asterinas 0.19.0 发布：新增可运行 X.org 的图形子系统](#item-tech-news-12) ⭐️ 7.0/10

**科技博客**
1. [从傅里叶热学到 LLM 位置编码](#item-tech-blog-1) ⭐️ 6.0/10

**财经新闻**
1. [香港证监会暂停茶百道交易，指其 IPO 涉嫌被操纵](#item-finance-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [谷歌 DeepMind 发布 Gemini 4 Argon 大模型](https://deepmind.google/models/gemini/) ⭐️ 8.0/10

谷歌 DeepMind 发布了新的大语言模型 Gemini 4 Argon，Hacker News 上的相关讨论获得 918 分、705 条评论。来源条目本身没有提供官方基准、版本号细节或模型规模，因此目前可确证的是发布这一事实，具体能力描述主要来自用户的主观体验。多名评论者称其在写作质量和回答结构上有明显提升，也有人反馈官网的试用入口存在落差：点击 Gemini 4 页面的“Try in Gemini”后默认进入的是 Gemini 3.6，且没有不升级即可试用 Gemini 4 的选项。

hackernews · 737max · 10月13日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=50073879)

**「背景」** Horizon 10 月 1 日的日报曾报道，谷歌在官方博客发布 Gemini 4 Argon，并指出当时该模型只面向早期测试者，尚未向开发者、企业和消费者开放，且公告材料中没有模型规格、基准成绩或定价信息（tool-1-1）。与那次报道相比，本次 Hacker News 讨论中的评论者已表示正通过 API 使用该模型，也有人描述在 Gemini 页面和订阅流程中尝试访问时遇到的限制，这暗示访问范围至少部分扩大，但这些都只是用户个人描述，并非官方确认。第三方整理帖称 Argon 于 2026 年 9 月 30 日发布，支持最高 100 万 token 输出，定价为每百万输入 token 2 美元、每百万输出 token 10 美元，此类数字尚待官方或独立验证（tool-2-3）。

**「影响」** 对想尝试新模型的用户来说，当前的直接障碍在访问与付费路径而非模型能力：有评论者称从 Gemini 4 介绍页进入后只得到默认的 Gemini 3.6 页面，另有用户表示注册 Google 账号后既找不到明确的入口，又无法用信用卡或 PayPal 购买小型 Gemini AI Ultra 套餐；相比之下，已有开发者表示可以通过 API 直接调用该模型。

**「社区讨论」** 正面反馈集中在文本能力上，有评论者认为它回答直击要点、逻辑清晰，并倾向于生成可调参数的模拟与模型，也有通过 API 使用的开发者特别称赞其语言表达，认为这比常见的图像渲染演示更能体现模型水平。批评则集中在 Google 的试用和购买流程上，一位评论者称点击“Try in Gemini”后被引导到 Gemini 3.6 并提示升级，认为这种引导与“可试用”的暗示不符——这些均为个人体验陈述，尚无官方说明佐证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">2026-10-01 — 谷歌发布 Gemini 4 Argon，暂限早期测试者</a></li>
<li><a href="https://datanorth.ai/news/google-releases-gemini-4-argon">Gemini 4 Argon : Google &#x27;s 1M output token model | DataNorth AI</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#large language models`, `#Google DeepMind`, `#Gemini`, `#model release`

---

<a id="item-tech-news-2"></a>
### [Anthropic 重新设计 monorepo 源代码控制](https://www.anthropic.com/engineering/redesigning-source-control) ⭐️ 8.0/10

Anthropic 在其工程博客中介绍，为内部大型 monorepo 重新设计了源代码控制，核心是把 Git 历史摄取到 Scion 的管道，并借助 AI 辅助完成大规模代码迁移。这是一篇关于内部开发基础设施的工程披露，而不是面向外部用户的产品发布；根据现有材料，Scion 的版本、开源计划和对外可用性均未说明。

hackernews · Philpax · 10月13日 15:49 · [社区讨论](https://news.ycombinator.com/item?id=50073633)

**「背景」** Anthropic 的 monorepo 规模被认为已超出 Git 原本的设计空间：社区评论引用原帖称，仅主分支的历史就接近 100 GB，这使合并与仓库管理本身成为需要重新设计的对象，工程团队因此搭建了从 Git 向 Scion 摄取（ingestion）的流水线，并用 Scion 承载该仓库。评论者将其类比为 SVN/Perforce 式的服务端版本控制系统，并指出它目前没有公司外部的生产使用、不支持非文本资产，且 Anthropic 未公布会开源相关代码——这些是社区基于文章的推断，而非已公开验证的能力。

**「社区讨论」** 评论区的一条争论是 zmmmmm 质疑是否应先重新考虑 monorepo 策略，而不是直接从 monorepo 走向重新设计版本控制。trnvll 引述博客称，Claude Mythos Preview 重写 Git-to-Scion 摄取管道后内存占用降至 1/20、速度提升 4 倍；tancop 则把 Scion 类比为 SVN/Perforce 式服务器端 VCS 和 Epic 的 Lore，并指出它未对外发布、不支持非文本资产。

**标签**: `#source control`, `#monorepo`, `#developer infrastructure`, `#AI-assisted coding`, `#Git`

---

<a id="item-tech-news-3"></a>
### [Google 发布 Gemini 4 Argon 机器人模型](https://developers.googleblog.com/gemini-4-argon-for-robotics/) ⭐️ 8.0/10

Google 开发者博客宣布推出 Gemini 4 Argon，定位为面向机器人/具身 AI 的模型，用于以视觉和语言控制机器人动作。Hacker News 上的讨论显示，已有开发者在实际机器人上尝试零样本视觉控制和动作原语，即让通用 LLM 通过一组预定义动作来指挥机器人。所提供的材料没有给出模型规格、支持的机器人平台、价格或可用地区等细节，这些方面仍不明确。

hackernews · xnx · 10月13日 16:55 · [社区讨论](https://news.ycombinator.com/item?id=50074869)

**「背景」** Google DeepMind 在机器人模型上已有前代积累：Gemini Robotics 系列包含负责具身推理的 Gemini Robotics-ER，以及可在机器人本地硬件上运行的轻量 VLA 版本 On-Device（tool-2-1）。Horizon 2026 年 7 月 31 日的日报曾报道 Gemini Robotics 2 主打全身智能，但演示中的成功率约 60%、准确率约 80%，当时尚未达到生产就绪水平（tool-1-1）。本次 Gemini 4 Argon 可视为这一路线在 Gemini 4 世代上的延续；Hacker News 评论者指出，目前常见做法是让通用大模型通过一组预定义的动作原语来指挥机器人，而不是端到端直接输出电机指令。

**「影响」** 对机器人开发者而言，这条路线可能把集成重点从为每个任务训练专用策略转向设计安全的动作原语和视觉接入；评论者报告 Argon 4 在其 Unitree 人形机器人上比 Opus/Astra 更会避免撞墙，但同一实践也指出 LIDAR 数据尚未接入，说明感知冗余与安全约束仍需自行处理。该后果基于社区实践描述，并非独立验证。

**「社区讨论」** 有评论者报告在 Unitree 人形机器人上做实验：此前用 Opus 和 Astra 会撞上桌子、床和表面，而 Argon 4 更谨慎地避开墙壁和物体；该评论同时承认尚未使用 LIDAR 数据。另一位开发者把“视觉外设 + 动作原语”的零样本控制视为值得关注的做法，但也有评论质疑现有模型的功耗和推理速度离机器人在非校车大小的平台上长时间自主运行还很远。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">2026-07-31 — Gemini Robotics 2 为机器人带来全身智能</a></li>
<li><a href="https://deepmind.google/models/gemini-robotics/">Gemini Robotics — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#AI`, `#robotics`, `#Gemini`, `#embodied AI`, `#LLM control`

---

<a id="item-tech-news-4"></a>
### [长鑫存储称年底前推出 4F² 数据中心内存，或领先三星与海力士](https://www.bloomberg.com/news/articles/2026-10-13/china-s-cxmt-claims-memory-breakthrough-ahead-of-samsung-hynix) ⭐️ 8.0/10

长鑫存储总裁曹堪宇在上海一场行业会议上称，公司计划在年底前推出采用 4F² 设计的数据中心服务器内存芯片，若成功将先于三星和 SK 海力士实现这一设计突破。消息引发芯片股抛售，三星与 SK 海力士周二在韩国市场下跌逾 7%，美光隔夜下跌 4%。分析人士提醒，从产品发布到可盈利量产之间仍存在时间差，且目前公开信息中缺少具体技术细节。Counterpoint 数据显示，长鑫存储今年二季度 DRAM 市场份额升至 10%，去年同期为 4%。

telegram · zaihuapd · 10月13日 05:38

**「背景」** 4F² 指把 DRAM 存储单元面积压缩到 4F² 的单元布局，通常与垂直栅极（vertical gate）结构相关；TrendForce 报道称三星（B1b 工艺，据称改名 D0a）与 SK 海力士也在推进各自的 4F² 方案，因此长鑫存储宣称的“领先”首先是时间点上的竞赛。Horizon 9 月 21 日的日报曾报道，长鑫科技在 2026 世界制造业大会上宣布第五代技术平台量产、24 GB LPDDR5X 已进入国产旗舰手机，但同样只有厂商宣布而缺少独立验证；本次的新内容是把 4F² 设计用于数据中心服务器内存，且仍是年底前推出的计划。

**「影响」** 对数据中心采购方和 DRAM 买家而言，直接后果是供应来源可能增加一个具备 4F² 设计的选项，但公司宣称不等于可盈利量产，分析人士已提示发布与量产之间的时间差，因此短期内不宜据此调整采购或产能规划；同时三星、SK 海力士与美光股价的明显下跌，反映出市场对现有厂商份额被侵蚀的即时担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.thepaper.cn/newsDetail_forward_34108116">2026-09-21 — 长鑫科技宣布第五代 DRAM 平台量产</a></li>
<li><a href="https://www.trendforce.com/news/2026/10/12/news-cxmt-accelerates-4f%C2%B2-dram-push-eyes-year-end-server-ddr5-rdimm-launch/">[News] CXMT Accelerates 4F² DRAM Push, Eyes Year-End Server ...</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#长鑫存储\(CXMT\)`, `#4F² 内存设计`, `#数据中心内存`, `#半导体行业`

---

<a id="item-tech-news-5"></a>
### [Apple 推出 HomeView 家用设备，主打 A18 Secure Exclaves](https://www.apple.com/apple-homeview/) ⭐️ 7.0/10

Apple 发布了名为 HomeView 的家用设备，其 A18 芯片包含 Secure Exclaves，按产品描述，摄像头与麦克风的数据在一个操作系统和 Apple 都无法访问的隔离区内处理，使设备能在不向系统暴露音视频数据的情况下识别人脸与语音。该设备不提供 App Store 访问。上述处理方式目前来自产品页面的描述，尚无独立验证；我掌握的资料中没有价格、上市时间和地区可用性信息。

hackernews · etothet · 10月13日 13:02 · [社区讨论](https://news.ycombinator.com/item?id=50071017)

**「背景」** HomeView 所强调的 Secure Exclaves 并非全新机制：据相关报道，苹果最早随 M4 版 iPad Pro 引入这一隐私隔离特性，随后将其带到搭载 A18 芯片的 iPhone 16。按 HomeView 产品页的说明，其内置的 A18 芯片正是用 Secure Exclaves 把摄像头与麦克风数据放在操作系统和苹果都无法访问的隔离区域中处理，以便在不向系统暴露音视频素材的前提下识别人脸与声音。此外，苹果的 “Welcome Home” 活动还介绍了可与 Apple Home 生态衔接的安防摄像头、智能门锁、可视门铃与恒温器等设备类别。

**「影响」** 对用户和第三方开发者而言，最直接的约束是这台设备只能运行 Apple 内置的功能：没有 App Store 意味着开发者无法为其发布应用，用户也无法像使用 iPad 那样通过安装第三方应用来扩展用途。潜在买家的取舍因此取决于设备自带功能是否覆盖其日常使用场景。

**「社区讨论」** 评论中一个主要观点认为 HomeView 最大的竞争对手是“旧 iPad”：schmichael 列举旧 iPad 有电池可脱离电源线、能装应用、且有大量第三方支架与挂墙配件。Brendinooo 表示，如果没有“足够完整”的 App Store 访问权限自己就不会购买，因为他家的通话和音乐播放都依赖 Messenger、Snapchat、Plexamp 等第三方应用；fmarasho 则对 Secure Exclaves 的隔离处理方式表示感兴趣。以上均为评论者的个人看法，不构成共识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/apple-homeview/">Apple HomeView - Apple</a></li>
<li><a href="https://www.mymobileindia.com/apple-brings-new-privacy-feature-secure-exclave-from-m4-ipad-pro-to-iphone-16-with-a18-chip/">Apple Brings New Privacy Feature &#x27; Secure Exclave &#x27; From M4 iPad...</a></li>
<li><a href="https://www.youtube.com/post/UgkxpMpv8PEILpsn6f5Nn0eGRCN4g_6apd8C">Here is a recap of Apple ’s &quot;Welcome Home &quot; event where... - YouTube</a></li>

</ul>
</details>

**标签**: `#Apple hardware`, `#smart home`, `#secure enclave`, `#on-device privacy`, `#platform ecosystem`

---

<a id="item-tech-news-6"></a>
### [Rust 借用检查器曝出 11 年前的不健全性缺陷](https://github.com/rust-lang/rust/issues/164250) ⭐️ 7.0/10

一个 Rust 编译器 GitHub issue（\#164250）报告借用检查器存在已持续约 11 年的不健全性缺陷：编译器接受了一段按 Rust 生命周期规则本应被拒绝的代码。该问题目前处于被报告和讨论的阶段，尚无证据表明官方已发布修复或已确认受影响的 crate 清单。评论者认为这不是类型系统本身的问题，修复方向是让编译器按既有生命周期规则拒绝该代码，因此相对直接，但该缺陷是否影响真实代码仍待确认。

hackernews · formerly\_proven · 10月13日 10:27 · [社区讨论](https://news.ycombinator.com/item?id=50069499)

**「背景」** Rust 的借用检查器（borrow checker）是编译器在编译期执行所有权与生命周期规则的组件；“不可靠性”（unsoundness）指编译器接受了按类型系统规则本应被拒绝的代码，从而使安全代码可能触发未定义行为。Rust 仓库此前就出现过借用检查器不可靠性的报告，例如涉及 union 的 issue \#45157（tool-2-1），说明这类问题并非首次出现。

**「对 Rust 用户的实际影响」** 对 Rust 使用者而言，这个不健全性意味着编译器接受了一段按 Rust 生命周期规则本应被拒绝的代码；对 rustc 缺陷的实证研究指出，这类编译器 bug 会削弱 Rust 的内存安全保证（tool-3-3）。当程序需要运行不可信或可能带有恶意意图的代码时，编译器层面的不健全性会成为直接的漏洞与阻碍（tool-3-1）。由于修复方向是让编译器改为拒绝该代码，兼容性关注点在于是否会导致现有 crate 编译失败——评论者明确提出这一点，但目前尚无证据表明实际受影响的代码范围。

**「社区讨论」** 评论者 GrantMoyer 认为该 bug 容易修，因为它只涉及编译器未按既有生命周期规则拒绝代码，而非类型系统规则有误；weinzierl 补充称 Rust 仓库目前有 100 多个 unsound 标签 issue，新的 trait solver 可能为其中部分修复解除阻碍，但不一定包括本案。Eridrus 则质疑这类问题是否真正影响实际代码，并关注修复后是否会导致某些 crate 无法编译。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rust-lang/rust/issues/45157">Borrow checker unsoundness with unions · Issue #45157...</a></li>
<li>Soundness Concern - help - The Rust Programming Language Forum</li>
<li>An Empirical Study of Rust-Specific Bugs in the rustc Compiler - arXiv</li>

</ul>
</details>

**标签**: `#Rust`, `#borrow checker`, `#compiler soundness`, `#programming languages`, `#open source`

---

<a id="item-tech-news-7"></a>
### [将 EmbeddingGemma 2 改造成语音转文字模型](https://eg2.haku.sh/) ⭐️ 7.0/10

一位开发者把 EmbeddingGemma 2 改造成语音转文字模型，做法是利用该模型中文本与音频共享同一向量空间，将音频映射到文本表示。创作者在 Hacker News 评论中表示，这个实验“能跑通”，准确率不错但低于云端模型，日常使用尚可，速度提升只是附带结果，并非最初目标。该实验并非正式发布的产品，给定材料未说明模型权重、代码或使用条件是否公开。

hackernews · amrrs · 10月13日 11:27 · [社区讨论](https://news.ycombinator.com/item?id=50069971)

**「背景」** EmbeddingGemma 2 是 Google DeepMind 发布的 740M 参数开放权重多模态嵌入模型，可将文本、代码、图像、视频帧与音频映射到同一个向量空间，主要用于本地隐私检索与多模态搜索，Horizon 10 月 8 日的日报曾报道其发布及配套的端侧演示（tool-1-3）。该模型本身面向嵌入与检索而非语音识别，因此这次实验的切入点正是它“文本与音频共享同一向量空间”这一特性：作者借此把音频表示直接对应到文本，从而在没有专门 ASR 架构的情况下完成转写（tool-2-1）。

**「对本地 ASR 开发者的实际影响」** 对想在本地跑语音转文字的开发者来说，这个实验提供了一条省去单独训练 ASR 模型的路径——直接复用 EmbeddingGemma 2 中文音频共享的向量空间；但作者本人说明准确率虽可用于日常，仍低于云端模型，因此对准确率敏感的场景目前仍要依赖云端或专用 ASR 模型。若要追求本地速度，社区建议把模型转成 CoreML 以便在 Apple 神经引擎上运行（whstl），而针对 Mac 的本地转写对比也显示，在 M 系列芯片上跑在神经引擎上的 Parakeet 比 Whisper 更快，是可先试的现成替代方案。

**「社区讨论」** 评论中的实用讨论集中在本地 ASR 加速与替代方案：有人建议把这类模型转成 CoreML 以在 macOS 神经引擎上运行，并称自己在多个音频/模型转换上有类似成功经验；另有用户报告在旧款 M1 MacBook Air 上用 Parakeet v3 配合 MacWhisper 转录“快得以为失败了”，以及 Apple 端上转录模型在自己的电脑上比官方报告结果慢约 3 倍、但错误率相近。这些均为用户个人报告，不是对模型性能的独立评测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/google-ai-edge-with-embeddinggemma-2/">2026-10-08 — Google 发布 740M 参数开放权重模型 EmbeddingGemma 2</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2026/10/embeddinggemma-2-multimodal-embeddings-guide/">EmbeddingGemma 2 : Google&#x27;s Open Multimodal Model</a></li>
<li><a href="https://localaimaster.com/blog/best-speech-to-text-mac">Fastest Local Speech -to-Text on a Mac : 3 Compared</a></li>
<li><a href="https://metawhisp.com/blog/parakeet-vs-whisper-mac/">Parakeet vs Whisper on Mac : Speed vs Coverage — MetaWhisp</a></li>

</ul>
</details>

**标签**: `#EmbeddingGemma 2`, `#speech-to-text`, `#ASR`, `#local-inference`, `#multimodal-embeddings`

---

<a id="item-tech-news-8"></a>
### [Character.ai 申请第 11 章破产并拟向迪士尼出售部分资产](https://blog.character.ai/an-update-on-character-ai/) ⭐️ 7.0/10

根据 10 月 13 日提交的一组报道链接，Character.ai 已启动自愿第 11 章破产程序，并同意将部分资产出售给迪士尼；路透社的标题把这项资产交易标注为 2000 万美元。原始提交只是 The Verge、TechCrunch、路透社和 Variety 的链接聚合，没有给出资产范围、交易结构、债权人处置或服务是否继续运营等细节，因此上述内容属于媒体标题层面的报道，而非已核实的完整方案。Character.ai 官方博客同日发布了关于此事的更新。

hackernews · nryoo · 10月13日 07:28 · [社区讨论](https://news.ycombinator.com/item?id=50068036)

**「背景」** Horizon 2026 年 6 月 19 日的日报曾报道，Character.AI 联合创始人 Noam Shazeer 于 2021 年离开 Google 创办该公司，后于 2024 年回到 Google，本次申请破产的是那笔交易之后留下的公司实体。第 11 章破产是美国破产法下的法院监督程序，公司可在此框架下继续运营并推进资产出售；Character.AI 在公告中称发起这一程序是为了促成法院监督下的公司出售。

**「影响」** 路透社标题显示，Character.ai 在申请第 11 章破产的同时同意以 2000 万美元向迪士尼出售部分资产，而评论中引用的公司博客称 CEO Karandeep Anand 将赴迪士尼任职并预期带走部分技术团队成员。对平台用户和依赖该平台发布角色的创作者来说，实际后果是账号数据与服务的归属要由破产程序中的资产出售结果决定，因此在资产交割细节公布前，不宜假定现有服务和角色内容会原样延续。

**「社区讨论」** 评论区的主流论点（如 fra、drewbitt）认为，Character.ai 实际上在 2024 年就已通过谷歌以约 27 亿美元挖走创始团队 Noam Shazeer、Daniel De Freitas 的方式被“收购”，如今申请破产的只是留下的公司空壳，受影响的是被留下的员工。另有评论（andsoitis）引用公司博客称 CEO Karandeep Anand 将加入迪士尼出任新设的高级执行副总裁兼 CTO，并带走部分技术团队成员；这些属于评论者陈述的观点与引述，并非本条目自身的独立确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://twitter.com/NoamShazeer/status/2067400851438932297">2026-06-19 — Noam Shazeer, Transformer Co-Author, Leaves Google for OpenAI</a></li>
<li><a href="https://blog.character.ai/an-update-on-character-ai/">An Update on Character . ai</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#generative AI`, `#bankruptcy/M&amp;A`, `#startup economics`, `#Character.ai`

---

<a id="item-tech-news-9"></a>
### [Nix 与 Lix 披露本地提权漏洞并发布修复版本](https://lwn.net/Articles/1100247/) ⭐️ 7.0/10

Nix 和 Lix 项目联合披露了一组本地权限提升漏洞，可用于在运行 Lix 或 Nix 守护进程的系统上将权限提升至 root。公告称“所有构建不可信 derivation 的系统均受影响”，但未提供 CVE 编号（称尚未申请），也未披露漏洞的技术细节。两个项目表示修复版本已在公告发布当天提供，来源未说明具体版本号。

rss · LWN.net · 10月13日 16:13

**「背景」** 官方把问题定位在 Nix 与 Lix 各自的守护进程实现上，oss-security 邮件列表上的通告同样将其描述为「守护进程中的本地权限提升」，并提示读者查阅受影响版本、修复版本与缓解措施（tool-2-2、tool-2-3）。受影响条件的表述是「所有构建不可信 derivation 的系统」，说明风险出现在守护进程以特权身份处理来自不可信构建的输入这一环节，而本次是两个项目联合发布的同一份通告。

**「影响」** 对多用户安装而言，Nix 守护进程以 root 身份运行，而 allowed-users 的默认值为 \`\*\`，即本机任何用户都能连接该守护进程，NixOS 与标准多用户安装均沿用这一默认配置，因此受影响面较广。尚未修复的部署应尽快升级到各项目发布的修复版本；无法立即升级时，收紧 allowed-users 并避免构建不受信任的 derivation 可缩小暴露范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openwall.com/lists/oss-security/2026/05/04/32">oss-security - Nix / Lix : local privilege escalation in daemon process</a></li>
<li><a href="https://seclists.org/oss-sec/2026/q2/401">oss-sec: Nix / Lix : local privilege escalation in daemon process</a></li>
<li><a href="https://zeropath.com/blog/cve-2026-44028-nix-lix-nar-parser-stack-overflow">Brief Summary: CVE- 2026 -44028 Local Privilege Escalation in Nix ...</a></li>

</ul>
</details>

**标签**: `#Nix`, `#Lix`, `#security vulnerability`, `#privilege escalation`, `#open source`

---

<a id="item-tech-news-10"></a>
### [Rust for Linux 提出 Ownable trait 管理 C 分配对象](https://lwn.net/Articles/1099015/) ⭐️ 7.0/10

在 Kangrejos 2026 上，Andreas Hindborg 介绍了 Rust for Linux 的一个补丁系列（邮件列表中的 v21 版本，2026 年 9 月发布），它新增 Ownable trait 和 Owned 智能指针，让 Rust 代码可以持有由 C 代码分配的对象，并在使用完毕后负责清理（但不一定释放内存）。Owned 像 KBox 一样提供对所指值的唯一访问，但生命期结束时调用 release\(\) 而非 free，因此只能指向实现了 Ownable 的 C 类型，例如块层中可复用的 bio 请求结构。该系列尚未合并，Hindborg 希望在数月邮件列表讨论后达成共识；主要争议在于 Owned 与 ARef 之间的转换可能破坏健全性，他提议把 AlwaysRefCounted 拆成两个 trait，并禁止同时实现 Ownable 的类型将内建引用升级为 ARef。讨论还涉及 page 结构是否可实现 Ownable，以及 IOMMU 页表、Rust binder 驱动和 USB 驱动等潜在使用场景。

rss · LWN.net · 10月13日 13:33

**「背景」** Rust for Linux 项目已经提供 KBox 和 ARef 等适配类型，用来在 Rust 代码中表达所有权与引用计数语义；其中 KBox 假定内存由 Rust 侧分配，ARef 则假定对象始终采用引用计数。内核块子系统把 I/O 请求放在 C 代码管理的内存池中复用，请求以 bio 结构表示，由驱动处理后再交还块层，因此这两种既有抽象都无法直接覆盖该场景。

**「影响：驱动的所有权 API 与 ARef 升级能力冲突」** 对使用 Rust for Linux 抽象的驱动作者而言，直接后果是 Hindborg 提出的折中方案会限制哪些 C 类型能用上 Owned：把 AlwaysRefCounted 拆成“可用于 ARef”和“可把内置引用升级为 ARef”两个 trait，并禁止同时实现 Ownable 的类型实现后者。这意味着依赖“内置引用升级为 ARef”的现有代码无法直接受益，例如 Rust binder 需要把 page 引用传给 vm\_insert\_page\(\)，Alice Ryhl 认为这一需求无法通过改绑定消除，因此 page 的 Rust 包装类型目前不适合实现 Ownable。该补丁系列仍在征求共识、尚未合入，LWN 此前记录的版本为 v15，本次讨论对应 v21，下游代码暂不能把该 API 视为稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1079571/">rust : add ` Ownable ` trait and `Owned` type [LWN.net]</a></li>

</ul>
</details>

**标签**: `#Rust for Linux`, `#Rust`, `#C interoperability`, `#Linux kernel`, `#ownership semantics`

---

<a id="item-tech-news-11"></a>
### [PostgreSQL 19 测试期多项功能被撤回，核心成员归因于 LLM 辅助审查](https://lwn.net/Articles/1100182/) ⭐️ 7.0/10

PostgreSQL 核心团队成员 Peter Eisentraut 在博客中回顾了进入 beta 阶段后被撤回的“异常多”的 PostgreSQL 19 功能。他表示，部分被撤回的功能存在难以在 beta 期间快速修复的重大架构缺陷，但还有一长串涉及边缘情况、本身相对无害的问题；LLM 辅助代码审查让这类问题被发现得快得多，于是面对约 40 份缺陷报告，即便平均每个只需三行修复，逐项处理的固定开销也会让人耗尽时间。他指出，这些被撤回的功能大多写于 LLM 辅助审查还不那么有用的年代，相当于在功能编写并提交之后，有效质量门槛被抬高了；他认为除非 LLM 辅助审查的能力持续按当前速度提升，未来开发周期里这种情况会自行缓解，而且这基本不属于“vibe coding”。LWN 曾在 9 月报道过 PostgreSQL 19 功能所需的异常多 bug 修复。

rss · LWN.net · 10月13日 13:21

**「背景」** PostgreSQL 19 原定于 2026 年 9 月发布、4 月 8 日进入功能冻结，但后期补丁暴露出异常多的缺陷：Horizon 9 月 11 日的日报曾报道，贡献者 Robert Haas 发起“scary patch contest”，点名外键快速路径、REPACK/REPACK CONCURRENTLY 以及在线启用或禁用数据校验和等补丁在功能冻结后分别需要约 16、28、25 次修复，其中至少一个补丁已被回退，并因此额外增加了一个 beta。Eisentraut 的这篇反思正建立在同一轮进程之上——当缺陷无法在 beta 期内快速修复时，相关功能会被整体撤出 19 版本，而不是零散修补。

**「影响」** 计划依赖这些被撤回功能的 PostgreSQL 19 使用者需要等到后续版本，或自行实现替代方案，因为相关功能已从这一即将发布的版本中移除。与此同时，贡献者应预期在 beta 阶段收到更密集的边缘缺陷报告：按 Eisentraut 的说法，功能提交后 LLM 辅助审查可能抬高有效质量门槛，而每份报告都有不可分摊的处理开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1092003/">2026-09-11 — PostgreSQL 19 后期补丁质量引担忧，新增一个 beta</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#open source`, `#LLM-assisted code review`, `#database development`, `#software process`

---

<a id="item-tech-news-12"></a>
### [Asterinas 0.19.0 发布：新增可运行 X.org 的图形子系统](https://lwn.net/Articles/1100055/) ⭐️ 7.0/10

用 Rust 编写操作系统内核的 Asterinas 项目发布了 0.19.0 版本。此次更新包含一个能够运行 X.org 的新图形子系统、“最小但可用”的 64 位 Arm 支持，以及更好的虚拟化支持。LWN 曾在 2025 年报道过该项目，本次发布信息来自 LWN 的报道与项目公告。

rss · LWN.net · 10月13日 12:55

**「背景」** Asterinas 是一个用 Rust 编写、以兼容 Linux ABI 为目标的操作系统内核，其代码库将安全性与可维护性置于优先位置。该项目此前已按架构逐步扩展：项目公告显示，0.16.0 版本首次加入对 LoongArch 架构的支持，0.19.0 的 64 位 Arm 支持延续了这条多架构移植路线。

**「影响」** 对希望在非 x86 平台或图形环境中试用 Asterinas 的开发者而言，0.19.0 提供了新的可运行目标：图形子系统可支撑 X.org，而 64 位 Arm 支持仍被项目自己描述为“最小但可用”，因此 Arm 上的功能覆盖仍有限，实际部署前需自行确认所需特性是否已具备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/asterinas/asterinas">GitHub - asterinas / asterinas : Asterinas aims to be...</a></li>
<li><a href="https://asterinas.github.io/2025/08/04/announcing-asterinas-0.16.0.html">Announcing Asterinas 0 .16.0</a></li>

</ul>
</details>

**标签**: `#Rust`, `#operating systems`, `#kernel`, `#open source`, `#ARM`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [从傅里叶热学到 LLM 位置编码](https://blog.bytebytego.com/p/how-the-math-used-in-19th-century) ⭐️ 6.0/10

rss · ByteByteGo · 10月13日 15:30

**「背景」** 1822 年傅里叶用正弦和余弦函数表示复杂温度分布；近两个世纪后，同样的函数出现在 Transformer 的位置编码中。作者指出，语言中词序本身携带信息（如“Alice 信任 Bob”与“Bob 信任 Alice”含义不同），但基础注意力机制并不自动把序列顺序变成可用特征——数组索引不会自动参与计算。

**「方案」** 位置编码把序列位置转换成数值表示，使模型同时获得词的身份与位置；原始 Transformer 将同维度的位置编码加到词嵌入上，同一词换位置或不同词同位置都会改变组合输入。作者认为，用正弦/余弦而非单个整数，是因为它们提供有界、多尺度的结构化特征：一个“手”绕圆旋转给出坐标，多个速度不同的“手”能在周期重复后继续区分位置，但并非无限可区分。这种表示还带来可复用的相对位移结构——前进固定步数时各频率对旋转固定角度，因此线性变换可映射到偏移后的编码，供模型训练学习利用。RoPE 把同样的旋转数学放进注意力，对查询和键的分量对按位置旋转，使比较结果依赖相对旋转即相对位置。作者也列出可学习位置嵌入、ALiBi 和因果掩码等替代或补充机制，并强调能算出很大位置的编码不等于能可靠理解任意长文档。

**「启示」** 正弦和余弦的价值不在于比位置编号多出信息，而在于它们把位置表达成有界、多尺度且在平移下关系一致的数值语言，训练再教会模型把这种位置结构与词义和上下文结合起来。

**标签**: `#positional encoding`, `#transformers`, `#Fourier analysis`, `#RoPE`, `#LLM architecture`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [香港证监会暂停茶百道交易，指其 IPO 涉嫌被操纵](https://apps.sfc.hk/edistributionWeb/gateway/TC/news-and-announcements/news/doc?refNo=26PR168) ⭐️ 8.0/10

香港证监会 10 月 13 日称，已调查两个涉嫌参与 IPO 欺诈计划、制造虚假股份需求表象的集团，并指示港交所自当日 9 时起暂停茶百道（02555）交易，认为其 IPO 可能遭人为操纵。证监会同时限制相关账户资产处置，其中涉及茶百道 IPO 的第一可疑集团金额上限为 43.79 亿港元，为同类案件最高；证监会表示调查仍在进行，相关各方日后可能被命令赔偿受影响投资者。

telegram · zaihuapd · 10月13日 10:15

**「背景」** IPO（首次公开募股）指公司首次向公众发售股份，而香港证监会作为香港证券市场的监管机构，可指示港交所暂停某只股票的买卖；此次针对茶百道（02555）的暂停交易自 10 月 13 日 9 时起生效。

**「影响」** 停牌意味着茶百道（02555）现有股东在调查期间无法在港交所买卖该股；证监会同时限制相关账户处置资产，而被点名集团及参与其 IPO、可能受损的投资者能否获得赔偿，仍取决于调查结果。

**标签**: `#Hong Kong SFC`, `#IPO manipulation`, `#trading suspension`, `#ChaBaidu`, `#regulatory enforcement`

---