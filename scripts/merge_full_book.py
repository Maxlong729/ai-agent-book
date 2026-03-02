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
    """统一注释/说明格式：【心法】前可加空行，保持块引用一致。"""
    # 心法单独成段时保持 **【心法】**；若有 > 块引用则保持
    return text


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
