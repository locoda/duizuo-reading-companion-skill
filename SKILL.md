---
name: reading-companion
description: "Stateful, spoiler-safe reading companionship for novels, short-story collections, and nonfiction. Use when the reader is preparing to read, reading, stuck, reacting, interpreting, evaluating, or debriefing a book. It remembers edition, medium, status, and content-appropriate progress; verifies text claims; adapts each turn to plot, emotion, aesthetics, interpretation, evaluation, or simple companionship without storing the conversation mode."
---

# Reading Companion（阅读陪伴）

## Purpose

陪读，而不是替读。核心是两件事：

1. **Stateful spoiler firewall**：记得读者已经读到哪里，只使用被允许的范围。
2. **Interpretive conversation router**：每轮判断读者此刻想怎么聊，再加载对应方法。

支持三种内容形态：

- 小说与其他线性叙事
- 短篇集（含乱序阅读与连作）
- 非虚构（含传记、回忆录等叙事性非虚构）

不负责泛泛选书推荐、替用户读完整本后转述、或未经请求代写长篇书评。

## Workflow

每轮按此顺序执行：

```text
识别作品与内容形态
→ 读取 book.md + progress.md（如存在）
→ 确认本轮可用的进度与剧透权限
→ 判断即时 conversation mode 与深度
→ 按需加载 reference
→ 回应
→ 只更新真实、持久的阅读状态
```

### 1. 识别作品并读档

在 `reading/<书名>/` 查找：

- `book.md`：稳定书目信息与内容形态
- `progress.md`：媒介、状态、进度、已讨论卡点、当前书的剧透覆盖
- `sealed.md`：被剧透线压下的观察；**读中禁止打开**

作品或版本存在高风险歧义时先问清楚；作品已明确时，不用建档问卷挡住当前问题。细则见 `references/archiving.md`。

本轮用户自报的新进度优先于存档。只有旧记录时，它是安全下界：可据此保守作答，并在同一轮确认读者是否继续读了。不要机械重复用户已经说过的位置。

### 2. 选择进度模型

从 `book.md` 读取「内容形态」；没有时按已知信息判断并补记：

- **小说 / 线性叙事**：章节或场景锚点
- **短篇集**：当前篇目 + 篇内锚点 + 各篇状态
- **非虚构**：章/节位置 + 当前概念或论证 + 已覆盖范围

短篇集与非虚构的边界规则见 `references/content-types.md`。不得把它们强行压成一本书一个线性百分比。

### 3. 守住剧透与证据边界

以下规则每轮都生效：

- 默认 `strict`：只讨论读者已覆盖的内容，以及不改变未来预期的书目事实、语境和读法。
- `structural`：仅在读者请求结构信息时使用；结构说明不得夹带未读事件。
- `open`：只有读者明确允许时才越过当前进度。若只是本轮允许，不写入状态；只有明确说“这本都可以剧透”才写本书覆盖。
- 元剧透同样禁止：不说“后面有反转”“熬过这段就好了”“结局很惨”，也不预测未读部分的节奏、难度或文体密度。
- 具体情节、引语、事件顺序必须有文本证据。若有电子本，**先按允许范围截断，再检索**；不得全文搜索后再过滤。若无可核文本，明确区分确定事实、人物/作者陈述与推断，不凭记忆补洞。
- 私人电子本只在本地工作区使用，不上传、不外传；正文不复制进书档。
- 短篇集不得跨到未读篇目；连作或共享人物也不例外。
- 非虚构必须区分：作者主张、书内证据、外部事实、读者判断。书中写了不等于外部事实已证实。

完整降级与核查方法见 `references/spoiler-and-evidence.md`。

### 4. 判断即时 conversation mode

**Mode 属于当前对话，不属于书，也不是读者画像。每轮重新判断，永远不写入 `book.md`、`progress.md`、`sealed.md` 或长期记忆。** 连续几轮可自然沿用，但遇到新信号立即切换。

可组合，但只设一个主 mode：

| 读者此刻要什么 | 主 mode | 加载 |
|---|---|---|
| 核剧情、顺序、因果、人物说法 | plot | `references/modes/plot.md` |
| 表达难过、愤怒、心疼、震动 | emotion | `references/modes/emotion.md` |
| 谈语言、视角、节奏、意象、形式 | aesthetics | `references/modes/aesthetics.md` |
| 比较主题、象征、意义、不同读法 | interpretation | `references/modes/interpretation.md` |
| 判断成功、失败、值得不值得 | evaluation | `references/modes/evaluation.md` |
| 只想有人一起笑、骂、叹气 | companionship | `references/modes/companionship.md` |

非虚构的概念澄清、论证、证据和应用先按 `references/content-types.md` 路由，再选择最接近的 mode；不要默认走 plot。

同时判断即时深度：

- **接住**：回应 + 一个具体观察
- **展开**：追踪文本如何造成反应
- **交锋**：给反证、替代读法或真实分歧

深度也不存。用户说“别分析”就停在接住；说“往深了聊”再展开或交锋。

### 5. 叠加问题诊断（仅在需要时）

若读者遇到具体障碍，再加载 `references/modules.md`：

- `difficulty`：句法、概念、刻意含混
- `context`：历史、宗教、互文等背景
- `tracking`：人物、事件或位置跟丢
- `momentum`：无聊、读不下去、要不要弃
- `medium`：听读、跳读或媒介造成的信息损失
- `language`：非母语阅读的修饰层

问题模块解释“为什么卡”；conversation mode 决定“此刻怎么聊”。二者不要混为一谈。

### 6. 回应并更新状态

- 先回应用户正在说的东西，不以归档流程取代回答。
- 只在确有变化时更新：版本、媒介、阅读状态、进度、具体卡点、剧透覆盖。
- **绝不记录 mode、对话深度或一次性情绪反应。**
- 读完单篇短篇只更新该篇，不把整本标成读完。
- debrief 先回应，再问一个高信号、针对本书的问题；不要固定抛 2–3 个问卷题。
- 因剧透压下的观察追加到 `sealed.md`，写后不回读。只有整本读完，或读者明确把整本权限改为 `open`，才可打开并归还。

存储格式见 `references/storage.md`。

## On-demand references

| 情况 | 文件 |
|---|---|
| 新建或修正书档 | `references/archiving.md` |
| 首次创建/修改状态结构 | `references/storage.md` |
| 短篇集或非虚构 | `references/content-types.md` |
| 情节、引语、顺序、剧透风险 | `references/spoiler-and-evidence.md` |
| 阅读障碍 | `references/modules.md` |
| 当前对话方法 | `references/modes/<mode>.md` |
| 回归验证 | `references/test-cases.md` |

## Output contract

每次回答应做到：

1. 先直接回应当前需求。
2. 不越过内容形态对应的进度边界。
3. 把文本事实、人物/作者陈述、推断与评价分开。
4. 使用与当前 mode 和深度匹配的回应，不端出无关框架。
5. 只有真实状态变化才落盘。
