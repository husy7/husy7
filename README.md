<!--
  区域0 · 头部：居中头像 + 打字机动画标题
  操作：
    1. 头像使用 GitHub API 提供的用户头像 URL（avatars.githubusercontent.com），尺寸 100px 圆形
    2. 打字机动画使用 readme-typing-svg 服务（readme-typing-svg.demolab.com），
       循环显示多行技术关键词，居中排列
    3. 原 <h3 align="center"></h3> 空标题已替换为头像 + 打字机组合
  数据源：
    - 头像：https://avatars.githubusercontent.com/husy7 （GitHub Users API 返回的 avatar_url）
    - 打字机：https://readme-typing-svg.demolab.com API
-->
<p align="center">
  <img src="https://avatars.githubusercontent.com/husy7?v=4" width="120" height="120" style="border-radius: 50%;" alt="husy7"/>
</p>

<p align="center">
  <a href="https://readme-typing-svg.demolab.com/demo/?lines=AI+Developer;Python;PyTorch;AI+Agent;持续学习，把复杂变简单&font=Fira+Code&size=28&duration=3000&pause=1000&center=true&repeat=true&width=440&height=60">
    <img src="https://readme-typing-svg.demolab.com?lines=AI+Developer;Python;PyTorch;AI+Agent;持续学习，把复杂变简单&font=Fira+Code&size=28&duration=3000&pause=1000&center=true&repeat=true&width=440&height=60" alt="Typing SVG"/>
  </a>
</p>

<hr/>

<!--
  区域1 · 个人简介区
  操作：手动编写学习方向、联系方式等内容。联系邮箱因 GitHub API 未公开 email 字段，
        改为指向 GitHub 主页链接。原模板中的占位符 your-email@example.com 已替换。
  数据源：GitHub 用户信息 https://api.github.com/users/husy7 （email 字段为 null）
-->
<!-- ====== 1. 个人简介区 ====== -->
<h3 align="left">👋 关于我</h3>
<p align="left">
  - 🔭 目前正在学习 <strong>AIagent</strong>（大模型应用）<br>
  - 🌱 最近主要学习 <strong>PyTorch</strong><br>
  - 💬 欢迎与我讨论：Python、Java、Docker、PostgreSQL、TypeScript<br>
  - 📫 如何联系我：<a href="https://github.com/husy7">在 GitHub 上给我留言</a><br>
</p>

<!--
  区域2 · 社交连接图标
  操作：使用 Shields.io 徽章（https://img.shields.io）生成图标，无需第三方依赖。
        统一配色主题：深色底（181717）+ 白色文字，与 GitHub 品牌色一致。
        原模板中 "你的用户名" 占位符已替换为 husy7；
        被注释掉的 LinkedIn 代码已删除，闭合了未正确关闭的 <a> 标签。
  数据源：GitHub 用户名 husy7
-->
<!-- ====== 2. 社交连接图标（使用 Shields.io 徽章） ====== -->
<h3 align="left">🌐 找到我</h3>
<p align="left">
  <a href="https://github.com/husy7" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-husy7-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

<!--
  区域3 · 语言与工具
  操作：使用 devicon 项目（https://github.com/devicons/devicon）提供的 SVG 图标，
        按个人技术栈选择对应语言/工具图标。每个图标 40×40，链接到官方文档。
        统一配色：使用原始品牌色 SVG（devicon original 系列），保持各语言官方配色。
  数据源：devicon SVG 原始文件 raw.githubusercontent.com/devicons/devicon/master/icons/
-->
<!-- ====== 语言与工具 ====== -->
<h3 align="left">🛠️ 语言与工具</h3>
<p align="left">
  <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/>
  </a>
  <a href="https://www.docker.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/>
  </a>
  <a href="https://www.java.com" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/>
  </a>
  <a href="https://www.linux.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/>
  </a>
  <a href="https://www.postgresql.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/>
  </a>
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
  <a href="https://redis.io" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/>
  </a>
  <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/>
  </a>
</p>

<!--
  区域4 · GitHub 统计
  操作：原模板使用 github-readme-stats.vercel.app 统计卡片，但该公共实例已被暂停
        （503 DEPLOYMENT_PAUSED），所有卡片显示失败。
        已替换为 shields.io 官方端点徽章（followers/stars/commit-activity/repo-count），
        统一配色：style=for-the-badge，深色主题，与社交图标风格一致。
        直接调用 GitHub 官方 API，不依赖第三方 Vercel 服务，不会宕机。
        用户手动注释掉了此区域，保留备用。
  数据源：shields.io https://img.shields.io/github/
  排查记录：https://github.com/anuraghazra/github-readme-stats/issues/4737
-->
<!-- ====== 3. GitHub 统计（使用 shields.io 官方端点，不依赖第三方 Vercel） ====== -->
<!-- <h3 align="left">📊 GitHub 统计</h3>
<p align="left">
  <img src="https://img.shields.io/github/followers/husy7?label=Followers&style=for-the-badge&color=181717" alt="Followers"/>
  <img src="https://img.shields.io/github/stars/husy7?label=Total%20Stars&style=for-the-badge&color=181717" alt="Stars"/>
  <img src="https://img.shields.io/github/commit-activity/m/husy7?label=Monthly%20Commits&style=for-the-badge&color=181717" alt="Monthly Commits"/>
  <img src="https://img.shields.io/github/repo-count/husy7?label=Public%20Repos&style=for-the-badge&color=181717" alt="Public Repos"/>
</p> -->

<!--
  区域5 · 展示个人项目（双栏表格布局）
  操作：原模板使用 "项目1/2/3" 假占位符，已替换为 GitHub API 返回的真实仓库。
        获取方式：调用 GitHub REST API 查询用户公开仓库列表，按更新时间倒序。
        筛选条件：排除 profile README 仓库 husy7/husy7，保留其余 5 个项目仓库，
        依据仓库 description 和 language 字段编写中文描述。
        布局升级：从 <ul> 列表改为双栏 HTML table，左栏项目名+语言 badge，右栏描述。
  数据源：https://api.github.com/users/husy7/repos?sort=updated&per_page=10
  配色：语言 badge 使用 shields.io style=flat-square，统一深色系
-->
<!-- ====== 4. 展示个人项目 ====== -->
<h3 align="left">📂 我的项目</h3>

<table>
  <tr>
    <td width="40%" valign="top"><strong><a href="https://github.com/husy7/Smart-Document-Q-A-Assistant---datawhale_hello_agent_chat8_Refactor">Smart-Document-Q-A-Assistant</a></strong><br/><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></td>
    <td width="60%" valign="top">智能文档问答助手重构版，基于 Datawhale Hello Agent 第8章</td>
  </tr>
  <tr>
    <td valign="top"><strong><a href="https://github.com/husy7/Snap2MD">Snap2MD</a></strong><br/><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></td>
    <td valign="top">基于本地 GLM-OCR 的剪贴板图片识别工具，将截图直接转为 Markdown 格式内容</td>
  </tr>
  <tr>
    <td valign="top"><strong><a href="https://github.com/husy7/NotionAILearningMentor">NotionAILearningMentor</a></strong><br/><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></td>
    <td valign="top">Notion AI 学习助手，帮助整理和规划学习路径</td>
  </tr>
  <tr>
    <td valign="top"><strong><a href="https://github.com/husy7/car_parking_fee">car_parking_fee</a></strong><br/><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></td>
    <td valign="top">停车费用计算系统</td>
  </tr>
  <tr>
    <td valign="top"><strong><a href="https://github.com/husy7/skill-es-search">skill-es-search</a></strong><br/><img src="https://img.shields.io/badge/Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Shell"/></td>
    <td valign="top">Everything 搜索工具的命令行封装技能</td>
  </tr>
</table>

<p align="left">
  更多项目请查看我的 <a href="https://github.com/husy7?tab=repositories">Repositories</a>。
</p>

<!--
  区域6 · 展示个人学习记录内容（学习笔记 · 双栏表格布局）
  操作：从 husy-notebook 仓库获取完整文件树，筛选出所有 .md 笔记文件，
        按目录分类（Python / ML / DL / NLP-LLM / CV / AI-Agent / Datawhale课程），
        为每个笔记文件生成 GitHub blob 链接（https://github.com/husy7/husy-notebook/blob/main/{path}），
        路径中的空格用 %20 编码。排除 .gitkeep、index.md、模板文件等非笔记内容。
        布局升级：从纵向 <ul> 列表改为双栏 table，左栏分类+笔记标题，右栏同分类继续，
        充分利用页面横向空间，减少滚动长度。
  数据源：GitHub Git Tree API（递归获取完整文件树）
        https://api.github.com/repos/husy7/husy-notebook/git/trees/main?recursive=1
  笔记仓库：https://github.com/husy7/husy-notebook
  分类依据：仓库 docs/ 目录的子文件夹命名（00-Index ~ 11-工具使用笔记）
-->
<!-- ====== 5. 展示个人学习记录内容 ====== -->
<h3 align="left">📚 学习笔记</h3>
<p align="left">
  以下是我的技术学习笔记，均收录在 <a href="https://github.com/husy7/husy-notebook">husy-notebook</a> 仓库中。
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>🐍 Python</strong>
      <ul>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Language-Features/Decorators.md">Decorators（装饰器）</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Language-Features/language-features-note.md">Python 语言特性</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Concurrency/concurrency-note.md">并发编程</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Type-Hints/type-hints-note.md">Type Hints（类型标注）</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Packaging/packaging-note.md">打包与分发</a></li>
      </ul>
      <strong>🤖 机器学习算法</strong>
      <ul>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Linear-Models/linear-models-note.md">线性模型</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Tree-Based/tree-based-note.md">树模型</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Clustering/clustering-note.md">聚类算法</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Evaluation/evaluation-note.md">模型评估</a></li>
      </ul>
      <strong>👁️ 计算机视觉</strong>
      <ul>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/05-CV/Image-Processing/image-processing-note.md">图像处理</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/05-CV/CNN-Architectures/cnn-architectures-note.md">CNN 经典架构</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/05-CV/Object-Detection/object-detection-note.md">目标检测</a></li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <strong>🧠 深度学习</strong>
      <ul>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/Fundamentals/fundamentals-note.md">深度学习基础</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/PyTorch/pytorch-note.md">PyTorch 笔记</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/TensorFlow/tensorflow-note.md">TensorFlow 笔记</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/Model-Zoo/model-zoo-note.md">经典模型 zoo</a></li>
      </ul>
      <strong>💬 NLP 与大语言模型</strong>
      <ul>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/Text-Preprocessing/text-preprocessing-note.md">文本预处理</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/Word-Embedding/word-embedding-note.md">词向量</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/Seq2Seq-Attention/seq2seq-attention-note.md">Seq2Seq 与注意力机制</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/LLM/LLM优化.md">LLM 优化技术</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/LLM/deepseek_v4笔记-note.md">DeepSeek 模型笔记</a></li>
      </ul>
      <strong>🤝 AI Agent</strong>
      <ul>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/Prompt-Engineering/prompt-engineering-note.md">Prompt Engineering</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/RAG/rag-note.md">RAG 检索增强生成</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/Use-Cases/use-cases-note.md">Agent 应用场景</a></li>
      </ul>
      <strong>🎯 Datawhale Hello Agent 课程</strong>
      <ul>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节4经典范式构建/环境准备与基础工具/env-and-tools-note.md">环境准备与基础工具</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节4经典范式构建/ReAct/react-note.md">ReAct 范式</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节4经典范式构建/Reflection%20机制/reflection-note.md">Reflection 反思机制</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节4经典范式构建/Plan-and-Solve/plan-and-solve-note.md">Plan-and-Solve 范式</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节4经典范式构建/小结.md">章节4 小结</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节5低代码平台/低代码agent-note.md">低代码 Agent 平台</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节6Frameworks开发/AgentScope/agentscope-note.md">AgentScope 框架</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节6Frameworks开发/AutoGen/autogen-note.md">AutoGen 框架</a></li>
        <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/datawhale_hello_agent课程/章节6Frameworks开发/CAMEL/camel-note.md">CAMEL 框架</a></li>
      </ul>
    </td>
  </tr>
</table>

<!--
  区域7 · 贪吃蛇贡献图（Snake Contribution Animation）
  操作：使用 Platane/snk@v3 GitHub Action，每日自动从 GitHub 贡献图生成贪吃蛇动画 SVG。
        Action workflow 文件位于 .github/workflows/snake.yml，
        生成的 SVG 推送到 output 分支，通过 raw.githubusercontent.com 引用。
        SVG 有亮色/暗色两个版本，使用 prefers-color-scheme 自动适配 GitHub 深色模式。
  数据源：Platane/snk@v3 GitHub Action → output 分支
  引用路径：https://raw.githubusercontent.com/husy7/husy7/output/github-contribution-grid-snake.svg
  参考文档：https://github.com/Platane/snk
-->
<!-- ====== 6. 贪吃蛇贡献图 ====== -->
<h3 align="left">🐍 贪吃蛇贡献图</h3>
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/husy7/husy7/output/github-contribution-grid-snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/husy7/husy7/output/github-contribution-grid-snake.svg"/>
    <img alt="github-contribution-grid-snake" src="https://raw.githubusercontent.com/husy7/husy7/output/github-contribution-grid-snake.svg"/>
  </picture>
</p>
