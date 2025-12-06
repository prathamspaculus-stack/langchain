from pydantic import BaseModel
from typing import Optional

class name(BaseModel):

    name: str
    age: Optional[int] = None


name_student = {'name':'Prtham'}

student = name(**name_student)

print(student)