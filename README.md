<!-- 标题区（居中） -->
<h3 align="center"></h3>

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
        原模板中 "你的用户名" 占位符已替换为 husy7；
        被注释掉的 LinkedIn 代码已删除，闭合了未正确关闭的 <a> 标签。
  数据源：GitHub 用户名 husy7
-->
<!-- ====== 2. 社交连接图标（使用 Shields.io 徽章） ====== -->
<h3 align="left">🌐 </h3>
<p align="left">
  <a href="https://github.com/husy7" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-husy7-181717?logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

<!--
  区域3 · 语言与工具
  操作：使用 devicon 项目（https://github.com/devicons/devicon）提供的 SVG 图标，
        按个人技术栈选择对应语言/工具图标。每个图标 40×40，链接到官方文档。
  数据源：devicon SVG 原始文件 raw.githubusercontent.com/devicons/devicon/master/icons/
-->
<!-- ====== 语言与工具（已修正原代码） ====== -->
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
        直接调用 GitHub 官方 API，不依赖第三方 Vercel 服务，不会宕机。
        用户手动注释掉了此区域，保留备用。
  数据源：shields.io https://img.shields.io/github/
  排查记录：https://github.com/anuraghazra/github-readme-stats/issues/4737
-->
<!-- ====== 3. GitHub 统计（使用 shields.io 官方端点，不依赖第三方 Vercel） ====== -->
<!-- <h3 align="left">📊 GitHub 统计</h3>
<p align="left">
  <img src="https://img.shields.io/github/followers/husy7?label=Followers&style=social" alt="Followers"/>
  <img src="https://img.shields.io/github/stars/husy7?label=Total%20Stars&style=social" alt="Stars"/>
  <img src="https://img.shields.io/github/commit-activity/m/husy7?label=Monthly%20Commits" alt="Monthly Commits"/>
  <img src="https://img.shields.io/github/repo-count/husy7?label=Public%20Repos" alt="Public Repos"/>
</p> -->

<!--
  区域5 · 展示个人项目
  操作：原模板使用 "项目1/2/3" 假占位符，已替换为 GitHub API 返回的真实仓库。
        获取方式：调用 GitHub REST API 查询用户公开仓库列表，按更新时间倒序。
        筛选条件：排除 profile README 仓库 husy7/husy7，保留其余 5 个项目仓库，
        依据仓库 description 和 language 字段编写中文描述。
  数据源：https://api.github.com/users/husy7/repos?sort=updated&per_page=10
-->
<!-- ====== 4. 展示个人项目 ====== -->
<h3 align="left">📂 我的项目</h3>
<p align="left">
  <ul>
    <li><strong><a href="https://github.com/husy7/Smart-Document-Q-A-Assistant---datawhale_hello_agent_chat8_Refactor">Smart-Document-Q-A-Assistant</a></strong> - 智能文档问答助手重构版，基于 Datawhale Hello Agent 第8章，使用 Python 构建</li>
    <li><strong><a href="https://github.com/husy7/Snap2MD">Snap2MD</a></strong> - 基于本地 GLM-OCR 的剪贴板图片识别工具，将截图直接转为 Markdown 格式内容</li>
    <li><strong><a href="https://github.com/husy7/NotionAILearningMentor">NotionAILearningMentor</a></strong> - Notion AI 学习助手，帮助整理和规划学习路径</li>
    <li><strong><a href="https://github.com/husy7/car_parking_fee">car_parking_fee</a></strong> - 停车费用计算系统，Python 实现</li>
    <li><strong><a href="https://github.com/husy7/skill-es-search">skill-es-search</a></strong> - Everything 搜索工具的命令行封装技能，Shell 实现</li>
  </ul>
  更多项目请查看我的 <a href="https://github.com/husy7?tab=repositories">Repositories</a>。
</p>

<!--
  区域6 · 展示个人学习记录内容（学习笔记）
  操作：从 husy-notebook 仓库获取完整文件树，筛选出所有 .md 笔记文件，
        按目录分类（Python / ML / DL / NLP-LLM / CV / AI-Agent / Datawhale课程），
        为每个笔记文件生成 GitHub blob 链接（https://github.com/husy7/husy-notebook/blob/main/{path}），
        路径中的空格用 %20 编码。排除 .gitkeep、index.md、模板文件等非笔记内容。
        最终用分类链接替换掉第5部分的空占位内容。
  数据源：GitHub Git Tree API（递归获取完整文件树）
        https://api.github.com/repos/husy7/husy-notebook/git/trees/main?recursive=1
  笔记仓库：https://github.com/husy7/husy-notebook
  分类依据：仓库 docs/ 目录的子文件夹命名（00-Index ~ 11-工具使用笔记）
-->
<!-- ====== 5. 展示个人学习记录内容 ====== -->
<h3 align="left">📚 学习笔记</h3>
<p align="left">
  笔记-均收录在 <a href="https://github.com/husy7/husy-notebook">husy-notebook</a> 仓库中。
</p>

<p align="left">
  <strong>🐍 Python</strong>
  <ul>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Language-Features/Decorators.md">Decorators（装饰器）</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Language-Features/language-features-note.md">Python 语言特性</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Concurrency/concurrency-note.md">并发编程</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Type-Hints/type-hints-note.md">Type Hints（类型标注）</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/01-Python/Packaging/packaging-note.md">打包与分发</a></li>
  </ul>
</p>

<p align="left">
  <strong>🤖 机器学习算法</strong>
  <ul>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Linear-Models/linear-models-note.md">线性模型</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Tree-Based/tree-based-note.md">树模型</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Clustering/clustering-note.md">聚类算法</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/02-ML-Algorithms/Evaluation/evaluation-note.md">模型评估</a></li>
  </ul>
</p>

<p align="left">
  <strong>🧠 深度学习</strong>
  <ul>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/Fundamentals/fundamentals-note.md">深度学习基础</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/PyTorch/pytorch-note.md">PyTorch 笔记</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/TensorFlow/tensorflow-note.md">TensorFlow 笔记</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/03-DeepLearning/Model-Zoo/model-zoo-note.md">经典模型 zoo</a></li>
  </ul>
</p>

<p align="left">
  <strong>💬 NLP 与大语言模型</strong>
  <ul>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/Text-Preprocessing/text-preprocessing-note.md">文本预处理</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/Word-Embedding/word-embedding-note.md">词向量</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/Seq2Seq-Attention/seq2seq-attention-note.md">Seq2Seq 与注意力机制</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/LLM/LLM优化.md">LLM 优化技术</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/04-NLP-LLM/LLM/deepseek_v4笔记-note.md">DeepSeek 模型笔记</a></li>
  </ul>
</p>

<p align="left">
  <strong>👁️ 计算机视觉</strong>
  <ul>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/05-CV/Image-Processing/image-processing-note.md">图像处理</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/05-CV/CNN-Architectures/cnn-architectures-note.md">CNN 经典架构</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/05-CV/Object-Detection/object-detection-note.md">目标检测</a></li>
  </ul>
</p>

<p align="left">
  <strong>🤝 AI Agent</strong>
  <ul>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/Prompt-Engineering/prompt-engineering-note.md">Prompt Engineering</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/RAG/rag-note.md">RAG 检索增强生成</a></li>
    <li><a href="https://github.com/husy7/husy-notebook/blob/main/docs/06-AI-Agents/Use-Cases/use-cases-note.md">Agent 应用场景</a></li>
  </ul>
</p>

<p align="left">
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
</p>
