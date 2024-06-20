import schedule
import time
from app.youtube_api import fetch_video_details
from app.data_processing import process_and_store_video_data
from app import app
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_data():
    try:
        with app.app_context():
            channel_ids = ['UC_x5XG1OV2P6uZZ5FSM9Ttw']  # Replace with actual channel IDs
            videos = fetch_video_details(channel_ids)
            process_and_store_video_data(videos)
    except Exception as e:
        logger.error(f"Error updating data: {e}")

# Schedule the update_data function to run every hour
schedule.every().hour.do(update_data)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
