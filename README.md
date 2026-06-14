# Create 造物.skill
一起创造新世界

最初，我们把这个项目叫造人。「你们搞大模型的简直是女娲，捏了同事，捏了前任，捏了老板，捏了导师，最后把自己也捏了一个，替自己上班。」那时候，我们像女娲一样，捏了前任、捏了老板、捏了导师，想让 AI 替我们上班。但很快我们发现，我们被人这个概念束缚了。于是便把它更名为造物。

真实的物理世界里，决定成败的往往不是某个人，一个人背后的组织才是决定这个世界走向的关键。不局限于一个人，一个职业，还可以让不同人一起开圆桌会议或者委员会讨论，更加接近真实世界的场景。单体 agent 的拟人化，只是 AI 使用的初级阶段。把隐藏在公文、财报、复盘报告背后的决策逻辑和思维方式，跟世间万物的本质提取出来，化作可以自由组合、推演碰撞的引擎，才是我们真正的天命。

License: MIT Claude Code AgentSkills

还能造什么？造人造项目造产品，万物皆可造。这就是造物主的项目，单个的蒸馏、炼化，都是属于AI使用的初级阶段。把agent和真实的人类员工组合起来创造新世界，才是我们的天命

> 「洞察 → 决策 → 执行」三层认知架构，让 AI 从聊天工具变成决策引擎。

[![Version](https://img.shields.io/badge/version-v4.1-blue)](https://github.com/taxueseek/create/releases/tag/v4.1)
[![Branch](https://img.shields.io/badge/backup-v3.0-green)](https://github.com/taxueseek/create/tree/backup/v3.0)

---

## 介绍

Create 是一套**认知世界的工具**——把隐藏在经验、文本、决策背后的逻辑，转化为可复用的 AI 工具。

不是让 AI 学说话，是让 AI 学办事。

---

## v4.1 核心升级

### 1. zaoren 决策层全面重构

v4.1 对决策层进行了从底层到顶层的翻新：

| 维度 | v4.0 | v4.1 |
|:---|:---|:---|
| 路由架构 | 扁平路由，手动选择 | 2 级优先级路由 + 消解前置 + 执行规律注入 |
| 世界数量 | 7 通用世界 + 6 组织/工具 | **9 专精认知世界** |
| 参考体系 | 3 个静态文档 | 4 个渐进式参考 + combo_map 连招网络 |
| 世界规范 | 无统一规范 | 公理/语言/硬规则/盲区/输出格式/验证方式/反模式 |
| 反模式声明 | 无 | 每个 skill 独立声明 3 条 |
| 执行效率 | 从头读到尾 | Step 0 按需注入，按需加载 |

### 2. 旧世界 → 新世界映射

```
v4.0 通用人格世界（删除）          v4.1 专精认知世界（新增）
─────────────────────────────    ────────────────────────────
zaoren-boss                       zaoren-culture    文化载体诊断
zaoren-investor                   zaoren-leader     影响力系统
zaoren-mentor                     zaoren-parents    父母视角模拟
zaoren-munger                     zaoren-process    流程节点断裂分析
zaoren-client                     zaoren-troll      杠精视角模拟
zaoren-naval                      zaoren-ulrich     组织系统能力
zaoren-review   →   zaoren-reviewer  四关审稿（完全重写）
zaoren-drucker  ✓   zaoren-drucker   保留，重写为完整世界
zaoren-roundtable ✓ zaoren-roundtable 保留，升级为置信度加权碰撞引擎
```

### 3. 三层架构

```
┌──────────────────────────────────────────┐
│  ming v2.0  洞察层 —— 看透「是什么」       │
│  中华思考者 · 哲思伙伴 · 思维兵器          │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│  zaoren v4.1 决策层 —— 判断「怎么做」      │
│  9个认知世界 + 连招网络 + 反模式声明        │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│  taxue v3.0 执行层 —— 解决「动手做」       │
│  快速解法 · 任务拆解 · 系统构建 · 版本管理  │
└──────────────────────────────────────────┘
```

**使用流程**：
```
遇到问题 → ming 想透 → zaoren 决策 → taxue 执行
```

### 4. 新架构亮点

**消解前置**：路由前先过 2 项检查（零信息/信号冲突），拦截模糊输入，减少空转。

**优先级路由**：单世界 > 圆桌碰撞 > 审稿 > 变革诊断 > 角色模拟，从上到下命中即走。

**执行规律注入（Step 0）**：grep 从 `execution-patterns.md` 按子 skill 名提取 1 条规律，7 条已积累，含置信度评级。

**连招网络（Combo Network）**：11 个 skill × 18 条组合，一个 skill 执行完毕后推荐 2 个自然延续。

**反模式声明**：每个 skill 独立声明 3 条最常见的 Agent 失败模式 + 纠正方法，质量控制内建于文件。

---

## 九世界速查

| 世界 | 核心问题 | 适用场景 |
|:---|:---|:---|
| **drucker** | 「这件事该不该做？」 | 战略取舍、放弃决策、业务评估 |
| **ulrich** | 「系统支不支持？能规模化吗？」 | 组织诊断、流程建设、团队结构 |
| **roundtable** | 「多视角碰撞后，盲区在哪？」 | 复杂决策验证、创业方向 |
| **reviewer** | 「人物立得住吗？剧情靠巧合吗？」 | 小说审稿、剧本评估、文案质量检查 |
| **culture** | 「谁在真正塑造这里的文化？」 | 变革阻力诊断、文化载体识别 |
| **leader** | 「没有职位，怎么让别人主动跟随？」 | 影响力分析、向上/跨部门推动 |
| **process** | 「流程总在同一位置卡住？」 | 交接优化、审批流诊断、瓶颈分析 |
| **parents** | 「怎么跟爸妈沟通？」 | 辞职/换工作/催婚/生活决策沟通 |
| **troll** | 「这篇文案会不会被喷？」 | 内容安全审查、争议点预判 |

---

## 安装

### 方式一：Agent Skills（推荐）

Create 是一套 Agent Skills，兼容 Claude Code、Codex、Grok Build：

```bash
# 克隆仓库
git clone https://github.com/taxueseek/create.git

# 安装 zaoren 系列
# Claude Code:
cp -r create/zaoren* ~/.claude/skills/

# Grok Build:
cp -r create/zaoren* ~/.grok/skills/

# 安装 taxue 系列（可选）
cp -r create/taxue* ~/.claude/skills/

# 验证安装
ls -d ~/.claude/skills/zaoren*   # 应看到 10 个目录
```

### 方式二：独立使用

zaoren 系列的每个 skill 都是独立的 Skill 文件，可以直接复制到对应平台的技能目录：

```bash
# 安装单个 skill（以 zaoren-drucker 为例）
cp create/zaoren-drucker/SKILL.md ~/.claude/skills/zaoren-drucker/

# 完整安装 zaoren 系列
for dir in create/zaoren*; do
  cp -r "$dir" ~/.claude/skills/;
done
```

### 方式三：增量更新

如果已经安装过旧版，建议先备份后删除再安装：

```bash
# 备份旧版
cp -r ~/.claude/skills/zaoren* ~/skills-backup-$(date +%Y%m%d)

# 删除旧版
rm -rf ~/.claude/skills/zaoren*

# 安装新版
cp -r create/zaoren* ~/.claude/skills/
```

---

## 使用

### 主入口（自动路由）

```
# 让系统自动判断你需要哪个世界
/zaoren 帮我看看这个方案的风险

# 明确指定世界
/zaoren 用德鲁克的视角看看这个项目
/zaoren 从组织能力的角度分析团队情况
```

### 直接进入特定世界

```
# 战略判断
/zaoren-drucker 这个新业务该不该做

# 组织诊断
/zaoren-ulrich 我们团队超过 10 人了，系统能撑住吗

# 文化分析
/zaoren-culture 变革推不下去，问题在哪

# 影响力分析
/zaoren-leader 我推不动这件事，怎么提高影响力

# 流程诊断
/zaoren-process 审批流程总是卡在同一个地方

# 父母沟通
/zaoren-parents 怎么跟爸妈说我想辞职

# 杠精审查
/zaoren-troll 帮我看看这篇文案会不会被喷

# 审稿
/zaoren-reviewer 帮我看看这篇小说

# 圆桌碰撞
/zaoren-roundtable 让德鲁克和尤里奇讨论一下这个决策
```

### 连招推荐

执行完一个世界后，如果对话自然结束，系统会推荐下一步：

```
接下来可能还需要：zaoren-ulrich（系统能力评估）、zaoren-roundtable（多视角碰撞）。要继续吗？
```

---

## 架构对比

### v3.x（旧版）
```
35个skill，平铺结构
├── zaoren-boss
├── zaoren-client
├── zaoren-compile
├── zaoren-content
├── zaoren-era
├── zaoren-org
├── zaoren-system
├── ...（还有很多）
```

### v4.0（上版）
```
17个skill，三层架构
├── ming（洞察层）
├── zaoren（决策层，7+6个世界）
└── taxue（执行层）
```

### v4.1（当前）
```
10个skill，决策层重构，三层架构
├── ming（洞察层）
├── zaoren（决策层，9个专精认知世界）
│   ├── 主路由：zaoren
│   └── 9个子世界：drucker/ulrich/roundtable/reviewer
│                  /culture/leader/process/parents/troll
└── taxue（执行层）
```

---

## 备份与迁移

- **v3.x 完整备份**: [`backup/v3.0`](https://github.com/taxueseek/create/tree/backup/v3.0) 分支
- **迁移指南**: 见 [MIGRATION.md](./MIGRATION.md)

---

## 核心理念

> 「单体 agent 的拟人化，只是 AI 使用的初级阶段。
> 把隐藏在公文、财报、复盘报告背后的决策逻辑，
> 化作可以自由组合、推演碰撞的引擎，
> 才是我们真正的天命。」

---

## 版本历史

| 版本 | 时间 | 核心变化 |
|:---|:---|:---|
| **v4.1** | 2026-06 | zaoren 决策层全面重构：9认知世界、消解前置、优先级路由、连招网络、反模式声明 |
| v4.0 | 2026-04 | 三层架构，统一格式，精简51% |
| v3.x | 2025 | 造境系统雏形，35个skill探索 |

---

*Create v4.1 · zaoren + taxue + ming · 2026-06-14*
