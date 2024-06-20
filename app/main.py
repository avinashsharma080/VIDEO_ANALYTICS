from app import app, db
from app.scheduler import run_scheduler
from flask import jsonify
import logging

logging.basicConfig(level=logging.INFO)

@app.route('/videos', methods=['GET'])
def get_videos():
    try:
        videos = Video.query.all()
        return jsonify([video.to_dict() for video in videos])
    except Exception as e:
        app.logger.error(f"Error fetching videos: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/insights', methods=['GET'])
def get_insights():
    try:
        insights = VideoInsight.query.all()
        return jsonify([insight.to_dict() for insight in insights])
    except Exception as e:
        app.logger.error(f"Error fetching insights: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    try:
        with app.app_context():
            db.create_all()
            run_scheduler()
        app.run(debug=True)
    except Exception as e:
        app.logger.error(f"Error starting the application: {e}")
