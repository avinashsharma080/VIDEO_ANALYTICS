import requests
from app.config import Config

def fetch_video_details(channel_ids):
    video_details = []
    for channel_id in channel_ids:
        url = f"{Config.YOUTUBE_API_URL}/search"
        params = {
            'part': 'snippet',
            'channelId': channel_id,
            'maxResults': 50,
            'order': 'date',
            'key': Config.YOUTUBE_API_KEY
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        for item in response.json().get('items', []):
            video_id = item['id']['videoId']
            video_data = fetch_video_data(video_id)
            video_details.append(video_data)
    return video_details

def fetch_video_data(video_id):
    url = f"{Config.YOUTUBE_API_URL}/videos"
    params = {
        'part': 'snippet,statistics',
        'id': video_id,
        'key': Config.YOUTUBE_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    video = response.json().get('items', [])[0]
    video_data = {
        'id': video['id'],
        'title': video['snippet']['title'],
        'description': video['snippet']['description'],
        'view_count': video['statistics']['viewCount'],
        'like_count': video['statistics']['likeCount'],
        'comment_count': video['statistics']['commentCount'],
        'published_at': video['snippet']['publishedAt']
    }
    return video_data
