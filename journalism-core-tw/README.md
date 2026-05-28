# journalism-core-tw

新聞工作者核心技能的繁體中文/台灣在地化版本,改寫自 [`journalism-core`](https://github.com/jamditis/claude-skills-journalism)。

## 命名約定

所有 skill 一律加 `-tw` 後綴 (例:`foia-requests-tw`),可與 upstream 英文版 `journalism-core` 並存安裝、對照比較。

## 已在地化 Skill

| Skill | 對應 upstream | 用途 |
|---|---|---|
| **foia-requests-tw** | foia-requests | 台灣《政府資訊公開法》申請流程、9 款限制公開事由、訴願與行政訴訟救濟、申請書範本、18 則行政法院判決見解、政府資料平台 |
| **ai-writing-detox-tw** | ai-writing-detox | 中文 AI 寫作 pattern (套語家族、中國大陸用語滲透、四字成語堆疊、新聞文體禁忌)、Before/After 對照、發稿前自我檢查清單 |
| **newsroom-style-tw** | newsroom-style | 台灣編務慣例 (依教育部《重訂標點符號手冊》、行政院《公文書數字使用原則》);數字、日期時間、人名譯名 (兩岸譯名差異)、職稱、引號標點、機構地名、引述動詞、性別族群用語、兩岸關係用語、常見錯字 |
| **fact-check-workflow-tw** | fact-check-workflow | 台灣查核生態 (IFCN 認證狀態須查證之專業查核機構、Cofacts 社群協作平台、蘭姆酒吐司與 LINE 訊息查證合作來源)、台灣資料來源、評等 6 級制、法律風險 (《刑法》§310、《社維法》§63)、常見假訊息類別 |
| **source-verification-tw** | source-verification | SIFT、台灣社群平台帳號驗證 (Threads/PTT/Dcard/LINE/FB)、反向圖搜、C2PA、深偽偵測、台灣 2024 大選深偽案例 (賴清德/高嘉瑜)、DoubleThink Lab/IORG、訪談前公開資料查證、法律風險 (《選罷法》§104 加重深偽條款) |
| **interview-prep-tw** | interview-prep | 採訪準備、5 必問/6 問句/4 訪談類型、**台灣錄音法律** (《刑法》§315-1、《通保法》§29 第 3 款、實務判決)、台灣媒體歸屬實務、**8 種特殊受訪對象** (政治人物、政務官、原民族長、移工、性平受害者、災難倖存者、兒少、加害人) |
| **social-media-intelligence-tw** | social-media-intelligence | 跨平台監測 (16 平台)、帳號真實性、台灣協同操作偵測 (GoLaxy 案例)、敘事擴散鏈、DoubleThink Lab/IORG 研究方法、Bellingcat 工具集、法律風險 (§104 加重深偽、§358 入侵電腦) |
| **interview-transcription-tw** | interview-transcription | 雅婷逐字稿、Whisper large-v3、台/客/原民族語、引語資料庫、引語精準度規則、檔案保存與銷毀 |
| **crisis-communications-tw** | crisis-communications | 11 種台灣常見危機類別、突發新聞時間軸 SOP (0-15 分/15-60 分/1-6 時/6-24 時/24-72 時)、NCC 廣電法、災害現場記者安全、誤報更正模板 |
| **data-journalism-tw** | data-journalism | 19 個台灣政府開放資料來源、台灣資料清理常見坑 (縣市改制、民國/西元、編碼)、Datawrapper/g0v 等視覺化工具、開放資料倫理 |
| **editorial-workflow-tw** | editorial-workflow | 編輯部選題追蹤、稿單管理、台灣中型編輯部架構、紙本/網路/週刊/廣電差異、三層審核流程、新進記者訓練 |
| **newsletter-publishing-tw** | newsletter-publishing | 方格子等台灣本地平台、Gmail/Yahoo/Outlook 寄信合規 (2024-2026)、台灣訂閱媒體標竿、《個資法》電子報規範 |
| **story-pitch-tw** | story-pitch | 16 家台灣主流媒體投稿指南 (報導者、天下、商周、READr、鏡週刊、INSIDE、關鍵評論網 等)、稿費行情、自由工作者合約注意事項 |

## 典型記者工作流

13 個 skill **互補不重疊**,涵蓋從**選題 pitch → 資料蒐集 → 來源驗證 → OSINT → 採訪轉錄 → 查核 → 文體 → 編務 → 突發應變 → 資料新聞 → 電子報發行 → 編輯部管理**之完整新聞生命週期。寫一篇涉及政府資料的深度報導,典型流程:

```
┌────────────────────────────────────────────────────────────┐
│                                                              │
│  [1. 資料蒐集]                                              │
│       │                                                      │
│       │   foia-requests-tw                                   │
│       │   ─ 寫政資法申請書                                   │
│       │   ─ 追蹤申請進度                                     │
│       │   ─ 拒絕時寫訴願書、行政訴訟訴狀                     │
│       ▼                                                      │
│  [2. 來源驗證 / 內容查證]                                   │
│       │                                                      │
│       │   source-verification-tw                              │
│       │   ─ SIFT 方法 + 台灣社群平台帳號驗證                 │
│       │   ─ 反向圖搜 + C2PA + 深偽偵測                       │
│       │   ─ 台灣 2024 大選深偽案例                          │
│       │   ─ 法律風險 (《選罷法》§104)                       │
│       ▼                                                      │
│  [2.5. 跨平台 OSINT / 協同操作偵測]                         │
│       │                                                      │
│       │   social-media-intelligence-tw                       │
│       │   ─ 跨 16 平台監測 (Threads/PTT/Dcard/LINE/X/TikTok…) │
│       │   ─ 帳號真實性 + 網絡分析                           │
│       │   ─ 台灣協同操作偵測 (GoLaxy/IORG 研究方法)          │
│       │   ─ 敘事擴散鏈追蹤                                  │
│       ▼                                                      │
│  [3. 採訪準備 / 採訪]                                       │
│       │                                                      │
│       │   interview-prep-tw                                  │
│       │   ─ 訪前 checklist + 5 必問 / 6 問句 / 4 訪談類型    │
│       │   ─ 台灣錄音法律 (《刑法》§315-1、《通保法》§29)    │
│       │   ─ 8 種特殊受訪對象 (政務官、原民、移工、兒少 …)   │
│       ▼                                                      │
│  [4. 事實查核 / 主張驗證]                                   │
│       │                                                      │
│       │   fact-check-workflow-tw                             │
│       │   ─ 主張提取與優先級                                 │
│       │   ─ 4 大查核機構 + LINE 訊息查證                    │
│       │   ─ 證據蒐集與存檔 (Wayback / Archive.today)        │
│       │   ─ 求證來源 + 評等 6 級制                          │
│       │   ─ 法律風險 (《刑法》§310、《社維法》§63)          │
│       ▼                                                      │
│  [5. AI 起草草稿]                                           │
│       │                                                      │
│       ▼                                                      │
│  [6. 去 AI 寫作味]                                          │
│       │                                                      │
│       │   ai-writing-detox-tw                                │
│       │   ─ 抓「值得我們深思」「在這個...時代」等套語        │
│       │   ─ 抓「視頻/網絡/賦能」等大陸用語                   │
│       │   ─ 抓「不僅...更...」三段排比等結構                 │
│       │   ─ 抓設問句、學者腔、廢話開場/結尾                  │
│       ▼                                                      │
│  [7. 編務校對]                                              │
│       │                                                      │
│       │   newsroom-style-tw                                  │
│       │   ─ 數字(阿拉伯/中文,依公文書數字使用原則)        │
│       │   ─ 標點(全形/半形、引號《》〈〉、破折號)         │
│       │   ─ 人名譯名(川普/特朗普 等兩岸差異)               │
│       │   ─ 職稱、機構名、地名                              │
│       │   ─ 引述動詞、消息來源等級                          │
│       │   ─ 性別族群用語、兩岸關係用語                      │
│       │   ─ 常見錯字(的/得/地、需/須、做/作)              │
│       ▼                                                      │
│  [8. 發稿]                                                  │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

### 互補關係速覽

| 維度 | foia-requests-tw | source-verification-tw | fact-check-workflow-tw | ai-writing-detox-tw | newsroom-style-tw |
|---|---|---|---|---|---|
| **時機** | 資料蒐集 | 來源/內容驗證 | 主張驗證 | 草稿初成 | 發稿前 |
| **層次** | 法律與程序 | 數位內容真偽 | 證據與紀律 | 文字風格 | 編務規範 |
| **權威來源** | 政資法、訴願法、行政訴訟法 | C2PA、SIFT、DoubleThink Lab、IORG | IFCN 5 原則、台灣 4 大查核機構、《刑法》§310、§311 | (語感經驗 + 兩岸譯名查證) | 教育部《標點手冊》、行政院《數字使用原則》 |
| **大陸用語** | 不處理 | **識別偽裝台灣帳號之滲透**(GoLaxy) | 不處理 | 一般用語(視頻、賦能、打造) | 人名地名(川普 vs 特朗普) |
| **新聞禁忌詞** | 不處理 | 不處理 | 不處理 | 詳述「驚爆」「揭密」改寫方向 | 簡列禁用詞 |
| **數字寫法** | 不處理 | 不處理 | **數據查證** | 不處理 | **格式權威處理** |
| **引述、消息來源** | 不具名來源法律保護 | **驗證帳號真偽** | **證據強度評估**(不具名僅為線索) | 不處理 | **引述動詞色彩** + 匿名規則 |
| **影像/影片驗證** | 不處理 | **主處理** (反向圖搜、C2PA、深偽偵測) | 配合 | 不處理 | 不處理 |
| **法律風險** | 政資法救濟 | **§315-1 妨害秘密、§104 加重深偽** | **誹謗、散布謠言、選罷法** | 不處理 | 不處理 |

### 重疊時的優先級

- **大陸用語**:`ai-writing-detox-tw` 抓一般用語、`newsroom-style-tw` 抓人名地名、`source-verification-tw` 抓偽裝台灣帳號之滲透,**三者互補**
- **標題禁忌詞**:`ai-writing-detox-tw` 為主(詳述);`newsroom-style-tw` 簡要呼應
- **「我們」「您」濫用**:以 `ai-writing-detox-tw` §五為準
- **數字寫法**:以 `newsroom-style-tw` §一為準(格式權威)
- **數據可信度**:以 `fact-check-workflow-tw` 為準(評估證據強度)
- **影像/影片真偽**:以 `source-verification-tw` §三、§四、§五為主(技術驗證);`fact-check-workflow-tw` §三輔助評估證據強度
- **不具名來源**:`source-verification-tw` §二(帳號驗證)+ `fact-check-workflow-tw`(證據強度)+ `newsroom-style-tw` §八(匿名規則)+ `foia-requests-tw`(法律保護) — **四 skill 搭配最完整**
- **妨害名譽風險**:`fact-check-workflow-tw` §九(誹謗、社維法)+ `source-verification-tw` §十二(深偽 §104) — **兩者各管一邊**
- **深偽 / AI 生成內容**:以 `source-verification-tw` 為主(C2PA + 偵測工具 + §選罷法 §104);跨入查核評等再轉 `fact-check-workflow-tw`

> 每個 SKILL.md 末尾有「**與其他 -tw skill 協作**」章節,有更詳細的轉手規則表。

### v0.8.0 新增 6 個 skill 的定位

| Skill | 何時用 | 與核心 5 skill 之關係 |
|---|---|---|
| `interview-prep-tw` | 採訪前準備、錄音同意 | 與 `fact-check-workflow-tw` 串接(訪後查核引語) |
| `interview-transcription-tw` | 訪後轉錄、引語管理 | `interview-prep-tw` 的延伸 |
| `social-media-intelligence-tw` | 跨平台 OSINT、協同操作偵測 | 與 `source-verification-tw` 互補(單帳號 vs 多帳號) |
| `crisis-communications-tw` | 突發新聞應變(< 24 小時) | 整合 `fact-check-workflow-tw` 快速版 + `source-verification-tw` 快速驗證 |
| `data-journalism-tw` | 資料新聞分析、視覺化 | 接續 `foia-requests-tw` 取得資料後 |
| `editorial-workflow-tw` | 編輯部流程、選題、稿單 | **管理層 skill**,協調其他 skill 在編輯部運作 |
| `newsletter-publishing-tw` | 電子報、訂閱媒體 | **發行層 skill**,接續寫稿 skill 後 |
| `story-pitch-tw` | 對外投稿、題目提案 | **入口層 skill**,在採訪前 |

### 依稿件類型的決策樹

| 稿件類型 | foia | source-ver | fact-check | ai-detox | newsroom | 說明 |
|---|---|---|---|---|---|---|
| 調查報導 / 深度資料新聞 | ✅ | ✅ | ✅ | ✅ | ✅ | 5 skill 全程串接;查核+驗證紀錄是日後法律抗辯關鍵 |
| 查核專題(專門評等某主張) | ⚠️ | ✅ | ✅ 主要 | ✅ | ✅ | 來源驗證 + 主張查核並重 |
| 影像/影片真偽報導 | ⛔ | ✅ 主要 | ✅ | ✅ | ✅ | 深偽偵測 + C2PA;法律風險(§104)需高度警覺 |
| 新聞稿改寫(英/簡中) | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | 若原文有圖檔需驗證;查證+去 AI 腔+在地化定稿 |
| 訪談特寫 / 人物報導 | ⛔ | ✅ 受訪者背景 | ⚠️ 引語查證 | ✅ | ✅ | 訪前公開資料查證 + 引語對照 |
| 純評論 / 社論 | ⛔ | ⛔ | ⚠️ 事實基礎 | ✅ 建議 | ✅ | 評論可表達意見,事實基礎仍須正確 |
| 社群貼文 (FB/X/IG/Threads) | ⛔ | ⚠️ 引用素材時 | ⚠️ 轉貼前 | ✅ 主要 | ⚠️ 選跑 | 媒體記者社群貼文亦負查核責任 |
| 即時新聞(快訊) | ⛔ | ✅ 影像快驗 | ✅ 快速核實 | ✅ 建議 | ✅ | 時效壓力下仍須核實 |
| 純文化 / 藝術評論 | ⛔ | ⛔ | ⚠️ 作品/人名 | ✅ 建議 | ✅ | 評論可主觀,事實項目須正確 |
| OSINT / 揭弊報導 | ✅ 若涉政府 | ✅ 主要 | ✅ | ✅ | ✅ | 帳號驗證 + 文件驗證;高法律風險,需法務協助 |

判斷各 skill 是否要跑的核心原則:
- `foia-requests-tw`:稿件是否涉及向政府機關申請資料或提出訴願
- `source-verification-tw`:稿件是否含**社群截圖、影像、影片、未經驗證之帳號發言、或匿名爆料來源**
- `fact-check-workflow-tw`:稿件是否含**任何可被驗證為真/偽的事實主張**(評論文章只要引用事實就要查核)

## 安裝

從 repo 根 marketplace 安裝:

```
/plugin marketplace add /Users/vt_god/claude-skills-journalism-tw
/plugin install journalism-core-tw@claude-skills-journalism-tw
```

## 並存安裝

`journalism-core-tw` 的 skill 名加 `-tw` 後綴 (例:`foia-requests-tw`),可與 upstream 英文版 `journalism-core` 同時安裝,Claude 會依語言/場景線索自動挑選。

要強制使用特定版本,在 prompt 直接指明:

```
用 foia-requests-tw ...     # 強制使用台灣版
用 foia-requests ...         # 強制使用英文版
```

對照比較範例:

```
用 foia-requests-tw 幫我寫向 NCC 申請某裁罰處分書的申請書,
之後再用 foia-requests (英文版) 寫一份同樣需求,我要比較兩版差異
```

## 授權

MIT — 繼承 upstream 授權。
