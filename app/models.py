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

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'view_count': self.view_count,
            'like_count': self.like_count,
            'comment_count': self.comment_count,
            'published_at': self.published_at
        }

class VideoInsight(db.Model):
    __tablename__ = 'video_insights'
    id = db.Column(db.String, primary_key=True)
    view_trend = db.Column(db.Integer)
    top_keywords = db.Column(db.String)
    engagement_rate = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'view_trend': self.view_trend,
            'top_keywords': self.top_keywords,
            'engagement_rate': self.engagement_rate
        }
