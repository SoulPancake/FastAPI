from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session

from .. import database,schema,models,utils

router=APIRouter(keys=['Authentication'])


@router.post("/login")
def login(user_credentials : schema.UserLogin,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=404,detail="Invalid credentials : User doesn't exist")
    
    entered_password=utils.hashFunction(user_credentials.password)
    if(user.password==entered_password):
        return "Logged-in"
    else:
        return "Incorrect Password"