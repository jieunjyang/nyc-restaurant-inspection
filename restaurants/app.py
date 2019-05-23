import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db


app = Flask(__name__)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


from models import Restaurants, Inspections


@app.route("/")
def hello():
    return "Hello World."

@app.route("/get_all", methods=['GET'])
def get_restaurant_list():
    try:
        # Restaurants: restaurant_id, name, cuisine_desc
        # Inspections:
        #
        #result = db.engine.execute("SELECT ")
        thai_food = Restaurants.query.filter_by(cuisine_desc='Thai').all()
        print(thai_food)
        return jsonify(thai_food.to_json())
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()
