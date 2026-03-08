#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将全书合并为单一 Markdown，统一标题层级与注释格式。"""

import re
from pathlib import Path

MANUSCRIPT_DIR = Path(__file__).resolve().parent.parent / "manuscript"
OUTPUT_FILE = MANUSCRIPT_DIR / "full-book.md"

# 篇名：在该章前插入（仅当为新篇时），与「前言」同级，用 ##
PARTS = {
    1: "## 第一篇　为什么你需要一套 AI Agent 工作流",
    4: "## 第二篇　从零搭建一套属于你的 AI Agent 工作流",
    7: "## 第三篇　五类典型人群的工作流范式",
    12: "## 第四篇　把你的 AI Agent 工作流升级成个人工作系统",
}

BOOK_TITLE = "《效率倍增的 AI Agent 工作流：从零搭建一套你的智能体工作方式》"


def adjust_headings_preface(text: str) -> str:
    """前言：# → ##，## → ###"""
    lines = text.split("\n")
    out = []
    for line in lines:
        if line.startswith("# 前言"):
            out.append("## 前言")
        elif line.startswith("## "):
            out.append("### " + line[3:])
        else:
            out.append(line)
    return "\n".join(out)


def adjust_headings_chapter(text: str) -> str:
    """章节：从最深到最浅替换，避免重复。# → ###，## → ####，### → #####，#### → ######"""
    # 从最深层级开始替换（#### → ######，### → #####，## → ####，# 第X章 → ###）
    text = re.sub(r"^(#### )(.+)$", r"###### \2", text, flags=re.MULTILINE)
    text = re.sub(r"^(### )(.+)$", r"##### \2", text, flags=re.MULTILINE)
    text = re.sub(r"^(## )(.+)$", r"#### \2", text, flags=re.MULTILINE)
    text = re.sub(r"^(# )(第[0-9]+章 .+)$", r"### \2", text, flags=re.MULTILINE)
    return text


def normalize_notes(text: str) -> str:
    """统一导出更稳定的 Markdown 结构。"""
    lines = text.split("\n")
    out: list[str] = []

    def is_image(line: str) -> bool:
        return bool(re.match(r"^!\[[^\]]*\]\([^)]+\)$", line.strip()))

    def is_standalone_bold(line: str) -> bool:
        return bool(re.match(r"^\*\*.+\*\*$", line.strip()))

    def starts_bold_text(line: str) -> bool:
        return line.lstrip().startswith("**")

    def starts_table(line: str) -> bool:
        return line.lstrip().startswith("|")

    def starts_list(line: str) -> bool:
        stripped = line.lstrip()
        return stripped.startswith(("* ", "*\t", "- ", "+ ")) or bool(re.match(r"^\d+\.\s", stripped))

    def strip_quote_prefix(line: str) -> str:
        if line.startswith("> "):
            return line[2:]
        if line == ">":
            return ""
        return line

    def is_quote_table_row(line: str) -> bool:
        return line.startswith("> |")

    def is_quote_example_line(line: str) -> bool:
        return line.startswith("> Step ") or line.startswith("> 🎯 ") or line.startswith("> 拆解结果：")

    i = 0
    while i < len(lines):
        line = lines[i]

        # 把“引用块里的步骤 + 表格”改写成普通段落/表格，保证 Word 能识别表格。
        if is_quote_example_line(line):
            out.append(strip_quote_prefix(line))
            i += 1
            first_table_row = True
            while i < len(lines):
                current = lines[i]
                if current == ">":
                    out.append("")
                    i += 1
                    continue
                if is_quote_table_row(current):
                    if first_table_row and out and out[-1] != "":
                        out.append("")
                    out.append(strip_quote_prefix(current))
                    first_table_row = False
                    i += 1
                    continue
                if current.startswith("> ") and not current.startswith("> >"):
                    out.append(strip_quote_prefix(current))
                    i += 1
                    continue
                break
            continue

        out.append(line)
        next_line = lines[i + 1] if i + 1 < len(lines) else None
        if next_line is None:
            break
        if next_line.strip() == "":
            i += 1
            continue

        # 普通段落后如果接列表或表格，补空行，让 Word 不把它们黏在一起。
        if line.strip() and not starts_list(line) and not starts_table(line) and not is_image(line) and (starts_list(next_line) or starts_table(next_line)):
            out.append("")
            i += 1
            continue

        # 图片后紧跟表格/列表时，给 pandoc 一行缓冲，避免导出成乱码或粘连。
        if is_image(line) and (starts_table(next_line) or starts_list(next_line)):
            out.append("")
            i += 1
            continue

        # 独立粗体提示语后紧跟表格/列表/另一段粗体时，补空行，避免 Word 中粘连。
        if is_standalone_bold(line) and (starts_table(next_line) or starts_list(next_line) or starts_bold_text(next_line)):
            out.append("")
        i += 1

    return "\n".join(out)


def main():
    parts: list[str] = []
    parts.append(f"# {BOOK_TITLE}\n")

    for i in range(0, 14):
        if i == 0:
            fname = MANUSCRIPT_DIR / "00-前言.md"
        else:
            fname = MANUSCRIPT_DIR / f"{i:02d}-第{i:02d}章.md"
        if not fname.exists():
            continue
        text = fname.read_text(encoding="utf-8")

        if i == 0:
            text = adjust_headings_preface(text)
            parts.append(text)
            parts.append("\n\n---\n\n")
            continue

        if i in PARTS:
            parts.append(PARTS[i] + "\n\n")
        text = adjust_headings_chapter(text)
        text = normalize_notes(text)
        parts.append(text)
        parts.append("\n\n---\n\n")

    out_text = "".join(parts).rstrip() + "\n"
    OUTPUT_FILE.write_text(out_text, encoding="utf-8")
    print(f"已生成：{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
