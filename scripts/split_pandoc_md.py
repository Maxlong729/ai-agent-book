#!/usr/bin/env python3
"""
将 pandoc 生成的 full-pandoc.md 按「前言」「第1章」「第2章」拆分为
00-前言.md、01-第01章.md、02-第02章.md，并统一为 # / ## 标题格式。
"""
import re
from pathlib import Path

def normalize_headings(text: str, first_heading_is_h1: bool = True) -> str:
    """将 **标题** 转为 # 或 ##：第一个单独成行的 **...** 转为 #，其余转为 ##。"""
    lines = text.split("\n")
    out = []
    first = first_heading_is_h1
    for line in lines:
        m = re.match(r"^\*\*(.+)\*\*\s*$", line)
        if m:
            title = m.group(1).strip()
            if first:
                out.append("# " + title)
                first = False
            else:
                out.append("## " + title)
            continue
        out.append(line)
    return "\n".join(out)

def main():
    project_root = Path(__file__).resolve().parent.parent
    full_path = project_root / "manuscript" / "full-pandoc.md"
    if not full_path.exists():
        print("未找到 manuscript/full-pandoc.md，请先用 pandoc 生成。")
        return 1
    text = full_path.read_text(encoding="utf-8")
    lines = text.split("\n")

    # 按 **第1章 / **第2章 拆分（**前言** 单独作为前言起始）
    chunks = []  # (title, start_line, end_line) 或 (title, lines)
    current = []
    current_title = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\*\*前言\s*\+\s*第", line):
            i += 1
            continue
        if re.match(r"^\*\*前言\s*\*\*\s*$", line):
            if current and current_title:
                chunks.append((current_title, current))
            current_title = "00-前言"
            current = [line]  # 保留 **前言** 行，后面统一转成 #
            i += 1
            continue
        m = re.match(r"^\*\*第\s*(\d+)\s*章\s*(.*)\*\*\s*$", line)
        if m:
            if current and current_title:
                chunks.append((current_title, current))
            num = m.group(1).zfill(2)
            current_title = f"{num}-第{num}章"
            current = [line]
            i += 1
            continue
        if current is not None:
            current.append(line)
        i += 1
    if current and current_title:
        chunks.append((current_title, current))

    manuscript_dir = project_root / "manuscript"
    for title, block in chunks:
        raw = "\n".join(block)
        normalized = normalize_headings(raw, first_heading_is_h1=True)
        out_path = manuscript_dir / f"{title}.md"
        out_path.write_text(normalized, encoding="utf-8")
        print("已写入:", out_path)
    return 0

if __name__ == "__main__":
    exit(main())
