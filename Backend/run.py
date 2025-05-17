from flask import Flask
from flask_cors import CORS
from routes.ping_routes import ping_bp
from database import db
from config import Config

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(ping_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(meeting_bp)

if __name__ == "__main__":
    app.run(debug=True)