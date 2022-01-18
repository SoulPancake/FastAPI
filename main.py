from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
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




#Retrieving a singular post
@app.get("/posts/{id}")
def get_post(id : int):
    post=findPost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} was not found")
    return {"post_detail": post }



#This is a cool way
#But a better way is just throwing a FastAPI HTTP Exception


#Instead of remembering which HTTP code to use
#We can use a FastAPI library called status

#This is where order matters!


#Now I'll write a decorator and a path 
#That would retrieve the latest post for me

# Whenever we have a path parameter it will always be returned
# as as string
# so Make sure to typecast it before you use integral comparisions on it

#If we get a string passed and it cannot be converted to an integer
#By Itself then we use FastAPI to validate it for us
#And If possible it will convert it to an integer