from typing import Union
from pydantic import BaseModel,EmailStr

class RegisterBody (BaseModel):
    
    email: EmailStr
    username: str
    password: str
    
    
    