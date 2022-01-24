from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schema,utils
from sqlalchemy.orm import Session
from ..database import get_db
from ..utils import hashFunction

router=APIRouter(
    prefix="/users"
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.UserResponse)
def create_user(user : schema.UserCreate,db: Session = Depends(get_db)):
      
    user.password=hashFunction(user.password)
    new_user=models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    

@router.get("/{id}",status_code=status.HTTP_201_CREATED,response_model=schema.UserResponse)  
def getUser(id:int,db: Session = Depends(get_db)):  
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail=f"User with id {id} does not exist")
    
    return user
    