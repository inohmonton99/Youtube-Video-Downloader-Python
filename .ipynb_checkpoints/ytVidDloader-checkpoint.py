import os
import sys
from pytube import YouTube
import logging
import time
from tqdm import tqdm

os.makedirs('./logs', exist_ok=True)
logging.basicConfig(filename="./logs/ytDownload.log", level=logging.DEBUG, format="%(levelname)s - %(message)s")

# Handles progress bar when downloading
def print_progress(stream, chunk, file_handle, bytes_remaining):
    for i in tqdm(range(bytes_remaining)):
        pass
    print("download complete!")
    exit()
    

# Confirms if feeded URL is Youtube
def confirmURL(ytUrl):
    if 'youtube' not in ytUrl.lower():
        print("Please use a youtube URL")
        exit()

# This will download URL provided to command
def downloadVideoUrl(stream, ytUrl, path):
    try:  # Always download video in highest resolution
        stream = yt.streams.first()
    except Exception as exc:
        print(exc)

    print("downloading", yt.title + " Video and Audio...")
    try:
        stream.download(path, yt.title)
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    default_output_dir = '/onepanel/output/'
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('USAGE: python ytVidDloaderL.py YoutubeURL OR python ytPlaylistDL.py YoutubeURL destPath')
        exit()
    else:
        ytUrl = sys.argv[1]
        yt = YouTube(ytUrl, on_progress_callback=print_progress)
        directory = default_output_dir if len(sys.argv) != 3 else sys.argv[2]
        confirmURL(ytUrl)
    
    if not ytUrl.startswith("http"):
        ytUrl = 'https://' + ytUrl

    # make directory if dir specified doesn't exist
    try:
        os.makedirs(directory, exist_ok=True)
        downloadVideoUrl(yt, ytUrl, directory)
    except OSError as e:
        print(e)
        exit()
