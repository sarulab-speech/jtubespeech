import re
from datetime import datetime as dt
from pathlib import Path
import subprocess

# YouTube video URL
def make_video_url(videoid: str) -> str:
  return f"https://www.youtube.com/watch?v={videoid}"

# YouTube Search URL
def make_query_url(query: str) -> str:
  q = query.rstrip("\n").strip(" ").replace(" ", "+")
  return f"https://www.youtube.com/results?search_query={q}&sp=EgQQASgB"

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

def get_subtitle_language(response_youtube):
  lang_code = ["aa","ab","ace","ady","af","ak","als","alt","am","an","ang","ar","arc","ary","arz","as","ast","atj","av","avk","awa","ay","az","azb","ba","ban","bar","bat-smg","bcl","be","be-tarask","bg","bh","bi","bjn","bm","bn","bo","bpy","br","bs","bug","bxr","ca","cbk-zam","cdo","ce","ceb","ch","cho","chr","chy","ckb","co","cr","crh","cs","csb","cu","cv","cy","da","de","din","diq","dsb","dty","dv","dz","ee","el","eml","en","eo","es","et","eu","ext","fa","ff","fi","fiu-vro","fj","fo","fr","frp","frr","fur","fy","ga","gag","gan","gcr","gd","gl","glk","gn","gom","gor","got","gu","gv","ha","hak","haw","he","hi","hif","ho","hr","hsb","ht","hu","hy","hyw","hz","ia","id","ie","ig","ii","ik","ilo","inh","io","is","it","iu","ja","jam","jbo","jv","ka","kaa","kab","kbd","kbp","kg","ki","kj","kk","kl","km","kn","ko","koi","kr","krc","ks","ksh","ku","kv","kw","ky","la","lad","lb","lbe","lez","lfn","lg","li","lij","lld","lmo","ln","lo","lrc","lt","ltg","lv","mad","mai","map-bms","mdf","mg","mh","mhr","mi","min","mk","ml","mn","mni","mnw","mr","mrj","ms","mt","mus","mwl","my","myv","mzn","na","nah","nap","nds","nds-nl","ne","new","ng","nia","nl","nn","no","nov","nqo","nrm","nso","nv","ny","oc","olo","om","or","os","pa","pag","pam","pap","pcd","pdc","pfl","pi","pih","pl","pms","pnb","pnt","ps","pt","qu","rm","rmy","rn","ro","roa-rup","roa-tara","ru","rue","rw","sa","sah","sat","sc","scn","sco","sd","se","sg","sh","shn","si","simple","sk","skr","sl","sm","smn","sn","so","sq","sr","srn","ss","st","stq","su","sv","sw","szl","szy","ta","tay","tcy","te","tet","tg","th","ti","tk","tl","tn","to","tpi","tr","trv","ts","tt","tum","tw","ty","tyv","udm","ug","uk","ur","uz","ve","vec","vep","vi","vls","vo","wa","war","wo","wuu","xal","xh","xmf","yi","yo","za","zea","zh","zh-classical","zh-min-nan",
  "zh-yue","zu"]

  sub_type = None
  subtitle = {"auto": [], "sub": []}
  for r in response_youtube.split("\n"):
    if r.startswith("Available automatic captions for"):
      sub_type = "auto"
    elif r.startswith("Available subtitles for"):
      sub_type = "sub"
    elif sub_type is not None:
      lang = r.split(" ")[0].lower()
      if lang in lang_code:
        subtitle[sub_type].append(lang)

  return subtitle["auto"], subtitle["sub"]

