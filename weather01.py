import requests
import time
import csv
from datetime import datetime

URL = "https://www.cwa.gov.tw/V8/C/W/County/County.html?CID=66"
CSV_FILE = "weather01.csv"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    )
}


def fetch_page():
    """抓取頁面內容"""
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def save_to_csv(page_text):
    """將頁面內容存成 weather01.csv"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["抓取時間", "頁面內容"])
        writer.writerow([now, page_text])
    print(f"[{now}] 已存檔: {CSV_FILE}")


def main():
    while True:
        try:
            page = fetch_page()
            save_to_csv(page)
        except Exception as e:
            print(f"抓取失敗: {e}")
        # 每 30 分鐘抓取一次
        time.sleep(1800)


if __name__ == "__main__":
    main()