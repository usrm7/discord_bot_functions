def get_random_kpop_video():
    """This function returns a YouTube URL for a random kpop video"""

    youtube_token = os.getenv('YOUTOKEN')
    API_KEY = youtube_token
    count = 100
    search_term = 'kpop+new'
    video_ids = []

    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(
        API_KEY, count, search_term)

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    for data in results['items']:
        videoId = (data['id']['videoId'])
        #print(videoId)
        video_ids.append(videoId)

    video_url = "https://youtu.be/" + random.choice(video_ids)
    #print(video_url)
    return video_url
