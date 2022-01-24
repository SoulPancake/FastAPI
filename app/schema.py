from pydantic import BaseModel

class PostBase(BaseModel):
    title:str
    content:str    
    published:bool=True
    
class PostCreate(PostBase):
    pass


#These classes are essentially schema/pydantic models
#which are used to validate the request and responses    