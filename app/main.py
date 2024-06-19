from app import app, db
from app.scheduler import run_scheduler

if __name__ == "__main__":
    db.create_all()
    run_scheduler()
