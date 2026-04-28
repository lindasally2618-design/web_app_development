# 流程圖文件 – 個人記賬簿

## 1️⃣ 使用者流程圖（User Flow）

```mermaid
flowchart LR
    A([使用者開啟網站]) --> B[登入/註冊頁面]
    B -->|成功登入| C[首頁儀表板]
    C --> D{想要執行什麼操作？}
    D -->|記錄收支| E[新增交易表單]
    E --> F[提交表單]
    F --> G[交易儲存成功] --> H[返回首頁並更新圖表]
    D -->|檢視圖表| I[分析圖表頁面]
    I --> J[切換不同圖表類型]
    D -->|管理分類| K[自訂標籤設定]
    K --> L[新增/編輯/刪除標籤]
    D -->|備份/匯出| M[資料備份與匯出頁面]
    M --> N[選擇匯出格式或觸發雲端備份]
```

## 2️⃣ 系統序列圖（Sequence Diagram） – 新增交易流程

```mermaid
sequenceDiagram
    participant User as 使用者
    participant Browser as 瀏覽器
    participant Flask as Flask Route
    participant Model as Model (SQLAlchemy)
    participant DB as SQLite

    User->>Browser: 開啟 "新增交易" 表單
    Browser->>Flask: POST /ledger/add (表單資料)
    Flask->>Model: create_transaction(data)
    Model->>DB: INSERT INTO transactions ...
    DB-->>Model: 成功回傳
    Model-->>Flask: 新增成功訊息
    Flask-->>Browser: 重導向至首頁，顯示最新數據
    Browser->>User: 顯示新增成功的 UI
```

## 3️⃣ 功能清單對照表

| 功能 | URL 路徑 | HTTP 方法 | 說明 |
|------|----------|-----------|------|
| 收支快速紀錄 | /ledger/add | POST | 新增收入或支出交易
| 查看交易列表 | /ledger | GET | 顯示所有交易，支援分頁與過濾
| 編輯交易 | /ledger/edit/<id> | POST | 更新既有交易資料
| 刪除交易 | /ledger/delete/<id> | POST | 移除指定交易
| 預算提醒 | /budget | GET | 取得當前預算使用率與超支警示
| 圖表分析 | /dashboard | GET | 回傳圖表資料 JSON，供前端渲染
| 自定義分類 | /tags | GET/POST/PUT/DELETE | 管理使用者標籤
| 雲端備份 | /backup | POST | 手動觸發備份或匯出 CSV/Excel
```

---
*此文件根據 `docs/PRD.md` 與 `docs/ARCHITECTURE.md` 產出，由 Antigravity 於 2026‑04‑28 自動生成。*
