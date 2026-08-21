# Prompt Engineering 作品集

面向生产环境的 Prompt 架构、评测、安全治理与领域 Agent 案例。

[English](README.md) · [作品集正文](docs/portfolio.md) · [静态展示页源码](docs/index.html)

## 作品集证明什么

- 将单体 System Prompt 拆解为优先级、上下文、工具、证据、安全和完成检查等可治理模块；
- 将“主观试玩”升级为带测试契约、评分卡、仲裁和发布门禁的 EvalOps；
- 将注入泄露、高影响动作和危机信号漏检设为硬门禁，不让平均分掩盖 P0 风险；
- 使用 JSON Schema、manifest、golden cases 和 evidence references 构建可追溯领域 Agent；
- 通过纯 Python 标准库提供可复现的校验、离线演示、聚合和回归测试。

> 这是公开脱敏版作品集。所有示例均经过重构或合成，不包含私有 System Prompt、内部工具名、生产数据、绝对路径或雇主保密信息。

## 三个核心案例

| 案例 | 解决的问题 | 可查看证据 |
|---|---|---|
| [System Prompt 架构](docs/case-studies/01-system-prompt-architecture.md) | 单体 Prompt 难维护、冲突和泄露面扩大 | 模块化样例、运行时边界、威胁模型 |
| [LLM EvalOps](docs/case-studies/02-llm-evalops.md) | 高均分无法代表可上线 | 测试契约、评分卡、硬门禁、结果聚合 |
| [领域 Agent](docs/case-studies/03-domain-agent.md) | 专业输出需要结构化与可追溯 | Schema、manifest、golden cases、证据引用 |

## 快速运行

仅需 Python 3.10+，无需安装第三方依赖。

```bash
python scripts/validate_assets.py
python scripts/run_demo.py
python scripts/aggregate_results.py
python -m unittest discover -s tests -v
```

离线 Demo 是确定性契约演示，用于证明评测结构与门禁逻辑可以运行；它不冒充真实大模型 Benchmark。

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

当前公开证据重点覆盖 Prompt / Agent / Evaluation / Safety，不宣称已有线上业务增长指标，也不把静态校验写成“生产验证通过”。RAG、微调和框架级多 Agent 是下一阶段补强方向，详见 [docs/limitations.md](docs/limitations.md)。

## 许可

当前未授予开源许可。本仓库仅用于作品集评审，后续如需复用会单独增加许可证。
