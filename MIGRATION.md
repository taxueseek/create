# 迁移指南

## 概述

| 版本 | 核心变化 |
|:---|:---|
| **v3.x → v4.0** | 35 skill 精简为 17 个，建立三层架构（ming → zaoren → taxue） |
| **v4.0 → v4.1** | zaoren 决策层全面重构：9专精认知世界取代旧通用人格世界 |

---

# v4.0 → v4.1 迁移

## 为什么升级

v4.0 的 zaoren 保留了旧版「通用人格」世界（boss/investor/mentor 等），这些世界的判断逻辑过于泛化，无法提供深度认知价值。v4.1 将其替换为 9 个**专精认知世界**，每个世界有独立公理、硬规则、盲区、反模式声明和验证方式。

## 变更总览

| 变更类型 | 数量 | 说明 |
|:---|:---|:---|
| 删除 | 11 | 旧通用人格世界 |
| 新增 | 7 | 专精认知世界 |
| 重写 | 2 | drucker（完整世界化）、roundtable（置信度碰撞引擎） |
| 保留 | 0 | 无任何旧世界原样保留 |

## 具体迁移路径

### 被删除的 skill（不再存在）

| 旧 skill | 替代方案 |
|:---|:---|
| `zaoren-boss` | → `zaoren-drucker` 战略有效性判断 |
| `zaoren-investor` | → `zaoren-ulrich` 组织系统能力评估 |
| `zaoren-mentor` | → `zaoren-leader` 影响力分析 + 个人成长 |
| `zaoren-munger` | → `zaoren-roundtable` 多视角碰撞 |
| `zaoren-client` | → `zaoren-drucker` 顾客价值判断 |
| `zaoren-naval` | → 已不在 zaoren 体系内，使用 ming |
| `zaoren-compare` | → `zaoren-roundtable` 多视角对比 |
| `zaoren-committee` | → `zaoren-roundtable` 陪审团决策模式 |
| `zaoren-decision` | → 不再单独存在，决策过程融入各世界 |
| `zaoren-insight` | → 已不在 zaoren 体系内，使用 ming |
| `zaoren-review` | → `zaoren-reviewer` 四关审稿系统（完全重写） |

### 新增的 skill（7 个）

| skill | 核心定位 | 使用场景 |
|:---|:---|:---|
| `zaoren-culture` | 文化载体分析 | 变革推不下去、文化价值观诊断 |
| `zaoren-leader` | 领导力影响系统 | 没有权力想推动、分析影响力 |
| `zaoren-parents` | 父母视角模拟 | 怎么跟爸妈说、父母不理解 |
| `zaoren-process` | 流程节点断裂分析 | 流程卡住、交接问题、审批流 |
| `zaoren-reviewer` | 毒舌书评人审稿 | 小说审稿、文案质量检查 |
| `zaoren-troll` | 杠精视角模拟 | 文案会不会被喷、争议预判 |
| `zaoren-ulrich` | 组织系统能力 | 系统支撑、规模化、组织能力 |

### 重写的 skill（2 个）

| skill | v4.0 | v4.1 |
|:---|:---|:---|
| `zaoren-drucker` | 简短视角描述 | 完整世界：4 公理 + 4 硬规则 + 盲区 + 结构化输出格式 |
| `zaoren-roundtable` | 简单多角色讨论 | 置信度加权碰撞引擎：7 公理 + 3 协议 + 8 硬规则 + 交锋信号 + Shapley 归因 |

### 其他变更

| 文件 | 变更 |
|:---|:---|
| `zaoren/SKILL.md` | 从扁平路由 → 2 级优先级路由 + 消解前置 + 连招网络 |
| `zaoren/references/` | 旧 3 文件（analysis-guide/routing-guide/team-guide）→ 新 4 文件（world-cheatsheet/system-boundaries/edge-cases/execution-patterns）|
| `zaoren/combo_map.json` | 新增：11 skill × 18 连招 |
| `taxue/SKILL.md` | 移除 `zaoren-naval` 引用 → 指向 ming |
| `taxue-upgrade/SKILL.md` | 示例从 zaoren-boss → zaoren-drucker |

## 安装 v4.1

```bash
# 1. 备份旧版
cp -r ~/.claude/skills/zaoren* ~/skills-backup-$(date +%Y%m%d)

# 2. 删除旧版（如果从 v4.0 升级）
rm -rf ~/.claude/skills/zaoren-boss
rm -rf ~/.claude/skills/zaoren-client
rm -rf ~/.claude/skills/zaoren-committee
rm -rf ~/.claude/skills/zaoren-compare
rm -rf ~/.claude/skills/zaoren-decision
rm -rf ~/.claude/skills/zaoren-insight
rm -rf ~/.claude/skills/zaoren-investor
rm -rf ~/.claude/skills/zaoren-mentor
rm -rf ~/.claude/skills/zaoren-munger
rm -rf ~/.claude/skills/zaoren-naval
rm -rf ~/.claude/skills/zaoren-review

# 3. 安装 v4.1
git clone https://github.com/taxueseek/create.git
cp -r create/zaoren* ~/.claude/skills/
cp -r create/taxue* ~/.claude/skills/

# 4. 验证
ls -d ~/.claude/skills/zaoren*
# 输出: zaoren  zaoren-culture  zaoren-drucker  zaoren-leader
#       zaoren-parents  zaoren-process  zaoren-reviewer
#       zaoren-roundtable  zaoren-troll  zaoren-ulrich
```

## 使用变更

| v4.0 命令 | v4.1 命令 |
|:---|:---|
| `/zaoren-boss` | `/zaoren-drucker` |
| `/zaoren-investor` | `/zaoren-ulrich` |
| `/zaoren-mentor` | `/zaoren-leader` |
| `/zaoren-review` | `/zaoren-reviewer` |
| `/zaoren-compare` | `/zaoren-roundtable` |
| `/zaoren-committee` | `/zaoren-roundtable`（陪审团模式） |
| `/zaoren-naval` | 使用 `ming` 系列 |
| `/zaoren-insight` | 使用 `ming` 系列 |

---

# v3.x → v4.0 迁移

## 概述

v4.0 是一次架构级重构，从平铺的 35 个 skill 精简为三层架构的 17 个 skill。

## 变更总览

| 变更类型 | 数量 | 说明 |
|:---|:---|:---|
| 保留 | 10个 | 核心决策世界 |
| 重写 | 7个 | 统一格式 |
| 合并 | 3个 | 功能整合 |
| 删除 | 15个 | 低频或重叠 |

## 具体迁移路径

### 1. 入口变更

| 旧命令 | 新命令 | 说明 |
|:---|:---|:---|
| `/zaoren` | `/zaoren` | 不变，但路由更精简 |
| `/zaoren-quickdistill` | 直接使用角色层 | 删除，不再单独存在 |

### 2. 角色层迁移

| 旧skill | 新skill | 迁移方式 |
|:---|:---|:---|
| `zaoren-boss` | `zaoren-boss` v4.0 | ✅ 保留，格式统一 |
| `zaoren-client` | `zaoren-client` v4.0 | ✅ 保留，格式统一 |
| `zaoren-investor` | `zaoren-investor` v4.0 | ✅ 保留，格式统一 |
| `zaoren-mentor` | `zaoren-mentor` v4.0 | ✅ 保留，重写统一格式 |
| `zaoren-munger` | `zaoren-munger` v4.0 | ✅ 保留，重写统一格式 |
| `zaoren-drucker` | `zaoren-drucker` v4.0 | ✅ 保留，重写统一格式 |
| `zaoren-naval` | `zaoren-naval` v4.0 | 🆕 新增（从ming并入） |

### 3. 组织层迁移

| 旧skill | 新skill | 迁移方式 |
|:---|:---|:---|
| `zaoren-roundtable` | `zaoren-roundtable` v4.0 | ✅ 保留，知识探索定位 |
| `zaoren-committee` | `zaoren-committee` v4.0 | ✅ 保留，补充权力博弈细节 |
| `zaoren-compare` | `zaoren-compare` v4.0 | ✅ 保留，统一格式 |

### 4. 工具层迁移

| 旧skill | 新skill | 迁移方式 |
|:---|:---|:---|
| `zaoren-insight` | `zaoren-insight` v4.0 | ✅ 保留，统一格式 |
| `zaoren-decision` | `zaoren-decision` v4.0 | ✅ 保留 |
| `zaoren-review` | `zaoren-review` v4.0 | ✅ 保留 |

### 5. 编译工具迁移

| 旧skill | 新skill | 迁移方式 |
|:---|:---|:---|
| `zaoren-compile` | `taxue-build --persona` | 🔀 合并，双模式 |
| `taxue-build` | `taxue-build --solution` | 🔀 增强，双模式 |

### 6. 删除的技能

以下 skill 不再作为独立 skill 存在：

| 技能 | 原因 | 替代方案 |
|:---|:---|:---|
| `zaoren-content` | 与 taxue 重叠 | 使用 `taxue-content` |
| `zaoren-infographic` | 与 taxue 重叠 | 使用 `taxue-infographic` |
| `zaoren-quickdistill` | 功能弱化 | 直接使用角色层 |
| `zaoren-era` | 低频 | 使用 `ming` 系列 |
| `zaoren-org` | 功能模糊 | 删除 |
| `zaoren-system` | 过于抽象 | 删除 |
| `zaoren-troll` | 用户排斥名字 | 作为 `roundtable` 压力测试模式 |
| `zaoren-reviewer` | 与 troll 重叠 | 作为 `roundtable` 压力测试模式 |
| `zaoren-reader` | 低频 | 作为 `taxue-content` 读者测试步骤 |
| `zaoren-parents` | 并入 mentor | 使用 `zaoren-mentor` 家庭子模式 |
| `zaoren-kol` | 低频 | 删除 |
| `zaoren-lawyer` | 专业度不够 | 删除 |
| `zaoren-coach` | 与 mentor 重叠 | 使用 `zaoren-mentor` |
| `zaoren-dijian` | 与 insight 重叠 | 使用 `zaoren-insight` |
| `zaoren-feisheng` | 功能不明确 | 删除 |

## 新功能（v4.0）

### taxue-upgrade（版本管理）

```bash
# 检测可更新
/upgrade

# 升级全部
/upgrade all

# 回滚
/upgrade --rollback 2026-04-07-143022
```

### taxue-build 双模式

```bash
# 从解法编译（轻量）
/build --solution

# 从人物编译（完整世界）
/build --persona
```

---

## 备份

v3.x 完整备份在 [`backup/v3.0`](https://github.com/taxueseek/create/tree/backup/v3.0) 分支。

如需继续使用 v3.x：
```bash
git checkout backup/v3.0
```

---

## 反馈

如有迁移问题，请在 [Issues](https://github.com/taxueseek/create/issues) 反馈。
