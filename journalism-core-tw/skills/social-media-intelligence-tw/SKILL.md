---
name: social-media-intelligence-tw
description: 台灣新聞社群媒體情報與 OSINT 工作流程 (繁體中文/台灣專用版,對應 upstream social-media-intelligence 的美國版)。涵蓋:跨平台即時監測 (台灣場景:Threads/PTT/Dcard/LINE/FB/X/TikTok)、帳號真實性分析、敘事追蹤、協同操作偵測、台灣資訊作戰研究方法 (DoubleThink Lab、IORG)、2024 大選境外干預案例、平台研究 API (Meta Content Library、X 付費 API、TikTok Research API、Bluesky Jetstream)、Bellingcat / WITNESS 等國際工具、法律風險 (《選罷法》§104 加重深偽、《社維法》§63 散布謠言、《刑法》§310)、倫理規範。追蹤協同操作、跨平台敘事擴散、突發新聞社群監測、調查報導 OSINT 時觸發。調查記者、查核員、跨平台追蹤研究員必備。
---

# 台灣新聞社群媒體情報工作流程

跨平台監測、敘事追蹤、調查協同操作之系統性方法,並依台灣社群生態與法律框架在地化。

> **與 `source-verification-tw` 互補**:
> - `source-verification-tw`:**單一**帳號或內容之真偽驗證(SIFT、反向圖搜、C2PA、深偽偵測)
> - `social-media-intelligence-tw`:**多帳號、多平台**之模式偵測(協同操作、敘事追蹤、影響力作戰)
> 
> 偵測單一帳號偽造 → 用 `source-verification-tw`;偵測 100 個帳號協同行為 → 用本 skill。

---

## 何時使用

- 追蹤一則新聞跨平台之擴散路徑
- 調查可疑之**協同無真實性行為**(Coordinated Inauthentic Behavior, CIB)
- 突發新聞時跨多個平台即時監測
- 分析帳號網絡與關係
- 偵測機器人活動與操弄行動
- 為數位調查建立證據鏈
- 在內容被刪除前**封存**

---

## 一、台灣資訊作戰生態速覽

> 詳細的研究機構介紹見 `source-verification-tw` §七。本節聚焦**方法論**。

### 主要威脅來源(2026 年 5 月)

| 來源 | 特徵 | 主要研究者 |
|---|---|---|
| **中國國家影響力作戰** | AI 生成帳號、GoLaxy 系統、跨平台協同;偽裝台灣居民 | DoubleThink Lab、IORG |
| **TikTok 演算法** | 推播偏中政治內容、青少年認知重構 | IORG 2025 報告 |
| **WeChat 視頻號** | 台商、新住民社群為入口 | DoubleThink Lab 報告 |
| **選舉期境外干預** | 2024 大選深偽影片、AI 仿聲 | 調查局、台灣事實查核中心 |
| **國內極端立場帳號** | 兩端政治極化、刻意挑釁 | (各家媒體自行監測) |
| **詐騙集團跨境操作** | 假名人投資、假投資 LINE 群 | 165 反詐騙、警政署 |

### 台灣本地常見敘事戰場

- **兩岸關係**:武統威脅、台灣經濟崩盤、美國棄台論
- **健保、年金**:制度崩潰、醫療資源不足
- **選舉**:候選人黑函、AI 仿聲、政黨內鬥
- **能源**:核電、綠能、限電議題
- **移工、移民**:族群偏見、犯罪統計操弄
- **食安、健康**:中藥治病、疫苗副作用

---

## 二、跨平台即時監測

### Python:多平台貼文資料結構

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum
import hashlib

class Platform(Enum):
    THREADS = "threads"
    PTT = "ptt"
    DCARD = "dcard"
    LINE_OPENCHAT = "line_openchat"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"
    TIKTOK = "tiktok"
    X = "x"  # 原 Twitter,2023 改名 X
    BLUESKY = "bluesky"
    MASTODON = "mastodon"
    TELEGRAM = "telegram"
    WEIBO = "weibo"        # 中國微博
    XIAOHONGSHU = "xhs"    # 中國小紅書
    DOUYIN = "douyin"      # 中國抖音
    WECHAT = "wechat"

@dataclass
class SocialPost:
    platform: Platform
    post_id: str
    author: str
    content: str
    timestamp: datetime
    url: str
    engagement: Dict[str, int] = field(default_factory=dict)
    media_urls: List[str] = field(default_factory=list)
    archived_urls: List[str] = field(default_factory=list)
    content_hash: str = ""

    def __post_init__(self):
        # 內容 hash 用於重複偵測
        self.content_hash = hashlib.md5(
            f"{self.platform.value}:{self.content}".encode()
        ).hexdigest()

@dataclass
class MonitoringQuery:
    keywords: List[str]
    platforms: List[Platform]
    accounts: List[str] = field(default_factory=list)
    hashtags: List[str] = field(default_factory=list)
    exclude_terms: List[str] = field(default_factory=list)
    start_date: Optional[datetime] = None
```

### 突發新聞偵測:關鍵字爆量警示

```python
from collections import defaultdict
from datetime import datetime, timedelta

class BreakingNewsDetector:
    """偵測關鍵字提及之突發爆量。"""

    def __init__(self, baseline_window_hours: int = 24):
        self.baseline_window = timedelta(hours=baseline_window_hours)
        self.mention_history = defaultdict(list)

    def add_mention(self, keyword: str, timestamp: datetime):
        self.mention_history[keyword].append(timestamp)
        cutoff = datetime.now() - self.baseline_window * 2
        self.mention_history[keyword] = [
            t for t in self.mention_history[keyword] if t > cutoff
        ]

    def is_spiking(self, keyword: str, threshold_multiplier: float = 3.0) -> bool:
        now = datetime.now()
        recent = sum(1 for t in self.mention_history[keyword]
                    if t > now - timedelta(hours=1))

        baseline_hourly = len([
            t for t in self.mention_history[keyword]
            if t > now - self.baseline_window
        ]) / self.baseline_window.total_seconds() * 3600

        if baseline_hourly == 0:
            return recent > 10
        return recent > baseline_hourly * threshold_multiplier
```

### 台灣場景突發新聞監測建議關鍵字

- 災害:颱風、地震、土石流、淹水、停電
- 重大事件:總統、立法院、行政院、外交、兩岸
- 突發醫療:疫情、食安、藥品回收
- 詐騙趨勢:假投資、假LINE群、假電商

---

## 三、台灣社群平台特性(2026 年)

> 詳細的單一帳號驗證見 `source-verification-tw` §二。本節聚焦**研究存取與監測**。

### 各平台研究存取狀態

| 平台 | 研究存取 | 注意事項 |
|---|---|---|
| **Threads** | Threads API(發布/嵌入);Meta Content Library(研究批次)|2026 年 3 月公開檔案門檻降至 100 追蹤者;歷史研究需 Meta CL 學術資格 |
| **Facebook / Instagram** | **Meta Content Library**(2024/8 取代 CrowdTangle);Junkipedia(免費);NewsWhip(付費)|CrowdTangle 已**永久停運**;Meta CL 自 2025/12/8 起改由 Meta 直接申請,學術或非營利為主 |
| **X (Twitter)** | **付費 API**(2026/2 改 pay-per-use);Brandwatch / Sprinklr(第三方付費)|2023 取消免費學術層;**禁止 scraping**;台灣記者多透過 X Pro Search 或第三方資料商 |
| **TikTok** | Research API(學術/非營利;EU DSA 第 40 條對 EU 研究者較寬鬆);Exolyt、Pentos(付費)|台灣記者較難直接取得;**IORG 2025 報告**經正式申請取得 |
| **PTT** | **完全開放網頁爬蟲**(無需 API);PTT Web、PttPedia |2026 年仍是台灣記者主要監測對象之一;**新註冊 ID 在政治看板發文要警覺**;不可錄製內部聊天 |
| **Dcard** | 無公開 API;**禁止商業 scraping**(2023 政策更新);需透過官方合作 |校園、年輕女性議題主場;熱門文章常被搬到其他平台 |
| **LINE OpenChat** | **無公開 API**;手動加入觀察 |**LINE 訊息查證**官方帳號是查核管道,非監測管道 |
| **YouTube** | YouTube Data API v3 |預設每日 10,000 units(約 100 次搜尋);**深度研究需申請較高配額** |
| **Reddit** | Reddit API(非商業研究免費);Arctic Shift(Pushshift 後繼,免費) |台灣使用者較少,但**台灣相關 subreddit**(/r/Taiwan、/r/taiwannews)有時可看 |
| **Bluesky** | Jetstream(無需驗證的 filtered JSON);raw firehose |**公開為預設**;成本低,適合記者監測 |
| **Mastodon / Fediverse** | 各 instance 的 public-timeline API;cross-instance search 在 search.noc.social |台灣使用者少但有,具公民團體聚集 |
| **Telegram** | Bot API + MTProto + 公開頻道預覽 t.me/s/`<channel>` |**公開頻道**多;**私人群組**禁止;Bellingcat 工具集(Telegago、Telepathy、TelegramDB) |
| **微博(中國)** | API 受限,需中國手機認證 |境外資訊作戰起點之一;**研究時用 VPN 注意法律風險** |
| **小紅書、抖音(中國)** | 無公開 API |**TikTok 與抖音為同公司不同 app**;字節跳動同集團 |

### EU DSA 第 40 條對台灣記者的影響

**EU DSA 第 40 條**允許 EU 研究者強制存取超大型平台之資料。**台灣記者非 EU 居民**,但可:
- 與**EU 大學或研究機構合作**(共同申請)
- 跟 IORG、DoubleThink Lab 等已有 EU 合作網絡的機構協同
- 用其**已發表之研究結果**作為延伸研究起點

### 台灣特有監測場景

| 場景 | 工具 | 備註 |
|---|---|---|
| LINE 訊息流傳 | LINE 訊息查證 + Cofacts | **被動接收**,不是主動監測 |
| PTT 政治板水軍 | PTT Web 爬蟲 + 帳號註冊日查詢 | **新註冊 ID 大量發文**是經典訊號 |
| Threads 政治擴散 | Meta Content Library + 手動觀察 | 2024 後成為台灣 Z 世代政治新場域 |
| TikTok 中國 narrative 擴散 | IORG 已發表研究 + 手動取樣 | 個別記者難建立大規模監測;倚賴民間 NGO |
| FB 不實廣告 | Meta 廣告資料庫(facebook.com/ads/library)| 政治廣告必須揭露金主(2018 後規範) |

---

## 四、帳號真實性分析

### Python:真實性指標

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class AccountAnalysis:
    username: str
    platform: Platform
    created_date: Optional[datetime] = None
    follower_count: int = 0
    following_count: int = 0
    post_count: int = 0

    # 真實性訊號
    profile_photo_is_stock_or_ai: Optional[bool] = None
    bio_contains_simplified_chinese: Optional[bool] = None
    posts_primarily_reshares: Optional[bool] = None
    posting_pattern_beijing_timezone: Optional[bool] = None
    engagement_ratio_suspicious: Optional[bool] = None

    def calculate_red_flags(self) -> dict:
        flags = {}

        if self.created_date:
            age_days = (datetime.now() - self.created_date).days
            if age_days < 30:
                flags['new_account'] = f"創立 {age_days} 天"

        if self.following_count > 0:
            ratio = self.follower_count / self.following_count
            if ratio < 0.1:
                flags['low_follower_ratio'] = f"比率: {ratio:.2f}"

        if self.created_date and self.post_count > 0:
            age_days = max(1, (datetime.now() - self.created_date).days)
            posts_per_day = self.post_count / age_days
            if posts_per_day > 50:
                flags['excessive_posting'] = f"{posts_per_day:.0f} 篇/天"

        # 台灣特有訊號
        if self.profile_photo_is_stock_or_ai:
            flags['ai_or_stock_profile'] = "頭貼疑似 AI 生成或 stock photo"

        if self.bio_contains_simplified_chinese:
            flags['simplified_chinese_in_bio'] = "自介含簡體中文用語"

        if self.posting_pattern_beijing_timezone:
            flags['beijing_timezone_pattern'] = "發文時間集中於北京時區 (UTC+8 09:00-18:00)"

        return flags

    def authenticity_score(self) -> int:
        score = 100
        flags = self.calculate_red_flags()
        score -= len(flags) * 20
        return max(0, score)
```

### 台灣特殊認證考量

- **PTT**:用 `/help` 或從文章作者點擊看 ID **註冊日**;`/W` 看歷史文章/推噓比
- **Dcard**:看**校園認證**標記(灰色畢業校徽);無認證者可疑度高
- **Threads**:看**對應 IG 帳號**;**新 IG + 新 Threads + 大量政治發言**警示高
- **FB 粉專**:看**過往粉專名稱變更歷史**(粉專可能從不相關主題更名為政治);**Meta CL** 有此歷史
- **YouTube**:看**頻道創立日 vs 第一支影片日**;**買來的舊頻道**(老創立日 + 短內容歷史)

---

## 五、網絡分析

### Python:帳號互動網絡

```python
from collections import defaultdict
from typing import Set, Dict, List

class AccountNetwork:
    def __init__(self):
        self.interactions = defaultdict(lambda: defaultdict(int))
        self.accounts = {}

    def add_interaction(self, from_account: str, to_account: str,
                       interaction_type: str = "mention"):
        self.interactions[from_account][to_account] += 1

    def find_clusters(self, min_interactions: int = 3) -> List[Set[str]]:
        """找頻繁互動之帳號群。"""
        adjacency = defaultdict(set)
        for from_acc, targets in self.interactions.items():
            for to_acc, count in targets.items():
                if count >= min_interactions:
                    adjacency[from_acc].add(to_acc)
                    adjacency[to_acc].add(from_acc)

        visited = set()
        clusters = []

        for account in adjacency:
            if account in visited:
                continue
            cluster = set()
            stack = [account]
            while stack:
                current = stack.pop()
                if current in visited:
                    continue
                visited.add(current)
                cluster.add(current)
                stack.extend(adjacency[current] - visited)
            if len(cluster) > 1:
                clusters.append(cluster)

        return sorted(clusters, key=len, reverse=True)

    def coordination_score(self, accounts: Set[str]) -> float:
        """評估一群帳號的協同程度 (0-1)。"""
        if len(accounts) < 2:
            return 0.0
        total_possible = len(accounts) * (len(accounts) - 1)
        actual_connections = 0
        for acc in accounts:
            for other in accounts:
                if acc != other and self.interactions[acc][other] > 0:
                    actual_connections += 1
        return actual_connections / total_possible if total_possible > 0 else 0
```

### 視覺化工具

- **Gephi**(免費,開源)— ICIJ Panama Papers 御用工具
- **Maltego CE**(社群版免費,需註冊)
- **Cytoscape**(免費,生物網絡為主但通用)
- **NodeXL**(Excel 插件,基本版免費)

---

## 六、敘事追蹤

### Python:主張擴散追蹤

```python
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict
from collections import defaultdict

@dataclass
class Claim:
    text: str
    first_seen: datetime
    first_seen_url: str
    variations: List[str] = field(default_factory=list)
    appearances: List[Dict] = field(default_factory=list)

    def add_appearance(self, url: str, platform: Platform,
                       timestamp: datetime, author: str):
        self.appearances.append({
            'url': url,
            'platform': platform.value,
            'timestamp': timestamp,
            'author': author
        })

    def spread_timeline(self) -> List[Dict]:
        return sorted(self.appearances, key=lambda x: x['timestamp'])

    def platforms_reached(self) -> Dict[str, int]:
        counts = defaultdict(int)
        for app in self.appearances:
            counts[app['platform']] += 1
        return dict(counts)

    def velocity(self, window_hours: int = 24) -> float:
        """擴散速率:每小時新出現次數。"""
        if not self.appearances:
            return 0.0
        recent = [
            a for a in self.appearances
            if a['timestamp'] > datetime.now() - timedelta(hours=window_hours)
        ]
        return len(recent) / window_hours
```

### 台灣敘事追蹤實務:從 PTT 到 LINE 的擴散鏈

常見台灣假訊息擴散路徑:

```
[微博 / 抖音 (中國)]
       ↓
[境外協同帳號:Threads / X]
       ↓
[台灣早期擴散:PTT 政黑 / 八卦 / 軍事板]
       ↓
[Threads / FB 二次擴散]
       ↓
[LINE 群組:長輩、社區、宗教群]
       ↓
[新聞媒體報導 (記者 LINE 群轉發或攝記分享)]
```

監測重點:
- **逆向溯源**:從 LINE 訊息往回追到最早出現處
- **跨平台時間軸**:同一主張在各平台的首次出現順序
- **語言變化**:從簡體 → 繁體 + 大陸用語 → 純繁體的清洗過程

---

## 七、協同操作偵測

### 行為訊號 checklist

```markdown
## 協同無真實性行為 (CIB) 指標

### 時間模式
- [ ] 多帳號於數分鐘內發出相同內容
- [ ] 跨帳號之同步發文時間
- [ ] 爆量活動後突然沈寂
- [ ] 發文間隔短於人類打字速度

### 內容模式
- [ ] 跨帳號相同或近乎相同的文字
- [ ] 相同圖片/影片被多帳號分享
- [ ] 相同錯字、格式錯誤
- [ ] 可見複製貼上痕跡

### 帳號模式
- [ ] 帳號創立時間集中
- [ ] 命名規則相似(姓名 + 數字)
- [ ] 通用或 stock 大頭照(**或 AI 生成寵物照** — GoLaxy 案)
- [ ] 個人內容極少,多為轉發
- [ ] 追蹤同樣帳號
- [ ] 互相互動比例失衡

### 網絡模式
- [ ] 在網絡分析中形成密集叢
- [ ] 放大同樣的外部來源
- [ ] 鎖定同樣的帳號或 hashtag
- [ ] 跨平台協同可見

### 台灣場景特有訊號
- [ ] 自介寫「台灣居民」但用簡中用語(視頻、網絡、賦能、打造)
- [ ] 帳號創立短期內大量政治發文
- [ ] 發文時間集中於 UTC+8 09:00-18:00 (中國辦公時間)
- [ ] 跨平台同一 narrative,字數略異(避過去重複偵測)
- [ ] 同一張(疑似 AI 生成)的人像或寵物照在多帳號出現
```

### Python:協同程度評分

```python
from typing import List

def coordination_likelihood(posts: List[SocialPost]) -> dict:
    """評估一組貼文是否為協同活動。"""

    if len(posts) < 2:
        return {'score': 0, 'signals': []}

    signals = []
    score = 0

    # 內容重複
    contents = [p.content for p in posts]
    unique_contents = set(contents)
    if len(unique_contents) < len(contents) * 0.5:
        signals.append("內容大量重複")
        score += 30

    # 時間集群
    timestamps = sorted(p.timestamp for p in posts)
    rapid_posts = 0
    for i in range(1, len(timestamps)):
        if (timestamps[i] - timestamps[i-1]).seconds < 60:
            rapid_posts += 1
    if rapid_posts > len(posts) * 0.3:
        signals.append("可疑時間集群")
        score += 25

    # 帳號數量 vs 內容相似度
    authors = set(p.author for p in posts)
    if len(authors) > 5 and len(contents) / len(authors) > 2:
        signals.append("少數帳號發出大量相似貼文")
        score += 20

    return {
        'score': min(100, score),
        'signals': signals,
        'posts_analyzed': len(posts),
        'unique_authors': len(authors)
    }
```

### 台灣協同操作真實案例(GoLaxy 範本)

依 DoubleThink Lab 2024-2025 揭露:

**特徵**:
- 大量帳號使用 **AI 生成寵物照**作為頭貼
- 自稱「台灣居民」「台灣愛國者」「關心台灣者」
- 偽裝個人帳號,發表政治見解
- 跨平台(X、Threads、FB)同步活動
- 攻擊目標:特定政治人物、政黨、立場

**研究方法**(可仿效):
1. **大規模帳號採樣**:用平台 API 或公開資料抓 N 萬帳號之 metadata
2. **頭貼分群**:用反向圖搜或 AI 偵測辨識 stock/AI 生成
3. **發文時區比對**:UTC+8 但時段分布不像台灣作息
4. **互動圈分析**:用 Gephi 找密集連線之帳號群
5. **內容主題比對**:NLP topic modeling 找重複 narrative

---

## 八、存檔(在內容被刪除前)

> 完整存檔工作流見 `source-verification-tw` §十。

### Python:雙重存檔(社群場景)

```python
import re
import requests
from datetime import datetime
from typing import Optional
from urllib.parse import quote, urljoin

class SocialArchiver:
    """在社群內容被刪除前存檔。"""

    def __init__(self):
        self.archived = {}

    def archive_to_wayback(self, url: str) -> Optional[str]:
        """送 URL 到 Internet Archive。"""
        try:
            save_url = f"https://web.archive.org/save/{quote(url, safe='')}"
            response = requests.get(save_url, timeout=30)
            if response.status_code == 200:
                self.archived[url] = {
                    'wayback': response.url,
                    'archived_at': datetime.now().isoformat(),
                }
                return response.url
        except Exception as e:
            print(f"Wayback 存檔失敗:{e}")
        return None

    def archive_to_archive_today(self, url: str) -> Optional[str]:
        """送 URL 到 archive.today。"""
        try:
            response = requests.post(
                'https://archive.today/submit/',
                data={'url': url, 'anyway': '1'},
                timeout=60,
                allow_redirects=False,
                headers={'User-Agent': 'Mozilla/5.0 (verification archive bot)'},
            )
            if response.status_code in (301, 302, 303, 307, 308):
                location = response.headers.get('Location')
                if location:
                    return urljoin(response.url, location)
            if response.status_code == 200:
                refresh = response.headers.get('Refresh', '')
                m = re.search(r'\burl\s*=\s*(.+)', refresh, re.IGNORECASE)
                if m:
                    return urljoin(response.url, m.group(1).strip().strip('\'"'))
        except Exception as e:
            print(f"archive.today 失敗:{e}")
        return None
```

**archive.today 2026 年實務狀態**:
- 2025 年 10 月 FBI 對其註冊商發出傳票調查營運者身分
- 2026 年 2 月 Wikipedia 投票決定**停用其為引用來源**(因 2026/1 該服務內含 DDoS 攻擊碼)
- **仍可用於 Wayback 無法擷取之頁面**,但視為**次要管道**
- 對 scraper 嚴格限流並出 CAPTCHA

### 台灣本地存檔資源

| 工具 | 用途 |
|---|---|
| 國家圖書館 | 紙本資料、舊報紙 |
| g0v 各專案資料庫 | 公民協作封存(立委質詢、地方議會) |
| **台灣事實查核中心檔案庫** | 已查核訊息存檔 |
| **個人 SSD + 雲端兩份** | 不要只放雲端 |

---

## 九、台灣資訊作戰研究方法論

### DoubleThink Lab 研究方法(範例)

**GoLaxy 案例研究步驟**:
1. **資料源**:洩漏文件 / 跨國 OSINT 網絡(Shadow FIMI Investigator Network)
2. **帳號識別**:從文件揭露之命名規則、頭貼特徵反向追蹤
3. **行為比對**:採樣已識別帳號之數月發文 → 比對命名相似帳號
4. **網絡分析**:用 Gephi 視覺化互動關係
5. **發布**:報告 + Medium 開源化,便於社群驗證

### IORG 研究方法(範例)

**「TikTok 對台灣青少年認知重構」研究**:
1. **抽樣**:多階段抽樣台灣青少年使用者
2. **問卷 + 行為資料**:問卷取意見、行為資料取觀看模式
3. **TikTok Research API**:申請 EU DSA Article 40 路徑取資料
4. **學術合作**:與大學研究中心合作確保方法學
5. **發布**:中英文版報告;媒體公關發送

### 你能用的「平民版」方法

如果你**不是 NGO,只是個別記者或小編輯部**,仍可做:

1. **手動採樣 20-50 個可疑帳號** → 試算表記錄頭貼、創立日、追蹤者數、發文 pattern
2. **逆向圖搜每個頭貼**(TinEye、Yandex)→ 找 AI 生成或 stock 照
3. **用 g0v 公開工具**(如 Cofacts)查訊息已知擴散管道
4. **找 DoubleThink Lab、IORG 已發表之相關研究**作為背景或引用
5. **報導發出前對被指控的帳號或人物提出查證機會**

---

## 十、OSINT 工具集(全球通用,加台灣相關)

### 帳號真實性與協同

- **Botometer X**(osome.iu.edu)— Twitter 機器人評分學術標準;**2023/6 後僅 archival 模式**,不能評 2023/5 後之帳號
- **Hoaxy / Hoaxy2**(osome.iu.edu)— 運作中;Hoaxy2 加 Mastodon 搜尋、Bluesky 即時監測、FB News Bridge
- **OSoMe Coordiscope** — 協同網絡視覺化,免費
- **CooRTweet**(R 套件)— CooRnet 後繼;原版於 2024/8 CrowdTangle 停運時一併消失
- **Bot Sentinel** — 2025 全年離線,2026 計畫重啟;**用前先驗證運作狀態**

### 反向圖搜(見 `source-verification-tw` §三)

- TinEye、Yandex Images、Google Lens、Bing Visual Search

### 影像鑑識

- **Forensically** (29a.ch) — error level analysis、clone detection
- **FotoForensics** — 同上
- **InVID-WeVerify**(EU vera.ai 計畫)— 2025 加合成圖偵測 + 語音複製偵測 beta

### 網絡分析

- **Gephi**(免費,開源)
- **Maltego CE**(社群版免費)
- **NodeXL**(Excel 插件)
- **Cytoscape**(免費)

### 台灣相關工具

- **Cofacts API**(g0v)— 已知 LINE 假訊息資料庫
- **PTT Crawler**(g0v 多個專案)— PTT 爬蟲開源工具
- **台灣事實查核中心**已發表報告查詢
- **DoubleThink Lab Medium 公開文章**(doublethinklab.medium.com)
- **IORG 月度監測報告**(iorg.tw)

### 方法論權威(2026 年)

- **Bellingcat Online Investigation Toolkit**(bellingcat.gitbook.io/toolkit)— 持續更新
- **Information Futures Lab @ Brown SPH** — First Draft News 後繼;Claire Wardle 共同主持
- **WITNESS Deepfakes Rapid Response Force**(gen-ai.witness.org)— 配對記者與媒體鑑識專家
- **CJR Tow Center 2025 深偽偵測指南**(非技術版,記者導向)

> **Stanford Internet Observatory** 已於 2024/6 解散,選舉研究角色轉到 **Stanford Social Media Lab** (Hancock) 與 **NYU Stern Center for Business and Human Rights**。

---

## 十一、法律風險

### 《選舉罷免法》§104 加重深偽條款(2023 修法)

意圖使候選人**當選**或**不當選**,以**散布、播送、揭露**深度偽造影音之方法,致**生損害於公眾**或他人者:
- **最重 7 年以下**有期徒刑,得併科 **1,000 萬元以下**罰金

**記者監測場景含義**:
- **記者監測**並**揭露**深偽影片是**正當新聞工作**,不在處罰範圍
- 但**轉發**深偽影片(即使為了「警示」)可能觸法 — **務必加上明確「為深度偽造」標記**
- 必要時模糊/打馬賽克

### 《社會秩序維護法》§63 第 5 款

「**散佈謠言,足以影響公共之安寧者**」處 3 日以下拘留或新台幣 3 萬元以下罰鍰。

**記者場景**:
- 監測 + 揭露假訊息 ≠ 散布假訊息(具公益必要性)
- 但**社群媒體轉發未經查證之傳言**可能觸法

### 《刑法》§310 誹謗罪

詳見 `fact-check-workflow-tw` §九。

**SMI 場景特有風險**:
- **揭露某帳號為「協同操作」「水軍」「網軍」**時,若該帳號為**真實人物**而非協同操作,可能構成誹謗
- **保護措施**:
  - 報告中用「**疑似**」「**符合協同操作特徵**」等保留語
  - 附**完整研究方法**讓讀者自行判斷
  - 給被點名帳號**回應機會**

### 《刑法》§358 入侵電腦罪

- **不可**為了監測而**駭入私人帳號、群組**
- **不可**用假帳號加入封閉群組進行監測(除非取得管理員同意)
- 公開頻道、公開貼文 OK;**私訊、私群組、Telegram 私頻道**禁止

### 《個資法》

- 監測公開資訊 OK
- **聚合多重個資**(姓名 + 地址 + 工作 + 親屬 + 病史)為「**人物剖繪**」即使資料皆來自公開,可能構成個資法疑慮
- **新聞自由抗辯**(§51)可主張,但**最低必要原則**仍須遵守

---

## 十二、倫理規範

- **只存檔公開內容**
- **不要為了監測建立假帳號**(無權立場 vs 學術研究有專案規範)
- **尊重平台 ToS**:X 2023 後明文禁止 scraping(即使公開貼文);依賴 API 或授權資料商
- **不轉用研究存取金鑰於非研究用途**:Meta、TikTok 對 ToS 偏離會撤銷存取
- **保護分享社群內容的消息來源**
- **發布前驗證**:**協同評分是假設,不是結論**
- **發放前考慮影響**:即使內容有害,放大可能造成更多傷害

---

## 與其他 -tw skill 協作

`social-media-intelligence-tw` 處理**跨帳號、跨平台之模式偵測**。實務中與其他 -tw skill 緊密協作。

### 典型記者工作流順序(7 個 skill 串接)

```
[1. 資料蒐集]                  ← foia-requests-tw
       ↓
[2. 來源驗證 / 內容查證]       ← source-verification-tw
       ↓
[2.5. 跨平台情報 / OSINT]      ← social-media-intelligence-tw  ← 你在這裡
       ↓
[3. 採訪準備 / 採訪]           ← interview-prep-tw
       ↓
[4. 主張驗證 / 查核]           ← fact-check-workflow-tw
       ↓
[5. AI 起草草稿]
       ↓
[6. 去 AI 寫作味]              ← ai-writing-detox-tw
       ↓
[7. 編務校對]                  ← newsroom-style-tw
       ↓
[8. 發稿]
```

> `social-media-intelligence-tw` 與 `source-verification-tw` 在**步驟 2** 並列工作:前者處理**多帳號模式**,後者處理**單一帳號真偽**。

### 重疊處理(同問題多 skill 都有)

- **帳號真偽**:
  - `source-verification-tw` §二:**單一帳號**驗證(SIFT + 平台特性)
  - `social-media-intelligence-tw` §四:**帳號群**真實性評分(authenticity score)
  - **單一帳號用前者;100 個帳號用後者**

- **協同操作**:
  - `social-media-intelligence-tw` §七:**主處理**(CIB 指標、評分)
  - `source-verification-tw` §二:輔助(GoLaxy 紅旗特徵)
  - **以 `social-media-intelligence-tw` 為準**

- **深偽案例**:
  - `source-verification-tw` §五 + §六:**單一影像/影片**之深偽偵測(C2PA、Hive、Reality Defender)+ 台灣案例
  - `social-media-intelligence-tw` §十一:**散布、轉發**之法律風險(§104 加重條款)
  - **兩者搭配最完整**

- **存檔**:
  - `source-verification-tw` §十:詳述
  - `social-media-intelligence-tw` §八:程式碼版本
  - **以 `source-verification-tw` 為主**

- **法律風險**:
  - `social-media-intelligence-tw` §十一:**SMI 場景特有**(揭露水軍之誹謗風險、§358 入侵電腦)
  - `source-verification-tw` §十二:來源驗證場景
  - `fact-check-workflow-tw` §九:查核場景
  - **三者互補**,場景不同

### 建議搭配安裝

`social-media-intelligence-tw` **強烈建議搭配** `source-verification-tw` 使用 — 兩者是 OSINT 工作的兩面。**新聞工作者**也建議加 `fact-check-workflow-tw`、`foia-requests-tw`、`newsroom-style-tw`、`ai-writing-detox-tw`。

---

## 附錄一:常用 OSINT 工具清單

| 類別 | 工具 | 網址 |
|---|---|---|
| 機器人偵測 | Botometer X | osome.iu.edu/tools/botometer |
| 敘事追蹤 | Hoaxy / Hoaxy2 | osome.iu.edu/tools/hoaxy |
| 協同網絡 | Coordiscope | osome.iu.edu |
| 協同分析 | CooRTweet (R) | github |
| 反向圖搜 | TinEye | tineye.com |
| 反向圖搜 | Yandex Images | yandex.com/images |
| 反向圖搜 | Google Lens | lens.google.com |
| 影像鑑識 | FotoForensics | fotoforensics.com |
| 影像鑑識 | Forensically | 29a.ch/photo-forensics |
| 影片驗證 | InVID-WeVerify | weverify.eu |
| 網絡視覺化 | Gephi | gephi.org |
| 網絡視覺化 | Maltego CE | maltego.com |
| 存檔 | Wayback Machine | web.archive.org |
| 存檔 | Archive.today | archive.ph |
| 台灣假訊息資料庫 | Cofacts | cofacts.tw |
| 台灣假訊息查核 | 台灣事實查核中心 | tfc-taiwan.org.tw |
| FB 廣告資料庫 | Meta Ad Library | facebook.com/ads/library |
| 台灣資訊作戰研究 | DoubleThink Lab | doublethinklab.org |
| 台灣資訊環境 | IORG | iorg.tw |

---

## 附錄二:Bellingcat / 跨國 OSINT 網絡

| 資源 | 用途 |
|---|---|
| Bellingcat Toolkit 2.0 | bellingcat.gitbook.io/toolkit |
| Bellingcat 訓練課程 | bellingcat.com/online-investigation-academy |
| WITNESS DRRF | gen-ai.witness.org |
| Information Futures Lab | informationfutureslab.org |
| Shadow FIMI Investigator Network | (跨國 OSINT 網絡,與 DoubleThink Lab 合作) |

---

**版本說明**

- 版本:1.0.0
- 截至:2026-05-28
- 改寫自:upstream `journalism-core/social-media-intelligence` (jamditis/claude-skills-journalism)
- 在地化重點:
  - **保留 upstream 通用 Python 程式碼**:多平台監測、突發新聞偵測、帳號真實性、網絡分析、敘事追蹤、協同評分
  - **保留 OSINT 工具集**:Botometer X、Hoaxy、Gephi、Bellingcat 等
  - **新增台灣 16 個平台清單**:Threads / PTT / Dcard / LINE OpenChat / FB / IG / YouTube / TikTok / X / Bluesky / Mastodon / Telegram / 微博 / 小紅書 / 抖音 / WeChat
  - **新增台灣資訊作戰生態章節**:中國 GoLaxy 系統、TikTok 演算法、WeChat 視頻號、選舉期境外干預
  - **新增台灣敘事追蹤實務**:從微博/抖音 → 境外協同帳號 → PTT → Threads/FB → LINE 群組 → 媒體之擴散鏈
  - **新增 GoLaxy 範本研究方法**(DoubleThink Lab 研究方法)
  - **新增「平民版」研究方法**(個別記者也能做)
  - **新增 Cofacts API、PTT Crawler 等 g0v 工具**
  - **新增法律風險章節**:《選罷法》§104 加重深偽條款、《社維法》§63、《刑法》§310 誹謗、§358 入侵電腦、《個資法》§51 新聞自由抗辯
  - **新增與其他 -tw skill 協作章節**(7 個 skill 串接;與 source-verification-tw 並列工作)
- 法律依據:截至 2026 年 5 月之《選舉罷免法》《社會秩序維護法》《刑法》《個人資料保護法》。具體條號與細節**請以全國法規資料庫公告版本為準**;涉及具體調查報導法律事項建議洽律師
- 平台 API 與工具狀態截至 2026 年 5 月;訪問前先驗證最新政策
