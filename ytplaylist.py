import yt_dlp
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Download a YouTube playlist using yt-dlp.")
parser.add_argument("playlist_url", help="The URL of the YouTube playlist to download.")
parser.add_argument("-o", "--output", default="C:/Users/veena/Music/", help="The directory where videos will be saved.")
parser.add_argument("-f", "--format", default="mp4", help="The preferred output format (default: mp4).")

# Parse arguments
args = parser.parse_args()

# Download configuration
ydl_opts = {
    'outtmpl': f"{args.output}/%(title)s.%(ext)s",  # Save in user-specified folder
    'format': 'bv+ba/best',  # Download best video and best audio separately
    'merge_output_format': args.format,  # Use the specified format
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': args.format,
    }]
}

# Running the downloader
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.playlist_url])