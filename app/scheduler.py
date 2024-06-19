import schedule
import time
from app.youtube_api import fetch_video_details
from app.data_processing import process_and_store_video_data

def update_data():
    channel_ids = ['UC_x5XG1OV2P6uZZ5FSM9Ttw']  # Replace with actual channel IDs
    videos = fetch_video_details(channel_ids)
    process_and_store_video_data(videos)

# Schedule the update_data function to run every hour
schedule.every().hour.do(update_data)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
