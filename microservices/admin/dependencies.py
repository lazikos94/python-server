from fastapi import Request
from core.exceptions import ForbiddenException, NonAuthenticatedException



def passport (req: Request):
    if req.headers.get("authorization") is None: raise NonAuthenticatedException()
    req.state.user = { "username": "@Mike", "role": "admin" }
    print ("something")
    
    
def admin_only (req: Request):
    if req.state.user["role"] is not "admin":
        raise ForbiddenException()