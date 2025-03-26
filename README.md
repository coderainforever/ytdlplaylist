# YouTube Playlist Downloader

This script allows you to download an entire YouTube playlist using `yt-dlp`.

## Features
- Downloads videos from a YouTube playlist.
- Saves videos to a user-specified directory.
- Supports different video formats (default: `mp4`).
- Uses `yt-dlp` for enhanced downloading features.

## Prerequisites
- Python 3.x installed
- `yt-dlp` installed
- `ffmpeg` installed (required for format conversion)

## Installation

### Install `yt-dlp`
```bash
pip install yt-dlp
```

### Install `ffmpeg`
#### Windows:
Download and install from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).

#### Linux (Debian/Ubuntu):
```bash
sudo apt update && sudo apt install ffmpeg
```

#### Mac (Homebrew):
```bash
brew install ffmpeg
```

## Usage
```bash
python script.py <playlist_url> [-o OUTPUT_DIRECTORY] [-f FORMAT]
```

### Arguments
- `<playlist_url>`: The URL of the YouTube playlist to download.
- `-o, --output`: (Optional) Directory where videos will be saved. Default: `C:/Users/veena/Music/`.
- `-f, --format`: (Optional) Preferred output format (default: `mp4`).

### Example
```bash
python script.py "https://www.youtube.com/playlist?list=PL12345" -o "D:/Downloads" -f mp4
```

## How It Works
1. Parses the provided playlist URL.
2. Sets up `yt-dlp` options, including the output directory and format.
3. Downloads the best available video and audio.
4. Merges them using `ffmpeg` into the specified format.

## Troubleshooting
- If you get errors related to `ffmpeg`, ensure it is installed and available in your system's PATH.
- If a video doesn't download, try updating `yt-dlp`:
  ```bash
  pip install --upgrade yt-dlp
  ```

## License
This project is open-source under the MIT License.

