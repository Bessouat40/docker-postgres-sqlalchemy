from sqlalchemy import create_engine, insert, text
import time

time.sleep(7)

engine = create_engine("postgresql+psycopg2://postgres:postgres@db:5432/medicalDB")
conn = engine.connect()
query="INSERT INTO  medicalTable (nom_patient, diagnostic)  VALUES(%s,%s)"
my_data=[('Michel', 'normal'),
        ('Gerard', 'normal'),]
id=conn.execute(query,my_data)
