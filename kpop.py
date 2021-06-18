import random
import urllib.request
import json
import os


def get_random_kpop_video():
    """This function returns a YouTube URL for a random kpop video"""

    youtube_token = os.getenv('YOUTOKEN')
    API_KEY = youtube_token
    count = 100
    search_term = 'kpop+new'
    video_ids = []

    url_data = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(
        API_KEY, count, search_term)

    web_url = urllib.request.urlopen(url_data)
    data = web_url.read()
    encoding = web_url.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    for data in results['items']:
        video_id = (data['id']['video_id'])
        # print(video_id)
        video_ids.append(video_id)

    video_url = "https://youtu.be/" + random.choice(video_ids)
    # print(video_url)
    return video_url
