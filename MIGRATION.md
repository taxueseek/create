# 迁移指南：v3.x → v4.0

## 概述

v4.0 是一次架构级重构，从平铺的 35 个 skill 精简为三层架构的 17 个 skill。

## 变更总览

| 变更类型 | 数量 | 说明 |
|:---|:---|:---|
| 保留 | 10个 | 核心决策世界 |
| 重写 | 7个 | 统一格式 |
| 合并 | 3个 | 功能整合 |
| 删除 | 15个 | 低频或重叠 |

---

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

---

## 新功能

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

## 升级步骤

1. **备份当前 skill**
   ```bash
   cp -r ~/.claude/skills ~/skills-backup-$(date +%Y%m%d)
   ```

2. **删除旧 skill**
   ```bash
   rm -rf ~/.claude/skills/zaoren*
   rm -rf ~/.claude/skills/taxue*
   ```

3. **安装新版**
   ```bash
   git clone https://github.com/taxueseek/create.git
   cp -r create/zaoren* ~/.claude/skills/
   cp -r create/taxue* ~/.claude/skills/
   ```

4. **验证**
   ```bash
   ls ~/.claude/skills/ | grep -E "^(zaoren|taxue)"
   # 应该看到 17 个目录
   ```

---

## 反馈

如有迁移问题，请在 [Issues](https://github.com/taxueseek/create/issues) 反馈。
