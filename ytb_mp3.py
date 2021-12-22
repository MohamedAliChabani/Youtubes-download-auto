from selenium import webdriver
import yt_dlp

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

filename = 'songs.txt'


def get_url(song):
    formatted_song_name = ""

    for i in song.split(" "):
        formatted_song_name += f'{i}+'

    formatted_song_name = formatted_song_name[:len(formatted_song_name)-1]


    driver.get(f"https://www.youtube.com/results?search_query={formatted_song_name}")
    driver.find_element_by_id("video-title").click()
    url = driver.current_url
    return url


def download(url):
    video_info = yt_dlp.YoutubeDL().extract_info(
        url = url,download=False
    )
    filename = video_info['title']
    options={
        'format':'bestaudio/mp3',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))


with open('songs.txt', 'r') as file:
    for song in file.readlines():
        song = song[:len(song)-1]
        url = get_url(song)
        download(url)
