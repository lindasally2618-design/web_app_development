# 系統架構文件 – 個人記賬簿

## 1. 技術架構說明
- **後端框架**: Python + Flask
  - 輕量且內建開發伺服器，適合小型 MVP。
- **模板引擎**: Jinja2
  - 直接在伺服器端渲染 HTML，簡化前端開發。
- **資料庫**: SQLite（使用 `sqlite3` 或 SQLAlchemy）
  - 單檔資料庫，部署簡單，滿足個人使用量。
- **部署環境**: 任意支援 Python 的主機（Heroku、Render、VPS），使用 `gunicorn` 作為生產 WSGI 伺服器。
- **雲端備份**: 透過定時任務把 `instance/database.db` 上傳至 Google Drive / OneDrive（使用 API），確保資料安全。

### 為何選擇這些技術？
- **Flask MVC** 能清晰分離 **Model**（資料庫模型）、**View**（Jinja2 模板）與 **Controller**（路由），有助於維護與擴充。
- **SQLite** 為單檔、免安裝，對於大學生的個人專案成本最低。
- **Jinja2** 讓前端與後端共享資料，減少前端框架學習曲線。

## 2. 專案資料夾結構
```
web_app_development/
├─ app.py                     # Flask 入口
├─ docs/                      # 文件資料夾
│   ├─ PRD.md                 # 需求文件（已完成）
│   └─ ARCHITECTURE.md        # 本文件
├─ instance/                  # 用於存放執行時資料（SQLite DB）
│   └─ database.db            # SQLite 資料庫（git 忽略）
├─ app/                       # 核心程式碼
│   ├─ __init__.py            # 建立 Flask app 並載入設定
│   ├─ models/                # 資料模型 (SQLAlchemy / sqlite3)
│   │   └─ transaction.py     # 收支紀錄模型
│   ├─ routes/                # 路由 (Controller)
│   │   ├─ auth.py            # 使用者註冊/登入
│   │   ├─ ledger.py          # 收支 CRUD
│   │   └─ dashboard.py       # 圖表與統計
│   ├─ templates/             # Jinja2 HTML 模板 (View)
│   │   ├─ base.html
│   │   ├─ login.html
│   │   ├─ ledger.html
│   │   └─ dashboard.html
│   └─ static/                # 靜態資源 (CSS/JS)
│       ├─ css/
│       │   └─ style.css
│       └─ js/
│           └─ main.js
└─ requirements.txt          # Python 套件需求
```

- **app.py**: 建立 `Flask(__name__)`、載入 `app` 包含的藍圖，設定 `instance_path` 指向 `instance/` 目錄。
- **models/**: 定義資料表結構與 CRUD 方法。
- **routes/**: 每個功能模組化為藍圖，負責處理 HTTP 請求、驗證、呼叫模型、渲染模板。
- **templates/**: 使用 Bootstrap 5 + 自訂 CSS，提供響應式 UI。
- **static/**: 包含全局樣式、交互腳本與圖表庫（Chart.js）

## 3. 元件關係圖
```mermaid
flowchart TD
    Browser[使用者瀏覽器] -->|HTTP Request| FlaskRoute[Flask Route (Controller)]
    FlaskRoute -->|呼叫| Model[Model (SQLite)]
    Model -->|回傳資料| FlaskRoute
    FlaskRoute -->|渲染| JinjaTemplate[Jinja2 Template (View)]
    JinjaTemplate -->|回傳 HTML| Browser
    Browser -->|顯示圖表| ChartJS[Chart.js (static/js)]
```

## 4. 關鍵設計決策
1. **單檔 SQLite vs. PostgreSQL** – 選擇 SQLite 因為資料量小、部署簡易，未來若使用者規模擴大可切換至 PostgreSQL。
2. **Flask MVC 內部耦合** – 控制器只負責業務邏輯與資料處理，避免直接在模板中寫太多 Python 程式碼，以提升可測試性。
3. **雲端備份策略** – 每日利用背景工作（Celery + Redis）或簡易 `cron` 任務將 DB 複製至 Google Drive，確保資料不會因本機硬碟損毀而遺失。
4. **前端圖表選擇** – 使用 Chart.js（輕量、支援多種圖表），避免引入大型框架如 React。
5. **使用者認證** – 初期採用 Flask‑Login + bcrypt，未來可擴充 OAuth（Google）作為備用方案。

---
*本文件根據 `docs/PRD.md` 產出，由 Antigravity 於 2026‑04‑28 自動生成。*
