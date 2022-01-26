from jose import JWTError,jwt
from datetime import datetime,timedelta
#Secret_key
#algorithm
#expiration time for auto-log out

SECRET_KEY="Iu1sPs8y1XKpzRWbU5gDY2oMMplQrAqq7v2RzHzT3fPtoSafo4Bi8Kg"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data :dict):
    to_encode=data.copy()
    expire=datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
    
    