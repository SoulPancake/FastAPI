from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session

from .. import database,schema,models,utils

router=APIRouter(tags=['Authentication'])


@router.post("/login")
def login(user_credentials : schema.UserLogin,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=404,detail="Invalid credentials : User doesn't exist")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=404,detail=f"Invalid Credentials")
    
    #create a token
    #return that token
    return {"Token":"Login successful : Example Token"}
