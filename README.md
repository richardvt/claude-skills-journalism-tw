# claude-skills-journalism-tw

新聞工作者用的 Claude Code plugin,**繁體中文 / 台灣在地化版本**。

改寫自 [jamditis/claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) 之 `journalism-core`。原 repo 內容以**美國新聞工作環境**為主(FOIA、AP Style、Gmail bulk sender、美國社群平台);本 repo 將其重點 skill 改寫為**台灣對應**的法規、媒體慣例、平台生態與法律框架。

**目前 v0.8.0,完整 13 個 skill 全部在地化,共約 350 KB。**

## 已在地化 Skill(13 個 — **100% 完成**)

| Skill | 對應 upstream | 內容重點 |
|---|---|---|
| `foia-requests-tw` | foia-requests | 《政府資訊公開法》申請流程、9 款限制公開事由、訴願與行政訴訟救濟、申請書範本、18 則行政法院判決見解 |
| `source-verification-tw` | source-verification | SIFT、C2PA、深偽偵測、台灣 2024 大選深偽真實案例、DoubleThink Lab/IORG、《選罷法》§104 加重深偽條款 |
| `social-media-intelligence-tw` | social-media-intelligence | 16 個平台跨平台 OSINT、台灣協同操作偵測(GoLaxy 案例)、敘事擴散鏈、DoubleThink Lab/IORG 研究方法 |
| `interview-prep-tw` | interview-prep | 台灣錄音法律(《刑法》§315-1、《通保法》§29 第 3 款)、8 種台灣特殊受訪對象 |
| `interview-transcription-tw` | interview-transcription | 雅婷逐字稿、台/客/原民族語、Whisper large-v3、引語資料庫 |
| `fact-check-workflow-tw` | fact-check-workflow | 台灣 4 大 IFCN 認證查核機構、LINE 訊息查證、評等 6 級制、法律風險(《刑法》§310、《社維法》§63) |
| `ai-writing-detox-tw` | ai-writing-detox | 中文 AI 寫作 pattern、中國大陸用語滲透對照表 40+ 組、四字成語堆疊、新聞文體禁忌 |
| `newsroom-style-tw` | newsroom-style | 教育部《重訂標點符號手冊》+ 行政院《公文書數字使用原則》、人名譯名(川普 vs 特朗普)、兩岸關係用語、常見錯字 |
| `crisis-communications-tw` | crisis-communications | 11 種台灣常見危機類別、突發新聞時間軸 SOP、NCC 廣電法、災害現場記者安全、誤報更正模板 |
| `data-journalism-tw` | data-journalism | 19 個台灣政府開放資料來源、台灣資料清理常見坑(縣市改制、民國/西元、編碼)、Datawrapper/g0v 等視覺化工具 |
| `editorial-workflow-tw` | editorial-workflow | 編輯部選題追蹤、稿單管理、台灣中型編輯部架構、紙本/網路/週刊/廣電差異、三層審核流程 |
| `newsletter-publishing-tw` | newsletter-publishing | 方格子等台灣本地平台、Gmail/Yahoo/Outlook 寄信合規、台灣訂閱媒體標竿、《個資法》電子報規範 |
| `story-pitch-tw` | story-pitch | 16 家台灣主流媒體投稿指南(報導者、天下、商周、READr、鏡週刊、INSIDE、關鍵評論網 等)、稿費行情、自由工作者合約注意事項 |

> 命名約定:本版 skill 一律加 `-tw` 後綴,可與 upstream 英文版**並存安裝**。
> 13 個 skill 涵蓋從**選題 pitch → 資料蒐集 → 來源驗證 → OSINT → 採訪轉錄 → 查核 → 文體 → 編務 → 突發應變 → 資料新聞 → 電子報發行 → 編輯部管理**之**完整新聞生命週期**。

## 安裝方式

### 方法一(推薦):從 GitHub 安裝

在 Claude Code 中執行:

```bash
/plugin marketplace add richardvt/claude-skills-journalism-tw
/plugin install journalism-core-tw@claude-skills-journalism-tw
/reload-plugins
```

### 方法二:從本機路徑安裝(開發/離線)

```bash
# 先 git clone
git clone https://github.com/richardvt/claude-skills-journalism-tw.git ~/claude-skills-journalism-tw

# 在 Claude Code 中執行
/plugin marketplace add ~/claude-skills-journalism-tw
/plugin install journalism-core-tw@claude-skills-journalism-tw
/reload-plugins
```

### 方法三:手動複製 skill 到 ~/.claude/skills/

```bash
git clone https://github.com/richardvt/claude-skills-journalism-tw.git
cp -r claude-skills-journalism-tw/journalism-core-tw/skills/* ~/.claude/skills/
```

> ✅ **可與 upstream 並存**:本版 skill 一律加 `-tw` 後綴 (例:`foia-requests-tw`),不會與 upstream 英文版 `foia-requests` 衝突。兩版本可同時安裝,用於對照比較或在不同場景觸發。Claude 會依語言 (中/英)、地名、機關名等線索自動挑選對應 skill;若想強制使用特定版本,可在 prompt 直接指明 (例:「用 foia-requests-tw 幫我寫」)。

## 觸發方式

裝完後不必手動呼叫,Claude 會在你描述相關任務時自動使用對應 skill。範例:

- 「幫我寫一份依政資法向衛福部食藥署申請某餐廳衛生稽查紀錄的申請書」→ 觸發 `foia-requests-tw`
- 「機關以政資法 §18-I-3 拒絕我,怎麼辦?」→ 觸發 `foia-requests-tw`
- 「draft a FOIA request to the FBI for X」→ 觸發 upstream `foia-requests` (英文版)

### 強制指定特定版本

若你想對照比較兩版本品質:

```
用 foia-requests-tw 幫我寫向 NCC 申請某裁罰處分書的申請書
用 foia-requests 幫我寫同樣需求 (英文版),我要比較兩版差異
```

## 與 upstream 的關係

- **授權**:upstream 為 MIT,本 repo 繼承同樣的 MIT 授權
- **追蹤**:本 repo 不會自動同步 upstream 變更,但 upstream 重大更新會評估是否回灌
- **回灌 upstream**:若部分 skill 之**通用部分**有改進 (非台灣特定內容),歡迎以 PR 形式提交至原 repo

## 編輯與貢獻

每個 skill 都是一個獨立的 `skills/<name>/SKILL.md`。編輯流程:

1. 確認你要在地化的 skill (參考上表「待翻譯/改寫中」)
2. 對照 `~/.claude/plugins/marketplaces/claude-skills-journalism/journalism-core/skills/<name>/SKILL.md`
3. 在本 repo 對應路徑撰寫繁中版本
4. 更新本 README 之狀態表
5. 提 PR

### 在地化原則

- **法規**:必以**全國法規資料庫 (law.moj.gov.tw)** 為準,標明條號但提醒讀者查最新版本
- **平台**:優先使用台灣主流平台 (Facebook、Threads、PTT、Dcard、LINE、YouTube),保留全球工具 (TinEye、Yandex 等)
- **媒體**:範例改為台灣媒體 (報導者、天下、商周、READr、鏡週刊、聯合、自由、中時、TVBS、東森、公視、中央社)
- **政府資料平台**:首選 data.gov.tw、gazette.nat.gov.tw、ppg.ly.gov.tw、cy.gov.tw、audit.gov.tw、web.pcc.gov.tw
- **語言**:繁體中文,全形標點 (引號用「」),技術名詞與函式名保留原文
- **命名**:本版所有 skill 一律加 `-tw` 後綴 (例:`foia-requests-tw`),確保可與 upstream 英文版並存
- **時效標記**:在每個 skill 結尾標明「截至 YYYY-MM-DD」,法律相關更需註明「以最新公告為準」

## 授權

MIT License — 詳見 `LICENSE`。

致謝原作者 Joe Amditis ([jamditis](https://github.com/jamditis)) 提供高品質的英文版作為改寫基礎。
