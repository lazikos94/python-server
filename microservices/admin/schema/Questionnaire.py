from pydantic import BaseModel,EmailStr,Field
from typing import List


class Answers(BaseModel):
    
    value: str
    label: str
    color: str
    correct: bool
  

class Questions(BaseModel):
    currentQuestionInfo: dict
    currentQuestionAnswers: List[Answers]


class NewQuestionnaire(BaseModel):
    title: dict
    questions: List[Questions]