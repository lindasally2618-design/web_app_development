# ROUTES – 個人記賬簿 系統路由設計

## 1️⃣ 路由總覽表格
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
|------|-----------|----------|----------|------|
| 使用者註冊 | GET | /auth/register | templates/auth/register.html | 顯示註冊表單 |
| 使用者註冊 | POST | /auth/register | — | 處理表單，建立使用者，重導向至登入 |
| 使用者登入 | GET | /auth/login | templates/auth/login.html | 顯示登入表單 |
| 使用者登入 | POST | /auth/login | — | 驗證憑證，建立 session，重導向至首頁 |
| 使用者登出 | POST | /auth/logout | — | 清除 session，重導向至登入頁 |
| 首頁儀表板 | GET | / | templates/dashboard/index.html | 顯示概覽圖表與近期交易 |
| 交易列表 | GET | /ledger | templates/ledger/list.html | 顯示使用者所有收支紀錄，支援分頁與過濾 |
| 新增交易 (表單) | GET | /ledger/add | templates/ledger/add.html | 顯示新增交易表單 |
| 新增交易 (提交) | POST | /ledger/add | — | 儲存交易資料，重導向至列表 |
| 編輯交易 (表單) | GET | /ledger/<int:id>/edit | templates/ledger/edit.html | 顯示編輯表單，預填現有資料 |
| 更新交易 (提交) | POST | /ledger/<int:id>/edit | — | 更新資料，重導向至列表 |
| 刪除交易 | POST | /ledger/<int:id>/delete | — | 刪除指定交易，重導向至列表 |
| 分類管理 (列表) | GET | /categories | templates/category/list.html | 顯示使用者自訂標籤清單 |
| 新增分類 | GET | /categories/add | templates/category/add.html | 顯示新增標籤表單 |
| 新增分類 (提交) | POST | /categories/add | — | 建立標籤，重導向至列表 |
| 編輯分類 | GET | /categories/<int:id>/edit | templates/category/edit.html | 顯示編輯表單 |
| 更新分類 (提交) | POST | /categories/<int:id>/edit | — | 更新標籤，重導向至列表 |
| 刪除分類 | POST | /categories/<int:id>/delete | — | 刪除標籤，重導向至列表 |
| 預算設定 (列表/檢視) | GET | /budget | templates/budget/list.html | 顯示使用者所有預算設定 |
| 新增/更新預算 (表單) | GET | /budget/add | templates/budget/add.html | 顯示預算表單 (建立或編輯) |
| 新增/更新預算 (提交) | POST | /budget/add | — | 儲存預算，重導向至列表 |
| 刪除預算 | POST | /budget/<int:id>/delete | — | 刪除預算，重導向至列表 |
| 雲端備份 & 匯出 | POST | /backup | — | 觸發資料備份或匯出 CSV/Excel，回傳成功訊息 |

## 2️⃣ 路由詳細說明（示例）
### /auth/register (GET)
- **輸入**: 無
- **處理邏輯**: 渲染 `templates/auth/register.html`
- **輸出**: 註冊表單頁面
- **錯誤處理**: 若已登入，重導向至 `/`

### /auth/register (POST)
- **輸入**: `email`, `password`, `confirm_password`
- **處理邏輯**: 檢查欄位與密碼一致性 → 呼叫 `User.create` → 設定 flash 訊息
- **輸出**: 成功則重導向至 `/auth/login`，失敗則重新渲染註冊頁並顯示錯誤
- **錯誤處理**: Email 已被註冊、表單驗證失敗

### /ledger/add (GET)
- **輸入**: 無
- **處理邏輯**: 從 `Category` 取得使用者標籤列表 → 渲染 `templates/ledger/add.html`
- **輸出**: 新增交易表單
- **錯誤處理**: 未登入 → 重導向至 `/auth/login`

### /ledger/add (POST)
- **輸入**: `amount`, `type`, `date`, `category_id`, `note`
- **處理邏輯**: 資料驗證 → 呼叫 `Transaction.create` → Flash 成功訊息
- **輸出**: 重導向至 `/ledger`
- **錯誤處理**: 欄位缺失或驗證失敗，重新渲染表單並顯示錯誤

（其餘路由以相同方式說明，可在實作階段補齊）

## 3️⃣ Jinja2 模板清單
- `templates/base.html` – 全局基礎模板，包含 navbar、flash 訊息
- `templates/auth/login.html`
- `templates/auth/register.html`
- `templates/dashboard/index.html`
- `templates/ledger/list.html`
- `templates/ledger/add.html`
- `templates/ledger/edit.html`
- `templates/category/list.html`
- `templates/category/add.html`
- `templates/category/edit.html`
- `templates/budget/list.html`
- `templates/budget/add.html`

---
*此檔案根據 `docs/PRD.md`、`docs/ARCHITECTURE.md` 與 `docs/DB_DESIGN.md` 產出，由 Antigravity 於 2026‑04‑28 自動生成。*
