import requests
import bz2
import argparse
import sys
from util import make_dump_url
from pathlib import Path

def parse_args():
  parser = argparse.ArgumentParser(
    description="Making search words from Wikipedia",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  )
  parser.add_argument("lang",     type=str, help="language code (ja, en, ...)")
  parser.add_argument("--outdir", type=str, default="word", help="dirname to save words")
  return parser.parse_args(sys.argv[1:])


def make_search_word(lang, outdir="word"):
  # download wikipedia index
  url = make_dump_url(lang)
  fn_index = Path(outdir) / "dump" / lang / Path(url).name # xxx.txt.bz2
  fn_index.parent.mkdir(parents=True, exist_ok=True)

  if not fn_index.exists():
    with open(fn_index, "wb") as f:
      f.write(requests.get(url).content)

  # obtain words
  fn_word = Path(outdir) / "word" / lang / fn_index.stem 
  fn_word.parent.mkdir(parents=True, exist_ok=True)

  with bz2.open(fn_index, "rt", encoding="utf-8") as f:
    words = list(map(lambda x: x.strip("\n").split(":")[-1], f.readlines()))
  words = [w.strip(" ") for w in set(words) if len(w) > 0]
  words.sort()

  with open(fn_word, "w", encoding="utf-8") as f:
    f.writelines([w + "\n" for w in words])

  return fn_word

if __name__ == "__main__":
  args = parse_args()

  filename = make_search_word(args.lang, args.outdir)
  print(f"save {args.lang.upper()} words to {filename}.")
