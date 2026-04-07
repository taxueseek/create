---
name: zaoren-upgrade
description: |
  升级 zaoren 系列 skills 到最新版本

  触发：/zaoren-upgrade、/升级zaoren、「升级造境技能」
---

# zaoren-upgrade

升级 zaoren 系列 skills 到最新版本。

## 升级流程

**Step 1: 检测安装位置**
- 检查 `~/.config/agents/skills`、`~/.claude/skills`、`~/.agents/skills`
- 找到包含 `zaoren/` 的目录

**Step 2: 获取当前版本**
- 从 `zaoren/SKILL.md` 提取版本信息（如有 VERSION 文件优先）

**Step 3: 获取远程版本**
- 从 GitHub 仓库获取 VERSION 文件
- 网络失败时提示手动升级选项

**Step 4: 版本比较**
- 版本相同 → 提示已是最新，结束
- 有新版本 → 继续升级

**Step 5: 备份当前版本**
- 创建带时间戳的备份目录 `.zaoren-backup-YYYYMMDD-HHMMSS`
- 保留 `zaoren-upgrade` 本身不被备份

**Step 6: 下载最新版本**
- `git clone --depth 1` 从 GitHub 拉取最新代码
- 失败时从备份恢复

**Step 7: 验证下载内容**
- 检查 `zaoren*/` 目录存在
- 结构异常时提示并退出

**Step 8: 替换旧版本**
- 删除旧 `zaoren*` skills（保留 `zaoren-upgrade`）
- 复制新版本到安装目录
- 复制失败时自动从备份恢复

**Step 9: 显示更新内容**
- 提取新版本号
- 显示更新要点（从 CHANGELOG 或 git log）
- 提供完整日志链接

**Step 10: 验证安装**
- 检查关键 skill 的 SKILL.md 存在

## 离线升级

```bash
zaoren-upgrade --local /path/to/downloaded/zaoren-skills
```

跳过 git clone，直接使用本地路径。

## 错误处理

| 场景 | 处理 |
|------|------|
| 找不到本地 skills | 提示安装位置，退出 |
| 网络失败 | 提示手动下载选项，退出 |
| git clone 失败 | 从备份恢复，提示检查仓库地址 |
| 文件复制失败 | 从备份恢复，提示磁盘空间/权限问题 |
| 版本号无法解析 | 继续升级，显示 unknown |

## 备份策略

- 每次升级自动创建带时间戳的备份
- 保留 7 天，自动清理脚本（可选添加到 crontab）

```bash
find "$SKILL_DIRS" -name ".zaoren-backup-*" -type d -mtime +7 -exec rm -rf {} +
```

## 版本号规则

- 格式：`v{major}.{minor}`（如 v1.2）
- 从 `zaoren/VERSION` 或 `zaoren/SKILL.md` 提取
- 远程版本从 GitHub 仓库根目录 VERSION 文件获取

## 注意事项

1. **只升级 zaoren 系列**：不触碰其他 skills（包括 taxue）
2. **保留 zaoren-upgrade**：升级过程中不删除自身
3. **原子操作**：失败时自动回滚到备份版本
4. **GitHub 依赖**：默认从 zaoren 官方仓库获取更新

---
*zaoren-upgrade · 让造境 skills 保持最新*
