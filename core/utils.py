from passlib.context import CryptContext
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from jose import jwt
from datetime import datetime, timedelta
from typing import Union, Any
from config import settings
import time
from typing import Dict

def dosomething ():
    print("Hello world from do something function")
    
    
def passwordEncrypt (password: str)->str:
    return password_context.hash(password)

    
def passwordVerify (password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
    
def jwtTokenEncode (user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    secret =  'MySuperSecret'
    algo = "HS256"
    token = jwt.encode(payload,secret, algo)
    return token

def jwtTokenRefresh (subject: Union[str, Any], expires_delta: int = None) -> str:

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings['REFRESH_TOKEN_EXPIRE_MINUTES'])
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings['JWT_ACCESS_SECRET_KEY'], settings["JWT_ALGORITHM"])
    return encoded_jwt
def jwtTokenDecode (token):
    secret =  'MySuperSecret'
    algo = "HS256"
    decoded_token = jwt.decode(token, secret , algo)
    return decoded_token if decoded_token["expires"] >= time.time() else None
