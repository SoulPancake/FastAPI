from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randint, randrange


app=FastAPI()


my_posts=[{"title":"Title of 1st post","content":"Content of 1st post","id":1},
          {"title":"My favourite food","content":"I love Nachos","id":2}]

class Post(BaseModel):
    title:str
    content:str    
    id:Optional[int]=None


@app.get("/")
def root():
    return {"message": "Hey There! Welcome to the API!"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def create_post(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,10000000)
    my_posts.append(post_dict)
    
    return {"New post":post_dict}