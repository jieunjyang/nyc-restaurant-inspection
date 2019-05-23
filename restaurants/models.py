from app import db


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)


class Restaurants(BaseModel, db.Model):
    __tablename__ = 'restaurants'

    restaurant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    boro = db.Column(db.String())
    building = db.Column(db.String())
    street = db.Column(db.String())
    zipcode = db.Column(db.Float())
    phone = db.Column(db.String())
    cuisine_desc = db.Column(db.String())

    def __init__(self, restaurant_id, name, boro, building, street, zipcode, phone, cuisine_desc):
        self.restaurant_id = restaurant_id
        self.name = name
        self.boro = boro
        self.building = building
        self.street = street
        self.zipcode = zipcode
        self.phone = phone
        self.cuisine_desc = cuisine_desc


class Inspections(BaseModel, db.Model):
    __tablename__ = 'inspections'

    restaurant_id = db.Column(db.Integer, foreign_key=True)
    inspection_date = db.Column()
    action = db.Column(db.String())
    violation_code = db.Column(db.String())
    violation_desc = db.Column(db.String())
    critical_flag = db.Column(db.String())
    score = db.Column(db.Float())
    grade = db.Column(db.String())
    grade_date = db.Column()
    record_date = db.Column()
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
