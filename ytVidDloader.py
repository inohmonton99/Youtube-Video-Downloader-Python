import os
import sys
from pytube import YouTube
import logging
from tqdm import tqdm

# os.makedir('./logs', exist_ok=True)
# logging.basicConfig(filename="./logs/ytDownload.log", level=logging.DEBUG, format="%(levelname)s - %(message)s")


# Confirms if feeded URL is Youtube
def confirmURL(ytUrl):
    if 'youtube' not in ytUrl.lower():
        print("Please use youtube URL")
        exit()


def progressBar(stream):
    for i in tqdm(range(stream.filesize)):
        pass


# This will download URL provided to command
def downloadVideoUrl(stream, path):
    try:  # Always download video in highest resolution
        stream = yt.streams.filter(file_extension='mp4').first()
    except Exception as exc:
        print(exc)

    print("downloading", yt.title + " Video and Audio...")
    try:
        stream.download(path, yt.title)
        progressBar(stream)
        print("files downloaded to {}".format(os.path.abspath(path)))
    except Exception as exc:
        print(exc)


def downloadAudio(stream, path):
    try:  # Always download audio in highest resolution
        stream = yt.streams.filter(only_audio=True).first()
    except Exception as exc:
        print(exc)

    print("downloading", yt.title + " Audio Only...")
    try:
        stream.download(path, yt.title + "_audio")
        progressBar(stream)
        print("{} downloaded to {}".format(yt.title, os.path.abspath(path)))
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    default_output_dir = '/onepanel/output/'
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('USAGE: python ytVidDloaderL.py YoutubeURL OR python ytPlaylistDL.py YoutubeURL destPath')
        exit()
    else:
        ytUrl = sys.argv[1]
        yt = YouTube(ytUrl)
        directory = default_output_dir
        confirmURL(ytUrl)

    if not ytUrl.startswith("http"):
        ytUrl = 'https://' + ytUrl

    try:
        # make directory if dir specified doesn't exist
        os.makedirs(directory, exist_ok=True)
        downloadVideoUrl(yt, directory)
        downloadAudio(yt, directory)

    except OSError as e:
        print(e)
        exit()
