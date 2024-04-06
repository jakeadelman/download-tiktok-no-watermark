# Download TikTok No Watermark

## Install using pip

```
pip install download_tiktok_no_watermark
```

## Using it in your project

```
from download_tiktok_no_watermark.download import download

download(video_url="https://www.tiktok.com/@sourcomedy/video/7340806842651528490",
        output_name="hello",
        output_dir="./")
```

## Args

```
video_url: url of tiktok video ('https://www.tiktok.com'+ @ + tiktokUserId + '/video/' + videoId)
output_name: video file name for output (don't include .mp4)
output_dir: output directory
```
