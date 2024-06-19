from app import db

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    view_count = db.Column(db.Integer)
    like_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    published_at = db.Column(db.DateTime)

class VideoInsight(db.Model):
    __tablename__ = 'video_insights'
    id = db.Column(db.String, primary_key=True)
    view_trend = db.Column(db.Integer)
    top_keywords = db.Column(db.String)
    engagement_rate = db.Column(db.Float)
