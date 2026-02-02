#!/usr/bin/env python3
"""
将 .docx 转为 Markdown（仅用 Python 标准库，不依赖 pandoc/python-docx）。
支持按「前言」「第N章」自动拆分为多个 .md 文件。
"""
import zipfile
import xml.etree.ElementTree as ET
import re
import sys
from pathlib import Path

# OOXML 命名空间
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
}

def extract_text_from_paragraph(p_elem):
    """从 <w:p> 中提取所有 <w:t> 的文本并拼接。"""
    texts = []
    for t in p_elem.findall(".//w:t", NS):
        if t.text:
            texts.append(t.text)
        if t.tail and t.tail.strip():
            texts.append(t.tail)
    return "".join(texts).replace("\n", " ").strip()

def get_paragraph_style(p_elem):
    """获取段落的大纲级别 outlineLvl（0=标题1, 1=标题2）。"""
    pPr = p_elem.find("w:pPr", NS)
    if pPr is None:
        return None
    outline = pPr.find("w:outlineLvl", NS)
    if outline is not None and outline.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val") is not None:
        return int(outline.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val"))
    return None

def docx_to_paragraphs(docx_path):
    """从 docx 解压并解析 word/document.xml，返回 (段落文本, 大纲级别) 列表。"""
    with zipfile.ZipFile(docx_path, "r") as z:
        with z.open("word/document.xml") as f:
            tree = ET.parse(f)
    root = tree.getroot()
    body = root.find("w:body", NS)
    if body is None:
        return []

    result = []
    for p in body.findall("w:p", NS):
        text = extract_text_from_paragraph(p)
        if not text:
            result.append(("", get_paragraph_style(p)))
            continue
        lvl = get_paragraph_style(p)
        result.append((text, lvl))
    return result

def paragraphs_to_markdown(paragraphs):
    """将段落列表转为单段 Markdown 文本。"""
    lines = []
    for text, lvl in paragraphs:
        if not text:
            lines.append("")
            continue
        if lvl == 0:
            lines.append("# " + text)
        elif lvl == 1:
            lines.append("## " + text)
        elif lvl == 2:
            lines.append("### " + text)
        else:
            lines.append(text)
    return "\n\n".join(lines)

def split_by_chapters(paragraphs):
    """
    按「前言」「第N章」拆分为多个块。
    支持纯「前言」、纯「第N章」或「第N章 副标题」形式。
    返回: [ ("前言", [ (text, lvl), ... ]), ("第01章", [...]), ("第02章", [...]), ... ]
    """
    chunks = []
    current_title = "前言"
    current = []

    for text, lvl in paragraphs:
        # 跳过文档开头的合并标题行（如「前言+第1章+第2章」）
        if re.match(r"^前言\s*\+\s*第\s*\d+\s*章", text) and not current:
            continue
        # 纯「前言」
        if re.match(r"^前言\s*$", text):
            if current:
                chunks.append((current_title, current))
            current_title = "前言"
            current = [(text, lvl)]
            continue
        # 「第N章」或「第N章 副标题」（仅当该段为一级标题 outlineLvl=0 时拆分）
        m = re.match(r"^第\s*(\d+)\s*章\s*(.*)$", text)
        if m and lvl == 0:
            if current:
                chunks.append((current_title, current))
            num = m.group(1).zfill(2)
            current_title = f"第{num}章"
            current = [(text, lvl)]
            continue
        current.append((text, lvl))

    if current:
        chunks.append((current_title, current))
    return chunks

def main():
    project_root = Path(__file__).resolve().parent.parent
    docx_path = project_root / "前言+第1章+第2章（批注）.docx"
    if not docx_path.exists():
        # 尝试从当前目录找
        for p in project_root.iterdir():
            if p.suffix.lower() == ".docx":
                docx_path = p
                break
        else:
            print("未找到 .docx 文件", file=sys.stderr)
            sys.exit(1)

    manuscript_dir = project_root / "manuscript"
    manuscript_dir.mkdir(exist_ok=True)

    paragraphs = docx_to_paragraphs(docx_path)
    chunks = split_by_chapters(paragraphs)

    # 文件命名：00-前言.md, 01-第01章.md, 02-第02章.md
    name_map = {"前言": "00-前言"}
    for i, (title, _) in enumerate(chunks):
        if title != "前言" and title not in name_map:
            name_map[title] = f"{len(name_map):02d}-{title}"

    for title, block in chunks:
        fname = name_map.get(title, title) + ".md"
        out_path = manuscript_dir / fname
        md = paragraphs_to_markdown(block)
        out_path.write_text(md, encoding="utf-8")
        print("已写入:", out_path)

if __name__ == "__main__":
    main()
