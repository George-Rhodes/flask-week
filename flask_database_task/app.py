from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://dev@ops@35.246.125.154/flask_db"


db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)

