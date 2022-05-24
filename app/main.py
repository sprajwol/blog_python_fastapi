import psycopg2
from fastapi import FastAPI, APIRouter
from random import randrange
from psycopg2.extras import RealDictCursor

from app.database import engine
from app import models
from app.routers import post, user


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency


# requests GET method url: "/"


while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection was successful.")
        break
    except Exception as error:
        # time.sleep(2)
        print("Connecting to database failed.")
        print(f"Error: {error}")

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2}
]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)


@app.get('/')
def root():
    return {"message": "Hello World"}
