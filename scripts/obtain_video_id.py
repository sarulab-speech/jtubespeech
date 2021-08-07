import time
import requests
import argparse
import re
import sys
from pathlib import Path
from util import make_query_url
from tqdm import tqdm


def parse_args():
  parser = argparse.ArgumentParser(
    description="Obtaining video IDs from search words",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  )
  parser.add_argument("lang",     type=str, help="language code (ja, en, ...)")
  parser.add_argument("wordlist", type=str, help="filename of word list")  
  parser.add_argument("--outdir", type=str, default="videoid", help="dirname to save video IDs")
  return parser.parse_args(sys.argv[1:])


def obtain_video_id(lang, fn_word, outdir="videoid", wait_sec=0.2):
  fn_videoid = Path(outdir) / lang / f"{Path(fn_word).stem}.txt"
  fn_videoid.parent.mkdir(parents=True, exist_ok=True)

  with open(fn_videoid, "w") as f:
    for word in tqdm(list(open(fn_word, "r").readlines())):
      try:
        # download search results
        url = make_query_url(word)
        html = requests.get(url).content

        # find video IDs
        videoids_found = [x.split(":")[1].strip("\"").strip(" ") for x in re.findall(r"\"videoId\":\"[\w\_\-]+?\"", str(html))]
        videoids_found = list(set(videoids_found))

        # write
        f.writelines([v + "\n" for v in videoids_found])
        f.flush()
      except:
        print(f"No video found for {word}.")

      # wait
      if wait_sec > 0.01:
        time.sleep(wait_sec)

  return fn_videoid


if __name__ == "__main__":
  args = parse_args()

  filename = obtain_video_id(args.lang, args.wordlist, args.outdir)
  print(f"save {args.lang.upper()} video IDs to {filename}.")
