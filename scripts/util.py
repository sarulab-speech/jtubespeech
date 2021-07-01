import re
from datetime import datetime as dt
from pathlib import Path
import subprocess

# YouTube video URL
def make_video_url(videoid: str) -> str:
  return f"https://www.youtube.com/watch?v={videoid}"

# YouTube Search URL
def make_query_url(query: str) -> str:
  return f"https://www.youtube.com/results?search_query={query}&sp=EgQQASgB"

# Wikipedia dump file URL
def make_dump_url(lang: str) -> str:
  return f"https://dumps.wikimedia.org/{lang}wiki/latest/{lang}wiki-latest-pages-articles-multistream-index.txt.bz2"


def make_basename(videoid: str) -> str:
  return str(Path(videoid[:2]) / videoid)


def count_total_second(t: dt) -> float:
  return t.hour * 3600 + t.minute * 60 + t.second * 1 + t.microsecond * 1e-6


def obtain_channelid(videoid: str) -> str:
  fn_html = Path("temp.html")

  # download
  url = make_video_url(videoid)
  subprocess.run(f"wget {url} -O {fn_html}", shell=True)

  # obtain ID
  html = "".join(open(fn_html, "r").readlines())
  try:
    # only Japanese
    channelid = re.findall(r"canonicalBaseUrl\":\"/channel/([\w\_\-]+?)\"\}\},\"subscriberCountText\":\{\"accessibility\":\{\"accessibilityData\":\{\"label\":\"チャンネル登録者数", html)[0]
  except:
    channelid = None

  return channelid


def vtt2txt(vtt: list) -> list:
  txt, is_started = [], False

  for v in vtt:
    m = re.match(r'(\d+\:\d+\:\d+\.\d+) --> (\d+\:\d+\:\d+\.\d+)', v.strip("\n"))
    if m is not None:
      st = count_total_second(dt.strptime(m.groups()[0], "%H:%M:%S.%f"))
      et = count_total_second(dt.strptime(m.groups()[1], "%H:%M:%S.%f"))
      txt.append([st, et, ""])
      is_started = True   
    elif is_started:
      v = v.replace("\n", " ").strip(" ").lstrip("-").replace("　", " ").replace("  ", " ").strip(" ").strip("\t")
      if len(v) == 0:
        is_started = False
      else:
        txt[-1][-1] += " " + v

  # refine
  txt_refined = []
  for t in txt:
    x = t[2].replace("\n", " ").replace("　", " ").replace("  ", " ").strip(" ").strip("\t").replace("»", "").replace("«", "")
    if len(x) > 0:
      txt_refined.append([t[0], t[1], x])

  return txt_refined
