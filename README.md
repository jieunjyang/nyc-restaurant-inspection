# nyc-restaurant-inspection
This is a Flask + PostgreSQL service that is deployed on Heroku. This service can retrieve all restaurant details and all restaurants that have a rating of 'B' or higher in their most recent inspection.

The deployed service can be found here: https://nyc-restaurant-inspection.herokuapp.com/

## Request and Response Examples:
### GET /restaurants
Example: curl https://nyc-restaurant-inspection.herokuapp.com/api/v1/restaurants

### GET /restaurants/[cuisine]
Example: curl https://nyc-restaurant-inspection.herokuapp.com/api/v1/restaurants/Thai

Example: curl https://nyc-restaurant-inspection.herokuapp.com/api/v1/restaurants/Peruvian

For this GET request, I execute the following SQL query:


        SELECT r.restaurant_id, r.name, g.grade,g.mostrecent
        FROM restaurants r
        LEFT JOIN (
                SELECT i.restaurant_id, i.grade, MAX(i.inspection_date)
                AS mostrecent
                FROM inspections i
                WHERE i.grade in ('A','B')
                GROUP BY i.restaurant_id, i.grade
        ) g ON r.restaurant_id = g.restaurant_id
        WHERE r.cuisine_desc='Thai';
	
## Run locally:
1. Git clone the repo into your local environment:

```git clone https://github.com/jieunjyang/nyc-restaurant-inspection.git```

2. Set up virtualenv: 

```virtualenv venv```

```source venv/bin/activate```

```source venv/bin/activate```

```pip install -r requirements.txt```


3. Assuming you already have postgresql installed, set up a db.

``` sudo -u username createdb db_name ```

```python manage.py db init```

```python manage.py db migrate```

```python manage.py db upgrade```

You can load the db by running the etl script:

```python etl.py```

4. Then run the server.

```python manage.py runserver```

## Schema Design:

### restaurants
Field | Type | Description
------|------|---------------
restaurant_id |  Integer | Unique identifer for restaurants, primary key
name | String | Name of the restaurant
boro | String | New York borough
building | String | Address
street | String | Address
zipcode | String | Address
phone | String | phone number
cuisine_desc | String | Cuisine description, categorical

### inspections
Field | Type | Description
------|------|---------------
id | Integer | serial, primary key
restaurant_id |  Integer | Unique identifer for restaurants, foreign key
inspection_date | Date | Date of inspection, not null
action | String | Action description
violation_code | String | categorical
violation_desc | String | Description
critical_flag | String | Critical/Not Critical
score | String | Numerical score
grade | String | Alphabetic score
grade_date | String | Date of grade
record_date | Date | Date of record
inspection_type | String | Initial/Re-Inspection
cuisine_desc | String | Cuisine description, categorical

I decided to normalize the original table to reduce data redundancy. In the original table, for every inspection, the restaurants' demographic information was often repetitive. The demographic data is mostly unique, therefore I thought it made sense to separate it into a different table and connect them using the restaurant_id as the primary key for the restaurants table and foreign key for the inspections table. This makes it easier to see the restaurants as its own entity, with unique information relating to one restaurant, whereas the inspection fields is mostly categorical. I also thought that it was necessary to separate the two entities because I needed to find a way to assign unique identifiers for each record.
