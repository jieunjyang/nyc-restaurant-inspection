import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models import db


app = Flask(__name__)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def hello():
    return "Hello World."


if __name__ == '__main__':
    app.run()
