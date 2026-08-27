#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新 husy7/husy7 主页 README 中的「学习笔记」区块。

工作原理：
    1. 调用 GitHub Git Trees API（递归）获取 husy7/husy-notebook 仓库的完整文件树。
       注意：是跨仓库读取 —— 本脚本运行在 husy7/husy7 的 Actions 里，
             但读取的是另一个公开仓库 husy7/husy-notebook 的文件树。
    2. 筛选 docs/ 目录下所有 .md 笔记文件，排除 index.md / README.md / .gitkeep 等。
    3. 按 docs/ 的顶级子目录（如 01-Python、02-ML-Algorithms …）分类；
       特别地，把 06-AI-Agents/datawhale_hello_agent课程 单独拆为一个分类，
       与手动维护时的结构保持一致。
    4. 生成双栏 HTML 表格（与 README 其余区块风格统一），写入
       <!-- NOTES_START --> … <!-- NOTES_END --> 标记之间。

鉴权：
    - 若环境变量 GITHUB_TOKEN 存在则携带（5000 次/小时），用于 Actions 内运行。
    - 否则以匿名身份调用（60 次/小时，对本脚本每日单次调用足够）。
    - husy-notebook 是公开仓库，匿名读取即可成功。

本地测试：
    python scripts/update_notes.py   # 不需要 token 也能跑
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

# ====== 配置 ======
REPO_OWNER = "husy7"
REPO_NAME = "husy-notebook"           # 笔记所在仓库（被读取的源仓库）
BRANCH = "main"
README_PATH = "README.md"             # 被更新的目标 README（本仓库 husy7/husy7 的）

MARKER_START = "<!-- NOTES_START -->"
MARKER_END = "<!-- NOTES_END -->"

# docs/ 顶级子目录 -> 分类显示名（emoji + 中文）
# 与 husy-notebook 实际目录结构对齐；未在表中的目录会回退为「去掉数字前缀的目录名」。
CATEGORY_MAP = {
    "00-Index": "📑 索引",
    "01-Python": "🐍 Python",
    "02-ML-Algorithms": "🤖 机器学习算法",
    "03-DeepLearning": "🧠 深度学习",
    "04-NLP-LLM": "💬 NLP 与大语言模型",
    "05-CV": "👁️ 计算机视觉",
    "06-AI-Agents": "🤝 AI Agent",
}

# datawhale_hello_agent课程 作为 06-AI-Agents 下的独立子分类单独展示
SPECIAL_SUBCATEGORY = {
    ("06-AI-Agents", "datawhale_hello_agent课程"): "🎯 Datawhale Hello Agent 课程",
}

# 排除的文件名（全路径包含即排除）
EXCLUDE_PATTERNS = [".gitkeep", "index.md", "README.md"]


# ====== 1. 获取文件树 ======
def get_repo_tree():
    """调用 GitHub Git Trees API（recursive=1）获取完整文件树。"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/trees/{BRANCH}?recursive=1"
    headers = {"Accept": "application/vnd.github.v3+json",
               "User-Agent": "husy7-readme-notes-updater"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error: 获取文件树失败 - {e}", file=sys.stderr)
        sys.exit(1)

    if "tree" not in data:
        print(f"Error: API 返回中无 tree 字段 - {data}", file=sys.stderr)
        sys.exit(1)
    return data["tree"]


# ====== 2. 解析并分类笔记 ======
def categorize_notes(tree):
    """从文件树筛选 .md 笔记并分类。

    返回：有序字典 {分类名: [(display_name, url), ...]}，
          按 CATEGORY_MAP 的顺序 + 字典序排列。
    """
    from collections import OrderedDict

    notes = OrderedDict()

    for item in tree:
        path = item.get("path", "")
        # 仅处理 docs/ 下的 .md 文件
        if not path.startswith("docs/") or not path.endswith(".md"):
            continue
        # 排除非笔记文件
        if any(p in path for p in EXCLUDE_PATTERNS):
            continue

        parts = path.split("/")
        # docs / <category> / ... / file.md  至少 3 段
        if len(parts) < 3:
            continue

        category_key = parts[1]              # 如 06-AI-Agents
        second_level = parts[2] if len(parts) >= 4 else ""

        # 特殊子分类优先（如 datawhale 课程）
        special_key = (category_key, second_level)
        if special_key in SPECIAL_SUBCATEGORY:
            category_name = SPECIAL_SUBCATEGORY[special_key]
        elif category_key in CATEGORY_MAP:
            # 00-Index 是索引目录，跳过其下的 index.md 已被排除；这里若还有别的也归入索引
            category_name = CATEGORY_MAP[category_key]
            if category_key == "00-Index":
                # 索引区不放笔记
                continue
        else:
            # 未知分类：去掉前缀数字，作为兜底
            stripped = re.sub(r"^\d+-", "", category_key)
            category_name = f"📂 {stripped}" if stripped else f"📂 {category_key}"

        url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/{path.replace(' ', '%20')}"
        display = make_display_name(path)

        notes.setdefault(category_name, []).append((display, url))

    return notes


def make_display_name(path):
    """从文件路径生成可读的展示名：去掉 .md / -note 后缀，首字母大写。"""
    filename = path.split("/")[-1]
    name = filename
    if name.endswith(".md"):
        name = name[:-3]
    if name.endswith("-note"):
        name = name[:-5]
    if name.endswith("_note"):
        name = name[:-6]
    # 首字母大写（对 CJK 无影响，仅美化英文）
    if name:
        name = name[0].upper() + name[1:]
    return name


# ====== 3. 生成双栏 HTML 表格 ======
def generate_html_table(notes):
    """按分类生成双栏 HTML 表格，左右两栏按笔记总数大致均衡。"""
    # 固定分类顺序：已知顺序 + 未知分类按字典序追加
    ordered = []
    for v in CATEGORY_MAP.values():
        if v in notes:
            ordered.append(v)
    # 特殊子分类插到 06-AI-Agents 之后
    for v in SPECIAL_SUBCATEGORY.values():
        if v in notes:
            ordered.append(v)
    # 兜底分类
    for k in sorted(notes.keys()):
        if k not in ordered:
            ordered.append(k)

    total = sum(len(notes[c]) for c in ordered)
    half = total / 2.0

    left, right = [], []
    running = 0
    for cat in ordered:
        target = left if running < half else right
        target.append(cat)
        running += len(notes[cat])

    def render_column(cats):
        blocks = []
        for cat in cats:
            blocks.append(f"      <strong>{cat}</strong>")
            blocks.append("      <ul>")
            for display, url in notes[cat]:
                blocks.append(f'        <li><a href="{url}">{display}</a></li>')
            blocks.append("      </ul>")
        return "\n".join(blocks)

    return (
        "<table>\n"
        "  <tr>\n"
        '    <td width="50%" valign="top">\n'
        f"{render_column(left)}\n"
        "    </td>\n"
        '    <td width="50%" valign="top">\n'
        f"{render_column(right)}\n"
        "    </td>\n"
        "  </tr>\n"
        "</table>"
    )


# ====== 4. 更新 README.md ======
def update_readme(new_content):
    """用 new_content 替换 README 中 NOTES_START … NOTES_END 之间的内容。"""
    readme = Path(README_PATH)
    if not readme.exists():
        print(f"Error: {README_PATH} 不存在！", file=sys.stderr)
        sys.exit(1)

    content = readme.read_text(encoding="utf-8")

    if MARKER_START not in content or MARKER_END not in content:
        print(f"Error: README 中未找到标记 {MARKER_START} / {MARKER_END}", file=sys.stderr)
        sys.exit(1)

    pattern = re.compile(
        f"{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}",
        re.DOTALL,
    )
    replacement = f"{MARKER_START}\n{new_content}\n{MARKER_END}"
    new_full = pattern.sub(replacement, content)

    if new_full == content:
        print("无变化，README 不需要更新。")
        return False

    readme.write_text(new_full, encoding="utf-8")
    print("README.md 已更新。")
    return True


# ====== 主程序 ======
def main():
    print("1. 获取 husy-notebook 仓库文件树 ...")
    tree = get_repo_tree()
    print(f"   共 {len(tree)} 个条目。")

    print("2. 解析并分类笔记 ...")
    categorized = categorize_notes(tree)
    total_notes = sum(len(v) for v in categorized.values())
    print(f"   共 {len(categorized)} 个分类，{total_notes} 篇笔记。")

    print("3. 生成 HTML 表格 ...")
    html = generate_html_table(categorized)

    print("4. 更新 README.md ...")
    changed = update_readme(html)
    print("完成！" if changed else "完成（无变更）。")


if __name__ == "__main__":
    main()
