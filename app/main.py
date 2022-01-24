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
from .routers import posts,users

from . import models,schema,utils
from .database import engine,get_db
from sqlalchemy.orm import Session
from .utils import hashFunction




models.Base.metadata.create_all(bind=engine)



app=FastAPI()



        
        
        

    

app.include_router(posts.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Hey There! Welcome to the API!"}

