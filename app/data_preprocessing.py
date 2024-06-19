from collections import Counter
import nltk
from nltk.corpus import stopwords
from app.models import Video, VideoInsight
from app import db

nltk.download('stopwords')
nltk.download('punkt')

def calculate_view_trends(videos):
    trends = {}
    for video in videos:
        trends[video['id']] = video['view_count']
    return trends

def extract_keywords(videos):
    stop_words = set(stopwords.words('english'))
    all_words = []
    for video in videos:
        words = nltk.word_tokenize(video['title'] + ' ' + video['description'])
        words = [word.lower() for word in words if word.isalnum()]
        all_words.extend([word for word in words if word not in stop_words])
    return Counter(all_words).most_common(10)

def analyze_engagement(videos):
    engagement = {}
    for video in videos:
        engagement[video['id']] = {
            'likes': video['like_count'],
            'comments': video['comment_count']
        }
    return engagement

def process_and_store_video_data(videos):
    trends = calculate_view_trends(videos)
    keywords = extract_keywords(videos)
    engagement = analyze_engagement(videos)

    for video in videos:
        db_video = Video(**video)
        db.session.add(db_video)

        db_insight = VideoInsight(
            id=video['id'],
            view_trend=trends[video['id']],
            top_keywords=', '.join([k for k, v in keywords]),
            engagement_rate=(int(video['like_count']) + int(video['comment_count'])) / int(video['view_count'])
        )
        db.session.add(db_insight)
    db.session.commit()
