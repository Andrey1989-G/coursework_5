from flask_sqlalchemy import SQLAlchemy

from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)
