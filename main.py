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
    return -1        

def deletePost(id):
    for i,p in enumerate(my_posts):
        if p["id"]==id:
          my_posts.pop(i)
          return "Post Successfully Deleted"
    return f"Post with ID {id} not found"  
       
    
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

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,10000000)
    my_posts.append(post_dict)
    
    return {"New post":post_dict}




#Retrieving a singular post
@app.get("/posts/{id}")
def get_post(id : int):
    post=findPost(id)
    if post==-1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} was not found")
    return {"post_detail": post }

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post=deletePost(id)
    if post==f"Post with ID {id} not found":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=post)
    return {"post_detail": post }    






#Finally implemented a successful delete operation by id
# Now the standard for a successful deletion is 204
#So we need to update the default status code of our delete operation using
#the decorator


# https://youtu.be/0sOvCWFmrtA?t=7403
# fEELING EXTREMELY TIRED WILL implement the delete Post later
#Let's do that to the create posts
#Just add a 201 to the decorator itself
#Now the HTTP Error things is fixed
#However even for successful tasks there are defined HTTP responses
#Such as we should a get a 201 for a successful creation
#Let's see how to do that 

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