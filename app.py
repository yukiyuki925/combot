import feedparser
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# 動画検知 -----------------------------------

# CHANNEL_ID = "UCpj_nD9850tykDqIrjtIXdg"

# # 現状、最新の動画のID
# last_vid = ["bv9ondE2rpg"]

# while True:
#   url = "https://www.youtube.com/feeds/videos.xml?channel_id={}".format(CHANNEL_ID)
#   d = feedparser.parse(url)
#   videoID = d.entries[0].yt_videoid
#   print(videoID,d.entries[0]["title"])

#   # 動画IDを比較
#   if videoID not in last_vid:
#     break
#   sleep(5)

# pyAutoGUI ------------------------------------------- 
driver_path="/Users/kumagai/Desktop/combot/tools/chromedriver"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# Googleの検索ページを開く
url = 'https://www.google.com'
driver.get(url)
