# JTubeSpeech: Corpus of Japanese speech collected from YouTube 
This repository provides a list of YouTube videos with Japanese subtitles.

## Description
`{YYYYMM}.csv` lists as follows.
|     | videoid     | auto  | sub   | channelid                 |
|---  |---          | ---   | ---   | ---                       |
|0    | 0017RsBbUHk | True  | True  | UCTW2tw0Mhho72MojB1L48IQ  |
|1    | 00PqfZgiboc | False | True  | UCzoghTgl4dvIW9GZF6UC-BA  |
|---  |---          | ---   | ---   | ---                       |
<br>

- `YYYYMM`: Year and month when we collect data
- `videoid`: YouTube video ID. Its YouTube page is `https://www.youtube.com/watch?v={videoid}`.
- `auto`: The video has an automatic subtitle or not.
- `sub`: The video has a manual (i.e., human-generated) subtitle or not.
- `channelid`: YouTube Channel ID. Its YouTube page is `https://www.youtube.com/channel/{channelid}`.

## Statistics
|                   | 202103.csv          | {YYYYMM}.csv  |
| ---               | ---                 | ---           |
| #videos-sub-true  | xxx (10,000 hours)  | (TBA)         |
| #videos-auto-true | xxx                 | (TBA)         |
<br>

## Contributors
- [Shinnosuke Takamichi](https://sites.google.com/site/shinnosuketakamichi/home) (The University of Tokyo, Japan) [main contributor]
- [Ludwig Kürzinger](https://www.ei.tum.de/mmk/personen/mitarbeiter/ludwig-kuerzinger/) (Technical University of Munich, Germany)
- [Takaaki Saeki](https://takaaki-saeki.github.io/) (The University of Tokyo, Japan)
- [Sayaka Shiota](http://www-isys.sd.tmu.ac.jp/) (Tokyo Metropolitan University, Japan)
- [Shinji Watanabe](https://sites.google.com/view/shinjiwatanabe) (Carnegie Mellon University, USA)

## Scripts
- coming soon

## Reference
- coming soon

## Link
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)