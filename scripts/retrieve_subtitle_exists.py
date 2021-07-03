import time
import requests
import argparse
import re
import sys
import subprocess
from pathlib import Path
from util import make_video_url
import pandas as pd
from tqdm import tqdm

def parse_args():
  parser = argparse.ArgumentParser(
    description="Retrieving whether subtitles exists or not.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  )
  parser.add_argument("lang",         type=str, help="language code (ja, en, ...)")
  parser.add_argument("videoidlist",  type=str, help="filename of video ID list")  
  parser.add_argument("--outdir",     type=str, default="sub", help="dirname to save results")
  parser.add_argument("--checkpoint", type=str, default=None, help="filename of list checkpoint (for restart retrieving)")
  return parser.parse_args(sys.argv[1:])


def retrieve_subtitle_exists(lang, fn_videoid, outdir="sub", wait_sec=0.2, fn_checkpoint=None):
  fn_sub = Path(outdir) / lang / f"{Path(fn_videoid).stem}.csv"
  fn_sub.parent.mkdir(parents=True, exist_ok=True)

  # if file exists, load it and restart retrieving.
  if fn_checkpoint is None:
    subtitle_exists = pd.DataFrame({"videoid": [], "auto": [], "sub": []}, dtype=str)
  else:
    subtitle_exists = pd.read_csv(fn_checkpoint)

  # load video ID list
  n_video = 0
  for videoid in tqdm(open(fn_videoid).readlines()):
    videoid = videoid.strip(" ").strip("\n")
    if videoid in set(subtitle_exists["videoid"]):
      continue

    # send query to YouTube
    url = make_video_url(videoid)
    try:
      result = subprocess.check_output(f"youtube-dl --list-subs --sub-lang {lang} --skip-download {url}", \
        shell=True, universal_newlines=True)

      se = {"videoid": [videoid], "auto": [False], "sub": [False]}
      sub_type = None
      for r in result.split("\n"):
        if r == f"Available automatic captions for {videoid}:":
          sub_type = "auto"
        elif r == f"Available subtitles for {videoid}:":
          sub_type = "sub"
        if r.startswith(lang) and sub_type is not None:
          se[sub_type] = [True]
      subtitle_exists = pd.concat([subtitle_exists, pd.DataFrame(se)])

      n_video += 1
    except:
      pass

    # write current result
    if n_video % 2 == 0:
      subtitle_exists.to_csv(fn_sub, index=None)
    
    # sleep
    if wait_sec > 0.01:
      time.sleep(wait_sec)

  # write
  subtitle_exists.to_csv(fn_sub, index=None)
  return fn_sub

if __name__ == "__main__":
  args = parse_args()

  filename = retrieve_subtitle_exists(args.lang, args.videoidlist, \
    args.outdir, fn_checkpoint=args.checkpoint)
  print(f"save {args.lang.upper()} subtitle info to {filename}.")
