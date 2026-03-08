#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将直双引号 "..." 替换为弯双引号 "..."，避免导出 Word 时显示成两个右引号。"""

import re
from pathlib import Path

MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
# 弯引号：左 " U+201C，右 " U+201D
LEFT, RIGHT = "\u201c", "\u201d"


def fix_quotes(text: str) -> str:
    # 将 "内容" 替换为 "内容"（按配对替换）
    return re.sub(r'"([^"]*)"', f"{LEFT}\\1{RIGHT}", text)


def main():
    files = list(MANUSCRIPT.glob("*.md"))
    files = [f for f in files if f.name.startswith(("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13")) or f.name == "full-book.md"]
    for path in sorted(files):
        s = path.read_text(encoding="utf-8")
        new_s = fix_quotes(s)
        if new_s != s:
            path.write_text(new_s, encoding="utf-8")
            print(f"已处理: {path.name}")
    print("完成。")


if __name__ == "__main__":
    main()
