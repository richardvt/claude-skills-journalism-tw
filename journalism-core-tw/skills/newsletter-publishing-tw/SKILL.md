---
name: newsletter-publishing-tw
description: 台灣電子報與訂閱媒體工作流程 (繁體中文/台灣專用版,對應 upstream newsletter-publishing 的美國版)。涵蓋:電子報平台選擇 (Substack、方格子、Beehiiv、ConvertKit、MailerLite)、寄信合規 (Gmail/Yahoo/Outlook 2024 bulk sender requirements 通用)、台灣訂閱經濟、內容策略、開信率/點擊率分析、退訂管理、《消保法》《個資法》電子報相關法律。獨立記者、自媒體、傳統媒體電子報部門、訂閱經濟工作者必備。
---

# 台灣電子報與訂閱媒體工作流程

電子報是**直接擁有讀者**的渠道。本 skill 提供平台選擇、合規寄送、台灣訂閱經濟之工作流。

---

## 何時使用

- 建立新電子報
- 從傳統媒體擴展到電子報
- 自媒體訂閱經營
- 寄信合規檢核
- 訂閱戶名單管理
- 退訂、刪除請求處理

---

## 一、平台選擇(2026 年台灣場景)

### 國際平台

| 平台 | 強項 | 弱項 | 月費 (基本付費) |
|---|---|---|---|
| **Substack** | 內建付費機制、社群網絡效應、Notes 短訊 | 抽 10% 服務費、品牌綁定 | 免費 + 抽成 |
| **Beehiiv** | 功能完整、廣告網絡、推薦交換 | 介面英文為主 | $39+ |
| **ConvertKit (Kit)** | 自動化、tag 系統強 | 不適合純內容創作 | $29+ |
| **MailerLite** | CP 值高、表單與 landing page | 進階功能較少 | $9+ |
| **Mailchimp** | 老牌、整合度高 | 介面複雜、貴 | $13+ |
| **Ghost** | 開源、自架、付費功能完整 | 需技術背景 | $9+ (cloud) 或自架 |

### 台灣本地平台

| 平台 | 強項 | 弱項 |
|---|---|---|
| **方格子 (Vocus)** | 繁中介面、訂閱+單篇付費、台灣金流 | 抽成、流量需依平台演算法 |
| **PressPlay** | 訂閱經濟、Podcast 整合 | 偏向自媒體網紅,記者較少 |
| **Matters** | 台港創作社群、Web3 整合 | 受眾較學術 / 文化 |
| **報導者 / 天下 / 商周 (傳統媒體會員)** | 既有品牌信任 | 限該媒體記者 |

### 建議

| 你是誰 | 推薦 |
|---|---|
| 獨立記者,起步 | **Substack**(便利,社群效應)+ **方格子**(台灣金流) |
| 已有讀者基礎,想 own brand | **Beehiiv** 或自架 Ghost |
| 編輯部品牌,想會員制 | 自架 + Stripe / 街口 / Line Pay 金流 |
| 純內容創作者 | **方格子** + **Substack** 雙線 |

---

## 二、寄信合規(2024-2026 新標準)

> **這部分技術標準全球通用**,upstream 內容可保留。台灣媒體使用 Gmail / Yahoo / Outlook 為主要收件平台,**必須**符合下列要求。

### Gmail / Yahoo bulk sender requirements (2024/2 起)

每天**發送 ≥ 5,000 封**給 Gmail / Yahoo 個人帳號之發信者必須:

#### 1. 完整 SPF / DKIM / DMARC 設置

```dns
; SPF 紀錄(允許哪些伺服器代發)
yourdomain.com.  IN  TXT  "v=spf1 include:_spf.google.com ~all"

; DKIM 紀錄(平台會給你的 selector)
default._domainkey.yourdomain.com.  IN  TXT  "v=DKIM1; k=rsa; p=MIGfMA0..."

; DMARC 紀錄(報告與隔離政策)
_dmarc.yourdomain.com.  IN  TXT  "v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com; ruf=mailto:dmarc-forensic@yourdomain.com; fo=1"
```

**注意**:`p=none` 是觀察期;穩定後改 `p=quarantine` 或 `p=reject`。

#### 2. 一鍵退訂

- 標頭含 `List-Unsubscribe: <https://yourdomain.com/unsubscribe?id=xxx>, <mailto:unsubscribe@yourdomain.com>`
- 標頭含 `List-Unsubscribe-Post: List-Unsubscribe=One-Click`
- 退訂連結**在郵件可見處**(底部 + 視覺明顯)
- **2 天內處理退訂**

#### 3. 垃圾郵件抱怨率 < 0.3%

- 持續監控 Google Postmaster Tools、Yahoo Sender Hub
- 若 spam rate > 0.3%,需立即:
  - 重新確認名單(double opt-in 確認)
  - 暫停可疑名單
  - 改善內容(避免標題誇張、CTA 過度)

### Outlook / Microsoft (2025 起加強)

- 與 Gmail 類似要求,但 Microsoft Smart Network Data Services (SNDS) 監控
- **Microsoft 365 個人帳號**與企業帳號分流,**個人帳號要求更嚴**

### 2025 年 11 月後的 Gmail 變化

- **永久 5xx 拒絕**(原為 4xx 暫時退信):一旦觸發,**訊息直接丟失**,寄件者必須先修正才能再發
- **DMARC `p=quarantine` 或 `p=reject` 成為大量發信實質必要**

---

## 三、台灣訂閱經濟現況

### 訂閱媒體標竿

| 媒體 | 模式 | 訂閱量級 (粗估) |
|---|---|---|
| **報導者** | 非營利 + 自願訂閱 | 高量(數萬讀者)|
| **天下雜誌會員** | 付費(月/年) | 中量 |
| **商業周刊 BW Premium** | 付費 | 中量 |
| **READr** | 公益、免費 | 低量 |
| **鏡週刊鏡好聽** | Podcast + 訂閱 | 中量 |
| **聯合報新聞網會員** | 月付 + 廣告 | 高量 |
| **獨立記者 substack** | 個人訂閱 | 數百至數千 |

### 訂閱定價

- **月費**:NT$ 100-300(平面深度報導)、NT$ 50-200(自媒體個人)
- **年費**:NT$ 1,000-3,000(月費 × 10-12)
- **企業會員**:NT$ 5,000-50,000(視服務)
- **單篇付費**:NT$ 30-50

### 金流

| 工具 | 用途 |
|---|---|
| **Stripe** | 國際信用卡;Substack/Beehiiv 內建 |
| **綠界、藍新、紅陽** | 台灣信用卡 + ATM + 超商 |
| **街口、LINE Pay、悠遊付** | 行動支付 |
| **方格子內建** | 平台代收 |
| **電匯、ATM 轉帳** | 企業會員 / 大額 |

---

## 四、內容策略

### 電子報結構模板

```markdown
# [標題:本期主題,8-15 字]

[作者]  |  [日期]  |  [刊號]

---

## 引言(50-100 字)
[本期重點摘要,讓讀者 3 秒決定是否往下看]

## 主文(800-3,000 字)
[依議題分節,3-5 個小標題]

## 延伸
[相關報導連結、推薦閱讀]

## 給訂閱戶的話 / 編輯後記(可選,100-200 字)
[個人視角、本週思考]

---

[退訂連結]  |  [分享給朋友]  |  [回信給我]
```

### 寫作風格

> 詳見 `ai-writing-detox-tw`、`newsroom-style-tw`。

**電子報特有**:
- **第一人稱可用**(個人視角是訂閱戶來的原因)
- **個人風格較容許**(相對於日報)
- **互動性高**:邀讀者回信、留言
- **不要 PR 味**:訂閱戶最反感新聞稿口吻

### 標題

- **避免**「驚爆」「揭密」(對應 `ai-writing-detox-tw` §六)
- **CTA**:讓讀者預期內容
- **個人化**:可用「我」「你」開場(電子報允許)
- **長度**:**Email 主旨 30-50 字最佳**;太長手機顯示截斷

### 開信率與點擊率

| 指標 | 業界平均 | 訂閱媒體較好目標 |
|---|---|---|
| 開信率 (Open rate) | 20-25% | 35%+ |
| 點擊率 (Click rate) | 2-3% | 5%+ |
| 退訂率 (Unsubscribe rate) | < 0.5% / 期 | < 0.2% |
| 垃圾抱怨率 (Spam rate) | < 0.3% (Gmail 要求) | < 0.1% |

---

## 五、訂閱戶名單管理

### Double opt-in(雙重確認)

- 訂閱表單 → 寄確認信 → 點連結確認 → 加入名單
- 比 single opt-in 流失約 20%,但**名單品質高、垃圾抱怨低**

### 名單衛生

- **6 個月未開信** → 標記休眠,移到「reactivation」名單
- **12 個月未開信** → **主動移除**(發信前先寄「您還想收嗎?」)
- **硬退信(hard bounce)** → 立即移除
- **連續軟退信(soft bounce)** > 5 次 → 移除

### 個資保護(《個資法》)

- **告知目的**:訂閱頁面寫明「您的 email 將用於○○○電子報之寄送與分析」
- **限定範圍**:不可未經同意把名單用於其他目的(轉售、廣告)
- **退訂權**:依《個資法》§11,當事人**得隨時要求停止寄送**
- **更正權**:當事人**得要求更正資料**
- **刪除權**:當事人**得要求刪除個資**
- **資料外洩通報**:若名單外洩,**必須通報**個資主管機關 + 通知當事人

---

## 六、退訂與刪除請求

### 退訂 SOP

1. **連結即時退訂**(< 1 秒)
2. **退訂頁面可選分流**:
   - 「暫停 1 個月」「降為週報」「完全退訂」
   - 「告訴我們為什麼?」(可選,改善內容)
3. **確認退訂郵件**(寄一封「您已退訂」)
4. **48 小時內生效**(Gmail 要求 2 天內)

### 個資刪除請求(GDPR-style)

- 收到請求 → **30 天內**處理
- **同時刪除**:電子報平台名單、CRM、CDP、備份檔
- **保留法律必要紀錄**(交易、訂閱開始/結束日期等)
- 回信確認**已刪除**

---

## 七、與其他 -tw skill 協作

```
[電子報內容]
   ├── 取得資料         ← foia-requests-tw
   ├── 主張查核         ← fact-check-workflow-tw
   ├── 來源驗證         ← source-verification-tw
   ├── 採訪             ← interview-prep-tw
       ↓
[撰稿]
   ├── 去 AI 味         ← ai-writing-detox-tw
   ├── 編務             ← newsroom-style-tw
       ↓
[發送]
   ├── 平台選擇         ← 本 skill §一
   ├── 寄信合規         ← 本 skill §二
   ├── 名單管理         ← 本 skill §五
       ↓
[分析與回饋]
```

---

**版本說明**

- 版本:0.1.0 / 截至 2026-05-28
- 改寫自 upstream `journalism-core/newsletter-publishing`
- 在地化重點:加入方格子、PressPlay、Matters 等台灣本地平台;台灣訂閱媒體標竿(報導者、天下、商周、鏡週刊);台灣金流選擇(綠界、藍新、街口、LINE Pay);台灣《個資法》電子報相關規範
- Gmail / Yahoo / Outlook 寄信合規部分為全球技術標準,沿用 upstream;2025/11 Gmail 永久 5xx 拒絕變化已納入
