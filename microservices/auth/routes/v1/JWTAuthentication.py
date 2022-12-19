from fastapi import APIRouter, Request, Depends
from core.exceptions import *
from core.utils import *
from microservices.auth.dependencies import *
from microservices.auth.schema.LoginBody import *
from microservices.auth.schema.RegisterBody import *
from microservices.auth.schema.AuthBody import *
from config import settings
#from core.db import getCollection
from core.db import database
from core.db import collection
from core.utils import (passwordEncrypt,passwordVerify,jwtTokenEncode,jwtTokenRefresh)
from uuid import uuid4

jwtauthentication_router = APIRouter()

@jwtauthentication_router.post("/login", dependencies=[])
async def login (loginBody: LoginBody):
    try:
        user = database['test-database'].find_one({"email":loginBody.email})
        print(user['password'])
        print(loginBody.password)
        print( passwordVerify(loginBody.password,user['password']))
        if passwordVerify(loginBody.password,user['password']):
            return {
                "token": jwtTokenEncode(user['email']),
                "user": loginBody.email    
            }
        return {
            "error": "Wrong login details!"
        }
    except:
        return "Error logining in"

@jwtauthentication_router.post("/register", dependencies=[])
async def register (registerBody: RegisterBody):
    try:
        user = {
            'email': registerBody.email,
            'username':registerBody.username,
            'password': passwordEncrypt(registerBody.password),
        }
        
        already = database['test-database'].find_one({'email':user['email']})
        if(already):
            print('User already exists')
            return 'User already exists'
        else:
            database['test-database'].insert_one(user).inserted_id   # saving user to database
            user['_id'] = str (user['_id'])
            return user
    except:
        return "Error registering"
   
   
@jwtauthentication_router.post("/authenticate",dependencies=[])
async def authenticate(authBody:AuthBody):
    try:
        auth={
        'token':authBody.token
       
        }

        check = jwtTokenDecode(auth['token'])

        return check
    except:
        return "Error authenticating token"


@jwtauthentication_router.get("/db",dependencies=[])
async def read(req: Request):
    post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"]}
    posts = database['test-database']
    post_id = posts.insert_one(post).inserted_id
    print(post_id)
    #created_student =  getCollection()
    return{
     # created_student
    }