from app import app, db
from app.scheduler import run_scheduler
from flask import jsonify

@app.route('/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    return jsonify([video.to_dict() for video in videos])

@app.route('/insights', methods=['GET'])
def get_insights():
    insights = VideoInsight.query.all()
    return jsonify([insight.to_dict() for insight in insights])

if __name__ == "__main__":
    db.create_all()
    run_scheduler()
    app.run(debug=True)
