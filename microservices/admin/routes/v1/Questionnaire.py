from fastapi import APIRouter, Request, Depends
from core.exceptions import *
from core.utils import *
from microservices.admin.dependencies import *
from config import settings
from microservices.admin.schema.Questionnaire import *
from core.db import database
from core.db import collectionq
from bson import json_util
import json
from fastapi.responses import JSONResponse
from core.exceptions import ForbiddenException, NonAuthenticatedException
questionnaire_router = APIRouter()


# , Depends(admin_only)
@questionnaire_router.get("/read", dependencies=[Depends(passport)])
async def readQuestionnaires (req: Request):
    return {

    }


@questionnaire_router.post('/post',dependencies=[])
async def postQuestionnaire (questions: NewQuestionnaire):
    try:
        print('hello')
        print(questions.dict())
      
        collectionq.insert_one(questions.dict())
      
        return questions.dict()

    except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)    
            raise ForbiddenException()

@questionnaire_router.get('/get',dependencies=[])
async def getQuestionnaire ():
    try:
        
        all= collectionq.find()
        details_dicts = [doc for doc in all]
        docs_list  = json.dumps(list(details_dicts), default=json_util.default)
        docs_json = json.loads(docs_list)

        return docs_json
    
        
    except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)    
            raise ForbiddenException()