from __future__ import unicode_literals
import json
import argparse
import youtube_dl
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def init_args():
    parser = argparse.ArgumentParser(description='Download exported spotify playlist to mp3s from youtube, see github readme for instructions')
    parser.add_argument('--output_dir', metavar='o', help='Downloaded songs output directory')
    parser.add_argument('--input_path', metavar='i', help='Songs json path')
    return parser.parse_args()

def run(args):
    with open(args.input_path, encoding='utf-8') as songs_json:
        parsed_songs = json.load(songs_json)
        song_count = len(parsed_songs["songs"])
        print(f'Loaded {song_count} songs from input json')
        for index, song in enumerate(parsed_songs['songs']):
            print(f'Downloading song {index}/{song_count}: {song}')

            link = find_yt_link(song)
            download_yt_mp3(link, args.output_dir)

def find_yt_link(query):

    words = query.split()
    search_link = 'http://www.youtube.com/results?search_query=' + '+'.join(words)

    session = HTMLSession()
    search_result = session.get(search_link)
    search_result.html.render(timeout=20)

    soup = BeautifulSoup(search_result.html.html, 'lxml')
    videos = soup.find_all('a', class_= 'yt-simple-endpoint style-scope ytd-video-renderer')
    if not videos:
        print(f'No video found for {query}')

    return 'https://www.youtube.com' + videos[0]['href']

def download_yt_mp3(link, output_dir):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == '__main__':
    args = init_args()
    run(args)