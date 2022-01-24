from ast import Str
from pydantic import BaseModel

class PostBase(BaseModel):
    title:str
    content:str    
    published:bool=True
    
class PostCreate(PostBase):
    pass


class PostResponse(BaseModel):
    title:str
    content:str
    
    class Config:
        orm_mode=True  #This is added so the pydantic model reads the data evenif
                       #It is not a dictionary
                       #orm_mode=true converts the SQL alchemy model to the dictionary
                       