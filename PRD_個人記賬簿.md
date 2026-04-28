# PRD – 個人記賬簿系統

## 1. Executive Summary
A lightweight, web‑based personal finance management application designed for university students. It enables quick daily income/expense logging, budget monitoring, visual analytics, custom categorisation, and secure cloud backup/export.

## 2. Goals & Success Metrics
- **Goal**: Provide an intuitive tool for students to track cash flow and stay within budgets.
- **Success Metrics**
  - >80% of weekly active users record at least one transaction per day.
  - <5% of users report budget‑overrun alerts as false positives.
  - 90% satisfaction in post‑launch survey.

## 3. Target Users
- University students (undergraduate & graduate) who manage personal expenses such as tuition, rent, food, transport, and entertainment.

## 4. Core Features
| # | Feature | Description |
|---|---------|-------------|
| 1 | 收支快速紀錄 | One‑click entry form (amount, category, date, optional note). Supports recurring entries. |
| 2 | 預算超支提醒 | User‑defined monthly budget per category. Real‑time alert when spend > 90% of budget. |
| 3 | 多維度圖表分析 | Interactive charts (line, bar, pie) for income vs expense, category breakdown, trend over time. |
| 4 | 自定義分類標籤 | Unlimited user‑created tags with colour coding; hierarchical tagging supported. |
| 5 | 雲端備份與匯出 | Automatic daily backup to secure cloud storage (e.g., Google Drive/OneDrive). Export CSV/Excel. |
| 6 | 使用者認證 (附加) | Email/password login with optional OAuth (Google). Data isolated per account. |
| 7 | 資料匯入 (附加) | Import existing CSV bank statements to seed initial data. |

## 5. User Stories
1. **快速記帳** – As a student, I want to tap a button and log a $5 coffee expense instantly, so I can capture spontaneous purchases.
2. **預算提醒** – As a student, I set a $200 monthly food budget and receive a push notification when I spend $180.
3. **圖表檢視** – As a student, I view a pie chart of my spending categories for the last month to see where my money goes.
4. **自訂標籤** – As a student, I create a "課外活動" tag with a blue badge and assign it to related expenses.
5. **雲端備份** – As a student, I travel abroad and still access my ledger because all data is synced to the cloud.
6. **匯出報表** – As a student, I export my transaction history as CSV for tax filing.

## 6. Functional Flow (high‑level)
1. User registers / logs in → Dashboard loads.
2. User adds transaction → Entry saved to SQLite → Sync triggered → Cloud backup updated.
3. Budget engine evaluates spend vs budget → If threshold exceeded, push notification sent.
4. Analytics module aggregates data → Generates charts on demand.
5. Export endpoint produces CSV/Excel file on request.

## 7. Non‑Functional Requirements
- **Performance**: Page load < 1 s on typical 3G/4G.
- **Security**: Passwords hashed with bcrypt; HTTPS enforced.
- **Scalability**: Designed for up to 5 000 active users; can shard DB if needed.
- **Usability**: Mobile‑first responsive UI; WCAG AA compliance.
- **Reliability**: Daily automated backups; 99.5% uptime SLA.

## 8. Scope & Prioritisation
| Phase | Features Included |
|-------|-------------------|
| **MVP** (Week 1‑3) | 快速紀錄、預算提醒、基本圖表、雲端備份、使用者認證 |
| **Stretch 1** (Week 4) | 自定義標籤、CSV匯出 |
| **Stretch 2** (Week 5‑6) | 多維度圖表進階、資料匯入、OAuth 登入 |

## 9. Assumptions & Risks
- Assumption: Users have internet access for cloud sync.
- Risk: Cloud provider API limits – mitigate with exponential back‑off and local cache.
- Risk: Data privacy – implement GDPR‑style consent and allow data deletion.

## 10. Milestones & Timeline
| Milestone | Deliverable | Target Date |
|-----------|-------------|-------------|
| 1️⃣ PRD completed | This document | 2026‑04‑28 |
| 2️⃣ Architecture design | `docs/ARCHITECTURE.md` | 2026‑05‑02 |
| 3️⃣ Database schema | `docs/DB_SCHEMA.md` | 2026‑05‑04 |
| 4️⃣ Core implementation | Flask API + Jinja2 UI | 2026‑05‑12 |
| 5️⃣ Testing & QA | Unit & UI tests | 2026‑05‑16 |
| 6️⃣ Release candidate | Deploy to staging | 2026‑05‑20 |
| 7️⃣ Production launch | Public URL | 2026‑05‑22 |

---
*Prepared by Antigravity on 2026‑04‑28*
