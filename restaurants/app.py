import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db
from sqlalchemy import text

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
        sql = text('''SELECT r.restaurant_id, r.name, g.grade,g.mostrecent
                    FROM restaurants r
                    LEFT JOIN (
                        SELECT i.restaurant_id, i.grade, MAX(i.inspection_date) AS mostrecent
                        FROM inspections i
                        WHERE i.grade in ('A','B')
                        GROUP BY i.restaurant_id, i.grade
                    ) g ON r.restaurant_id = g.restaurant_id
                    WHERE r.cuisine_desc='Thai';''')
        thai_restaurants = db.engine.execute(sql)
        return_json = "restaurant_id': {}, 'name': {}, 'grade': {}, 'most_recent_inspect_date': {}"
        return jsonify([return_json.format(r[0],r[1],r[2],r[3]) for r in thai_restaurants])
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()
