# 第五章《给 Agent 写一份清楚的"岗位说明书"》配图生图提示词

请将以下提示词直接复制粘贴给 Gemini 等支持生图的大模型（建议使用英文版以获得更稳定画质，但其中的中文必须原样保留）。本章配图继续采用**结构化高级信息图（Infographic）**的统一风格，强化“模具化、标准化”的视觉感受。

---

## 配图 1：Agent 岗位说明书的四大要素（5.1 节）
**用途**：帮助读者记忆撰写一个及格 Agent 提示词必须具备的四个核心模块。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: A large 2x2 grid layout (four quadrants), acting as a "blueprint" or "ID badge" for a robot. 
> - Top-left quadrant (Light blue): Icon of a glowing target or compass.
> - Bottom-left quadrant (Light orange): Icon of an inbox tray or a magnifying glass over documents.
> - Top-right quadrant (Light green): Icon of a neatly formatted checklist or a gift box.
> - Bottom-right quadrant (Light red/pink): Icon of a stop sign, caution tape, or a fence.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the grid write: "Agent 岗位说明书 (JD) 四要素".
> - In Top-left write: "1. 工作目的", Below it: "解决什么问题？", "明确阅读对象与用途".
> - In Bottom-left write: "2. 输入来源", Below it: "提供什么原料？", "明确物理隔离的安全边界".
> - In Top-right write: "3. 输出成果", Below it: "交付物长什么样？", "锁定结构、格式与字数".
> - In Bottom-right write: "4. 限制条件", Below it: "绝不能做什么？", "设定语气禁区与逻辑红线".
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter5_four_elements_of_jd.png`

---

## 配图 2：三类核心 Agent 岗位画像（5.2 节）
**用途**：说明不同类型的任务需要雇佣不同特长的“数字员工”，坚决不要大包大揽的全能助理。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: Three vertical rectangular cards arranged side-by-side. 
> - Left card (Light blue): A robot wearing a librarian's glasses, holding a magnifying glass and a neat stack of files.
> - Middle card (Light yellow): A robot wearing a judge's wig or detective hat, holding a balancing scale or a gavel.
> - Right card (Light orange): A robot wearing a beret, typing on a vintage typewriter or holding a quill pen.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the diagram write: "三类核心 Agent 岗位对应".
> - In Left card write: Title "信息类 Agent", Subtitle "档案管理员". Bullet 1: "专注搜集整理资料". Bullet 2: "红线：只陈述事实，不编造". Bottom badge: "交付：干净资料包". 
> - In Middle card write: Title "分析类 Agent", Subtitle "铁面判官". Bullet 1: "基于证据推导结论". Bullet 2: "红线：禁凭空猜测". Bottom badge: "交付：有据可依的判断". 
> - In Right card write: Title "写作类 Agent", Subtitle "戴镣铐的代笔人". Bullet 1: "按结构填充给定的要点". Bullet 2: "红线：不负责想观点". Bottom badge: "交付：标准排版文案". 
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter5_three_agent_types.png`

---

## 配图 3：为什么要拆分 Agent？避免认知脑裂（5.3 节）
**用途**：用视觉化比喻解释为什么不能让一个 Agent 同时做找资料、做判断和写文章这三件矛盾的事。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: A split-screen horizontal comparison. A "VS" symbol in the middle.
> - Left card (Light red/pink background): A chaotic scene. One extremely stressed robot with six arms trying to chop vegetables, stir a burning pot, and read a recipe all at once. Ingredients are flying everywhere.
> - Right card (Light mint green background): An orderly and peaceful relay race scene. Robot A (sous-chef) neatly hands a chopped bowl of ingredients (a baton) to Robot B (head chef) waiting at the stove.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the diagram: "拆分 Agent 的本质原因".
> - In Left card write: Title "全能型 Agent", Subtitle "认知与逻辑打架". Bullet 1: "边搜集边判断，易带偏见". Bullet 2: "边写作边精简，精神分裂". Bottom badge: "结果：四不像的废件". 
> - In Right card write: Title "流水线 Agent", Subtitle "上游终点即下游起点". Bullet 1: "专注单点，降低犯错概率". Bullet 2: "通过接力棒传递确定信息". Bottom badge: "结果：极度稳定的输出". 
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter5_split_agent_relay.png`

---

## 配图 4：随意指令 vs 结构化说明书（5.4 节实例演示）
**用途**：直观对比“一句话 Prompt”与“万能 JD 模板”带来的降维打击。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: A split-screen horizontal comparison. A "VS" symbol in the middle.
> - Left card (Light orange background): A simple chat bubble from a human saying a casual sentence, leading to a robot producing a generic, boring piece of paper marked with a large "Zzz".
> - Right card (Light blue background): A highly structured blueprint document with sections like "Role", "Rules", "Input", leading to a robot producing a shiny, beautifully crafted masterwork document with a gold star.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the diagram: "提示词的进化".
> - In Left card write: Title "小白：随意聊天", Subtitle "帮我写篇小红书笔记". Bullet 1: "依赖 AI 自行脑补". Bullet 2: "语气虚假，AI味极重". Bottom badge: "一锤子买卖，无法复用". 
> - In Right card write: Title "高手：结构化 JD", Subtitle "设定角色、红线与目标". Bullet 1: "框死格式与情绪价值". Bullet 2: "拒绝空话，直击痛点". Bottom badge: "数字资产，随时唤起即插即用". 
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter5_bad_prompt_vs_good_jd.png`
