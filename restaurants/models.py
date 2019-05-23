from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class RestaurantInspections(db.Model):
    __tablename__= 'restaurant_inspections'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer)
    name = db.Column(db.String(), nullable=True)
    boro = db.Column(db.String())
    building = db.Column(db.String(), nullable=True)
    street = db.Column(db.String(), nullable=True)
    zipcode = db.Column(db.String(), nullable=True)
    phone = db.Column(db.String(), nullable=True)
    cuisine_desc = db.Column(db.String())
    inspection_date = db.Column(db.String())
    action = db.Column(db.String(), nullable=True)
    violation_code = db.Column(db.String(), nullable=True)
    violation_desc = db.Column(db.String(), nullable=True)
    critical_flag = db.Column(db.String())
    score = db.Column(db.String(), nullable=True)
    grade = db.Column(db.String(), nullable=True)
    grade_date = db.Column(db.String(), nullable=True)
    record_date = db.Column(db.Date())
    inspection_type = db.Column(db.String(), nullable=True)

    def __init__(self, restaurant_id, name, boro, building, street, zipcode,
                    phone, cuisine_desc, inspection_date, action, violation_code,
                    violation_desc, critical_flag, score, grade, grade_date,
                    record_date, inspection_type):
        self.restaurant_id = restaurant_id
        self.name = name
        self.boro = boro
        self.building = building
        self.street = street
        self.zipcode = zipcode
        self.phone = phone
        self.cuisine_desc = cuisine_desc
        self.inspection_date = inspection_date
        self.action = action
        self.violation_code = violation_code
        self.violation_desc = violation_desc
        self.critical_flag = critical_flag
        self.score = score
        self.grade = grade
        self.grade_date = grade_date
        self.record_date = record_date
        self.inspection_type = inspection_type


class Restaurants(db.Model):
    __tablename__ = 'restaurants'
    restaurant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    boro = db.Column(db.String())
    building = db.Column(db.String())
    street = db.Column(db.String())
    zipcode = db.Column(db.String())
    phone = db.Column(db.String())
    cuisine_desc = db.Column(db.String())

    def __init__(self,restaurant_id, name, boro, building, street, zipcode, phone, cuisine_desc):
        self.restaurant_id = restaurant_id
        self.name = name
        self.boro = boro
        self.building = building
        self.street = street
        self.zipcode = zipcode
        self.phone = phone
        self.cuisine_desc = cuisine_desc

    def __repr__(self):
        return '<restaurant_id {}>'.format(self.restaurant_id)

    def to_json(self):
        return {
            'restaurant_id': self.restaurant_id,
            'name': self.name,
            'boro': self.boro,
            'building': self.building,
            'street': self.street,
            'zipcode': self.zipcode,
            'phone': self.phone,
            'cuisine_desc': self.cuisine_desc
        }


class Inspections(db.Model):
    __tablename__ = 'inspections'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))
    inspection_date = db.Column(db.Date())
    action = db.Column(db.String())
    violation_code = db.Column(db.String())
    violation_desc = db.Column(db.String())
    critical_flag = db.Column(db.String())
    score = db.Column(db.String())
    grade = db.Column(db.String())
    grade_date = db.Column(db.String())
    record_date = db.Column(db.Date())
    inspection_type = db.Column(db.String())

    def __init__(self, restaurant_id, inspection_date, action, violation_code, violation_desc, critical_flag, score, grade, grade_date, record_date, inspection_type):
        self.restaurant_id = restaurant_id
        self.inspection_date = inspection_date
        self.action = action
        self.violation_code = violation_code
        self.violation_desc = violation_desc
        self.critical_flag = critical_flag
        self.score = score
        self.grade = grade
        self.grade_date = grade_date
        self.record_date = record_date
        self.inspection_type = inspection_type

    def __repr__(self):
        return '<restaurant_id {}>'.format(self.restaurant_id)

    def to_json(self):
        return {
            'restaurant_id': self.restaurant_id,
            'inspection_date': self.inspection_date,
            'action': self.action,
            'violation_code': self.violation_code,
            'violation_desc': self.violation_desc,
            'critical_flag': self.critical_flag,
            'score': self.score,
            'grade': self.grade,
            'grade_date': self.grade_date,
            'record_date': self.record_date,
            'inspection_type': self.inspection_type
        }
