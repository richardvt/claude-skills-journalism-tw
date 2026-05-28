# Security Policy

本 plugin 的安全與隱私聲明。涵蓋資料蒐集、外部呼叫、漏洞回報管道、貢獻者規範。

---

## 一、Plugin 本身的資料與隱私

### 不收集任何使用者資料

- 本 plugin 是**純文字 markdown 集合**(SKILL.md 檔案)
- **沒有 telemetry、analytics、追蹤碼**
- **不呼叫任何外部 API**;不上傳檔案、不發送請求
- 不存取使用者的:Claude API key、本機檔案系統(超出 plugin 安裝路徑)、瀏覽器、剪貼簿

### Skill 載入流程

```
你的 Prompt → Claude Code → 載入相關 SKILL.md 內容到 context →
Claude 用 SKILL.md + 一般知識回答你
```

- SKILL.md 內容**只在你的 Claude session 內**作為 context
- 你的 prompt 與回應**依循 Claude Code 自身的隱私政策**(由 Anthropic 處理),本 plugin 無權限介入

### SKILL.md 內容定位

SKILL.md 內容**僅為文字參考**,**不構成**:
- 法律意見
- 醫療建議
- 投資建議
- 對特定個人或機構的事實判斷

使用者依本 plugin 內容採取之**所有行動**,責任由使用者承擔。詳見 [README - 重要聲明](README.md#重要聲明)。

---

## 二、漏洞回報

### 哪些算「漏洞」

| 類別 | 範例 |
|---|---|
| **內容錯誤** | SKILL.md 引用的法條條號、判決案號錯誤、機構名稱錯誤 |
| **過時資訊** | 法規修法後 SKILL.md 未更新、機構改制後仍用舊名 |
| **誤導性 prompt 引導** | 某 SKILL 可能誘使 Claude 產生違法、傷害他人之內容 |
| **跨 plugin 衝突** | 本 plugin 與其他 Claude Code plugin 載入時崩潰、互相覆蓋 |
| **誹謗、隱私洩漏風險** | SKILL.md 範例不慎引用真實個資、真實案件當事人姓名 |

### 回報管道

依**嚴重度**選擇:

| 嚴重度 | 管道 | 預期回應時間 |
|---|---|---|
| **嚴重**(立即可被濫用、有人格傷害風險) | 直接 email maintainer(repo owner 聯絡資訊)+ 標題 `[SECURITY]` | 48 小時內初步回應 |
| **一般**(法條錯誤、過時資訊、SKILL.md 修正) | [開 GitHub Issue](https://github.com/richardvt/claude-skills-journalism-tw/issues/new) | 1 週內回應 |
| **建議改進**(新增 skill、新功能) | GitHub Issue + label `enhancement` | 視情況 |

### 我們承諾

- 嚴重議題**不公開揭露**直到修補完成
- 回報者**列入致謝**(若願意)
- **不會**因為合理回報而對你採取法律行動
- 修補後在 [CHANGELOG.md](CHANGELOG.md) 公開說明變更

---

## 三、使用本 plugin 的安全注意(給新聞工作者)

> 詳見 [README - 安全與隱私](README.md#安全與隱私)。摘要如下。

1. **吹哨者、匿名線人之身分資訊,不要丟給 LLM 處理**
2. **政資法申請書中之敏感案件**:寄出前再次核對個資、機構、調查對象描述
3. **引語必須對照原始錄音**(LLM 可能不自覺改寫引語)
4. **法律相關內容請以全國法規資料庫與律師意見為準**,SKILL.md 僅為流程參考
5. **時效**:SKILL.md 每份檔案結尾標「截至 YYYY-MM-DD」,法規/平台政策可能已變動

---

## 四、貢獻者安全規範

### PR 規則

提交 PR 修改 SKILL.md 時:

- ❌ **不要**在 SKILL.md 中放入**真實個人姓名、身分證、地址、電話**(範例請用「○○○」「王小明」)
- ❌ **不要**引用**進行中之具體案件**(司法案件、調查中之新聞)
- ❌ **不要**直接複製其他媒體之版權內容(可摘要、可引用片段並標來源)
- ✅ **請**在 PR 描述中說明:你修改的依據(法規條號、機關公告、學術論文等)
- ✅ **請**在 PR 描述中標明:你引用之資料**截至 YYYY-MM-DD**

### Skill 內容變更需通知範圍

| 變更類型 | 是否需在 CHANGELOG 標明 |
|---|---|
| 錯字、格式 | 不必 |
| 法條條號修正 | **必須** + 標明依據(全國法規資料庫連結) |
| 機構名稱變更(改制) | **必須** + 標明變更日期 |
| 加入新案例、新判決 | **必須** + 標明案號與來源 |
| 整段大幅改寫 | **必須** + 標明改寫理由 |

### 安全相關 PR 之優先處理

涉以下事項之 PR,**優先 review**:

- 法條條號錯誤
- 機構訴願管轄錯誤(會影響使用者實際救濟程序)
- 訴願 / 行政訴訟期間錯誤
- 法律風險警示遺漏

---

## 五、第三方依賴

本 plugin **無任何執行時依賴**:

- 不需安裝 Python、Node.js 等 runtime(SKILL.md 內的 Python code snippet 僅為**範例**,不會被執行)
- 不引入 npm / pip 套件
- 不依賴外部服務、CDN、image registry

唯一「依賴」是 Claude Code(plugin 載入機制本身),本 plugin 不引入額外風險。

---

## 六、致謝與責任

本 plugin 在 production-grade 測試前,經多輪內部審核:
- 法律條號逐字對照全國法規資料庫(`foia-requests-tw` v0.2.0 校對紀錄見 CHANGELOG)
- 判決見解經新北市政府法規查詢系統交叉驗證
- 大陸用語對照表參考國家教育研究院、教育部辭典

但**沒有任何保證**內容完全正確、完全反映最新法規。**使用者承擔最終判斷與行動責任**。

---

## 七、相關連結

- [README - 重要聲明](README.md#重要聲明)
- [README - 安全與隱私](README.md#安全與隱私)
- [CHANGELOG](CHANGELOG.md)
- [License (MIT)](LICENSE)
- [GitHub Issues](https://github.com/richardvt/claude-skills-journalism-tw/issues)
