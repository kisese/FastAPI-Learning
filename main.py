from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"data": "Index"}


#  uery params
@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published Blogs from the db"}
    else:
        return {"data": f"{limit} Blogs from the db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id ~> id
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    # fetch commeents of blog with id
    return {"data": {"1", "2", "3"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {"data": f"Post created with title as {request.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port="9000")
