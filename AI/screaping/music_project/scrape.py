import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://charts.youtube.com/charts/TopSongs/uz"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

songs = []

rows = soup.select("ytmc-entry-row")

for row in rows:
    rank = row.select_one("span.rank").text.strip()
    song = row.select_one("span.title").text.strip()
    artist = row.select_one("span.artist").text.strip()

    songs.append({
        "Rank": rank,
        "Song": song,
        "Artist": artist
    })

df = pd.DataFrame(songs)

print(df.head())
