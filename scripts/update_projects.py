#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新 husy7/husy7 主页 README 中的「我的项目」区块。

工作原理：
    1. 调用 GitHub REST API 获取 husy7 的公开仓库列表（按更新时间倒序）。
    2. 筛选：排除 fork 仓库、profile README 仓库（husy7/husy7），
       排除名称以 "." 开头的隐藏仓库。
    3. 取前 10 个仓库，生成双栏 HTML 表格（左栏项目名 + 语言 badge，
      右栏描述），写入 <!-- PROJECTS_START --> … <!-- PROJECTS_END --> 标记之间。
    4. 与 update_notes.py 一致：若无变化则不写入。

鉴权：
    - 若环境变量 GITHUB_TOKEN 存在则携带（5000 次/小时），用于 Actions 内运行。
    - 否则以匿名身份调用（60 次/小时，对本脚本每日单次调用足够）。

本地测试：
    python scripts/update_projects.py   # 不需要 token 也能跑
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

# ====== 配置 ======
GITHUB_USER = "husy7"
README_PATH = "README.md"          # 被更新的目标 README（本仓库 husy7/husy7 的）

MARKER_START = "<!-- PROJECTS_START -->"
MARKER_END = "<!-- PROJECTS_END -->"

MAX_PROJECTS = 10  # 最多展示多少个项目

# 排除的仓库（profile README 仓库本身）
EXCLUDE_REPOS = {f"{GITHUB_USER}/{GITHUB_USER}"}

# 语言 -> shields.io badge 颜色码映射（与原手写表格风格一致）
LANG_BADGE = {
    "Python":     ("Python",     "3776AB", "python"),
    "Shell":      ("Shell",      "4EAA25", "gnubash"),
    "TypeScript": ("TypeScript", "3178C6", "typescript"),
    "JavaScript": ("JavaScript", "F7DF1E", "javascript"),
    "Java":       ("Java",       "ED8B00", "openjdk"),
    "HTML":       ("HTML",       "E34F26", "html5"),
    "C":          ("C",          "A8B9CC", "c"),
    "C++":        ("C++",        "00599C", "cplusplus"),
    "Go":         ("Go",         "00ADD8", "go"),
    "Rust":       ("Rust",       "DEA584", "rust"),
    "Vue":        ("Vue",        "42B883", "vuedotjs"),
}


# ====== 1. 获取仓库列表 ======
def get_repos():
    """调用 GitHub REST API 获取用户公开仓库列表（按更新时间倒序）。"""
    url = (
        f"https://api.github.com/users/{GITHUB_USER}/repos"
        f"?sort=updated&per_page=30&type=owner"
    )
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": f"{GITHUB_USER}-readme-projects-updater",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error: 获取仓库列表失败 - {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(data, list):
        print(f"Error: API 返回非列表 - {data}", file=sys.stderr)
        sys.exit(1)
    return data


# ====== 2. 筛选仓库 ======
def filter_repos(repos):
    """筛选仓库：排除 fork、profile README 仓库、隐藏仓库，取前 MAX_PROJECTS 个。"""
    filtered = []
    for repo in repos:
        full_name = repo.get("full_name", "")
        name = repo.get("name", "")

        # 排除 profile README 仓库
        if full_name in EXCLUDE_REPOS:
            continue
        # 排除 fork 仓库
        if repo.get("fork", False):
            continue
        # 排除隐藏仓库（以 . 开头）
        if name.startswith("."):
            continue

        filtered.append(repo)

    return filtered[:MAX_PROJECTS]


# ====== 3. 生成语言 badge ======
def make_lang_badge(language):
    """根据语言名生成 shields.io badge URL。

    已知语言使用预设配色；未知语言使用灰色兜底。
    """
    if not language:
        return None

    if language in LANG_BADGE:
        label, color, logo = LANG_BADGE[language]
        return (
            f"https://img.shields.io/badge/{label}-{color}"
            f"?style=flat-square&logo={logo}&logoColor=white"
        )
    # 未知语言：灰色兜底
    safe = language.replace(" ", "%20").replace("-", "--")
    return (
        f"https://img.shields.io/badge/{safe}-666666"
        f"?style=flat-square"
    )


# ====== 4. 生成双栏 HTML 表格 ======
def generate_html_table(repos):
    """生成双栏 HTML 表格，左栏项目名 + 语言 badge，右栏描述。"""
    rows = []
    for repo in repos:
        name = repo.get("name", "")
        full_name = repo.get("full_name", name)
        description = repo.get("description") or "暂无描述"
        language = repo.get("language")
        html_url = repo.get("html_url", f"https://github.com/{full_name}")

        # 左栏：项目名（链接）+ 语言 badge
        badge = make_lang_badge(language)
        if badge:
            left = (
                f'<strong><a href="{html_url}">{name}</a></strong>'
                f'<br/><img src="{badge}" alt="{language or ""}"/>'
            )
        else:
            left = f'<strong><a href="{html_url}">{name}</a></strong>'

        row = (
            "  <tr>\n"
            f'    <td width="40%" valign="top">{left}</td>\n'
            f'    <td width="60%" valign="top">{description}</td>\n'
            "  </tr>"
        )
        rows.append(row)

    return "<table>\n" + "\n".join(rows) + "\n</table>"


# ====== 5. 更新 README.md ======
def update_readme(new_content):
    """用 new_content 替换 README 中 PROJECTS_START … PROJECTS_END 之间的内容。"""
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
    print("1. 获取仓库列表 ...")
    repos = get_repos()
    print(f"   共 {len(repos)} 个仓库。")

    print("2. 筛选仓库 ...")
    filtered = filter_repos(repos)
    print(f"   筛选后 {len(filtered)} 个项目。")

    print("3. 生成 HTML 表格 ...")
    html = generate_html_table(filtered)

    print("4. 更新 README.md ...")
    changed = update_readme(html)
    print("完成！" if changed else "完成（无变更）。")


if __name__ == "__main__":
    main()
