from ast import Raise
from logging import raiseExceptions
from typing import Optional
from xmlrpc.client import boolean
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randint, randrange
import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor
import time
app=FastAPI()

while True:
    
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='clear',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successsful")
        break
    except Exception as error:
        print("Connecting to Database failed")  
        print("The error was",error) 
        time.sleep(3)


my_posts=[{"title":"Title of 1st post","content":"Content of 1st post","id":1},
          {"title":"My favourite food","content":"I love Nachos","id":2}]

class Post(BaseModel):
    title:str
    content:str    
    published:Optional[boolean]=True


def find_post_index(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i
        



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
       
    



@app.get("/")
def root():
    return {"message": "Hey There! Welcome to the API!"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()
    return {"data":posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,
                   (post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit() #Pushes the above changes to the database
    return {"Data ":new_post}




#Retrieving a singular post
@app.get("/posts/{id}")
def get_post(id : int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""",(id,))
    post=cursor.fetchone()
    # post=findPost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} was not found")
    return {"post_detail": post }

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post=deletePost(id)
    if post==f"Post with ID {id} not found":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)    


@app.put("/posts/{id}")
def update_post(id : int,post: Post):
    index=find_post_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} does not exist")
    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict    
    return {"data":post_dict}
    


#Execute's second parameter accepts tuple as the second parameter so just add
#a comma after that "id"

#Now we will implement the createPosts function using SQL queries



#Now we will implement the getPosts function
#Using SQL statements to get the posts from the database
#USing the cursor
#Which runs our queries


#Now the reconnection attempt might be way too fast
#So we need something to delay it a bit before attempting to reconnect
#So we'll import the time module and do that
#This would be a nice way of handling the internet disconnection or a similar
#issue

#We need to ensure that the database connection is established 
#And we need to wait till it is established and we cannot move on with the rest of
#the code if the connection is not properly established
#So throwing the error and starting the server anyway is of no use
#So we need to ensure that the connection is established
#SO we place the entire logic for the connnection to the database inside a while loop
#the while loop will go on indefinitely until we successfully 
#establish a connection and then we can break out of the loop

#We restructured our folders
#Kept everything inside of our app directory
#Now we can simply change the uvicorn thing
#to refer to this package
# uvicorn app.main:app --reload



#Python has a fancy word for folder -> packages
#and for a folder to become a package you need to add a __init__.py
#inside that
#Now we'll restructure our folders
#and put this file inside an app folder


#Beautiful
#we might not even need to use POSTMAN and we can just use swagger UI
#to test out our operations
#we also have something called redoc
#which has a different UI for trying out all these operations
#WE CAN GET A DOCUMENT POWERED BY REDOC

#We can click on TryItOut and execute to get it to execute the path operations
#we defined

#FastAPI has default swaggerUI SUPPORT
#FastAPI does all the documentation for you automatically
#You don't need to write a single line of code for that
#Which is pretty awesome
#It updates the documentation for your path operations by itself


#That's all about CRUD operations 
#They all work perfectly!!
#If not index apparently broke the update operation at index 0 
#So,Changed that to index==None


#Now we're going to create the Update post operation

#I'm not getting that error but 
#The basic idea is that when you're sending back a 204 you must not send back any 
#data
#However it is essential that with a 204 we don't send any data back
#So we need to send a response that follows this protocol


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