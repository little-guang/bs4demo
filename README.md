<div align="center">

# 🌤️ weather01.py ☀️

### 🏙️ 臺中市天氣爬蟲小幫手 🐻

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.x-2CA5E0?style=for-the-badge&logo=python&logoColor=white)
![CWA](https://img.shields.io/badge/資料來源-中央氣象署-FF6B6B?style=for-the-badge)

</div>

---

<div align="center">

```
  ☀️  ⛅  🌧️  ⛈️  🌤️  🌥️  🌦️
```

</div>

## 🌈 這是什麼？

<div style="background: linear-gradient(135deg, #FFF3E0, #E3F2FD); border-radius: 15px; padding: 20px;">

這是一個使用 Python 撰寫的**網路爬蟲程式** 🕷️，會定時去 **中央氣象署（CWA）** 🏛️ 抓取 **臺中市未來 36 小時的天氣預報** 🌡️，然後把資料乖乖存進 CSV 檔 📁 裡！

</div>

## ✨ 功能特色

<div style="background: linear-gradient(135deg, #FCE4EC, #F3E5F5); border-radius: 15px; padding: 20px;">

| 🎀 特色 | 📝 說明 |
|:---:|:---|
| 🌤️ **天氣預報** | 抓取臺中市未來 36 小時的溫度與降雨機率 |
| ⏱️ **定時抓取** | 每 5 分鐘自動抓取一次，超勤勞！ |
| 📄 **CSV 儲存** | 自動存成 CSV 檔（UTF-8 with BOM，Excel 直接開沒問題） |
| 🛡️ **錯誤處理** | 內建逾時與錯誤處理，不怕網路不穩 |

</div>

## 🚀 怎麼使用？

<div style="background: linear-gradient(135deg, #E8F5E9, #E0F2F1); border-radius: 15px; padding: 20px;">

### 1️⃣ 安裝相依套件

```bash
pip install requests
```

### 2️⃣ 執行程式

```bash
python weather01.py
```

### 3️⃣ 完成！🎉

程式會自動開始抓取，並在同目錄下產生 `weather01.csv` 檔案～

</div>

## 📊 輸出檔案說明

<div style="background: linear-gradient(135deg, #FFF8E1, #FFECB3); border-radius: 15px; padding: 20px;">

程式會產生 **`weather01.csv`**，欄位長這樣：

| 🗂️ 欄位 | 📖 說明 |
|:---:|:---|
| 🕐 抓取時間 | 執行抓取的時間 |
| 📅 預報時段 | 預報的起訖時間 |
| 🥶 低溫(°C) | 該時段最低溫 |
| 🥵 高溫(°C) | 該時段最高溫 |
| ☔ 降雨機率(%) | 該時段降雨機率 |

</div>

## 🧩 程式碼小教室

<div style="background: linear-gradient(135deg, #E8EAF6, #EDE7F6); border-radius: 15px; padding: 20px;">

| 🔧 函式 | 📖 在做什麼？ |
|:---:|:---|
| `fetch_page()` | 向中央氣象署發送請求，用正規表達式 🔍 解析出臺中市的溫度與降雨資料 |
| `save_to_csv(records)` | 把抓到的資料寫入 CSV 檔，檔案不存在會自動建立並寫入表頭 ✍️ |
| `main()` | 主程式迴圈 🔄，每 5 分鐘抓一次，直到設定的停止時間為止 |

</div>

## ⚠️ 小提醒

<div style="background: linear-gradient(135deg, #FFEBEE, #FCE4EC); border-radius: 15px; padding: 20px;">

- 🕒 程式預設抓取到 `2026-08-21 16:00` 為止，想改時間可以調整 `STOP_DATETIME` 變數
- 🙏 請遵守中央氣象署的網站使用規範，不要過度頻繁請求喔！

</div>

---

<div align="center">

### 🌟 祝你有個美好的一天！ 🌟

```
  ╔══════════════════════════╗
  ║  ☀️  ⛅  🌧️  ⛱️  🌈  ⭐  ║
  ║  天氣預報小幫手 上線囉！  ║
  ╚══════════════════════════╝
```

</div>