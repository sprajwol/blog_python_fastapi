import psycopg2
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor

DB_CONNECTION_STRING = "postgresql://postgres:postgres@localhost/fastapi"

engine = create_engine(DB_CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connection was successful.")
#         break
#     except Exception as error:
#         # time.sleep(2)
#         print("Connecting to database failed.")
#         print(f"Error: {error}")