from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randint, randrange


app=FastAPI()


my_posts=[{"title":"Title of 1st post","content":"Content of 1st post","id":1},
          {"title":"My favourite food","content":"I love Nachos","id":2}]




def findPost(id):
    for p in my_posts:
        if p["id"]==id:
          return p
        else:
            continue  
    return "404 : Post Not Found"
    
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


@app.get("/posts/latest")
def get_latest_post():
    return {"latest Post" : my_posts[len(my_posts)-1]}

#Retrieving a singular post
@app.get("/posts/{id}")
def get_post(id : int):
    print("id = ",id)
    return {"post_detail": findPost(id)}





#This is where order matters!


#Now I'll write a decorator and a path 
#That would retrieve the latest post for me

# Whenever we have a path parameter it will always be returned
# as as string
# so Make sure to typecast it before you use integral comparisions on it

#If we get a string passed and it cannot be converted to an integer
#By Itself then we use FastAPI to validate it for us
#And If possible it will convert it to an integer