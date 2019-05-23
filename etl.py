import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from models import RestaurantInspections, Restaurants, Inspections


DATABASE_URL = os.environ['DATABASE_URL']


# Read in data
url = "https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD"
rest_insp_df = pd.read_csv(url)


restaurant_cols = ["CAMIS", "DBA", "BORO", "BUILDING", "STREET", "ZIPCODE",
                    "PHONE", "CUISINE DESCRIPTION"]
inspection_cols = ["CAMIS","INSPECTION DATE", "ACTION", "VIOLATION CODE", "VIOLATION DESCRIPTION",
                    "CRITICAL FLAG", "SCORE", "GRADE", "GRADE DATE", "RECORD DATE", "INSPECTION TYPE"]

restaurants_df = rest_insp_df[restaurant_cols].drop_duplicates()
dup_ids = set(restaurants_df.groupby(['CAMIS']).filter(lambda x: len(x) > 1).index)
restaurants_df = restaurants_df.drop(dup_ids.pop(), axis=0).fillna('')

inspection_df = rest_insp_df[inspection_cols]
inspection_df = inspection_df.drop_duplicates().fillna('')


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

ids_dict = {}

for index, line in restaurants_df.iterrows():
    if line['CAMIS'] in ids_dict.keys() or index == 0:
        pass
    else:
        row = {}
        row['restaurant_id'] = line['CAMIS']
        row['name'] = line['DBA']
        row['boro'] = line['BORO']
        row['building'] = line['BUILDING']
        row['street'] = line['STREET']
        row['zipcode'] = line['ZIPCODE']
        row['phone'] = line['PHONE']
        row['cuisine_desc'] = line['CUISINE DESCRIPTION']
        restaurant = Restaurants(**row)
        ids_dict[line['CAMIS']] = 1
        session.add(restaurant)

for index, line in inspection_df.iterrows():
    if index is not 0:
        row = {}
        row['restaurant_id'] = line['CAMIS']
        row['inspection_date'] = line['INSPECTION DATE']
        row['action'] = str(line['ACTION'])
        row['violation_code'] = str(line['VIOLATION CODE'])
        row['violation_desc'] = str(line['VIOLATION DESCRIPTION'])
        row['critical_flag'] = str(line['CRITICAL FLAG'])
        row['score'] = str(line['SCORE'])
        row['grade'] = str(line['GRADE'])
        row['grade_date'] = str(line['GRADE DATE'])
        row['record_date'] = line['RECORD DATE']
        row['inspection_type'] = str(line['INSPECTION TYPE'])
        inspection = Inspections(**row)
        session.add(inspection)

session.commit()
session.close()
