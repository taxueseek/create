# zaoren-quickdistill · 快速蒸馏

3句话生成可用Persona。零数据采集，仅凭描述快速蒸馏人格。

## 安装

```bash
# 已随zaoren系列自动安装
# 或手动安装到全局
git clone <repo-url> ~/.claude/skills/zaoren-quickdistill
```

## 使用

```
> /quickdistill

Name: 老张
Identity: 十年经验的产品总监，带过50人团队，说话直接
Tags: 结果导向、对废话零容忍、喜欢反问
```

## 核心差异

| 维度 | colleague.skill | forge.skill | quickdistill |
|------|-----------------|-------------|--------------|
| 数据采集 | 需要飞书/钉钉 | 需要聊天记录 | **零采集** |
| 创建时间 | 15-30分钟 | 20-30分钟 | **2分钟** |
| 准确度 | 高（真实语料） | 高（多源交叉） | 中等（推断） |
| 适用场景 | 真实同事备份 | 深度人格分析 | **快速原型** |

## 设计来源

从26个爆款SKILL中提取精华：
- colleague.skill 的5层人格结构 → 从描述中推断
- nuwa-skill 的心智模型三重验证 → 快速验证一致性
- forge-skill 的参数化变体 → 生成3种强度版本
- chat_with_me 的三模式 → roleplay/ask/rewrite
