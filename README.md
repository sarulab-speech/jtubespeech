# JTubeSpeech: Corpus of Japanese speech collected from YouTube 
This repository provides a list of YouTube videos with Japanese subtitles.

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
| #videos-sub-true  | xxx (10,000 hours)      | (TBA)         |
| #videos-auto-true | xxx                     | (TBA)         |
<br>

## Contributors
- [Shinnosuke Takamichi](https://sites.google.com/site/shinnosuketakamichi/home) (The University of Tokyo, Japan) [main contributor]
- [Ludwig Kürzinger](https://www.ei.tum.de/mmk/personen/mitarbeiter/ludwig-kuerzinger/) (Technical University of Munich, Germany)
- [Takaaki Saeki](https://takaaki-saeki.github.io/) (The University of Tokyo, Japan)
- [Sayaka Shiota](http://www-isys.sd.tmu.ac.jp/) (Tokyo Metropolitan University, Japan)
- [Shinji Watanabe](https://sites.google.com/view/shinjiwatanabe) (Carnegie Mellon University, USA)

## Scripts
This repository provides scripts for data collection from YouTube. Since processes of the scripts are language independent, users can collect data of their favorite langauges. [youtube-dl](https://github.com/ytdl-org/youtube-dl) is required.

### step1: making search words 
This downloads the wikipedia dump file and finds words for searching videos. `{lang}` is the languag code, e.g., `ja` (Japanese) and `en` (English).
```
$ python scripts/make_search_word.py {lang}
```
### step2: obtaining video IDs
This obtains YouTube video IDs by searching words. `{filename_word_list}` is a word list file made in step1. After this step, the process will take a long time. It is recommended to split the files (e.g., `{filename_word_list}`) and run them in parallel.
```
$ python scripts/obtain_video_id.py {lang} {filename_word_list}
```
### step3: checking if subtitles are available
This retrieves whether the video has subtitles or not. `{filename_videoid_list}` is a videoID list file made in step2. This process will make a CSV file.
```
$ python scripts/obtain_video_id.py {lang} {filename_videoid_list}
```
### step4: downloading videos with manual subtitles
This downloads audio and manual subtitles. Note that, this process requires a very large amount of storage.`{filename_subtitle_list}` is a subtitle list file makde in step3. The audio and subtitles will be saved in `video/wav` and `video/txt`, respectively.
```
$ python scripts/obtain_video_id.py {lang} {filename_subtitle_list}
```

## Reference
- coming soon

## Link
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)