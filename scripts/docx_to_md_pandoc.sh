#!/usr/bin/env bash
# 使用 pandoc 将 .docx 转为 Markdown（更好保留表格、列表等格式）
# 用法：在项目根目录执行 ./scripts/docx_to_md_pandoc.sh [docx路径]
# 若未指定路径，则使用项目根目录下第一个 .docx 文件

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

DOCX="${1:-}"
if [ -z "$DOCX" ]; then
  for f in *.docx; do
    [ -f "$f" ] && DOCX="$f" && break
  done
fi
if [ -z "$DOCX" ] || [ ! -f "$DOCX" ]; then
  echo "未找到 .docx 文件。请指定路径，例如："
  echo "  ./scripts/docx_to_md_pandoc.sh \"前言+第1章+第2章（批注）.docx\""
  exit 1
fi

mkdir -p manuscript
OUT="$PROJECT_ROOT/manuscript/full-pandoc.md"

echo "正在用 pandoc 转换: $DOCX -> $OUT"
pandoc "$DOCX" -f docx -t markdown -o "$OUT" --wrap=none

echo "已写入: $OUT"
echo "说明：pandoc 会更好保留表格、列表等；若需按章节拆分，可用 scripts/docx_to_md.py 或手动按标题拆分。"
