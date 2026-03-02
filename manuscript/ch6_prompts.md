# 第六章《让流程进入日常：从试跑到稳定执行》配图生图提示词

请将以下提示词直接复制粘贴给 Gemini 等支持生图的大模型（建议使用英文版以获得更稳定画质，但其中的中文必须原样保留）。本章配图继续采用**结构化高级信息图（Infographic）**的统一风格。

---

## 配图 1：MVP 试跑逻辑（6.1 节）
**用途**：对比“追求完美导致烂尾”和“MVP（最小可行性产品）快速跑通”两种心态。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: A split-screen horizontal comparison. A "VS" symbol in the middle.
> - Left card (Light orange background): A stick figure crying while trying to build a massive, overwhelmingly complex and exploding rocket ship before taking a single step.
> - Right card (Light mint green background): A happy stick figure successfully riding a simple, functional skateboard or scooter forward.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the diagram: "试跑的第一原则".
> - In Left card write: Title "错误：追求完美", Subtitle "预想 100 种情况才敢跑". Bullet 1: "全量数据一次性投入". Bullet 2: "遇到报错直接放弃". Bottom badge: "结果：永远无法上线". 
> - In Right card write: Title "正确：MVP试跑", Subtitle "先跑通，再跑对". Bullet 1: "切 10 行数据做低风险测试". Bullet 2: "容忍局部错误，重点看主流程". Bottom badge: "结果：获得真实反馈". 
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter6_mvp_testing.png`

---

## 配图 2：红绿灯检查机制（6.2 节）
**用途**：明确在自动化流程中，哪些环节必须留有“人工安检站”。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: Three horizontal rows or vertical cards arranged to represent a traffic light system (Green, Yellow, Red). 
> - Green section (Light green): A robot sprinting freely on a track.
> - Yellow section (Light yellow): A robot handing a draft document to a human for editing.
> - Red section (Light red): A robot standing behind a locked gate, waiting for a human to press a giant "Confirm" button.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the diagram write: "流程中的人工安检站".
> - In Green section write: "绝对绿灯 (全自动)", Below it: "资料归档 / 录音整理", "错也无妨，后续可修".
> - In Yellow section write: "警戒黄灯 (人机共创)", Below it: "写草稿 / 发周报", "AI 铺底，人工润色发出".
> - In Red section write: "禁行红灯 (强制确认)", Below it: "报价 / 转账 / 公关稿", "涉及底线，必须人工签字放行". 
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter6_traffic_light_checkpoints.png`

---

## 配图 3：错题本与打补丁机制（6.3 节）
**用途**：改变读者对 Agent 报错的畏惧心理，将其视为优化提示词的养料。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: A split-screen horizontal comparison. A "VS" symbol in the middle.
> - Left card (Light pink background): A human angrily sweeping trash (representing bugs) under a rug, while a robot repeatedly trips over the same stone.
> - Right card (Light blue background): A human happily picking up the trash (bug), forging it into a shiny gear (patch), and inserting it into the robot's head.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the diagram: "面对报错的两种态度".
> - In Left card write: Title "掩耳盗铃", Subtitle "手动改掉就完事". Bullet 1: "同一条错下周接着犯". Bullet 2: "永远离不开人工干预". Bottom badge: "流程永远是婴儿". 
> - In Right card write: Title "打补丁机制", Subtitle "把错误变成养料". Bullet 1: "定位偏差，修改源头 JD". Bullet 2: "写入禁令（如：不许编数据）". Bottom badge: "流程越用越聪明". 
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter6_bug_patching.png`

---

## 配图 4：V1 到 V3 的工作流演进路径（6.4 节）
**用途**：展示一个工作流从诞生到成熟的三个阶段，进行合理的预期管理。

> **Prompt:**
> A minimalist sketchnote infographic illustration, horizontal 16:9 aspect ratio, 4k high definition. Layout must be clean with plenty of negative space cream beige paper texture background (#FEFCE8). Professional study notes or presentation slide style. Dark brown imperfect hand-drawn outlines, light watercolor textures used for card backgrounds. 
> 
> Content: Three vertical rectangular cards arranged side-by-side, connected by forward arrows showing an evolutionary upgrade.
> - Left card (Light gray/yellow): A wobbly, hand-drawn tricycle or a baby crawling. 
> - Middle card (Light blue): A sturdy, functional bicycle or a person walking briskly.
> - Right card (Light mint green): A sleek, high-speed sports car or a rocket soaring.
> 
> Text requirements: The image MUST strictly render the following text in legible, bold Simplified Chinese handwriting style. Above the diagram: "工作流的演进路径".
> - In Left card write: Title "V1.0 婴儿期", Subtitle "首要目标：跑通". Bullet 1: "状态：经常报错磕磕绊绊". Bullet 2: "动作：人盯着跑主流程". Bottom badge: "容忍局部错误". 
> - In Middle card write: Title "V2.0 成长期", Subtitle "首要目标：跑对". Bullet 1: "状态：偶遇边缘情况失效". Bullet 2: "动作：打补丁，堵住漏洞". Bottom badge: "追求输出稳定". 
> - In Right card write: Title "V3.0 成熟期", Subtitle "首要目标：跑快". Bullet 1: "状态：敢放进后台无人值守". Bullet 2: "动作：优化成本与并发数". Bottom badge: "释放个人生产力". 
> No other English text.
>
> 📁 **推荐保存文件名**: `chapter6_workflow_evolution.png`
