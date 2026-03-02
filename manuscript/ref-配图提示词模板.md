# 《效率倍增的 AI Agent 工作流》- 统一配图提示词模板

为了保证全书配图在色彩、画风、隐喻和文字排版上的高度一致性，所有的概念插图、场景说明图都应严格使用以下模板结构进行生成。

## 🎨 核心视觉设定 (Design System)

1. **整体风格与媒介**：采用充满活力的手绘涂鸦笔记 (Sketchnote) 风格，专业知识笔记的“学霸”风格，不要太卡通。结构极度精炼，大面积留白。
2. **线条特征**：所有轮廓线使用深棕色、略带抖动的不完美手绘线条，给人一种柔软、亲切的感觉。
3. **配色方案 (关键)**：画面主体五彩斑斓。采用明亮、清新、和谐的色彩组合（海军蓝 `#1E3A8A`，浅蓝 `#60A5FA`，金色 `#F59EOB`，背景为带有纸张纹理的奶油色 `#FEFCE8`）。填充模仿彩铅或水彩质感，有自然笔触。
4. **字体要求 (关键)**：在画面核心位置直接生成简体中文的手写体汉字。标题关键词加粗并带边框。不要使用死板的电脑字体，与插图融为一体。
5. **构图与尺寸**：最高清 4K 分辨率，比例强制要求为 **横板 4:3 (Horizontal 4:3 ratio)**。

---

## 📝 提示词万能公式 (Prompt Formula)

使用以下中英文结合的结构化 Prompt 喂给 AI 绘图工具（如 Nano Banana 2 / DALL-E 3 等多模态旗舰模型）：

### 中英文联合提示词模板：

```text
A minimalist sketchnote infographic illustration, horizontal 4:3 aspect ratio, 4k high resolution. Layout must be extremely simplified with plenty of negative space cream beige paper texture background (#FEFCE8). 

Art style: Professional study notes style, not too cartoonish. Dark brown imperfect hand-drawn, slightly trembling outlines. Colored with light watercolor and colored pencil textures, natural strokes. Bright, fresh harmonious colors: navy blue (#1E3A8A), light blue (#60A5FA), gold (#F59EOB). 

Content: [画面主体的精简描述，例如：左侧画一个乱糟糟的手绘齿轮代表旧方式，右侧画一个整洁可爱的传送带代表新方式，中间用彩色手绘箭头连接]. 

Text requirements: The image MUST strictly render the following text in legible, bold Chinese handwriting style. At the top: "【需要生成的精确中文大标题】". Next to the graphics: "【需要生成的精确中文副标题】". No English words allowed, only the specified simplified Chinese characters.
```

---

## 🛠️ 典型场景生成样例

### 场景 1：手工作坊 vs 智能工厂（第1章）
> **Prompt**: A minimalist sketchnote infographic illustration, horizontal 4:3 aspect ratio, 4k high definition. Layout must be extremely simplified with plenty of negative space cream beige paper texture background. Professional study notes style. Dark brown imperfect hand-drawn outlines, light watercolor textures (navy blue, light blue, gold). Left side: a single messy gear and wrench doodle. Right side: a single cute automated conveyor belt doodle. A hand-drawn arrow pointing from left to right. The text MUST strictly be written in bold Simplified Chinese handwriting: On the left write "手工作坊", and on the right write "智能工厂". No other English text.

### 场景 2：AI Agent 员工（第2章）
> **Prompt**: A minimalist sketchnote infographic illustration, horizontal 4:3 aspect ratio, 4k high definition. Layout must be extremely simplified with plenty of negative space cream beige paper texture background. Professional study notes style. Dark brown imperfect hand-drawn outlines, light watercolor textures (navy blue, light blue, gold). Center: a simple, cute robot worker holding a glowing puzzle piece or gear. Colorful hand-drawn doodle layouts, sparks and stars. The text MUST strictly be written in bold Simplified Chinese handwriting. Above the robot write: "AI 智能体". Below write: "自动化执行". No other text.
