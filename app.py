import feedparser
from time import sleep

CHANNEL_ID = "UCpj_nD9850tykDqIrjtIXdg"

last_vid = ["bv9ondE2rpg"]

while True:
  url = "https://www.youtube.com/feeds/videos.xml?channel_id={}".format(CHANNEL_ID)
  d = feedparser.parse(url)
  videoID = d.entries[0].yt_videoid
  print(videoID,d.entries[0]["title"])

  if videoID not in last_vid:
    break
  sleep(5)