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
| en | en/202108_tiny.csv | 74,227 | 65,570 |
| zh | zh/202108_tiny.csv | 63,126 | 23,387 |
| th | th/202108_tiny.csv | 40,886 | 26,907 |
| ru | ru/202108_tiny.csv | 39,890 | 46,061 |
| hi | hi/202108_tiny.csv | 34,034 | 31,439 |
| ar | ar/202108_tiny.csv | 31,993 | 42,649 |
| de | de/202108_tiny.csv | 30,727 | 66,954 |
| tr | tr/202108_tiny.csv | 27,317 | 68,079 |
| el | el/202108_tiny.csv | 25,947 | 26,735 |
| fr | fr/202108_tiny.csv | 25,371 | 70,466 |
| ta | ta/202108_tiny.csv | 21,860 | 26,120 |
| da | da/202108_tiny.csv | 18,779 | 62,094 |
| id | id/202108_tiny.csv | 18,086 | 72,760 |
| bn | bn/202108_tiny.csv | 16,315 | 57,112 |
| fi | fi/202108_tiny.csv | 15,561 | 50,626 |
| my | my/202108_tiny.csv | 14,729 | 95,755 |
| hu | hu/202108_tiny.csv | 13,154 | 49,237 |
| te | te/202108_tiny.csv | 11,929 | 24,444 |
| pt | pt/202108_tiny.csv | 11,692 | 48,974 |
| az | az/202108_tiny.csv | 11,188 | 52,025 |
| ur | ur/202108_tiny.csv | 10,917 | 26,503 |
| is | is/202108_tiny.csv | 10,632 | 38,268 |
| fa | fa/202108_tiny.csv | 10,482 | 24,102 |
| ka | ka/202108_tiny.csv | 10,395 | 23,914 |
| uk | uk/202108_tiny.csv | 9,103 | 36,392 |
| ml | ml/202108_tiny.csv | 9,080 | 42,359 |
| ga | ga/202108_tiny.csv | 9,058 | 51,411 |
| be | be/202108_tiny.csv | 7,622 | 37,739 |
| ky | ky/202108_tiny.csv | 7,241 | 42,027 |
| kk | kk/202108_tiny.csv | 6,917 | 26,163 |
| tg | tg/202108_tiny.csv | 5,491 | 40,244 |
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