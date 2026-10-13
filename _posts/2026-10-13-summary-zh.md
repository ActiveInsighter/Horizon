---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 41 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [Python 3.15 发布：PEP 810 惰性导入与 3.10 支持终止](#item-tech-news-1) ⭐️ 9.0/10
2. [黑客触发欧洲超市冷柜自动化霜](#item-tech-news-2) ⭐️ 8.0/10
3. [GitHub 项目把 WiFi 7 路由器变成 320 Msps SDR 接收机](#item-tech-news-3) ⭐️ 8.0/10
4. [用 C 构建并部署现代 Web 应用](#item-tech-news-4) ⭐️ 7.0/10
5. [Codex CLI 默认装入自更新后台守护进程](#item-tech-news-5) ⭐️ 7.0/10
6. [Show HN：PS2 游戏静态重编译为 WebAssembly](#item-tech-news-6) ⭐️ 7.0/10
7. [Rich Hickey 撰文称 AI 不是工具，引发 HN 讨论](#item-tech-news-7) ⭐️ 7.0/10
8. [AI 编码代理产出更多代码，却未带来更多软件](#item-tech-news-8) ⭐️ 7.0/10
9. [Linux 内核维护者峰会：Sashiko 调整与 Assisted-by 标签取消](#item-tech-news-9) ⭐️ 7.0/10
10. [LineageOS 24.0 发布，重新基于 Android 17](#item-tech-news-10) ⭐️ 7.0/10

**科技博客**
1. [ReplaySSM：缓存 SSM 输入而非状态](#item-tech-blog-1) ⭐️ 9.0/10
2. [不用语言的模型：能量基推理如何解约束问题](#item-tech-blog-2) ⭐️ 7.0/10
3. [下一概念建模：快速并行的由粗到细文本生成](#item-tech-blog-3) ⭐️ 6.0/10

**财经新闻**
1. [中国下调新能源汽车出口退税率 13%降至 9%](#item-finance-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Python 3.15 发布：PEP 810 惰性导入与 3.10 支持终止](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 9.0/10

Python 3.15 已正式发布（python.org 提供下载），其 What&\#x27;s new 指南由 3.14 和 3.15 发布经理 Hugo van Kemenade 整理。最受关注的新特性是 PEP 810 显式惰性导入，允许用 \`lazy import json\` 或 \`lazy from pathlib import Path\` 将实际导入推迟到首次使用，Simon Willison 称这直接解决了 LLM CLI 插件因加载 \`sentence\_transformers\` 等重依赖而给每次 \`llm\` 命令增加数秒启动开销的问题。此外，PEP 798 为列表、集合和字典推导式加入 \`\[\*L for L in lists\]\` 等解包语法，标准库新增采样分析器 \`profiling.sampling\`（代号 Tachyon），原有的 \`cProfile\` 追踪分析器更名为 \`profiling.tracing\`。随着 Python 3.10 结束支持，Simon 表示他将不再兼容 3.10，转而采用 3.11 的特性；Miguel Grinberg 对 3.15.0rc3 的独立测试显示，3.15 整体性能与 3.14 大致相同，但实验性 JIT 在斐波那契测试中带来 1.2 倍加速，这是他首次观察到 JIT 的显著提升。

rss · Simon Willison · 10月12日 18:15

**「背景」** Horizon 9 月 2 日的日报曾报道，Python 3.15.0 RC2 是 3.15 的最后一个候选版，正式版计划于 10 月发布；进入 RC 阶段后仅允许合入经评审的明确缺陷修复，当时还建议第三方项目维护者提前针对 3.15 测试并发布 PyPI wheel，并说明基于候选版构建的二进制 wheel 与后续 3.15 版本兼容。如今正式版按该计划落地，同时 Python 3.10 已不再处于受支持版本之列：对需要覆盖所有受支持版本的维护者而言，支持矩阵的下限由此从 3.10 上移到 3.11。

**「影响」** 对于 LLM CLI 插件开发者，PEP 810 的 \`lazy import\` 可取代此前文档中建议的手动惰性导入，避免安装 \`sentence\_transformers\` 等重依赖的插件拖慢每次 \`llm\` 命令的启动。对于库维护者，Python 3.10 结束支持意味着可将最低支持版本提升到 3.11，而直接引用旧 \`cProfile\` 名称的代码需要迁移到 \`profiling.tracing\`。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Sep/1/python-315-rc-2/">2026-09-02 — Python 3.15.0 RC2 发布：生态需准备 10 月正式版</a></li>

</ul>
</details>

**标签**: `#Python 3.15`, `#PEP 810`, `#lazy imports`, `#programming languages`, `#open source`

---

<a id="item-tech-news-2"></a>
### [黑客触发欧洲超市冷柜自动化霜](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

媒体报道称，法国多家超市连锁遭遇一起针对联网制冷控制器的网络攻击，攻击者远程触发自动化霜，导致冷柜停机并影响门店运营。路透相关报道点名 Intermarché，称有 150 家门店被针对；《世界报》则报道法国超市连锁表示网络攻击迫使冷柜关机，事件波及欧洲多国的超市冷链。安全公司 Claroty 的 Team82 研究曾披露 Danfoss 制冷控制器漏洞，但目前报道未确认本次攻击利用的具体 CVE、攻击者身份或确切损失。

hackernews · Zeekaas · 10月12日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**「背景」** 本条报道所附的相关资料中，包含 Claroty 的 Team82 对 Danfoss 制冷控制器漏洞的分析（题为《Freeze the controller, defrost the food》），但检索结果指出，目前没有已读到的来源把这次事件直接归因于 Claroty 披露的漏洞。同一检索结果称，法新社在报道中点名了 AK-SM800、AK-SC355 等早已停产的旧型号，Danfoss 也提到相关设备固件陈旧（tool-2-3）；Danfoss 表示受影响的多数设备已处于生命周期终点（tool-2-1）。报道附带的相关链接还指向 2026 年 8 月 Hacker News 上关于美军基地冷柜疑似遭入侵的讨论帖。

**「影响」** 对 Intermarché 等受影响超市而言，除制冷控制被干扰外，tool-3-1 报道该攻击还导致近 30 万名客户个人数据被窃，受影响客户需按通知防范钓鱼和身份盗用。对仍运行联网旧款制冷控制器的零售商，tool-3-2 指出这类事件暴露的过时软件、弱访问控制和第三方风险意味着应优先盘点并限制控制器的互联网暴露面。

**「社区讨论」** 评论者争论冷柜为何要联网：有人引用 Danfoss 的宣传称远程诊断和启动化霜可减少上门服务并提升能效，也有人指出嫌疑设备包括已停止支持的旧控制器（如 2021 年 EOS 的 SM800、2016 年 EOS 的 SC355），并称一线轮班运维缺乏安全审查和更换预算。另有评论提到医院实验室设备因订阅制也必须联网，并猜测本次事件可能与 2026 年 8 月底美国军事基地冷柜遭入侵有关，但这些关联尚未得到证实。

<details><summary>参考链接</summary>
<ul>
<li>French fridge attack: Danfoss says most hit units were end of life</li>
<li>French Supermarket Cyber Attack: Does International Law Apply?</li>
<li><a href="https://www.connexionfrance.com/news/intermarche-cyberattack-affects-nearly-300000-customers/806317">Intermarché cyberattack 2026 : Nearly 300,000 customers&#x27; data stolen...</a></li>
<li><a href="https://insights.made-in-china.com/How-the-Intermarch-Cyberattack-Exposed-Critical-Flaws-in-U-S-Retail-Cybersecurity_STXAwugOfxIF.html">How the Intermarché Cyberattack Exposed Critical Flaws in...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#IoT security`, `#operational technology`, `#embedded systems`, `#refrigeration controllers`

---

<a id="item-tech-news-3"></a>
### [GitHub 项目把 WiFi 7 路由器变成 320 Msps SDR 接收机](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

GitHub 用户 h0m3us3r 发布 w1700k-sdr 项目，演示如何把 WiFi 7 路由器改造成 320 Msps 的软件定义无线电（SDR）接收机。项目面向希望以低成本获得高采样率接收能力的 SDR 与嵌入式无线开发者。现有信息主要来自项目本身和 Hacker News 评论，项目页没有提供独立的性能测试或完整兼容性列表。

hackernews · djfergus · 10月12日 12:41 · [社区讨论](https://news.ycombinator.com/item?id=50055593)

**「背景」** 软件定义无线电接收需要拿到射频芯片输出的原始 IQ 采样，而路由器官方固件通常不开放这一通道；Horizon 2026 年 10 月 2 日的日报曾报道，多个独立项目在 ESP32 微控制器上发现了未公开的 SDR 接收能力，当时仅限接收且无官方支持（tool-2-1）。本次项目把相同思路用到 Gemtek W1700K 这类 WiFi 7 路由器上：据搜索结果，它替换 MediaTek 固件，让 MediaTek MT7996 射频芯片输出最高 320 Msps 的 14 位原始 IQ（覆盖 2.4/5/6 GHz），再由 Airoha AN7581 SoC 经 10GbE 送往 Linux 主机（tool-1-1、tool-1-2、tool-1-3）；Hacker News 评论指出，同一位开发者此前还做过 ESP32 版的 eSpDR 接收项目。

**「影响」** 对 SDR 爱好者而言，直接结果是可以尝试用路由器硬件探索高采样率接收，而不必先购买专用 SDR 设备；但项目未给出完整兼容性列表，已有评论者仅凭相同芯片组推测 Banana Pi R4 也可能适用，实际移植仍需自行验证。

**「社区讨论」** 评论者 yonatan8070 指出同一开发者还做过基于 ESP32 的 SDR，并希望更多常见 Wi-Fi 网卡能被这样利用；thebeardisred 认为相同芯片组的 Banana Pi R4 很可能适用，alightsoul 则把手机 FM 收音机受合同限制与软件定义无线电联系起来。aftbit 称这是其所知的 5 GHz 下最便宜的 320 Msps 接收方案。

<details><summary>参考链接</summary>
<ul>
<li>Turn a WiFi 7 Router into a 320Msps Software Defined Radio Receiver</li>
<li>Turn a WiFi 7 Router into a 320Msps Software Defined Radio Receiver</li>
<li>h0m3us3r on X: &quot;Turned a WiFi 7 router into a 320Msps SDR. Custom ...</li>
<li><a href="https://www.rtl-sdr.com/various-projects-independently-find-hidden-sdr-capabilities-in-esp32-microcontrollers/">2026-10-02 — 多个项目在 ESP32 中发现未公开 SDR 接收能力</a></li>

</ul>
</details>

**标签**: `#software-defined-radio`, `#wifi-7`, `#hardware-hacking`, `#embedded-systems`, `#wireless-communication`

---

<a id="item-tech-news-4"></a>
### [用 C 构建并部署现代 Web 应用](https://prophitt.me/writing/a-modern-web-app-in-c) ⭐️ 7.0/10

面向希望在 C 中构建 Web 应用的开发者，这篇文章演示了如何用 CGI/FastCGI、通过 pledge/chroot 等方式降权并进行部署。由于原文正文未提供，具体代码、版本和步骤无法核实；以下信息来自分析摘要与 Hacker News 讨论。评论者总体上认可文章的降权思路，ramses0 称其中相关内容“100% 真实且推理充分”，并补充 BusyBox 内置 cgi-bin 支持，同时有人比较 Go 等单二进制替代方案。

hackernews · prophittcorey · 10月12日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50058528)

**「背景」** 这篇文章展示的做法建立在 CGI 之上：按文章所述，1994 年想做动态网站，就是写一个 C 程序放进 cgi-bin 目录，让 Apache 在每个请求时 fork 一次（tool-1-2）。作者 Corey Prophitt 用 BCHS 栈（OpenBSD、C、httpd）上线了商业产品 marketyour.games，属于把这条老技术路径重新用于实际部署（tool-1-1）。正因为如此，文中关于 FastCGI、权限隔离与部署方式的取舍才成为讨论焦点。

**「影响」** 如果开发者按该文路线用 C 部署 Web 应用，就需要自行处理 CGI/FastCGI 的进程模型、降权与并发问题；评论中提到 fork/exec 后 .bss/.data 段仍需初始化，而 Go 可通过 CGO\_ENABLED=0 生成内含 HTTP/TLS 的单二进制程序，减少对 nginx 等传统 Web 服务器的依赖。

**「社区讨论」** ramses0 认可文章的降权思路，并补充 BusyBox 自带 CGI 支持以及 rclone serve webdav；assimpleaspossi 分享早年用 C/FastCGI 交付订餐系统的经验，称系统被加盟商收购后改用微软技术栈反而问题不断。benlivengood 则认为 Go 的单二进制、CGO\_ENABLED=0 和内置 HTTP/TLS 更适合替代传统 Web 服务器，并指出 C 并发编程和 fork/exec 后的数据段初始化是实际难点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/50058528">A Modern Web App in C · Hacker News | Zeli</a></li>
<li><a href="https://upstract.com/x/ff7e87d60c67529f">A Modern Web App in C - upstract.com</a></li>

</ul>
</details>

**标签**: `#C`, `#web development`, `#CGI/FastCGI`, `#systems programming`, `#privilege separation`

---

<a id="item-tech-news-5"></a>
### [Codex CLI 默认装入自更新后台守护进程](https://github.com/openai/codex/issues/48195) ⭐️ 7.0/10

据 GitHub issue 及 Hacker News 讨论，OpenAI 的 Codex CLI 默认会安装一个常驻的自更新后台守护进程（daemon），用户称没有官方文档化的关闭选项，只能通过 ~/.codex/config.toml 中的特性开关 \[features\] daemon\_auto\_start = false 停用。有用户报告该守护进程在自动更新时会破坏文件权限、导致 .git 变为只读，并因保留旧版本占用约 12 GB 磁盘空间；这些均属用户报告，现有材料中没有 OpenAI 的回应或确认。

hackernews · whimblepop · 10月12日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694)

**「背景」** Codex CLI 的守护进程自动启动并非一直默认开启：检索结果显示，Codex 0.157 将 \`features.daemon\_auto\_start\` 默认打开，使交互式会话运行在一个共享后台服务器中（tool-2-2）。在同一 0.157.0 版本上，若要在没有后台服务器的情况下运行，需要加上 \`--no-daemon\`（tool-2-3）。相关问题报告要求把该标志改回按需启用（opt-in），并指出守护进程通过 \`codex app-server --managed-daemon\` 启动，在无 TTY 的独立会话中持续运行（tool-2-1）。

**「影响与应对」** 对使用 Codex CLI 的开发者，社区给出的实际做法是在 ~/.codex/config.toml 中设置 \[features\] daemon\_auto\_start = false，并清理 ~/.codex 目录下由守护进程写入的 pid、lock 等文件；有用户建议把这些文件替换为指向 /dev/null 的符号链接，再用 chattr +i 之类的方式标记为不可写。这些都是评论者提供的变通方法，材料中没有官方文档或修复方案。

**「社区讨论」** 有用户称该守护进程自动更新时会随机弄坏权限、使 .git 变为只读，因此不敢再依赖它执行任务；另有人表示已改用只提供极少工具、主要靠 bash 的简易 harness（hax），认为比这类“过度工程化”的工具更省心。也有评论质疑 ChatGPT/Codex 桌面端与 Android 应用的前端质量，这属于个人意见而非常规事实。

<details><summary>参考链接</summary>
<ul>
<li>CLI: make `daemon_auto_start` opt-in — a persistent, self-updating ...</li>
<li>Run Codex CLI from Your Phone - Moshi</li>
<li>Codex 0.157.0 no longer starts with the Arch Linux package unless</li>

</ul>
</details>

**标签**: `#Codex CLI`, `#background daemon`, `#OpenAI`, `#developer tooling`, `#software bugs`

---

<a id="item-tech-news-6"></a>
### [Show HN：PS2 游戏静态重编译为 WebAssembly](https://github.com/snuri00/ps2-web-recomp) ⭐️ 7.0/10

Hacker News 的 Show HN 栏目出现了 deadxwarrior 提交的 ps2-web-recomp 项目，它把 PS2 游戏静态重编译为 WebAssembly。该仓库的目标是让这类游戏能在 WebAssembly 环境（包括浏览器）中运行。提供材料没有给出已支持游戏列表、兼容性范围、性能数据或发行版本，因此这目前更像是一个技术演示或开源方向，而非已经验证可广泛使用的方案。

hackernews · deadxwarrior · 10月12日 06:46 · [社区讨论](https://news.ycombinator.com/item?id=50052251)

**「背景」** 这类项目走的是静态重编译（AOT）路线：与在运行时解释指令并模拟硬件的传统模拟器不同，它先把游戏的 Emotion Engine 机器码整体翻译成 C++，再编译为 WebAssembly，并链接到对该主机操作系统与硬件的重实现，由 WebGPU 负责绘制（tool-2-1、tool-2-3）。同一作者此前已把相同方法用于掌机：Horizon 10 月 8 日的日报曾报道 snuri00 的 psp-web-recomp，该项目把 PSP《战神》的 MIPS 机器码提前翻译为 C++ 再编译成 WebAssembly，链接到一个小型重实现的 PSP 操作系统和图形层，用 WebGL2 绘制，并且没有提供兼容性清单或性能保证（tool-1-1、tool-2-2）。本次可视为这条路线从 PSP 扩展到 PS2，渲染后端由 WebGL2 换成了 WebGPU。

**「影响」** 对想尝试的玩家和开发者来说，最直接的行动影响是信任与审查：静态重编译产物不像成熟模拟器那样已有社区审查记录，评论者明确担心其中可能隐藏恶意软件，因此在运行或分发前应检查源码与构建来源。

**「社区讨论」** 评论者 aceazzameen 担心，越来越多的静态重编译项目以原生方式运行，但其信任与审查水平还不及模拟器社区，可能带来隐藏恶意软件风险。开发者 kodablah 则报告自己用类似思路为 PS Vita 做了 ARM-to-WASM 转译器，目前只测试了少量游戏，仍处早期，但在旗舰 Android 手机的 Chrome 上运行得相当好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/snuri00/psp-web-recomp">2026-10-08 — psp-web-recomp：PSP《战神》重编译为 WebAssembly 在浏览器运行</a></li>
<li><a href="https://github.com/snuri00/ps2-web-recomp">GitHub - snuri00/ps2-web-recomp: PS2 games in the browser ...</a></li>
<li><a href="https://github.com/snuri00/psp-web-recomp">GitHub - snuri00/psp-web-recomp: PSP games in the browser ...</a></li>
<li><a href="https://blog.adafruit.com/2026/10/12/ps2-games-in-browser-static-recompilation-to-webassembly-with-a-native-runtime/">PS2 games in browser: static recompilation to WebAssembly ...</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#static recompilation`, `#PS2 emulation`, `#reverse engineering`, `#open source`

---

<a id="item-tech-news-7"></a>
### [Rich Hickey 撰文称 AI 不是工具，引发 HN 讨论](https://www.linkedin.com/pulse/ai-tool-rich-hickey-kjl8e) ⭐️ 7.0/10

软件工程界知名人物 Rich Hickey 发表文章《AI Is Not a Tool》，主张不应把对话式 AI 系统简单称为“工具”。根据 Hacker News 讨论中的引述，Hickey 承认 LLM 本身可看作一种用自然语言查询、内置摘要的有损知识库；他批评的是把这类系统包装成做作业、研究、编程、写作的“工具”的说法。该文在 Hacker News 上引发关于 LLM 的能动性、工具与代理边界以及软件工程实践的讨论；帖子本身只给出 gist 链接，未提供更多技术细节。

hackernews · svieira · 10月12日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=50060269)

**「背景」** 这篇随笔延续了 Rich Hickey 此前对 AI 的批评立场：据外部分析，他在题为《Thanks, AI》的演讲中把 AI 直接产出代码视为绕过了软件开发中最难的部分——理解问题本身（tool-2-2）。Hickey 以设计 Clojure 为开发者所熟知（tool-2-1）。讨论涉及的核心概念是“工具”与具备自主性的“代理”之间的区分：有评论者认为 LLM 处在从“工具性”到“代理性”的连续谱上，而 Hickey 在回复中澄清，他针对的不是 LLM 本身，而是那些被宣传为做作业、研究、编程、写作“工具”的对话式系统。

**「对开发者的实际影响」** 对把会话式 LLM 助手接入编码、写作或研究流程的开发者来说，可直接落地的提醒是：Hickey 把“工具性”描述为一段连续谱，越接近“点单式”使用就越不像工具，因此沿用确定性输入输出、结果可验证这类传统工具标准来评估此类系统会出现预期失配。采用前宜针对具体工作流单独定义验收标准，而不是照搬既有工具选型清单。

**「社区讨论」** 评论者 atleastoptimal 认为 LLM 位于“工具到代理”的连续谱上，人类也处于同一谱系；didibus 引用 Hickey 的回复说，争论焦点是对话系统被宣传为学习、研究、编程工具，而非否认 LLM 可作为有损知识库。iLemming 则报告自己在最近的 Conj 上问过 Hickey，后者称“不参与这个实验”、未深入研究 LLM，并对其效果及道德、经济等问题持怀疑态度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=YR5WdGrpoug">Maybe Not - Rich Hickey - YouTube</a></li>
<li><a href="https://karangoyal.cc/blog/rich-hickey-thanks-ai-analysis">Rich Hickey &#x27;s &quot;Thanks AI &quot;: A Critical Analysis</a></li>
<li><a href="https://news.ycombinator.com/item?id=50060269">&#x27;AI&#x27; Is Not a Tool by Rich Hickey | Hacker News</a></li>
<li><a href="https://news.mcan.sh/item/50060269">&#x27;AI&#x27; Is Not a Tool by Rich Hickey | Remix Hacker News</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#software engineering`, `#AI criticism`, `#Hacker News discussion`

---

<a id="item-tech-news-8"></a>
### [AI 编码代理产出更多代码，却未带来更多软件](https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/) ⭐️ 7.0/10

Ars Technica 的一篇文章及 Hacker News 上的讨论指出，AI 编码代理虽然让代码产出量上升，却没有带来等比例的软件交付成果，瓶颈转移到代码审查与代码质量上。讨论中的从业者表示，代码审查原本就是显著瓶颈，在代理式编码下更加突出；尝试更多依赖自动化审查迄今没有转化为实际改善。有评论提醒，相关研究描述的是研究进行时的状况，主要涉及 Claude 3.5 至 Sonnet 4.5、GPT-4.1 至 GPT-5、Gemini 2.5 等模型，论文写作与发表存在滞后，因此反映的是 2025 年前后的图景，未必代表当前模型能力。需要说明的是，所依据的材料为分析摘要与社区讨论，未包含原文全文。

hackernews · gumby · 10月12日 17:14 · [社区讨论](https://news.ycombinator.com/item?id=50059523)

**「背景」** 围绕 AI 编程代理究竟是否提升交付效率的争论早于这项研究。Horizon 2026 年 3 月 26 日的日报曾报道，代理框架 Pi 的作者 Mario Zechner 批评当时的代理化工程趋势把最大化代码产出置于软件工程纪律之上，并警告缺少人工监督会让错误与复杂度迅速累积（tool-1-2）。据二手报道，这项研究由哈佛研究者 Fiona Chen 与 James Stratton 完成，基于 700 多家软件公司的约 3 亿条工程活动记录，数据截止于 2026 年 3 月，其涉及的主导模型大致为 Claude 3.5 至 Sonnet 4.5、GPT-4.1 至 GPT-5 和 Gemini 2.5（tool-2-1、tool-2-2）。

**「对开发团队的实际影响」** 对采用 AI 编码代理的团队来说，交付效率的约束点从写代码转移到人工代码审查：Ars Technica 引用的研究把人工审查列为整体效率的显著瓶颈，FlowVerify 汇总的 2026 年数据也把瓶颈描述为「从编写代码转向审查代码」。厂商博客 Alex Cloudstar 给出的量化是 PR 数量增长 98%、审查时间增加 91%（属博客自述数据，非独立测量），因此团队在扩大代理使用前更适合先评估并扩容审查能力与自动化检查，而不是假定代码产出增加会自动缩短交付周期。

**「社区讨论」** 评论者 staminade 称其职业经历与文章相符：代码审查一直是并愈发成为代理式编码的瓶颈，团队讨论过更多依赖自动审查，但未取得实际改善，资深工程师仍难以放弃逐行审查；jacquesm 补充说，代理生成的代码往往重复、缺少抽取与重构、冗长难读，还会在不必要处过度注释、在必要处缺少文档。jefftk 提醒这是学术论文，反映的其实是 2025 年（主要涉及 Claude 3.5 至 Sonnet 4.5、GPT-4.1 至 GPT-5、Gemini 2.5）的模型状态，而 blauditore 以赛车引擎与轮胎作比，认为编码只占整体工作的一小部分，引擎变强后瓶颈会转移到其他环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything">2026-03-26 — Critique of AI Agent Speed: Advocating for Discipline Over Code Output</a></li>
<li><a href="https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/">AI coding agents generate more code, but not more software</a></li>
<li><a href="https://lumienai.com/news/ai-coding-agents-more-code-not-more-software-output">AI Coding Agents Write More Code, But Ship No More Software</a></li>
<li><a href="https://www.flowverify.co/blog/ai-code-review-bottleneck-2026-data">The AI Code Review Bottleneck, By the 2026 Numbers | FlowVerify</a></li>
<li><a href="https://alexcloudstar.com/blog/ai-code-review-bottleneck-2026/">AI Code Review Bottleneck 2026: PR Crisis | Alex Cloudstar</a></li>
<li><a href="https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/">AI coding agents generate more code, but not more software</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#developer productivity`, `#code review`, `#software engineering`, `#LLM limitations`

---

<a id="item-tech-news-9"></a>
### [Linux 内核维护者峰会：Sashiko 调整与 Assisted-by 标签取消](https://lwn.net/Articles/1099594/) ⭐️ 7.0/10

对 Linux 内核维护者和贡献者而言，补丁审查流程将出现几项变化：Sashiko 自动审查不再在补丁审查中报告已存在的旧缺陷，而是将其存入单独数据库；补丁的 Assisted-by 标签要求也将被移除。这些是 2026 年 10 月 8 日在布拉格举行的维护者峰会上的讨论结论，约 30 名内核开发者参加，会议还涉及 LLM 对开发社区的影响、安全漏洞洪流和长期接班规划。据 Jonathan Corbet 的会议记录，Linus Torvalds 认为问题不在 LLM 本身，而在于不熟悉内核和工具的使用者，并主张对低质量贡献给予低优先级；部分最紧急的安全修复可能绕过维护者直接交给 Torvalds。Corbet 强调这些结论是他的个人解读，并非峰会的官方公告。

rss · LWN.net · 10月12日 15:27

**「背景」** 本次峰会上争议的中心——Sashiko——是一个基于大语言模型的内核补丁自动评审系统：5 月 26 日的日报曾报道，LSFMM+BPF 峰会为其举行了专题讨论，当时社区关注的是它能否减轻人工维护者的负担（tool-1-1）；10 月 6 日的日报则报道了维护者 Roman Gushchin 在 Kernel Recipes 上介绍的最新进展，其中已明确提到该系统会在未改动的代码上反复报出同一问题（tool-1-2）。峰会围绕“既有缺陷不再出现在补丁评审中、改为存入单独数据库”的争论，正是对这一已知局限的后续处理。

**「影响」** 内核贡献者提交补丁时不再需要添加 Assisted-by 标签，但维护者仍会追问补丁是否由 LLM 生成；同时 Sashiko 审查不再列出已存在的旧缺陷，因此提交者不会被要求在处理自己改动前先修复这些旧问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1073583/">2026-05-26 — LLM-based kernel patch review debated at LSFMM+BPF</a></li>
<li><a href="https://lwn.net/Articles/1096963/">2026-10-06 — Sashiko：LLM 内核补丁评审系统的进展</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#open source`, `#LLM`, `#maintainership`, `#security`

---

<a id="item-tech-news-10"></a>
### [LineageOS 24.0 发布，重新基于 Android 17](https://lwn.net/Articles/1099950/) ⭐️ 7.0/10

LineageOS 项目宣布发布 LineageOS 24.0，将这个社区 Android 发行版重新基于 Android 17——项目称 Android 17 的首个版本于今年 6 月发布。LineageOS 表示，由于此前几代已经适应了 Google 的大幅代码重构，这次迁移到 Android 17 代码库比预期更快，因此发布时间早于往年。公告称 Android 17 的首个版本主要包含迭代改进和部分 UI/UX 调整，但公告本身未列出受支持机型或新增功能清单。项目还提到，LineageOS 将于 2026 年 12 月 24 日迎来成立十周年。

rss · LWN.net · 10月12日 13:13

**「背景」** LineageOS 的这次重基依赖上游 Android 代码库的开放。Horizon 6 月 18 日的日报曾报道，Android 17 已面向 Pixel 设备发布并开放源代码，当时的主要变化包括强制大屏支持、通过 AppFunctions 接入 Gemini 的 AI 集成，以及全面转向 Jetpack Compose（该条目的日期为日报日期，并非已验证的事件日期）。LineageOS 此次正是在 Android 17 发布后重基其改动与功能，并称因前几个版本已适应 Google 的重构，此次进度快于预期。

**「影响」** 对用户而言，LineageOS 24.0 提供了较新的 Android 17 基线，但升到新基线需要各机型维护者跟进适配，因此某一具体设备能否获得 24.0 取决于它是否仍有活跃维护者——公告也把“让众多设备延续生命”归功于维护者群体。由于公告未给出受支持设备列表，用户应以各机型的构建状态为准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://android-developers.googleblog.com/2026/06/Android-17.html">2026-06-18 — Android 17 Released: Mandatory Large-Screen Support, AI Integration</a></li>

</ul>
</details>

**标签**: `#LineageOS`, `#Android`, `#open source`, `#mobile OS`, `#custom ROM`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [ReplaySSM：缓存 SSM 输入而非状态](https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/) ⭐️ 9.0/10

rss · NVIDIA Inference Performance Blog · 10月12日 16:00

**「背景」** 混合模型把 SSM 层与少量注意力层交错，SSM 用固定状态代替随上下文增长的 KV 缓存；但作者指出，在服务批量下，SSM 层可在最长约 100K token 的上下文中成为解码瓶颈，并使投机解码和量化更复杂。

**「方案」** ReplaySSM 的核心是缓存最近的 SSM 输入而非完整状态，把状态表示成“检查点 + 输入缓冲区”。非 flush 步只追加当前输入，并用检查点和缓冲区计算输出，不写状态；缓冲区（最优窗口 L=16）填满后，flush 步把缓冲输入折叠进检查点并写一次 HBM，从而把输出计算与状态更新解耦。作者在 Nemotron 3（Mamba-2）和 Qwen3.5（GDN）的四个模型、H100 与 B300 上评估，batch 256 下内核提速 1.46–1.80×、解码步提速 1.20–1.47×，但 batch 1 无收益。投机解码只需追加草稿输入并按接受前缀推进缓冲区指针，不保存状态快照；配合 output-only 计算，GSM8K、T=4、batch 512 下吞吐达 vLLM 投机解码的 1.85–2.10×（接受长度匹配）。量化也被拆分：高精度检查点用于循环更新，低精度副本只用于非 flush 读，舍入误差不再回灌；Qwen3.5-4B 上 NVFP4 读加 FP32 循环把 128K token 的 KL 从 0.136 降到 0.0038，GPQA-Diamond 上共享 NVFP4 检查点损失 3–31 个百分点，分离精度则恢复到多数模型约 2 个百分点内。

**「启示」** 作者的核心结论是：把 SSM 状态从每步读写的矩阵改为检查点加近期输入缓冲，能让 SSM 层重新变快，并把投机回滚与读写精度解耦；这一表示层改动已进入 TensorRT-LLM、vLLM、SGLang、FlashInfer 以及 GLM-5.3-Flash、Kimi-K3 的生产服务。

**标签**: `#SSM`, `#speculative decoding`, `#quantization`, `#inference optimization`, `#hybrid models`

---

<a id="item-tech-blog-2"></a>
### [不用语言的模型：能量基推理如何解约束问题](https://blog.bytebytego.com/p/how-to-build-models-without-language) ⭐️ 7.0/10

rss · ByteByteGo · 10月12日 15:00

**「背景」** 大语言模型逐 token 从左到右生成，输出又是离散的，因此在数独这类需要同时满足多重约束的问题上很吃力：据 Logical Intelligence 的一场公开演示，GPT-5.2、Claude Opus 4.5、Gemini 3 Pro、DeepSeek V3.2 等前沿模型合计只解出 2%，烧掉约 1.1 万美元 API 费用，而参数量小约千倍的 Kona 解出 96.2%、仅用 4 美元 GPU 时间（均为厂商自报数据）。作者由此提出：大多数日常任务本就不是语言问题，语言只是智能的界面，而非智能本身。

**「方案」** Logical Intelligence 的替代方案是能量基推理模型（EBRM）：它不生成 token，而是学习能量函数 E\(x,y\)，能量越低表示候选答案与问题越一致。训练用对比损失压低正确答案、抬高错误答案（可由扰动正确答案或模型自身搜索产生），从而形成连续的能量地形；推理从随机噪声出发，沿能量下降梯度迭代至能量不再下降，对多步问题还会对每一步中间状态打分，即作者所说的“在理解而非数据上导航”。Kona 平均 313 毫秒收敛，LLM 单题最长要 90 秒；随后用机器可校验的检查（数独用简单程序，定理证明用 Lean 4）判定，不通过就回到搜索——中间是概率性的，末端是精确的。作者强调能量只是规则的近似、搜索依赖起点，低能量是强证据而非证明，约束是否写对仍靠人；EBRM 也不擅长需要判断与表达的写作任务，且文中未与经典约束求解器对比。

**「启示」** 作者的核心论点是：语言是智能的界面而非智能本身，硬约束、可机器验证的任务更适合小模型加潜空间搜索，未来更可能是专用模型与语言模型分工协作的生态，而非单一通用大模型包打天下。

**标签**: `#energy-based models`, `#latent reasoning`, `#constraint satisfaction`, `#LLM limitations`, `#AI verification`

---

<a id="item-tech-blog-3"></a>
### [下一概念建模：快速并行的由粗到细文本生成](https://hazyresearch.stanford.edu/blog/2026-10-12-ncm) ⭐️ 6.0/10

rss · Stanford Hazy Research Blog · 10月12日 07:00

**「背景」** 自回归模型逐词生成，输出变长后推理成本高，扩散语言模型（DLM）虽并行细化多个 token，却仍需较多采样步、每步处理整条序列，并多次遍历训练数据。作者由此提出一种介于两者之间的非自回归路线。

**「方案」** Next-Concept Modeling（NCM）把文本表示为由短到长的离散码层级：高层级只含少量码、捕捉整体结构，低层级逐步补足细节。第一阶段训练多尺度 tokenizer，借鉴 VAR 的图像做法并为文本改动：每层独立码本、用嵌套 dropout 迫使浅层不依赖深层也能承载有效信息、以 token 级重建目标保证还原准确。第二阶段冻结 tokenizer，训练 transformer 依据前面各层的累积重建预测下一层，一次前向传播覆盖所有层，并损坏一部分条件码以增强对生成错误的鲁棒性；推理时逐层生成、层内所有码并行预测，最后由解码器还原文本。作者报告在 TinyStories、LM1B、OpenWebText 上生成困惑度不劣于或优于最强扩散基线，且函数评估次数（NFE）更少；在单张 H100 SXM 80GB 上，LM1B 无条件生成快 21 倍、OpenWebText 快 10 倍，XSum 上 ROUGE-L 持平同时快 31 倍，WMT14 De-En 与 Sudoku 推理同样不劣于甚至更好，作者认为先定结构的粗到细生成有助于全局规划。训练方面，计入 tokenizer 与生成器后，LM1B 与 OpenWebText 分别少用约 4.9 倍与 4 倍 token；初步规模实验显示参数增加持续改善困惑度，而快速采样使 MBR 测试时扩展能在相同时限内生成更多候选，从而超过扩散基线。

**「启示」** 作者认为 NCM 说明“由粗到细、层内并行”是一条可行的第三条语言建模路线，并已给出有竞争力的早期结果；但它随参数、FLOPs 与数据规模的进一步扩展、表示与生成联合训练，以及按样本难度自适应分配计算，仍是尚未解答的问题。

**标签**: `#non-autoregressive language models`, `#coarse-to-fine generation`, `#diffusion language models`, `#multiscale tokenization`, `#text generation`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国下调新能源汽车出口退税率 13%降至 9%](https://www.news.cn/20261012/9709731f470b42f9a84825c2e4eb914b/c.html) ⭐️ 8.0/10

财政部、税务总局 10 月 12 日发布公告，自 2027 年 4 月 1 日起，将新能源汽车增值税出口退税率由 13%下调至 9%，同时取消电子烟设备装置等产品的增值税出口退税；公告称对上述产品中征收消费税的，出口消费税政策不作调整。

telegram · zaihuapd · 10月12日 11:00

**「背景」** 中国此前已对清洁产品出口退税做过类似下调：自 2024 年 12 月 1 日起，清洁产品增值税出口退税率从 13%降至 9%，柴油、航空煤油和汽油出口相当于每桶增加约 4 美元税负。与此同时，新能源汽车出口近期高速增长，2026 年 3 月出口 34.9 万辆，同比增长 139.9%。

**「影响」** 出口退税率下调 4 个百分点，意味着新能源车出口商获得的增值税返还减少、实际出口成本相应上升，可参照 2024 年 12 月清洁产品退税率同样由 13%降至 9%时出口商迅速应对的情形（tool-2-2），以 2026 年 7 月出口 6.633 万辆、占中国乘用车新能源出口 12.3%的特斯拉中国为代表的出口企业，其利润与海外报价将直接承压（tool-2-3）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://carnewschina.com/2026/04/21/geely-nev-exports-soar-479-as-china-ships-349000-evs-up-139-9-amid-oil-shock/">Geely NEV exports soar 479% as China ships 349,000 EVs, up...</a></li>
<li><a href="https://www.linkedin.com/pulse/chinas-vat-rebate-cut-clean-products-whats-behind-r9rvf">China ’s Vat Rebate Cut On Clean Products: What’s Behind The Move?</a></li>
<li><a href="https://www.linkedin.com/pulse/chinas-vat-rebate-cut-clean-products-whats-behind-r9rvf">China ’s Vat Rebate Cut On Clean Products: What’s Behind The Move?</a></li>
<li><a href="https://cnevpost.com/2026/08/13/automakers-share-china-nev-exports-jul-2026/">Automakers&#x27; share of China NEV exports in July: BYD... - CnEVPost</a></li>

</ul>
</details>

**标签**: `#中国`, `#新能源汽车`, `#出口退税`, `#税收政策`, `#电子烟`

---