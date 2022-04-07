from importlib import import_module
from multiprocessing.spawn import import_main_path
from turtle import title
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

@app.get("/")
def get_posts():
    return {"data": "Welcome"}



@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}



@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.dict())
    return {"message" : "New post added"}
