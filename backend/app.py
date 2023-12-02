from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from API.models import db
from API.routes import api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api)
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)