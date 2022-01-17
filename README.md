# JTubeSpeech: Corpus of Japanese speech collected from YouTube 
This repository provides 1) a list of YouTube videos with Japanese subtitles (JTubeSpeech), 2) scripts for making new lists of new languages, and 3) tiny lists for other languages.

## Description
`data/{lang}/{YYYYMM}.csv` lists as follows. See step4 for download.
|     | videoid     | auto  | sub   | channelid                 |
|---  |---          | ---   | ---   | ---                       |
|0    | 0017RsBbUHk | True  | True  | UCTW2tw0Mhho72MojB1L48IQ  |
|1    | 00PqfZgiboc | False | True  | UCzoghTgl4dvIW9GZF6UC-BA  |
|---  |---          | ---   | ---   | ---                       |
<br>

- `lang`: Language ID (ja [Japanese], en [English], ...)
- `YYYYMM`: Year and month when we collect data
- `videoid`: YouTube video ID. Its YouTube page is `https://www.youtube.com/watch?v={videoid}`.
- `auto`: The video has an automatic subtitle or not.
- `sub`: The video has a manual (i.e., human-generated) subtitle or not.
- `channelid`: YouTube Channel ID. Its YouTube page is `https://www.youtube.com/channel/{channelid}`.

## Statistics
| lang | filename (data/) | #videos-sub-true | #videos-auto-true |
| ---  | ---              | ---           | ---           |
| **ja** | ja/202103.csv  | **110,000** (10,000 hours) | **4,960,000** |
| en | en/202108_middle.csv | 739543 | 667555 |
|    | en/202108_tiny.csv |  74227 |  65570 |
| ru | ru/202203_middle.csv | 258222 | 349388 |
|    | ru/202108_tiny.csv |  39890 |  46061 |
| de | de/202203_middle.csv | 194468 | 527993 |
|    | de/202108_tiny.csv |  30727 |  66954 |
| fr | fr/202203_middle.csv | 164261 | 524261 |
|    | fr/202108_tiny.csv |  25371 |  70466 |
| ar | ar/202203_middle.csv | 158568 | 311697 |
|    | ar/202108_tiny.csv |  31993 |  42649 |
| th | th/202203_middle.csv | 154416 | 250417 |
|    | th/202108_tiny.csv |  40886 |  26907 |
| tr | tr/202203_middle.csv | 154213 | 494187 |
|    | tr/202108_tiny.csv |  27317 |  68079 |
| hi | hi/202203_middle.csv | 132175 | 172565 |
|    | hi/202108_tiny.csv |  34034 |  31439 |
| zh | zh/202108_middle.csv | 126271 | 23387 |
|    | zh/202108_tiny.csv |  63126 |  23387 |
| id | id/202203_middle.csv | 105334 | 447836 |
|    | id/202108_tiny.csv |  18086 |  72760 |
| el | el/202203_middle.csv | 96436 | 156445 |
|    | el/202108_tiny.csv |  25947 |  26735 |
| pt | pt/202203_middle.csv | 90600 | 436425 |
|    | pt/202108_tiny.csv |  11692 |  48974 |
| da | da/202203_middle.csv | 86027 | 421190 |
|    | da/202108_tiny.csv |  18779 |  62094 |
| bn | bn/202203_middle.csv | 75371 | 303335 |
|    | bn/202108_tiny.csv |  16315 |  57112 |
| fi | fi/202203_middle.csv | 68571 | 347307 |
|    | fi/202108_tiny.csv |  15561 |  50626 |
| ta | ta/202203_middle.csv | 66923 | 89209 |
|    | ta/202108_tiny.csv |  21860 |  26120 |
| hu | hu/202203_middle.csv | 64792 | 351426 |
|    | hu/202108_tiny.csv |  13154 |  49237 |
| uk | uk/202203_middle.csv | 55098 | 283741 |
|    | uk/202108_tiny.csv |  9103 |  36392 |
| fa | fa/202203_middle.csv | 54165 | 203794 |
|    | fa/202108_tiny.csv |  10482 |  24102 |
| ur | ur/202203_middle.csv | 47426 | 177232 |
|    | ur/202108_tiny.csv |  10917 |  26503 |
| az | az/202203_middle.csv | 42906 | 272895 |
|    | az/202108_tiny.csv |  11188 |  52025 |
| te | te/202203_middle.csv | 41478 | 110521 |
|    | te/202108_tiny.csv |  11929 |  24444 |
| ka | ka/202203_middle.csv | 38199 | 158179 |
|    | ka/202108_tiny.csv |  10395 |  23914 |
| ml | ml/202203_middle.csv | 35477 | 249624 |
|    | ml/202108_tiny.csv |  9080 |  42359 |
| be | be/202203_middle.csv | 33935 | 227854 |
|    | be/202108_tiny.csv |  7622 |  37739 |
| is | is/202203_middle.csv | 32272 | 159506 |
|    | is/202108_tiny.csv |  10632 |  38268 |
| kk | kk/202203_middle.csv | 26021 | 148230 |
|    | kk/202108_tiny.csv |  6917 |  26163 |
| ga | ga/202203_middle.csv | 22177 | 131863 |
|    | ga/202108_tiny.csv |  9058 |  51411 |
| ky | ky/202203_middle.csv | 20583 | 150884 |
|    | ky/202108_tiny.csv |  7241 |  42027 |
| tg | tg/202203_middle.csv | 15451 | 135276 |
|    | tg/202108_tiny.csv |  5491 |  40244 |
<br>

## Contributors
- [Shinnosuke Takamichi](https://sites.google.com/site/shinnosuketakamichi/home) (The University of Tokyo, Japan) [main contributor]
- [Ludwig Kürzinger](https://www.ei.tum.de/mmk/personen/mitarbeiter/ludwig-kuerzinger/) (Technical University of Munich, Germany)
- [Takaaki Saeki](https://takaaki-saeki.github.io/) (The University of Tokyo, Japan)
- [Sayaka Shiota](http://www-isys.sd.tmu.ac.jp/) (Tokyo Metropolitan University, Japan)
- [Shinji Watanabe](https://sites.google.com/view/shinjiwatanabe) (Carnegie Mellon University, USA)

## Scripts for data collection
`scripts/*.py` are scripts for data collection from YouTube. Since processes of the scripts are language independent, users can collect data of their favorite languages. [youtube-dl](https://github.com/ytdl-org/youtube-dl) and ffmpeg are required.

### step1: making search words 
The script `scripts/make_search_word.py` downloads the wikipedia dump file and finds words for searching videos. `{lang}` is the language code, e.g., `ja` (Japanese) and `en` (English).
```
$ python scripts/make_search_word.py {lang}
```
### step2: obtaining video IDs
The script `scripts/obtain_video_id.py` obtains YouTube video IDs by searching by words. `{filename_word_list}` is a word list file made in step1. After this step, the process will take a long time. It is recommended to split the files (e.g., `{filename_word_list}`) and run them in parallel.
```
$ python scripts/obtain_video_id.py {lang} {filename_word_list}
```
### step3: checking if subtitles are available
The script `scripts/retrieve_subtitle_exists.py` retrieves whether the video has subtitles or not. `{filename_videoid_list}` is a videoID list file made in step2. This process will make a CSV file. 
```
$ python scripts/retrieve_subtitle_exists.py {lang} {filename_videoid_list}
```
### step4: downloading videos with manual subtitles
The script `scripts/download_video.py` downloads audio and manual subtitles. Note that, this process requires a very large amount of storage.`{filename_subtitle_list}` is a subtitle list file made in step3. The audio and subtitles will be saved in `video/{lang}/wav16k` and `video/{lang}/txt`, respectively.
```
$ python scripts/download_video.py {lang} {filename_subtitle_list}
```
### step5 (ASR): alignment and scoring
Subtitles are not always correctly aligned with the audio and in some cases, subtitles not fit to the audio.
The script `scripts/align.py` aligns subtitles and audio with CTC segmentation using an ESPnet 2 ASR model:
```
$ python scripts/align.py {asr_train_config} {asr_model_file} {wavdir} {txtdir} {output_dir}
```
The result is written into a segments file `segments.txt` and a log file `segments.log` in the output directory.
Using the segments file, bad utterances or audio files can be sorted-out:
```
min_confidence_score=-0.3
awk -v ms=${min_confidence_score} '{ if ($5 > ms) {print} }' ${output_dir}/segments.txt
```
### step5 (ASV): speaker variation scoring
There are three types of videos: text-to-speech (a.k.a., TTS) video, single-speaker (i.e., monologue) video, and multi-speaker (e.g., dialogue) video. The script `scripts/xxx.py` obtains scores of speaker variation within a video to classify videos into three types. 
```
$ python scripts/xxx.py
```

## Reference
- coming soon

## Link
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [Other corpora by main contributor](https://sites.google.com/site/shinnosuketakamichi/publication/corpus)

## Update
- Aug. 2021: first update (`{lang}/*_tiny.csv`)
- Jan. 2022: add mid-size data (`{lang}/*_middile.csv`)