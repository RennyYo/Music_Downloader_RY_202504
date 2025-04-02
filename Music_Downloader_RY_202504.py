### Music_Downloader_RY_202504

# Install below git first
    # pip install selenium
    # pip install yt_dlp
    # pip install ffmpeg

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import yt_dlp
import time
import re


class MusicDownloader:
    def __init__(self):
        # Set Chrome browser
        chrome_options = webdriver.ChromeOptions()
        # Disable Chrome notifications
        chrome_options.add_argument("--disable-notifications")  
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        # Maximize browser Window
        self.driver.maximize_window()

    # remove prohibited symbols
    def clean_filename(self, filename):
        return re.sub(r'[\\/*?:"<>|]', '', filename)
    
    # Search and download music on Youtube according to inserted song name
    def download_music(self, search_query):
        # Open YouTube
        self.driver.get("https://www.youtube.com")  

        try:
            #Wait for input box
            wait = WebDriverWait(self.driver, 10)
            search_input = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))

            # Separate multiple songs by commas and remove any whitespace
            songs = [song.strip() for song in search_query.split(",")]  

            # Iterate through each song to search and download
            for song in songs:
                # Clear input box
                search_input.clear()
                # Insert song name and press ENTER
                search_input.send_keys(song + Keys.ENTER)
                # Wait
                time.sleep(5)
                
                # Obtain video link
                video_links = self.driver.find_elements(By.XPATH, "//a[@id='video-title']")
                
                if video_links:
                    # Obtain the first video
                    href = video_links[0].get_attribute("href")
                    
                    # Set yt-dlp download options
                    ydl_opts = {
                        # Download with the best sound quality
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        # Set path and format of file name
                        'outtmpl': 'Downloaded_Music/%(title)s.%(ext)s',
                    }
                    
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        # Download music
                        ydl.download([href])
                else:
                    # If failed to find music
                    print(f"未找到歌曲：{song}")
        
        # Get exceptions and output error messages
        except Exception as e:
            print(f"發生錯誤：{e}")  
    
    # Close WebDriver
    def close_driver(self):
        self.driver.quit()


if __name__ == "__main__":
    # Execute MusicDownloader
    downloader = MusicDownloader()
    # Insert music name
    search_query = input("請輸入要下載的音樂，多首歌曲請以逗號分隔：")  
    # Download music file
    downloader.download_music(search_query)  
    # Close browser
    downloader.close_driver()