import requests
import time
import csv
import re
from urllib.parse import urljoin
from pathlib import Path
from datetime import datetime

URL = "https://www.cwa.gov.tw/V8/C/W/County/County.html?CID=66"
DATA_URL = urljoin(URL, "/Data/js/TableData_36hr_County_C.js?")
TAICHUNG_COUNTY_ID = "66"
CSV_FILE = Path(__file__).resolve().parent / "weather01.csv"
STOP_DATETIME = datetime(2026, 8, 21, 16, 0)
FETCH_INTERVAL_SECONDS = 5 * 60

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    )
}


def fetch_page():
    """抓取臺中市未來 36 小時的溫度資料，最多等待 10 秒"""
    response = requests.get(
        DATA_URL,
        headers=HEADERS,
        timeout=10
    )
    response.raise_for_status()
    response.encoding = "utf-8"

    county_match = re.search(
        rf"'{TAICHUNG_COUNTY_ID}'\s*:\s*\[(.*?)]\s*,\s*'",
        response.text,
        re.S,
    )
    if county_match is None:
        raise ValueError(f"找不到臺中市溫度資料: {TAICHUNG_COUNTY_ID}")

    records = re.findall(
        r"'TimeRange'\s*:\s*'([^']+)'.*?"
        r"'Temp'\s*:\s*\{'C'\s*:\s*\{'L'\s*:\s*'([^']+)'\s*,\s*"
        r"'H'\s*:\s*'([^']+)'\s*\}.*?"
        r"'PoP'\s*:\s*'([^']+)'",
        county_match.group(1),
        re.S,
    )
    if not records:
        raise ValueError("找不到臺中市溫度欄位")

    return records


def save_to_csv(records):
    """將臺中市溫度資料存成 weather01.csv"""
    if not records or any(len(record) != 4 for record in records):
        raise ValueError("資料格式錯誤，只接受臺中市的溫度紀錄")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    should_write_header = not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0

    with open(CSV_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if should_write_header:
            writer.writerow(["抓取時間", "預報時段", "低溫(°C)", "高溫(°C)", "降雨機率(%)"])
        for time_range, low, high, pop in records:
            writer.writerow([now, time_range, low, high, pop])

    print(f"[{now}] 已存檔: {CSV_FILE}")


def main():
    while True:
        if datetime.now() >= STOP_DATETIME:
            print("已到 2026-08-21 16:00，停止抓取。")
            break

        try:
            print("開始抓取 CWA 網頁...")

            records = fetch_page()
            save_to_csv(records)

        except requests.exceptions.Timeout:
            print("抓取逾時：10 秒內沒有回應")

        except requests.exceptions.RequestException as e:
            print(f"網路請求失敗：{e}")

        except Exception as e:
            print(f"其他錯誤：{e}")

        print("等待 5 分鐘後再次抓取...")
        time.sleep(FETCH_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
