from collections import Counter
import nltk
from nltk.corpus import stopwords
from app.models import Video, VideoInsight
from app import db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

nltk.download('stopwords')
nltk.download('punkt')

def calculate_view_trends(videos):
    try:
        trends = {}
        for video in videos:
            trends[video['id']] = video['view_count']
        return trends
    except Exception as e:
        logger.error(f"Error calculating view trends: {e}")
        return {}

def extract_keywords(videos):
    try:
        stop_words = set(stopwords.words('english'))
        all_words = []
        for video in videos:
            words = nltk.word_tokenize(video['title'] + ' ' + video['description'])
            words = [word.lower() for word in words if word.isalnum()]
            all_words.extend([word for word in words if word not in stop_words])
        return Counter(all_words).most_common(10)
    except Exception as e:
        logger.error(f"Error extracting keywords: {e}")
        return []

def analyze_engagement(videos):
    try:
        engagement = {}
        for video in videos:
            engagement[video['id']] = {
                'likes': video['like_count'],
                'comments': video['comment_count']
            }
        return engagement
    except Exception as e:
        logger.error(f"Error analyzing engagement: {e}")
        return {}

def process_and_store_video_data(videos):
    try:
        trends = calculate_view_trends(videos)
        keywords = extract_keywords(videos)
        engagement = analyze_engagement(videos)

        for video in videos:
            if video is None:
                continue
            db_video = Video(**video)
            db.session.add(db_video)

            db_insight = VideoInsight(
                id=video['id'],
                view_trend=trends.get(video['id'], 0),
                top_keywords=', '.join([k for k, v in keywords]),
                engagement_rate=(int(video['like_count']) + int(video['comment_count'])) / int(video['view_count'])
            )
            db.session.add(db_insight)
        db.session.commit()
    except Exception as e:
        logger.error(f"Error processing and storing video data: {e}")
        db.session.rollback()
