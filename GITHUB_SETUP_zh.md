# 在 GitHub Actions 上运行 Horizon

部署仓库：https://github.com/ActiveInsighter/Horizon 。工作流和配置随本指南提交；完整日报运行需要先添加下方密钥及模型配置。
使用 OpenAI 兼容 AI 接口、Apify X 抓取，生成中英双语日报并保存为 Actions Artifact。**2026-10-17 因费用复核，工作流已手动禁用；当前不会定时运行。** Cron 模板仍保留北京时间约 07:17 的设置，恢复启用前需要确认费用安排。

## 1. 获取 Apify Token

截图中的 Actor 页面 **API** 菜单是 API 调用说明入口。Token 位于 Apify 的 **Settings → API & Integrations**：

https://console.apify.com/account/integrations

创建一个专用于 Horizon 的 Token。GitHub 工作流会通过 API 启动 `altimis/scweet`，无需另外在 Apify 创建定时任务。

## 2. 仓库和文件

本仓库 Fork 自 https://github.com/Thysrael/Horizon ，部署地址为 https://github.com/ActiveInsighter/Horizon 。

以下文件已随本指南提交到默认分支：

- `.github/workflows/horizon-daily.yml`
- `data/config.actions.json`
- `scripts/run_actions.py`

无需自行上传文件。工作流入口：https://github.com/ActiveInsighter/Horizon/actions/workflows/horizon-daily.yml 。

不要上传 `.env`、`.venv`、`.tools`、`.cache`。上述文件均不含密钥。本机的 `run.sh`、`check.sh` 不是这个 Actions 工作流的依赖。

上游的 `.github/workflows/daily-summary.yml.disabled` 保持原样；本指南启用的是 `horizon-daily.yml`，避免两份日报任务重复运行。

## 3. 设置 Secrets 和 Variables

进入自己仓库的 **Settings → Secrets and variables → Actions**。

在 **Secrets** 页选择 **New repository secret**，添加：

| 名称 | 内容 |
| --- | --- |
| `OPENAI_API_KEY` | AI 服务的 API Key；即使是其他 OpenAI 兼容服务，也用这个变量名 |
| `APIFY_TOKEN` | Apify 的 Token，通常以 `apify_api_` 开头 |

在 **Variables** 页选择 **New repository variable**，添加：

| 名称 | 内容 |
| --- | --- |
| `HORIZON_AI_MODEL` | 你的服务商提供的模型 ID |
| `HORIZON_AI_BASE_URL` | 服务商的 OpenAI 兼容 API 地址；省略时使用 `https://api.openai.com/v1` |

模型名和 API 地址也支持放在同名 **Secrets** 中；如果两处都设置，优先使用 Secret。Secrets 入口：https://github.com/ActiveInsighter/Horizon/settings/secrets/actions 。Variables 入口：https://github.com/ActiveInsighter/Horizon/settings/variables/actions 。

AI Key 和模型尚未准备好时，先完成配置，等填好之后再启用任务。工作流会在缺少必填配置时明确报出变量名。

GPT Load 使用 OpenAI 兼容接口时，Base URL 应为 `https://你的域名/v1`；工作流对域名根地址自动补齐 `/v1`。本次部署的模型 ID 为 `gemini-3.5-flash-lite`，注意拼写是 `gemini`。

GitHub 会自动提供 `GITHUB_TOKEN`，不必自己申请或新增同名 Secret。

## 4. 修改要关注的账号

编辑 GitHub 仓库中的 `data/config.actions.json`：

- `sources.twitter.users`：改成自己的关注列表，不带 `@`。当前示例为 `karpathy`、`ylecun`。
- `sources.twitter.keywords`：可选的全站搜索查询；默认空数组。
- 暂时不用 X 时，可把 `sources.twitter.enabled` 改为 `false`，并从工作流 `required` 列表移除 `APIFY_TOKEN`。

X 抓取每次 Actor 运行至少请求 100 条。每个关键词额外启动一次 Actor，回复抓取也可能增加调用。最终日报 10 条上限不会将抓取量或 AI 评分量限制为 10 条。

## 5. 手动验证，再等待定时运行

打开自己仓库的 **Actions**；Fork 仓库如果提示工作流被禁用，先点击启用工作流的按钮。

选择 **Horizon Daily → Run workflow → Run workflow**。工作流文件需要在仓库默认分支上，手动运行入口才会出现。

当前工作流已暂停，需要先恢复启用才可操作。手动任务默认**只检查已有 Apify 任务并导出其结果**，不会启动新的 Actor 或调用 AI。只有勾选 `paid_refresh` 才会重新抓取并调用 AI，产生对应使用量。定时事件在工作流恢复启用后会执行完整流程。

等待成功后，进入这次运行详情，下方 **Artifacts** 中下载 `horizon-briefings-序号`。解压后，`summaries/` 包含中文和英文 Markdown 日报，`run-evidence/x-posts.md` 包含本次采集的 X 原帖；`collected-items.json`、`analyzed-items.json` 和 `source-counts.json` 供核对来源、评分和数量。附件当前保留 14 天。

流程会先用一个很小的 JSON 请求验证模型调用，再抓取信息源。AI 预检失败时直接终止；全部内容分析失败时也会报错，避免把空日报误报为成功。已经抓到的公开内容在后续处理失败时也会尝试上传，便于排错。

工作流设定 `17 23 * * *`，即 UTC 23:17、北京时间次日 07:17。GitHub 定时运行可能延迟，不保证准点；公共仓库连续 60 天没有活动时，定时工作流会被自动禁用。

## 费用和抓取数量

2026-10-17 的三次完整测试各启动了一次 Actor，每次返回 100 条，共 300 条；最近 24 小时内的内容分别为 9、9、0 条，前两次的近期帖子重复，最终只有 9 条不同的近期帖子。原逻辑没有把时间条件传给 Apify，而是在数据返回后才过滤，导致旧帖也消耗了额度。本地去重和 AI 筛选不会退回上游使用量。

修正后，采集请求会向 Actor 传入 `since`；多个账号还会分配 `per_profile_limit`，避免一个账号占满总上限。`apify-fetch-receipts.json` 会分别记录上游返回行数和本地保留行数。时间条件与统计逻辑已通过模拟测试，费用复核期间没有启动新的 Actor 实测，不能据此保证新的实际费用。

Scweet 将小于 100 的 `max_items` 请求值调至 100；这是请求大小限制，不能据此理解为每次必然计费 100 条。实际结果费另有启动费，按 Actor 页面及账号费用明细核对。平台每月赠送额度与 Actor 的 3,000 条试用总额是不同限制，不能把 3,000 条试用理解为每月重置。

本机不需要开着；抓取和 AI 处理在 GitHub runner 上完成。Apify 与 AI API 的使用量仍由对应账号计费，GitHub Actions 额度按仓库及账号方案计算。

## 可选：以后发布为网页

当前版本将日报保存为下载附件。若要固定的日报网址，可以再配置 GitHub Pages 的官方部署工作流；项目会把可发布的日报复制到 `docs/`。

先验证 AI 与 X 抓取都正常，再增加 Pages 或推送渠道，便于定位配置问题。

## 排错

- `Missing repository Secrets / Variables`：按报错列出的名称补齐；注意 Secrets 和 Variables 是两个页签。
- AI 401/403：核对 AI Key、API 地址、模型权限。
- Apify 鉴权失败或无结果：到 Apify Console 查看 Actor Runs，检查 Token 权限、额度、Actor 试用限制和用户名。
- Apify 抓取器可能只打印警告而让其余来源继续运行；工作流显示绿色不保证包含 X 内容。需同时检查日志和日报里的来源。
- 没有手动运行按钮：确认 `.yml` 文件已提交默认分支，并启用了 Actions。
- 没有准时运行：检查时区、默认分支、工作流启用状态及 GitHub 调度延迟。

官方参考：

- Apify Token：https://docs.apify.com/integrations/api
- GitHub Secrets：https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
- GitHub Variables：https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/store-information-in-variables
- 定时任务：https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule
- 下载日报附件：https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts
