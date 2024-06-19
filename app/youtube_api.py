from googleapiclient.discovery import build
from app.config import Config

def get_youtube_service():
    return build('youtube', 'v3', developerKey=Config.YOUTUBE_API_KEY)

def fetch_video_details(channel_ids):
    youtube = get_youtube_service()
    video_details = []
    for channel_id in channel_ids:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=50,
            order='date'
        )
        response = request.execute()
        for item in response['items']:
            video_id = item['id']['videoId']
            video_data = fetch_video_data(video_id)
            video_details.append(video_data)
    return video_details

def fetch_video_data(video_id):
    youtube = get_youtube_service()
    request = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    )
    response = request.execute()
    video = response['items'][0]
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
