import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/youtube_analytics')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'YOUR_API_KEY')
    YOUTUBE_API_URL = os.getenv('YOUTUBE_API_URL', 'https://www.googleapis.com/youtube/v3')
