import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()
cursor.execute("""
COPY restaurant_inspections(restaurant_id,name,boro,building,street,zipcode,phone,cuisine_desc,inspection_date,action,violation_code,violation_desc,critical_flag,score,grade,grade_date,record_date,inspection_type)
FROM PROGRAM 'curl "https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD"'
WITH CSV HEADER NULL AS ''
""")


print("Connected!")
