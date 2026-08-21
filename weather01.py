import requests
import time
import csv
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime

URL = "https://www.cwa.gov.tw/V8/C/W/County/County.html?CID=66"
TAICHUNG_GROUP_ID = "C66"
CSV_FILE = Path(__file__).resolve().parent / "weather01.csv"
STOP_DATETIME = datetime(2026, 8, 21, 16, 0)
FETCH_INTERVAL_SECONDS = 30 * 60

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    )
}


def fetch_page():
    """抓取頁面並擷取臺中市地圖區塊，最多等待 10 秒"""
    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=10
    )
    response.raise_for_status()
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    taichung_group = soup.find("g", id=TAICHUNG_GROUP_ID)
    if taichung_group is None:
        raise ValueError(f"找不到臺中市資料區塊: {TAICHUNG_GROUP_ID}")

    return str(taichung_group)


def save_to_csv(page_text):
    """將頁面內容存成 weather01.csv"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    should_write_header = not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0

    with open(CSV_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if should_write_header:
            writer.writerow(["抓取時間", "頁面內容"])
        writer.writerow([now, page_text])

    print(f"[{now}] 已存檔: {CSV_FILE}")


def main():
    while True:
        if datetime.now() >= STOP_DATETIME:
            print("已到 2026-08-21 16:00，停止抓取。")
            break

        try:
            print("開始抓取 CWA 網頁...")

            page = fetch_page()
            save_to_csv(page)

        except requests.exceptions.Timeout:
            print("抓取逾時：10 秒內沒有回應")

        except requests.exceptions.RequestException as e:
            print(f"網路請求失敗：{e}")

        except Exception as e:
            print(f"其他錯誤：{e}")

        print("等待 30 分鐘後再次抓取...")
        time.sleep(FETCH_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
