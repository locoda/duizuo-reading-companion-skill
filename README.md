# 对坐（Reading Companion）

> 读到哪，聊到哪；此刻想怎么聊，就怎么陪。

A stateful, spoiler-safe reading companion for novels, short-story collections, and nonfiction.

它做两件事：

1. 用适合内容形态的方式记住真实阅读进度；
2. 每轮根据当前对话选择回应方法，但不把 conversation mode 存成书或读者的固定属性。

## 支持内容

- 小说与其他线性叙事
- 短篇集：乱序阅读、篇目级进度、连作边界
- 非虚构：概念、论证、证据、结构与应用
- 传记、回忆录等叙事性非虚构仍保留剧透边界

## Conversation modes

按当前一轮加载：

- `plot`：事实、顺序、因果与歧义
- `emotion`：角色情绪、读者情绪与叙述诱导
- `aesthetics`：形式 → 效果 → 代价
- `interpretation`：读法、证据、反证与可信度
- `evaluation`：意图 → 实效 → 权衡 → 判断
- `companionship`：只陪在那个反应里，不强行分析

即时深度为：接住 / 展开 / 交锋。Mode 与深度都不写入书档或读者画像。

## 存储

```text
reading/<书名>/
  book.md
  progress.md
  sealed.md
```

- `book.md`：稳定、无读者痕迹的信息与内容形态
- `progress.md`：媒介、状态、内容形态对应的进度和真实卡点
- `sealed.md`：被剧透边界压下的观察；读中不得读取

不创建 `index.md`、edition/session 层或每篇短篇独立目录。私人电子本留在本地，只记路径。

## 进度模型

- 线性叙事：章/节 + 内容锚点
- 短篇集：当前篇目 + 篇内锚点 + 各篇状态
- 非虚构：章/节 + 当前概念或论证 + 已覆盖范围 + 待澄清问题

## 剧透与证据

- 默认只讨论读者确认已覆盖的范围。
- 禁止未读事件，也禁止“后面有反转”“会更好读”等元剧透。
- 精确情节、引语和事件顺序需要文本证据。
- 有电子本时先按进度截断再检索，不全文搜索后过滤。
- 非虚构区分作者主张、书内证据、外部事实和当前判断。
- `sealed.md` 只有整本读完，或读者明确把整本设为 `open` 时才可打开。

## 文件结构

- `SKILL.md`：紧凑路由器与不可违反的规则
- `references/archiving.md`：风险式建档与生命周期
- `references/storage.md`：三文件格式
- `references/content-types.md`：短篇集与非虚构
- `references/spoiler-and-evidence.md`：剧透与证据边界
- `references/modules.md`：阅读障碍诊断
- `references/modes/*.md`：即时 conversation methods
- `references/test-cases.md`：行为回归测试

## 安装

```bash
npx skills add locoda/reading-companion-skill
```

MIT License.
