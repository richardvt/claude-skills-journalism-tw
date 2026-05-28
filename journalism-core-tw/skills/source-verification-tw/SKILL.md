---
name: source-verification-tw
description: 台灣新聞來源驗證與數位內容查證工作流程 (繁體中文/台灣專用版,對應 upstream source-verification 的美國版)。涵蓋:SIFT 方法、來源可信度評估、社群帳號驗證 (Threads/PTT/Dcard/LINE/FB/X)、反向圖片搜尋 (TinEye/Yandex/Google Lens)、影片驗證 (InVID/WeVerify)、C2PA 內容憑證、AI 生成內容與深偽偵測 (Hive AI/Reality Defender/法務部調查局)、台灣深偽真實案例 (2024 大選賴清德、高嘉瑜變造影片)、台灣資訊作戰研究機構 (DoubleThink Lab/IORG)、文件驗證、訪談前公開資料查證、法律風險 (《選罷法》§104 加重深偽條款、《刑法》§310、§315-1、《個資法》)。驗證社群帳號真偽、查證圖片影片、偵測 AI 生成內容、追蹤協同操作帳號、訪談前公開資料查證時觸發。記者、查核員、調查報導工作者必備。
---

# 台灣新聞來源驗證工作流程

數位內容驗證**是系統性流程,不靠肉眼直覺**。本 skill 提供來源評估、社群帳號分析、影像驗證、深偽偵測、文件驗證的完整結構,並依台灣資訊環境與法律框架在地化。

> **與 `fact-check-workflow-tw` 互補**:
> - `fact-check-workflow-tw`:**主張**(claim)的查核與評等
> - `source-verification-tw`:**來源**(source)的驗證、數位內容的真偽
> 
> 一則 LINE 訊息查核時:用 `fact-check-workflow-tw` 評等其主張;用 `source-verification-tw` 驗證其附帶的影像、轉傳者帳號、引用網址。

---

## 何時使用

- 收到匿名爆料、未確認來源訊息時
- 社群媒體爆紅內容欲報導前
- 驗證影像、影片是否經 AI 生成或變造
- 訪談前對受訪者背景之公開資料查證
- 跨平台追蹤同一則訊息的擴散路徑
- 突發新聞中快速驗證流傳內容
- 評估「該不該引述」一個來源

---

## 一、驗證框架

### SIFT 方法(全球通用)

| 步驟 | 含義 | 做什麼 |
|---|---|---|
| **S - Stop** | 暫停 | 不要立即分享或引用未經查證之內容 |
| **I - Investigate the source** | 查源 | 誰在背後散布?帳號創立日、身分、過往紀錄 |
| **F - Find better coverage** | 找更好的報導 | 其他可信來源怎麼說? |
| **T - Trace claims** | 溯源 | 找到主張的**原始來源**,不要二手轉述 |

### 輸入 / 輸出與信心分級

每次驗證都應留下可追溯輸出,避免把「感覺可疑」寫成結論。

| 欄位 | 必填內容 |
|---|---|
| 驗證對象 | URL、截圖、原始檔、帳號 ID、收到時間 |
| 方法 | SIFT 步驟、反向圖搜、C2PA、偵測器、聯絡來源 |
| 證據 | 可重查連結、截圖、hash、存檔網址、聯絡紀錄 |
| 限制 | 無法取得原始檔、平台剝 metadata、來源拒答等 |
| 判斷 | `可確認` / `疑似` / `無法判定` / `不建議引用` |

**信心分級**:
- **高**:原始來源 + 獨立旁證 + 可重現證據一致
- **中**:多個外部訊號一致,但缺原始檔或直接來源
- **低**:僅有自動工具、肉眼判讀或二手截圖

### 來源可信度 checklist

```markdown
## 來源評估模板

### 基本識別
- [ ] 全名/組織已識別
- [ ] 聯絡資訊可驗證
- [ ] 專業資歷可查證
- [ ] 跨平台線上身分一致

### 專業性評估
- [ ] 主張之領域與其專業相關
- [ ] 該領域之過往紀錄
- [ ] 受同行認可
- [ ] 無散布錯誤資訊之歷史

### 動機分析
- [ ] 已識別潛在利益衝突
- [ ] 是否與結果有財務利害關係?
- [ ] 是否有政治或意識形態動機?
- [ ] 是否涉個人恩怨?

### 旁證
- [ ] 主張可獨立驗證?
- [ ] 其他可信來源確認?
- [ ] 有文件證據?
- [ ] 有反對來源?
```

---

## 二、社群帳號驗證(台灣平台)

> **若需深度 OSINT 追蹤協同操作、敘事追蹤、跨平台分析**,請進一步使用 `social-media-intelligence-tw`。本節聚焦「**引述前該驗證**」的快速判斷。

### 帳號驗證 checklist(通用)

```markdown
### 帳號年齡與歷史
- 創立日期(較舊帳號通常較可信)
- 發文頻率與規律性
- 活動空窗(沈寂多年突然爆量發文?)
- 用詞與風格隨時間一致性

### 網絡分析
- 追蹤者/被追蹤比
- 追蹤者品質(真實 vs 機器人/活殭屍)
- 互動模式(誰跟他互動?)
- 與已驗證帳號之共同連結

### 內容模式
- 原創內容 vs 純轉貼
- 持續關注之主題
- 貼文中之地理線索
- 發文時區/時間規律

### 紅旗(高風險警示)
- 近期創立帳號卻發出重大主張
- 主題或語氣突然大轉變
- 與其他帳號有協同行為
- 大頭照是 stock photo 或 AI 生成
- 自我介紹空泛無細節
- 大頭照貓狗寵物(GoLaxy 案例)
- 簡介寫「台灣人」但用詞偏簡體中文用語
```

### 台灣主要社群平台特性

| 平台 | 台灣使用情境 | 驗證重點 |
|---|---|---|
| **Threads** | Z 世代/即時新聞擴散主場,2024 起爆紅 | 帳號創立日(2023 後普遍開放);與 IG 連動但獨立經營;**追蹤關係不對稱**(無「好友」概念) |
| **PTT** | 中年男性/政治、3C、股票 | **看 ID 註冊日**(`/help` 看註冊年份);看發文歷史(`/W` 顯示文章/推噓);**新註冊 ID 在政治板發文要警覺** |
| **Dcard** | 大學生/年輕女性/校園話題 | **校園認證**(有畢業學校資訊);**主題板偏向輕量 / 生活**;爆紅文章可能來自匿名洩漏需驗證 |
| **Facebook** | 全年齡層/政治、地方新聞、社團 | **個人檔案**:朋友數、共同朋友、過往貼文;**粉專**:認證 ✅ 標記;**社團**:管理員身分、社團成立日 |
| **LINE** | 全年齡層/即時通訊、長輩、群組轉傳 | **無公開個人檔案**,難以驗證;LINE 群組轉傳訊息要先**追溯來源截圖**;LINE OpenChat 有公開資訊 |
| **X (Twitter)** | 媒體記者、學術圈、國際新聞 | **藍勾勾自 2023 改成付費認證**,非身分驗證;改看帳號創立日、follower 品質;blue check ≠ 可信 |
| **YouTube** | 全年齡層/影片、新聞剪輯 | 頻道創立日、訂閱數、總觀看;**新頻道大量轉發政治內容警覺**;與 TikTok 帳號交叉比對 |
| **Instagram** | 年輕族群/視覺內容 | 個人檔案與 Threads 連動;**商業帳號**有公司資訊 |
| **TikTok** | 青少年/短影音、跳舞 | **IORG 2025 研究指出 TikTok 對台灣青少年資訊環境影響顯著**;帳號註冊 IP 可能在境外;敏感政治話題慎信 |
| **Telegram** | 公民團體、抗爭運動、加密訊息 | **匿名性高**,難驗證;頻道訂閱數可購買 |
| **微博 / 小紅書** | 主要為中國使用者,但部分台灣使用者交流 | 註冊需手機實名;**境外資訊操作起點** |

### 台灣特有警示訊號

依台灣民主實驗室(DoubleThink Lab)2025 年 GoLaxy 文件研究與 IORG 報告:

| 訊號 | 含義 | 範例 |
|---|---|---|
| **AI 生成大頭照** | 中國影響力作戰使用 AI 寵物照片、人像 | GoLaxy 案例:AI 生成貓狗頭貼 + 「台灣居民」自我介紹 |
| **「視頻」「網絡」用語滲透** | 自稱「台灣人」但用簡中用語 | 看 §`ai-writing-detox-tw` §二大陸用語表 |
| **發文時間集中於北京時區** | 帳號謊稱在台灣但活動模式與北京時區同步 | UTC+8 但發文聚集在 09:00-18:00 (中國上班時間) |
| **轉貼但無原創** | 大量轉貼特定 narrative,無個人生活內容 | 純政治轉發、無日常 |
| **批次帳號特徵相似** | 多個帳號用相同模板、命名規則 | 4 字命名 + 數字結尾 |
| **跨平台同步發文** | 同則訊息在 X / Threads / FB 同時發布,字數略異 | 協同操作之典型特徵 |

---

## 三、反向圖片搜尋(全球通用)

### 主要工具

| 工具 | 強項 | 網址 |
|---|---|---|
| **Google Lens / Google Images** | 整合 Google 知識圖譜 | images.google.com |
| **TinEye** | 找最早出現處 | tineye.com |
| **Yandex Images** | **人臉辨識最強**(俄系演算法,部分臉孔 Google 找不到時有用) | yandex.com/images |
| **Bing Visual Search** | 微軟生態系 | bing.com/visualsearch |

### 圖像驗證流程

```markdown
### Step 1: 反向搜尋
- 同時跑 Google + TinEye + Yandex
- 看最早出現時間
- 看出現之網站類別

### Step 2: 檢視 metadata (EXIF)
- 拍攝日期/時間
- 相機/裝置型號
- GPS 座標(若有)
- 編輯軟體痕跡

工具:
- Jeffrey's EXIF Viewer (exif.regex.info)
- FotoForensics (fotoforensics.com)
- InVID/WeVerify 瀏覽器擴充

### Step 3: 內容分析
- 天氣狀況(與所稱日期一致?)
- 陰影方向(與所稱拍攝時間一致?)
- 招牌/文字(語言、文字與地點一致?)
- 建築風格(與所稱地點一致?)
- 服裝(季節是否合理?)
- 車牌/路標(台灣 vs 大陸 vs 港日韓)
- 電線/招牌特徵(台灣街景特徵明顯)

### Step 4: 找原始出處
- 線上最早出現處
- 原拍攝者
- 原始發布脈絡
- 此圖是否曾在其他脈絡使用?
```

> **EXIF 在台灣場景的限制**:Threads、LINE、FB 上傳會**剝除 EXIF**;只有從原始來源(攝影者直接提供、新聞照原檔)才有可靠 EXIF。

---

## 四、影片驗證

### 影片驗證 checklist

```markdown
### 技術分析
- [ ] 解析度全程一致
- [ ] 聲音與畫面同步
- [ ] 無可見剪輯痕跡
- [ ] 燈光全程一致
- [ ] 陰影行為自然

### 內容分析
- [ ] 地點可識別且可驗證
- [ ] 時間線索(陽光位置、陰影)
- [ ] 天氣與氣象記錄符合
- [ ] 背景細節一致
- [ ] 人物服裝符合脈絡

### Metadata 檢查
- [ ] 上傳日期 vs 所稱事件日期
- [ ] 原始來源已識別
- [ ] 監管鏈可追溯
- [ ] 有無多角度版本?

### 工具
- InVID/WeVerify 瀏覽器擴充(weverify.eu)
- YouTube DataViewer (citizenevidence.amnestyusa.org)
- 逐 frame 分析工具
```

---

## 五、AI 生成內容與深偽偵測

2026 年的現實:**肉眼已無法可靠分辨高階 AI 生成媒體**。Columbia Journalism Review 2025 指南直言:偵測工具「**大多跟不上 diffusion 模型**」。**單一工具的判斷只是一個輸入,不是定論**。

### 驗證堆疊兩層

- **Layer 1 — 來源憑證 (provenance)**:內容生成時是否有加密簽章
- **Layer 2 — 偵測 (detection)**:內容看起來/聽起來是否為 AI 生成

來源憑證**有則為強訊號**;**沒有**不代表「假」(多數相機與手機影像目前都沒簽章)。

### Layer 1:C2PA 內容憑證

**Coalition for Content Provenance and Authenticity (C2PA)** 標準在影像、音訊、影片檔案內嵌**加密 manifest**,描述其來源與編輯歷史。

**C2PA 採用狀態核對清單(以 2026 年 5 月為起點)**:

下列清單是查核時的**起點**,不是永久事實。C2PA 支援、韌體、平台 metadata 保留政策與廠商命名會快速變動;使用前應重新查官方頁、Content Credentials Verify、Content Authenticity Initiative 公告與廠商支援文件,並在報告中註明 `last_checked` 日期。

**生成式工具**:
- OpenAI DALL-E / Sora 系列(查官方 Content Credentials 說明;部分輸出另有可見浮水印)
- Adobe Photoshop / Lightroom / Firefly(查 Content Credentials 設定是否啟用)
- Microsoft Bing Image Creator / Designer / Copilot(查當前輸出格式與憑證保留)
- Google Gemini / SynthID 相關工具(查官方 C2PA / SynthID 支援範圍)

**相機(拍攝端簽章)**:
- Leica M11-P、SL3-S
- Sony Alpha 1 II、Alpha 9 III
- Canon EOS R1、R5 Mark II(2025 韌體)
- Google Pixel 系列新機(查機型、OS 版本與相機 app 支援)

**已知有問題的相機**:
- Nikon Z6 III 曾有簽章金鑰漏洞爭議;查核時應確認廠商最新修補狀態,不要只看「有效簽章」四字。

**新聞機構**(製作端):
- BBC、NYT、AP、Reuters 為 CAI/C2PA 會員
- 台灣新聞機構採用狀態需逐家確認;不可概括假設已導入或未導入。

### 驗證工具

| 工具 | 用途 |
|---|---|
| **contentcredentials.org/verify** | 拖檔即驗證 C2PA manifest、拍攝裝置、編輯歷史、AI 介入 |
| **Adobe Content Authenticity Inspector** | 同上,Adobe 出品 |
| **Digimarc C2PA 瀏覽器擴充** | 瀏覽網頁時即時偵測 |

### 高變動工具狀態核對

| 項目 | 使用前核對 | 不可直接假設 |
|---|---|---|
| C2PA 支援機型 / 工具 | 官方支援頁、韌體版本、Verify 結果 | 有 C2PA = 一定真、無 C2PA = 一定假 |
| AI 偵測器 | 服務是否仍運作、模型更新日期、免費額度 | 單一分數可當結論 |
| 社群 metadata | 平台是否保留、下載檔是否為原始檔 | 截圖仍保留原始 metadata |
| 調查局 / 政府工具 | 是否有正式受理管道與案件門檻 | 記者可直接取得 API 或內部報告 |

### 已知限制

- **截圖會剝除 hard binding manifest**(perceptual fingerprint 軟綁定可能仍可恢復)
- **多數社群平台上傳會剝 metadata**(TikTok、Meta 部分介面開始保留,覆蓋不完整)
- **無 Credentials 不代表「假」** — 目前流通的多數相機、手機影像仍未簽章
- **簽章金鑰可能被入侵**(Nikon 2025 案)— 「有效簽章」可能背後是上游被駭

### Layer 2:自動偵測工具(2026 年 5 月狀態)

下表是 2026 年 5 月的工作清單。使用前先打開服務、確認價格 / 配額 / 上傳限制與隱私條款;涉及未公開影像或受害者影像時,不要上傳到不明第三方服務。

| 工具 | 狀態 | 定價 | 用途 |
|---|---|---|---|
| **Hive AI** (thehive.ai) | 運作中 | Demo + 付費 API | 影像、影片、音訊;高用量強項 |
| **Reality Defender** (realitydefender.com) | 運作中 | 免費:50 次/月 | 影像、影片、音訊、文字一體 |
| **AI or Not** (aiornot.com) | 運作中 | 免費 + 付費 | 影像快速分流(不是定論) |
| **Sensity AI** (sensity.ai) | 運作中 | 企業價,鑑識級 | 政府/法律用;不適合一般記者預算 |
| **DeepFake-o-Meter** (Univ. Buffalo) | 運作中 | 免費,學術 | CJR 推薦記者用 |
| **TrueMedia.org** | **2025 年 1 月停運** | n/a | 技術已開源 |
| **Optic** | 2025 CJR 指南列出,未驗證 | 免費 | 一個輸入,別當定論 |
| **Deepware Scanner** | 域名活躍,功能未驗證 | 免費網頁 | 使用前先確認回應 |
| **法務部調查局深偽偵測** | 內部運作 | 不對外開放 API | 政府/檢警用;**重大案件**可透過正式管道請求協助 |

**單一工具不足為憑**。**至少跑兩個偵測器**,意見分歧時升級到深度分析或聯絡來源。

### Layer 3:肉眼/耳朵偵測(2026 校準)

舊有指標(多手指、奇怪耳朵、不對稱瞳孔)在當前 diffusion 與 Sora-2 級影片中**大多已消失**。2026 年 5 月仍會洩漏的線索:

- **邊界區域**:髮際線、耳緣、牙齒邊界、眼鏡與皮膚交接 — 細查有 sub-pixel 不一致
- **燈光與陰影物理**:高光方向與場景光不符;投影陰影缺失或矛盾
- **眼睛反光**:左右眼 catchlight 與場景不一致
- **音畫不同步**:多秒 clip 中音素與唇形漂移
- **皮膚紋理**:某些區域過於蠟質或平滑;雜訊型態整幀均勻(真實照片應隨表面變化)
- **語音複製**:呼吸位置、爆破音、室內回音(Fortune 2025 年 12 月報告:語音複製已跨越「**一般聽眾無法分辨**」門檻 — 假設純語音驗證已失效)

肉眼偵測**單獨不可靠**。用於 triage 與決定是否升級,不可作為最終定論。

### 可疑媒體驗證流程

1. **先檢查 Content Credentials** — 拖檔到 contentcredentials.org/verify。**已知簽章者之有效 manifest = 強正面證據**;缺乏不證明任何事
2. **反向圖片搜尋** — Google Lens、TinEye、Yandex(臉孔仍最強)。找最早出現處
3. **跑兩個自動偵測器** — Hive + Reality Defender(影像);AI or Not(快速分流)。**意見分歧時升級**
4. **逐 frame 與音訊分析** — 影片看邊界與唇同步;音訊看頻譜、呼吸、室內音
5. **聯絡來源** — **直接聯絡是最高信心步驟**。C2PA 告訴你**誰簽**,但無法告訴你**誰目擊**
6. **發布前降風險** — 深偽或疑似深偽素材不得原樣轉傳;必要引用時加明確標籤、模糊處理、縮短片段,並避免提供可再散播的原始檔。

```markdown
## 可疑媒體驗證輸出

- 判斷:可確認 / 疑似 / 無法判定 / 不建議引用
- 信心:高 / 中 / 低
- 最早來源:
- 已跑工具:
- 直接來源回應:
- 限制:
- 報導處理:不嵌入原片 / 打馬賽克 / 標示深偽 / 僅文字描述
```

---

## 六、台灣深偽真實案例(2024 大選為主)

> 用作訓練判讀的指標案例,**所有案例均經查核機構或調查局確認**。

### 案例 1:賴清德加密貨幣詐騙影片(2023 年底 - 2024 年初)

**型態**:Deepfake 變臉影片;蔡英文總統、賴清德副總統(時任)皆為受害者
**內容**:被合成發表加密貨幣投資言論,置入詐騙廣告詞「投資加密貨幣 250 美元,每月賺取 20,000 美元」
**散布**:Meta(Facebook)、Instagram 廣告
**回應**:Meta 下架;刑事局與調查局介入

### 案例 2:賴清德「藍白合」變造影片(2023 年底)

**型態**:剪輯 + AI 變造現有受訪影片,置換言論
**內容**:擷取賴清德受訪畫面,變造為對藍白合表態
**偵測**:調查局技術檢測指出「**惡意變造合成判斷指數高達 98.1%**」
**特徵**:聲音模糊有雜訊,影像不真實自然

### 案例 3:高嘉瑜 AI 仿聲影片(2024 年下半)

**型態**:AI 仿聲(voice cloning)+ 真實影像剪輯
**內容**:仿造高嘉瑜聲音喊「民進黨倒台」
**來源**:抖音特定帳號,該帳號**持續製造**台灣政治人物 AI 影片
**查核**:MyGoPen 評等「**錯誤**」,指出聲音為 AI 仿聲變造

### 案例 4:中國 GoLaxy 影響力作戰(2024-2025)

**型態**:大規模 AI 生成假帳號 + AI 寵物頭貼 + 偽裝「台灣居民」
**規模**:七個已識別帳號(實際數量可能遠超)
**特徵**:
- AI 生成的寵物照片作為頭貼
- 假冒台灣居民身分
- **持續發表**台灣政治事務之意見
- 跨平台協同行為
**揭露**:DoubleThink Lab + Shadow FIMI 跨國研究網絡

### 共通教訓

1. **影片即使「真實畫面」也可能被剪輯+變聲**(賴清德藍白合案)
2. **詐騙廣告與政治深偽常用相同工具鏈**(賴清德/蔡英文加密貨幣案)
3. **境外協同帳號**會持續演進(GoLaxy 案;AI 寵物頭貼是 2024-2025 才出現的 pattern)
4. **聲音偽造已超越「一般聽眾辨別」門檻**(高嘉瑜案;Fortune 2025/12)
5. **影像偵測判斷指數可量化**(調查局 98.1% 例)

---

## 七、台灣資訊作戰研究機構

### 主要研究組織

| 機構 | 性質 | 強項 | 網址 |
|---|---|---|---|
| **台灣民主實驗室 (DoubleThink Lab)** | 民間 NGO | 跨國協同操作研究、Shadow FIMI 網絡、GoLaxy 文件揭露 | doublethinklab.org |
| **台灣資訊環境研究中心 (IORG)** | 民間研究中心,2019 成立 | 中國官宣分析、TikTok 對青少年影響、月度監測 | iorg.tw |
| **台灣事實查核中心** | IFCN 認證查核機構 | 個別假訊息查核(主要)+ 敘事追蹤 | tfc-taiwan.org.tw |
| **g0v 零時政府** | 公民科技社群 | 開源工具(Cofacts、政府透明專案) | g0v.tw |
| **法務部調查局** | 政府機關 | 深偽鑑識(影像判斷指數);選舉期警示 | mjib.gov.tw |
| **台灣 AI 實驗室 (Taiwan AI Labs)** | 民間研究 | AI 倫理、生成 AI 應用研究 | ailabs.tw |

### 引用建議

- **學術等級研究**(深度報導用):**DoubleThink Lab、IORG**
- **個別訊息查核結果**:**台灣事實查核中心、MyGoPen、Cofacts**(已在 `fact-check-workflow-tw` 詳述)
- **法律層面深偽鑑識**:**法務部調查局**(透過正式管道請求)
- **跨平台技術工具**:**g0v** 社群

---

## 八、文件驗證

### PDF 與文件分析

```markdown
### Metadata 檢視
- 建立日期與修改歷史
- 作者資訊
- 製作軟體
- 嵌入字型與圖像

### 視覺檢查
- 全文格式一致
- 字型一致(無拼接文字)
- 文字與圖像對齊
- 各頁品質一致
- 簽章看起來真實

### 內容驗證
- 日期內部一致
- 姓名拼寫全文一致
- 參照編號有效
- 聯絡資訊可驗證
- 抬頭與已知範本相符

### 出處
- 文件如何取得?
- 監管鏈是否文件化?
- 原件 vs 副本?
- 來源可提供額外脈絡?
```

### 台灣政府文件驗證重點

- **公文格式**:依《文書處理手冊》規範,有發文機關、文號、日期、保存年限、附件
- **印鑑**:公文印鑑與機關公告之印鑑比對
- **發文字號**:可在行政院公報網(gazette.nat.gov.tw)或機關官網「資訊公開」專區查證
- **簽章版**:近年公文多採電子簽章(自然人憑證或機關電子簽章),可在內政部憑證管理中心驗證

---

## 九、建立驗證紀錄

```markdown
## 驗證紀錄

**被驗證之主張或內容**
[陳述具體]

**來源**
- 姓名/帳號:
- 平台:
- 首次發現日期:
- URL(已存檔):

**驗證步驟**

### Step 1: [描述]
- 採取行動:
- 工具/方法:
- 結果:
- 截圖/證據已存:[檔名]

### Step 2: [描述]
- 採取行動:
- 工具/方法:
- 結果:
- 截圖/證據已存:[檔名]

**佐證來源**
1. [來源 1] - [它確認了什麼]
2. [來源 2] - [它確認了什麼]
3. [來源 3] - [它確認了什麼]

**反證資訊**
1. [來源] - [它反駁了什麼]

**信心評估**
- [ ] 已驗證為真
- [ ] 可能為真(高信心)
- [ ] 無法驗證(證據不足)
- [ ] 可能為假(有反證)
- [ ] 已驗證為假

**推論**
[基於證據之結論]

**驗證者**:
**日期**:
```

---

## 十、存檔(台灣場景補強)

### 雙重存檔(最低標)

upstream 通用建議:**同時存到 Wayback Machine 與 Archive.today**,單一服務掛了不會失去證據。

```python
import requests
from urllib.parse import quote

def archive_url(url: str, perma_cc_api_key: str | None = None) -> dict:
    """同時 archive 到 Wayback Machine 與 Archive.today。"""
    results = {}

    try:
        response = requests.get(
            f'https://web.archive.org/save/{quote(url, safe="")}',
            timeout=60,
            allow_redirects=True,
        )
        if response.status_code == 200:
            results['wayback'] = response.url
    except requests.RequestException as e:
        results['wayback_error'] = str(e)

    try:
        response = requests.post(
            'https://archive.ph/submit/',
            data={'url': url},
            timeout=120,
            allow_redirects=False,
            headers={'User-Agent': 'Mozilla/5.0 (verification archive bot)'},
        )
        archived = response.headers.get('Refresh', '').split('url=')[-1] \
            or response.headers.get('Location', '')
        if archived:
            results['archive_today'] = archived
    except requests.RequestException as e:
        results['archive_today_error'] = str(e)

    return results
```

### 台灣本地存檔資源

| 工具 | 用途 | 網址 |
|---|---|---|
| **國家圖書館** | 紙本資料、舊報紙、政府公報、舊書 | ncl.edu.tw |
| **中央通訊社 ANC 影音資料庫** | 央社新聞影像庫(部分可付費取得) | cna.com.tw |
| **g0v 各專案資料庫** | 社群協力封存(立委質詢、地方議會) | g0v.tw |
| **法律扶助基金會公開檔案** | 訴訟相關公開記錄 | laf.org.tw |
| **個人 SSD + 雲端兩份備份** | 不要只放雲端;雲端服務政策會變 | (自設) |

### 截圖最佳實務

- **完整頁面擷取**(瀏覽器擴充 Hunchly、Screenpresso)
- **包含網址列**(顯示來源 URL)
- **包含時間戳記**(系統時鐘或外加標註)
- **儲存 metadata**(何時、如何拍攝)
- **多種格式**(PNG 無損 + PDF)
- **檔案 hash 並安全儲存**

---

## 十一、訪談前公開資料查證(台灣場景)

```markdown
## 受訪者背景查證

### 公開記錄
- [ ] 專業執照(衛福部醫事人員執業登記、律師公會、會計師公會等)
- [ ] 法院判決(司法院法學資料檢索 judgment.judicial.gov.tw)
- [ ] 公司登記(經濟部商業司 gcis.nat.gov.tw)
- [ ] 不動產登記(地政司線上查詢)
- [ ] 政治獻金 / 競選財務(中選會、廉政署)
- [ ] 公職人員財產申報(廉政署 ace.moj.gov.tw)
- [ ] 公開資訊觀測站(若為上市櫃公司董監事 mops.twse.com.tw)

### 專業背景
- [ ] LinkedIn 已檢視
- [ ] 雇主已確認
- [ ] 前雇主已聯絡(若關鍵)
- [ ] 發表作品已檢視(學術用 Google Scholar、台灣博碩士論文知識加值系統)
- [ ] 研討會出席紀錄

### 社群媒體稽核
- [ ] 所有平台已識別(Threads / FB / X / IG / LinkedIn / PTT 等)
- [ ] 發文歷史已檢視
- [ ] 連結/追蹤者已分析
- [ ] 對該議題之既有發言
- [ ] 是否有已刪除內容?(Wayback / Archive.today 找)

### 媒體露出
- [ ] 過往受訪已找出
- [ ] 與當前主張一致性
- [ ] 其他記者之評估
- [ ] 是否有撤回或更正?
```

### 台灣公開資料查詢清單(2026 年常用)

| 資源 | 內容 | 網址 |
|---|---|---|
| 全國法規資料庫 | 法律、命令、解釋函令 | law.moj.gov.tw |
| 司法院法學資料檢索 | 判決全文 | judgment.judicial.gov.tw |
| 經濟部商業司 | 公司登記 | gcis.nat.gov.tw |
| 公開資訊觀測站 | 上市櫃公司財報、董監事 | mops.twse.com.tw |
| 公職人員財產申報 | 候選人、政務官、民代財產 | ace.moj.gov.tw |
| 公職人員利益衝突 | 利益衝突迴避申報 | (廉政署) |
| 中央選舉委員會 | 選舉公報、候選人 | cec.gov.tw |
| 監察院 | 糾正、彈劾、調查報告 | cy.gov.tw |
| 審計部 | 審計報告 | audit.gov.tw |
| 政府電子採購網 | 標案、廠商 | web.pcc.gov.tw |
| 衛福部醫事人員登錄 | 醫師、護理師、藥師執照 | (衛福部) |
| 教育部全國教師查詢 | 公立學校教師 | (教育部) |

---

## 十二、法律風險(來源驗證特別注意)

`fact-check-workflow-tw` §九 已詳述查核之法律框架。本節聚焦**驗證程序中**可能觸發的法律風險。

### 《刑法》§315-1 妨害秘密

> **記者實務的灰色地帶**

**第 315-1 條**(整理摘要):
- 無故利用工具或設備窺視、竊聽他人非公開之活動、言論、談話或身體隱私部位者 → 3 年以下有期徒刑、拘役或新台幣 30 萬元以下罰金
- 無故以錄音、照相、錄影或電磁紀錄竊錄他人非公開之活動、言論、談話或身體隱私部位者 → 同上

**記者實務含義**:
- **自己為對話之一方**:多數實務見解認為**不構成「無故」竊錄**(類似美國 one-party consent),但建議**告知對方錄音**
- **第三人對話**:**未經同意錄影/錄音可能觸犯**,即使在公共場所
- **進入私人空間**:不可未經同意進入採訪
- **詳細錄音法律請參考 `interview-prep-tw`**

### 《個人資料保護法》

驗證來源、進行背景查證時:
- **公開來源**(公開資訊觀測站、法院判決、政府公報)→ **得使用**,但仍應「**特定目的內**」
- **非公開個資**(身分證、住址、電話)→ **不得擅自蒐集、利用**
- **新聞自由抗辯**:個資法 §51 規定,「**為新聞報導之公益目的**」之蒐集處理利用,有相對寬鬆規範,但仍須衡量比例
- **記者實務**:**最低必要原則** — 不要過度蒐集個資,並且只將必要部分寫入報導

### 《選舉罷免法》§104 加重深偽條款(2023 修法)

意圖使候選人**當選**或**不當選**,而以散布、播送、揭露**深度偽造影音之方法**,致**生損害於公眾**或他人者:
- **最重 7 年以下有期徒刑**,得併科 1,000 萬元以下罰金
- 散布、播送、揭露「**經修改或變造、合成**」之影音、文書(明知為虛假),亦有處罰

**記者實務**:
- 報導深偽案件時,**避免在標題與第一段使用未經查證之深偽影片畫面**(即使是為了「揭露」)
- 引用深偽影片之片段,須**清楚標示「為示警之用,內容為深度偽造」**
- **必要時模糊/打馬賽克**

### 《刑法》§310 誹謗、§311 善意言論免責

詳見 `fact-check-workflow-tw` §九。

### 「告知後同意」(Informed consent)

在敏感題材(性騷擾受害者、未成年人、心理創傷當事人)的驗證程序中:
- **告知**:你是誰、為何聯絡、報導目的、可能後果(被改名、被點名)
- **取得書面同意**(電子郵件、紙本)
- **保留拒絕選擇**:當事人隨時可撤回同意
- **匿名選項**:若當事人不同意公開姓名,提供匿名引述選項

---

## 與其他 -tw skill 協作

`source-verification-tw` 處理**來源真偽、數位內容真偽**。實務中與其他 -tw skill 緊密協作。

### 典型記者工作流順序(5 個 skill 串接)

```
[1. 資料蒐集]              ← foia-requests-tw
       ↓
[2. 來源驗證 / 內容查證]   ← source-verification-tw  ← 你在這裡
       ↓
[2.5. 跨平台 OSINT]        ← social-media-intelligence-tw
       ↓
[3. 採訪準備 / 採訪]       ← interview-prep-tw
       ↓
[4. 主張驗證 / 查核]       ← fact-check-workflow-tw
       ↓
[5. AI 起草草稿]
       ↓
[6. 去 AI 寫作味]          ← ai-writing-detox-tw
       ↓
[7. 編務校對]              ← newsroom-style-tw
       ↓
[8. 發稿]
```

### `source-verification-tw` 結束後,何時觸發其他 skill

| 場景 | 轉手 skill | 章節 |
|---|---|---|
| 已驗證來源/內容後,要對其陳述之主張進行查核與評等 | `fact-check-workflow-tw` | §二主張提取、§五評等 |
| 受訪者背景查證需要政府公開資料(財產申報、判決) | `foia-requests-tw` | (若公開資料無法取得時) §10 申請書 |
| 寫成報導後文體有 AI 味 | `ai-writing-detox-tw` | §三、§六.新聞文體禁忌 |
| 寫成報導後編務細節(深偽案號、機構名、人名譯名) | `newsroom-style-tw` | §一數字、§三人名譯名、§六機構名稱 |
| 訪談前準備(尤其錄音法律) | `interview-prep-tw` | 《通保法》《刑法》§315-1 |

### 重疊處理(同問題多 skill 都有)

- **影像 / 影片 / 音訊查證**:
  - `source-verification-tw` §三、§四、§五:**主處理** (反向圖搜、C2PA、深偽偵測)
  - `fact-check-workflow-tw` §三:評估證據強度
  - **以 `source-verification-tw` 為主**;`fact-check-workflow-tw` 為配合

- **社群帳號真偽**:
  - `source-verification-tw` §二:**主處理**(SIFT、台灣平台特性、紅旗)
  - `fact-check-workflow-tw` §四:評估能否引用該帳號之發言
  - **兩者搭配最完整**

- **「不具名來源」「匿名來源」**:
  - `source-verification-tw` §九 + §十一:驗證對方身分
  - `fact-check-workflow-tw` §三:評估證據強度
  - `newsroom-style-tw` §八:寫稿時匿名規則
  - `foia-requests-tw`:法律保護
  - **四 skill 搭配最完整**

- **深偽偵測與法律風險**:
  - `source-verification-tw` §五 + §十二:偵測 + 《選罷法》§104 加重條款
  - `fact-check-workflow-tw` §九:其他法律框架
  - **以 `source-verification-tw` §十二為主**(專門條款)

### 建議搭配安裝

`source-verification-tw` 可獨立用於「**數位內容驗證**」(也適用 OSINT、調查工作)。**新聞工作者** **強烈建議同時安裝** `fact-check-workflow-tw`、`foia-requests-tw`、`ai-writing-detox-tw`、`newsroom-style-tw` — 5 個 skill 涵蓋從資料蒐集、來源驗證、主張查核到發稿的完整工作流。

---

## 附錄一:常用驗證工具清單

### 反向圖搜
| 工具 | 用途 | 網址 |
|---|---|---|
| Google Lens / Images | 通用反向搜尋 | images.google.com |
| TinEye | 找最早出現 | tineye.com |
| Yandex Images | 人臉辨識 | yandex.com/images |
| Bing Visual Search | 微軟版 | bing.com/visualsearch |

### 影像/影片 metadata
| 工具 | 用途 | 網址 |
|---|---|---|
| Jeffrey's EXIF Viewer | EXIF 檢視 | exif.regex.info |
| FotoForensics | 影像錯誤層級分析 | fotoforensics.com |
| InVID/WeVerify | 影片驗證瀏覽器擴充 | weverify.eu |
| YouTube DataViewer | YT 影片 metadata | citizenevidence.amnestyusa.org |

### C2PA / AI 偵測
| 工具 | 用途 | 網址 |
|---|---|---|
| Content Credentials Verify | C2PA manifest 檢視 | contentcredentials.org/verify |
| Adobe Content Authenticity Inspector | C2PA 檢視 | Adobe |
| Hive AI | 影像/影片/音訊 AI 偵測 | thehive.ai |
| Reality Defender | 多模態 AI 偵測 | realitydefender.com |
| AI or Not | 影像快速分流 | aiornot.com |
| DeepFake-o-Meter | 學術版 | (Univ. Buffalo) |

### 存檔
| 工具 | 用途 | 網址 |
|---|---|---|
| Wayback Machine | 網頁存檔 | web.archive.org |
| Archive.today | 替代網頁存檔 | archive.ph |
| Hunchly | 自動截圖與記錄 | hunch.ly |
| Screenpresso | 全頁截圖與標註 | screenpresso.com |
| Perma.cc | 學術用永久連結(需註冊) | perma.cc |

### 文件 / 公司 / 資料庫
| 工具 | 用途 | 網址 |
|---|---|---|
| OpenCorporates | 全球公司記錄 | opencorporates.com |
| OCCRP Aleph | 文件與實體搜尋 | aleph.occrp.org |
| 公開資訊觀測站 | 台灣上市櫃公司 | mops.twse.com.tw |
| 經濟部商業司 | 台灣公司登記 | gcis.nat.gov.tw |

### 訓練資源
- **Bellingcat 指南** — bellingcat.com/resources
- **Google News Initiative** — newsinitiative.withgoogle.com
- **Verification Handbook** — verificationhandbook.com
- **台灣事實查核中心查證指南** — tfc-taiwan.org.tw
- **DoubleThink Lab 研究報告** — doublethinklab.org
- **IORG 研究報告** — iorg.tw
- **First Draft News** — firstdraftnews.org(已於 2022 停運,但網站為有用之 archive)

---

## 附錄二:法律與救濟資源

| 對象 | 用途 |
|---|---|
| 法律扶助基金會 (laf.org.tw) | 免費法律諮詢 |
| 各地方律師公會公益服務委員會 | 在地律師媒合 |
| 台灣新聞自由基金會 | 新聞自由相關案件 |
| 法務部調查局 | 重大深偽案件鑑識(透過正式管道) |
| 國家通訊傳播委員會 (NCC) | 廣電媒體相關 |
| 個人資料保護委員會 | 個資爭議 |

---

**版本說明**

- 版本:1.0.1
- 截至:2026-05-28
- 改寫自:upstream `journalism-core/source-verification` (jamditis/claude-skills-journalism)
- 在地化重點:
  - **保留 upstream 通用工具與方法論**(SIFT、反向圖搜、C2PA、自動偵測工具)
  - **新增台灣社群平台特性**:Threads / PTT / Dcard / LINE / FB / TikTok 等平台之驗證重點
  - **新增台灣特有警示訊號**:依 DoubleThink Lab GoLaxy 文件研究與 IORG 報告(AI 寵物頭貼、簡中用語滲透、北京時區發文等)
  - **新增台灣深偽真實案例**:2024 大選賴清德詐騙影片、賴清德藍白合變造影片、高嘉瑜 AI 仿聲、GoLaxy 影響力作戰
  - **新增台灣資訊作戰研究機構**:DoubleThink Lab、IORG、台灣事實查核中心、g0v、調查局、台灣 AI 實驗室
  - **新增台灣公開資料查詢清單**:全國法規庫、司法院判決、公開資訊觀測站、財產申報、政府電子採購網等 12 個關鍵資源
  - **新增法律風險章節**:《刑法》§315-1 妨害秘密(錄音灰色地帶)、《個資法》§51 新聞自由抗辯、《選罷法》§104 加重深偽條款 (2023 修法,最重 7 年)
  - **新增與其他 -tw skill 協作章節**(5 個 skill 串接工作流)
- 法律依據:截至 2026 年 5 月之《刑法》《個人資料保護法》《選舉罷免法》。具體條號與細節**請以全國法規資料庫公告版本為準**;涉及具體法律事項建議洽律師。
- 工具狀態截至 2026 年 5 月;C2PA 採用與 AI 偵測工具狀態請以官方公告為準
