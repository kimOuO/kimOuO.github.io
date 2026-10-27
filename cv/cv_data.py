# -*- coding: utf-8 -*-
"""兩份 CV 的全部內容。改這裡，中英文一起改，再跑 build_cv.py 重新產出 PDF。"""

CONTACT = {
    'email': 'kim36991294@gmail.com',
    'github': 'github.com/kimOuO',
    'phone': '0958-831-242',
}

SKILLS = [
    ('Programming Languages', 'Python, SQL, Cython, JavaScript'),
    ('Full-Stack & Database', 'React, Django, REST API, PostgreSQL, MariaDB, MySQL'),
    ('AI & Agent', 'Dify, Multi-Agent, ReAct, LangGraph, MCP, CLI, RAG, n8n'),
    ('Cloud Infrastructure', 'Linux, Docker, Kubernetes, Nginx, Harbor, Rancher, Harvester'),
    ('DevOps', 'Git, GitHub Actions, CI/CD'),
    ('GPU Computing', 'NVIDIA MPS, CUDA, NVIDIA DCGM'),
    ('Monitoring & Testing', 'Prometheus, Istio, eBPF'),
    ('Digital Twin & Simulation', 'NVIDIA Omniverse, NVIDIA Sionna RT'),
    ('5G & Networking', 'O-RAN, 5G NR, OpenAirInterface (OAI), E2AP'),
]

ZH = {
    'lang': 'zh-TW',
    'name': '黃耀慶',
    'name_en': 'HUANG, YAO-CHING',
    'affil': '國立臺灣科技大學 電子工程研究所｜資訊技術行動化實驗室（MITLab）',
    'photo': True,
    'sections': [
        ('學歷｜Education', 'edu', [
            {'title': '國立臺灣科技大學 電子工程研究所｜碩士班　<b>GPA 4.18 / 4.30</b>',
             'date': '2025.09 – 2027.07（預計）', 'sub': '', 'items': []},
            {'title': '國立臺灣科技大學 電子工程學系｜學士班　<b>GPA 4.04 / 4.30</b>',
             'date': '2021.09 – 2025.06',
             'sub': '大學班排名 <b>3 / 29</b>｜系排名 <b>10 / 104</b>', 'items': []},
        ]),
        ('產學研究｜Industry–Academia Research', 'exp', [
            {'title': '國科會四年期 6G 前瞻技術研發計畫｜AI/ML 平台與 AI Agent',
             'date': '2025.06 – 進行中', 'sub': '', 'items': [
                 '<b>平台整合</b>：整合 <b>20+ Docker / Kubernetes</b> 服務與 <b>Kubeflow / Argo</b> 工作流程，支援 AI/ML 平台運作。',
                 '<b>平台維運</b>：透過 <b>Prometheus</b>、<b>NVIDIA DCGM</b> 建立監控及 <b>9 組</b>自動化壓測，定位並解決 <b>7 項</b>平台問題。',
                 '設計 <b>NVIDIA MPS</b> GPU 調度機制，提升整體吞吐量 <b>21–24%</b>，批次任務完成時間縮短 <b>13%</b>。',
                 '開發 <b>Dify Multi-Agent ReAct</b> 工作流程，結合意圖辨識、工具調用與後端邏輯，實現模型訓練、監控與診斷自動化。',
             ]},
            {'title': '工研院｜5G NR RAN 數位孿生與 O-RAN 系統整合',
             'date': '2026.04 – 進行中', 'sub': '', 'items': [
                 '開發 <b>E2 Adapter</b> 串接模擬 RAN 與 <b>Near-RT RIC</b>，整合 <b>NVIDIA Omniverse</b>、<b>Sionna RT</b> 建置 3D 無線通道模擬環境。',
                 '與 <b>OAI rfsim</b> 關鍵指標達 <b>90–96%</b> 一致性；以 ML 校正將平均誤差從 <b>50.1%</b> 降至 <b>2.5%</b>。',
             ]},
        ]),
        ('工作經驗｜Professional Experience', 'exp', [
            {'title': 'SparkAmplify（美國加州）｜Backend / DevOps 實習生',
             'date': '2026.01 – 2026.03', 'sub': '', 'items': [
                 '參與 MySphere 平台開發，設計後端 <b>REST API</b>、資料庫 <b>Schema</b>，並整合 <b>LLM API</b> 聊天機器人。',
                 '使用 <b>Docker</b>、<b>Nginx</b>、<b>Harbor</b> 建置容器化服務與私有映像檔儲存庫，透過 <b>GitHub Actions CI/CD</b> 自動完成建置及部署。',
             ]},
            {'title': '國立臺灣科技大學｜系所資訊系統維運與資料庫管理',
             'date': '2026.09 – 迄今', 'sub': '', 'items': [
                 '維護 <b>PHP / MariaDB</b> 系統，開發與修改後端功能，負責系統異常排除及使用者需求處理。',
             ]},
            {'title': '國立臺灣科技大學｜EMI 微積分教學助理',
             'date': '2025.09 – 迄今', 'sub': '', 'items': [
                 '使用 <b>React</b>、<b>Django</b>、<b>RAG</b>、<b>AI Agent</b> 開發教學管理與智慧出題系統，整合工具調用自動產製 Word 考卷。',
             ]},
            {'title': '應拿實業有限公司｜IT 系統管理員',
             'date': '2025.08 – 迄今', 'sub': '', 'items': [
                 '負責公司伺服器、資料庫與資訊系統維運、資料備份，以及設備採購、軟體授權與同仁 IT 技術支援。',
             ]},
        ]),
        ('獲選與研習｜Awards & Activities', 'list', [
            {'title': '', 'date': '', 'sub': '', 'items': [
                '<b>2026 韓國漢陽大學 6G AI-RAN / O-RAN 國際工作坊</b>：實作 <b>Open5GS</b>、<b>srsRAN</b>、<b>FlexRIC</b> 系統建置及 KPM xApp。',
                '<b>2026 智慧網路 SIG 研討會</b>：代表實驗室展示 <b>6G RAN Digital Twin</b> 與 <b>AI Agent</b> 技術。',
                '<b>2025–2026 經濟部太空產業暨網通新星飛揚計畫</b>：連續兩年入選，2025 年獲頒「<b>表現優異</b>」證書。',
            ]},
        ]),
        ('其他實作專題｜Selected Projects', 'proj', [
            {'title': '第一屆臺科青創－創業黑客松', 'date': '2026.08', 'sub': '', 'items': [
                '擔任<b>組長</b>，參賽作品「<b>FairWinds 借風</b>」IoT 風扇共享租借服務，負責 <b>ESP32</b> 智慧櫃韌體與雲端串接、'
                '<b>後端 API 與資料庫設計</b>及前端動畫串接，三天內完成下單、開櫃、計時計費至跨站歸還結算之完整原型。',
            ]},
            {'title': 'LLM 智慧工作助理系統', 'date': '', 'sub': '', 'items': [
                '使用 <b>LangGraph</b>、<b>ReAct</b> 設計 Agent 流程，整合短／長期記憶、<b>MySQL</b> 查詢及 <b>MCP</b> 工具，支援郵件與行事曆操作。',
            ]},
            {'title': 'SSD 垃圾回收排程最佳化', 'date': '', 'sub': '', 'items': [
                '以 <b>Deep Q-Learning</b> 分析 SSD 排程，使用 <b>Cython</b> 串接既有 C++ 模擬器，並以十萬筆 I/O trace 驗證。',
            ]},
        ]),
    ],
}

EN = {
    # 英文字較長，整體再縮一點才收得進一頁
    'css': "body { font-size: 8.1pt; } .e-title { font-size: 8.6pt; } .awards li { margin-bottom: 2.5px; }",
    'lang': 'en',
    'name': 'YAO-CHING HUANG',
    'name_en': '',
    'affil': 'M.S. in Electronic Engineering, NTUST | Mobile Information Technology Lab (MITLab)',
    'photo': False,
    'sections': [
        ('Education', 'edu', [
            {'title': 'NTUST | M.S. in Electronic Engineering | <b>GPA 4.18 / 4.30</b>',
             'date': 'Sep 2025 – Jul 2027 (expected)', 'sub': '', 'items': []},
            {'title': 'NTUST | B.S. in Electronic Engineering | <b>GPA 4.04 / 4.30</b>',
             'date': 'Sep 2021 – Jun 2025',
             'sub': 'Class rank <b>3 / 29</b> | Department rank <b>10 / 104</b>', 'items': []},
        ]),
        ('Research &amp; Industry Projects', 'exp', [
            {'title': 'NSTC Four-Year 6G Initiative | AI/ML Platform &amp; AI Agents',
             'date': 'Jun 2025 – Present', 'sub': '', 'items': [
                 '<b>Platform Integration:</b> Integrated <b>20+ Docker/Kubernetes</b> services and <b>Kubeflow/Argo</b> workflows to support AI/ML operations.',
                 '<b>Platform Reliability:</b> Built monitoring with <b>Prometheus/NVIDIA DCGM</b>, developed nine automated stress-test suites, and resolved <b>seven</b> platform-level issues.',
                 'Designed an <b>NVIDIA MPS</b> GPU scheduler, increasing aggregate throughput by <b>21–24%</b> and reducing batch completion time by <b>13%</b>.',
                 'Developed <b>Dify Multi-Agent ReAct</b> workflows with intent-aware tools and backend execution logic for automated model training, monitoring, and diagnosis.',
             ]},
            {'title': 'ITRI | 5G NR RAN Digital Twin &amp; O-RAN Integration',
             'date': 'Apr 2026 – Present', 'sub': '', 'items': [
                 'Developed an <b>E2 Adapter</b> connecting simulated RAN to <b>Near-RT RIC</b>; integrated <b>NVIDIA Omniverse/Sionna RT</b> for 3D radio-channel simulation.',
                 'Achieved <b>90–96%</b> agreement with <b>OAI rfsim</b> metrics; reduced mean simulation error from <b>50.1%</b> to <b>2.5%</b> using ML calibration.',
             ]},
        ]),
        ('Professional Experience', 'exp', [
            {'title': 'SparkAmplify (California, USA) | Backend / DevOps Engineering Intern',
             'date': 'Jan – Mar 2026', 'sub': '', 'items': [
                 'Developed <b>REST APIs</b>, database <b>schemas</b>, and <b>LLM API</b> chatbot integration for the MySphere platform.',
                 'Deployed containerized services using <b>Docker/Nginx/Harbor</b> and automated image builds and deployment with <b>GitHub Actions CI/CD</b>.',
             ]},
            {'title': 'NTUST | Systems Operations &amp; Database Administrator',
             'date': 'Sep 2026 – Present', 'sub': '', 'items': [
                 'Maintained <b>PHP/MariaDB</b> systems, developed and extended backend features, and resolved system and user-reported issues.',
             ]},
            {'title': 'NTUST | Calculus Teaching Assistant (EMI)',
             'date': 'Sep 2025 – Present', 'sub': '', 'items': [
                 'Built a course system with <b>React/Django</b> and a <b>RAG-powered AI Agent</b> for automated exam and Word document generation.',
             ]},
            {'title': 'Ying Na Industrial Co., Ltd. | IT Systems Administrator',
             'date': 'Aug 2025 – Present', 'sub': '', 'items': [
                 'Maintained servers, databases, internal IT systems and backups; handled equipment procurement, licensing, and employee IT support.',
             ]},
        ]),
        ('Awards &amp; International Activities', 'list', [
            {'title': '', 'date': '', 'sub': '', 'items': [
                '<b>2026 Hanyang University 6G AI-RAN/O-RAN Workshop:</b> Deployed <b>Open5GS, srsRAN, FlexRIC</b> and a KPM monitoring xApp.',
                '<b>2026 Intelligent Networking SIG Seminar:</b> Presented <b>6G RAN Digital Twin</b> and <b>AI Agent</b> demonstrations.',
                '<b>2025–2026 MOEA Space &amp; Networking R&amp;D Program:</b> Selected in two consecutive years; received a <b>2025 Outstanding Performance</b> certificate.',
            ]},
        ]),
        ('Selected Projects', 'proj', [
            {'title': '1st NTUST Youth Startup Hackathon', 'date': 'Aug 2026', 'sub': '', 'items': [
                '<b>Team lead.</b> Entry <b>FairWinds</b> &mdash; an IoT fan-sharing rental service. Built the <b>ESP32</b> locker firmware and cloud '
                'integration, <b>backend APIs and database schema</b>, and frontend animation wiring; a full rent-to-return prototype in three days.',
            ]},
            {'title': 'LLM-Powered Productivity Assistant', 'date': '', 'sub': '', 'items': [
                'Built <b>LangGraph/ReAct</b> agent workflows with short- and long-term memory, <b>MySQL</b> queries, and <b>MCP</b> tools for email and calendar tasks.',
            ]},
            {'title': 'SSD Garbage Collection Scheduling Optimization', 'date': '', 'sub': '', 'items': [
                'Studied <b>Deep Q-Learning</b> scheduling; connected Python to an existing C++ simulator via <b>Cython</b> and evaluated 100,000 I/O traces.',
            ]},
        ]),
    ],
}
