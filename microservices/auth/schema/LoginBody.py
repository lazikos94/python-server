from typing import Union
from pydantic import BaseModel,EmailStr

class LoginBody (BaseModel):
    email: EmailStr
    password: str