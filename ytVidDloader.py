import os
import sys
import time
from pytube import YouTube
import logging

os.makedirs('./logs', exist_ok=True)
logging.basicConfig(filename="./logs/ytDownload.log", level=logging.DEBUG, format="%(levelname)s - %(message)s")

'''
class progressBar:
    def __init__(self, barlength=25):
        self.barLength = barlength
        self.position = 0
        self.longest = 0

    def print_progress(self, cur, total, start):
        currentPer = cur / total
        elapsed = int(time.clock() - start) + 1
        curBar = int(currentPer * self.barLength)
        bar = '\r[' + '='.join(['' for _ in range(curBar)])  # Draws Progress
        bar += '>'
        bar += ' '.join(['' for _ in range(int(self.barLength - curBar))]) + '] '  # Pads remaining space
        bar += bytesToSTR(cur / elapsed) + '/s '  # Calculates Rate
        bar += getHumanTime((total - cur) * (elapsed / cur)) + ' left'  # Calculates Remaining time
        if len(bar) > self.longest:  # Keeps track of space to over write
            self.longest = len(bar)
            bar += ' '.join(['' for _ in range(self.longest - len(bar))])
        sys.stdout.write(bar)

    def print_end(self, *args):  # Clears Progress Bar
        sys.stdout.write('\r{0}\r'.format((' ' for _ in range(self.longest))))


def getHumanTime(sec):
    if sec >= 3600:  # Converts to Hours
        return '{0:d} hour(s)'.format(int(sec / 3600))
    elif sec >= 60:  # Converts to Minutes
        return '{0:d} minute(s)'.format(int(sec / 60))
    else:  # No Conversion
        return '{0:d} second(s)'.format(int(sec))


def bytesToSTR(bts):
    bts = float(bts)
    if bts >= 1024 ** 4:  # Converts to Terabytes
        terabytes = bts / 1024 ** 4
        size = '%.2fTb' % terabytes
    elif bts >= 1024 ** 3:  # Converts to Gigabytes
        gigabytes = bts / 1024 ** 3
        size = '%.2fGb' % gigabytes
    elif bts >= 1024 ** 2:  # Converts to Megabytes
        megabytes = bts / 1024 ** 2
        size = '%.2fMb' % megabytes
    elif bts >= 1024:  # Converts to Kilobytes
        kilobytes = bts / 1024
        size = '%.2fKb' % kilobytes
    else:  # No Conversion
        size = '%.2fb' % bts
    return size
'''

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
