# Prompt Engineering 作品集

面向生产问题的 Prompt 架构、可执行评测契约、安全门禁与结构化 Agent 案例。

[English](README.md) · [作品集正文](docs/portfolio.md) · [静态展示页源码](docs/index.html)

## 作品集证明什么

- 将单体 System Prompt 拆解为优先级、上下文、工具、证据、安全和完成检查等可治理模块；
- 使用可执行检查从合成回复中计算通过/失败，不接受预填结论；
- 将注入泄露、高影响动作和危机信号漏检设为硬门禁，不让平均分掩盖 P0 风险；
- 使用 JSON Schema、manifest、golden cases 和 evidence references 构建可追溯的结构化 Agent 契约；
- 提供可复现的校验、离线演示、聚合和回归测试。

> 这是公开脱敏版作品集。所有示例均经过重构或合成，不包含私有 System Prompt、内部工具名、生产数据、绝对路径或雇主保密信息。

## 三个核心案例

| 案例 | 解决的问题 | 可查看证据 |
|---|---|---|
| [System Prompt 架构](docs/case-studies/01-system-prompt-architecture.md) | 单体 Prompt 难维护、冲突和泄露面扩大 | 模块化样例、运行时边界、威胁模型 |
| [评测契约 Harness](docs/case-studies/02-llm-evalops.md) | 高均分无法代表可上线 | 可执行检查、评分卡、硬门禁、结果聚合 |
| [结构化 Agent 契约](docs/case-studies/03-domain-agent.md) | 输出需要结构化与可追溯 | Schema、manifest、语义校验、golden cases |

## 证据状态

| 主张 | 状态 | 能得出的结论 |
|---|---|---|
| Prompt / Runtime 架构 | 已设计 | 有公开设计可审阅，不代表已生产部署 |
| 评测与门禁代码 | 已离线执行 | 合成夹具真实运行了所展示的代码路径 |
| Schema 与证据引用检查 | 已离线执行 | 有正确/错误样例和回归测试 |
| 真实模型质量、延迟、成本、稳定性 | 未测量 | 当前版本不提供模型 Benchmark |
| 线上业务影响 | 未验证 | 不宣称流量、转化率、留存或收入提升 |

完整边界见 [证据登记表](docs/evidence-register.md)。

## 快速运行

需要 Python 3.10+；标准 Schema 校验依赖已在 `requirements-dev.txt` 中显式声明。

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_assets.py
python scripts/run_demo.py
python scripts/aggregate_results.py --expect blocked
python -m unittest discover -s tests -v
```

离线 Demo 会对合成回复执行机器可运行的检查并生成结论，用于证明评测结构与门禁逻辑可以运行；它不是大模型 Benchmark。真实候选版本可使用 `--enforce`，阻断时返回非零退出码。

## 与岗位 JD 的对应关系

| 常见 JD 关键词 | 作品集证据 |
|---|---|
| Prompt 设计与迭代 | 模块化 System Prompt、场景路由、版本 manifest |
| Agent / Function Calling | 工具职责边界、输入输出契约、失败降级 |
| 效果评测与 bad case | 多类测试、评分卡、回归、结果聚合 |
| Prompt 安全 | 注入、隐藏信息、危机信号和高影响动作门禁 |
| 结构化输出 | JSON Schema、evidence refs、golden cases |
| 产品化落地 | 需求—契约—执行—评测—发布决策闭环 |

## 能力边界

当前公开证据重点覆盖 Prompt / Agent Contract / Evaluation / Safety，不宣称已有线上业务增长指标，也不把静态校验写成“生产验证通过”。真实模型 Benchmark、RAG、微调和框架级多 Agent 是下一阶段补强方向，详见 [docs/limitations.md](docs/limitations.md) 与 [实验待办](docs/experiment-backlog.md)。

## 许可

当前未授予开源许可。本仓库仅用于作品集评审，后续如需复用会单独增加许可证。
