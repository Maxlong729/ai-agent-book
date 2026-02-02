# 书稿目录（manuscript）

本目录按「第 01 章、第 02 章…」命名，便于续写和在 Cursor 中用 `@` 引用。

| 文件 | 内容 |
|——|——|
| `00-前言.md` | 前言 |
| `01-第01章.md` | 第 1 章 重新认识AI、Agent与工作流 |
| `02-第02章.md` | 第 2 章 Agent与普通AI工具的本质区别 |

**引用方式**：在 Cursor 中可输入 `@manuscript/01-第01章.md` 等，将对应章节带入上下文。

**转换方式**：
- **按章拆分**：`scripts/docx_to_md.py`（Python 标准库，不依赖 pandoc）→ 得到 `00-前言.md`、`01-第01章.md` 等。
- **整稿 + 表格/格式更好**：`./scripts/docx_to_md_pandoc.sh`（需已安装 pandoc）→ 得到 `manuscript/full-pandoc.md`，表格、列表等保留更完整。
- **批注**：pandoc 默认不会把 Word 批注写进 Markdown；批注仍在原 .docx 中，需要时可手动整理到正文或脚注。
