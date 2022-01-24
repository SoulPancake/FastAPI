from ast import Raise
from logging import raiseExceptions
from typing import Optional,List
from xmlrpc.client import boolean
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randint, randrange
import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor
import time


from . import models,schema,utils
from .database import engine,get_db
from sqlalchemy.orm import Session
from .utils import hashFunction




models.Base.metadata.create_all(bind=engine)



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




def find_post_index(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i
        
#Testing out the DB connection and disconnection


    


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

