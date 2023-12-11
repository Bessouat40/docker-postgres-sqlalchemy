from sqlalchemy import create_engine, insert, text
import time

time.sleep(5)

engine = create_engine("postgresql+psycopg2://postgres:postgres@db:5432/DB")
conn = engine.connect()
query=text("INSERT INTO identity (_name, surname) VALUES ('Michel', 'Palefrois'), ('Renaud', 'Bertop');")
conn.execute(query)
conn.commit()

print('done')