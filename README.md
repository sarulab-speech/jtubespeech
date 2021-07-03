# JTubeSpeech: Corpus of Japanese speech collected from YouTube 
This repository provides 1) a list of YouTube videos with Japanese subtitles and 2) scripts for making new lists of new languages.

## Description
`data/{lang}/{YYYYMM}.csv` lists as follows.
|     | videoid     | auto  | sub   | channelid                 |
|---  |---          | ---   | ---   | ---                       |
|0    | 0017RsBbUHk | True  | True  | UCTW2tw0Mhho72MojB1L48IQ  |
|1    | 00PqfZgiboc | False | True  | UCzoghTgl4dvIW9GZF6UC-BA  |
|---  |---          | ---   | ---   | ---                       |
<br>

- `lang`: Language (ja, ...)
- `YYYYMM`: Year and month when we collect data
- `videoid`: YouTube video ID. Its YouTube page is `https://www.youtube.com/watch?v={videoid}`.
- `auto`: The video has an automatic subtitle or not.
- `sub`: The video has a manual (i.e., human-generated) subtitle or not.
- `channelid`: YouTube Channel ID. Its YouTube page is `https://www.youtube.com/channel/{channelid}`.

## Statistics
|                   | ja/202103.csv           | {lang}/{YYYYMM}.csv  |
| ---               | ---                     | ---           |
| #videos-sub-true  | 110,000 (10,000 hours)  | (TBA)         |
| #videos-auto-true | 4,960,000               | (TBA)         |
<br>

## Contributors
- [Shinnosuke Takamichi](https://sites.google.com/site/shinnosuketakamichi/home) (The University of Tokyo, Japan) [main contributor]
- [Ludwig Kürzinger](https://www.ei.tum.de/mmk/personen/mitarbeiter/ludwig-kuerzinger/) (Technical University of Munich, Germany)
- [Takaaki Saeki](https://takaaki-saeki.github.io/) (The University of Tokyo, Japan)
- [Sayaka Shiota](http://www-isys.sd.tmu.ac.jp/) (Tokyo Metropolitan University, Japan)
- [Shinji Watanabe](https://sites.google.com/view/shinjiwatanabe) (Carnegie Mellon University, USA)

## Scripts for data collection
`scripts/*.py` are scripts for data collection from YouTube. Since processes of the scripts are language independent, users can collect data of their favorite langauges. [youtube-dl](https://github.com/ytdl-org/youtube-dl) is required.

### step1: making search words 
This downloads the wikipedia dump file and finds words for searching videos. `{lang}` is the languag code, e.g., `ja` (Japanese) and `en` (English).
```
$ python scripts/make_search_word.py {lang}
```
### step2: obtaining video IDs
This obtains YouTube video IDs by searching by words. `{filename_word_list}` is a word list file made in step1. After this step, the process will take a long time. It is recommended to split the files (e.g., `{filename_word_list}`) and run them in parallel.
```
$ python scripts/obtain_video_id.py {lang} {filename_word_list}
```
### step3: checking if subtitles are available
This retrieves whether the video has subtitles or not. `{filename_videoid_list}` is a videoID list file made in step2. This process will make a CSV file.
```
$ python scripts/obtain_video_id.py {lang} {filename_videoid_list}
```
### step4: downloading videos with manual subtitles
This downloads audio and manual subtitles. Note that, this process requires a very large amount of storage.`{filename_subtitle_list}` is a subtitle list file made in step3. The audio and subtitles will be saved in `video/{lang}/wav16k` and `video/{lang}/txt`, respectively.
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



## Reference
- coming soon

## Link
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)