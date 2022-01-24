from ast import Str
from datetime import datetime
import email
from pydantic import BaseModel, EmailStr

class PostBase(BaseModel):
    title:str
    content:str    
    published:bool=True
    
class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id:int
    created_at:datetime
    
    class Config:
        orm_mode=True  #This is added so the pydantic model reads the data evenif
                       #It is not a dictionary
                       #orm_mode=true converts the SQL alchemy model to the dictionary
                       
                       
class UserCreate(BaseModel):
    email:EmailStr
    password:str
    
          
        
        
class UserResponse(BaseModel):
    id:int
    email:EmailStr   
    created_at:datetime
    
    class Config:
        orm_mode=True     
                    

class UserLogin(BaseModel):
     email:EmailStr
     password:str                       