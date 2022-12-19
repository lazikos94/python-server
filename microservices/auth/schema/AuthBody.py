from pydantic import BaseModel,EmailStr

class AuthBody (BaseModel):
    
    token: str
    
    