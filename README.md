# Music Downloader (Modified by Renny Yo, 2025.4)

A Python script that uses Selenium to search for music on YouTube and downloads it using `yt_dlp`.
The downloaded music files are saved in MP3 format with the best audio quality.

## Prerequisites

Before running the script, you need to install the following dependencies:

- [Selenium](https://pypi.org/project/selenium/)
- [yt-dlp](https://pypi.org/project/yt-dlp/)
- [FFmpeg](https://ffmpeg.org/)

You can install the dependencies using the following commands:

```bash
pip install selenium
pip install yt_dlp
pip install ffmpeg
```
or

```bash
pip install selenium yt_dlp ffmpeg
```

## Execute steps on MacOS
1.Open Terminal

2.Navigate to your project directory
```bash
cd /path/to/your/project
```
3.Create the virtual environment
```bash
python3 -m venv myenv
```
4.Activate the virtual environment
```bash
source myenv/bin/activate
```
5.Install dependencies
```bash
pip install selenium yt_dlp ffmpeg
```
6.Execute
```bash
python3 Music_Downloader_RY_202504.py
```
7.Insert song name and see if it has been downloaded

8.Deactivate the virtual environment
```bash
deactivate
```