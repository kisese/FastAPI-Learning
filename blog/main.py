from fastapi import FastAPI
from . import schemas

app = FastAPI()


@app.post('/blog')
def create_blog(request: schemas.Blog):
    return request
