from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)

from app import models

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500
