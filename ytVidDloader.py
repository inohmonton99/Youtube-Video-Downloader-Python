import os
import sys
from pytube import YouTube
import logging

os.makedirs('./logs', exist_ok=True)
logging.basicConfig(filename="./logs/ytDownload.log", level=logging.DEBUG, format="%(levelname)s - %(message)s")


# Confirms if feeded URL is Youtube
def confirmURL(ytUrl):
    if 'youtube' not in ytUrl.lower():
        print("Please use a youtube URL")
        exit()

# This will download URL provided to command
def downloadVideoUrl(ytUrl, path):
    yt = YouTube(ytUrl)
    try:  # Always download video in highest resolution
        stream = yt.streams.first()
    except Exception as exc:
        print(exc)

    print("downloading", yt.title + " Video and Audio...")
    try:
        # bar = progressBar()
        stream.download(path, yt.title)
        print("successfully downloaded", yt.title, "!")
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('USAGE: python ytVidDloaderL.py YoutubeURL OR python ytPlaylistDL.py YoutubeURL destPath')
        exit()
    else:
        ytUrl = sys.argv[1]
        directory = os.getcwd() if len(sys.argv) != 3 else sys.argv[2]

        # make directory if dir specified doesn't exist
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as e:
            print(e)
            exit()

        if not ytUrl.startswith("http"):
            ytUrl = 'https://' + ytUrl

        confirmURL(ytUrl)
        downloadVideoUrl(ytUrl, directory)
