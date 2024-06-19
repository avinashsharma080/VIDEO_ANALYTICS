import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/youtube_analytics')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_KEY = os.getenv('https://www.googleapis.com/youtube/v3', 'AIzaSyAVx43tU_fMN5Sm11Kw9kntO_f8W6waOEQ')
