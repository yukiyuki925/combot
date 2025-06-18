import pyautogui
import pyperclip
import feedparser
import tempfile
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ---------- 設定 ----------
CHANNEL_ID = "UCvMVMPFJKbn2JztHP-jYpaA"
COMMENT_TEXT = "素晴らしい動画でした！"
CHROME_PROFILE_PATH = "/Users/kumagai/Library/Application Support/Google/Chrome"
CHROME_PROFILE_NAME = "Default"
CHROMEDRIVER_PATH = "/Users/kumagai/Desktop/Python/combot/tools/chromedriver"

# ---------- Chrome 設定 ----------
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")

# ---------- 最新動画のチェック ----------
feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
d = feedparser.parse(feed_url)
last_video_id = d.entries[0].yt_videoid
print("初回検出された動画ID:", last_video_id)

# 新しい動画が出るまで監視
while True:
    d = feedparser.parse(feed_url)
    current_video_id = d.entries[0].yt_videoid
    video_title = d.entries[0]["title"]
    print("現在の動画:", video_title, current_video_id)

    if current_video_id != last_video_id:
        print("🎬 新しい動画を検出しました。処理を開始します...")
        break

    sleep(10)

#----------- chromeにログイン -------------------
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# アドレスバーを選択し、Googleログインページにアクセス
pyautogui.keyDown("command")
pyautogui.keyDown("l")
pyautogui.keyUp("command")
pyautogui.keyUp("l")
time.sleep(0.5)

pyperclip.copy("https://accounts.google.com/ServiceLogin")
pyautogui.hotkey("command", "v")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=705, y=478)
time.sleep(3)
pyperclip.copy("ppeni2976@gmail.com")
pyautogui.hotkey("command", "v")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=970, y=702)
time.sleep(5)
pyautogui.click(x=620, y=616)
time.sleep(10)
pyautogui.click(x=982, y=457)
time.sleep(5)

# ---------- YouTube動画ページへアクセス ----------
video_url = "https://www.youtube.com/watch?v=gMkJ5ZIoRBQ"

pyautogui.keyDown("command")
pyautogui.keyDown("l")
pyautogui.keyUp("command")
pyautogui.keyUp("l")
time.sleep(0.5)

pyperclip.copy(video_url)
time.sleep(0.5)

pyautogui.hotkey("command", "v")
time.sleep(0.5)

pyautogui.press("enter")
time.sleep(10)

# ---------- コメント欄にコメントを入力 ----------

# コメント入力欄をクリック
pyautogui.click(x=159, y=921)
time.sleep(5)

pyautogui.click(x=159, y=921)
time.sleep(5)

# 実際のコメント入力欄を取得し、コメントを入力
pyperclip.copy(COMMENT_TEXT)
time.sleep(0.5)

pyautogui.hotkey("command", "v")
time.sleep(0.5)

# 投稿ボタンを押す
pyautogui.click(x=682, y=960)
time.sleep(5)
print("コメントを投稿しました！")

# 投稿済IDを記録
last_vid.append(videoID)

driver.quit()
