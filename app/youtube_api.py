import requests
from app.config import Config
import logging
from ratelimit import limits, sleep_and_retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Assume the YouTube Data API has a quota of 10,000 units per day
# We can split this into a per-minute limit for simplicity, e.g., 100 units per minute
API_CALLS_PER_MINUTE = 100

@sleep_and_retry
@limits(calls=API_CALLS_PER_MINUTE, period=60)
def make_request(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response

def fetch_video_details(channel_ids):
    video_details = []
    for channel_id in channel_ids:
        try:
            url = f"{Config.YOUTUBE_API_URL}/search"
            params = {
                'part': 'snippet',
                'channelId': channel_id,
                'maxResults': 50,
                'order': 'date',
                'key': Config.YOUTUBE_API_KEY
            }
            response = make_request(url, params)
            for item in response.json().get('items', []):
                video_id = item['id']['videoId']
                video_data = fetch_video_data(video_id)
                if video_data:
                    video_details.append(video_data)
        except requests.RequestException as e:
            logger.error(f"Error fetching video details for channel {channel_id}: {e}")
    return video_details

def fetch_video_data(video_id):
    try:
        url = f"{Config.YOUTUBE_API_URL}/videos"
        params = {
            'part': 'snippet,statistics',
            'id': video_id,
            'key': Config.YOUTUBE_API_KEY
        }
        response = make_request(url, params)
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
    except requests.RequestException as e:
        logger.error(f"Error fetching video data for video {video_id}: {e}")
        return None
    except IndexError:
        logger.error(f"No data found for video {video_id}")
        return None
