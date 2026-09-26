# YouTube Playlist Link Extractor

A lightweight Python utility that takes a YouTube playlist URL and extracts the URLs of every video in it, saving them to a text file — using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for fast, reliable metadata extraction without downloading the videos themselves.

## Features

- Extracts all video URLs from a public YouTube playlist
- No video/audio downloading — metadata only, so it's fast
- Saves results to a simple `video_links.txt` file, one URL per line

## Requirements

- Python 3.7+
- `yt-dlp`

## Installation

```bash
pip install yt-dlp
```

## Usage

```bash
python main.py
```

You'll be prompted to enter a playlist URL:

```
Enter playlist URL: https://www.youtube.com/playlist?list=XXXXXXXXXXXXXXXXXXXX
```

Once finished, the script prints:

```
Done! Video links saved to video_links.txt
```

All video links from the playlist will be saved in `video_links.txt` in the same directory.

## Example

```
Enter playlist URL: https://www.youtube.com/playlist?list=PLxxxxxxxx
Done! Video links saved to video_links.txt
```

`video_links.txt`:
```
https://www.youtube.com/watch?v=xxxxxxxxxxx
https://www.youtube.com/watch?v=yyyyyyyyyyy
https://www.youtube.com/watch?v=zzzzzzzzzzz
```

## Notes

- Only works with public or unlisted playlists (private playlists require authentication, which this script does not handle).
- Uses `extract_flat` mode, so it retrieves video URLs without parsing full video metadata — keeping it quick even for large playlists.

## License

MIT
