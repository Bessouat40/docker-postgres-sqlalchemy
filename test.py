from sqlalchemy import create_engine, insert, text
import time

time.sleep(7)

engine = create_engine("postgresql+psycopg2://postgres:postgres@db:5432/medicalDB")
conn = engine.connect()
conn.execute(text("INSERT INTO medicalTable (nom_patient, diagnostic) VALUES ('spongebob', 'pneumonia');"))
