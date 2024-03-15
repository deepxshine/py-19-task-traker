from pydantic import BaseModel
from datetime import  datetime


class CreateUser(BaseModel):
    first_name:str  # STR
    last_name:str  # STR
    username:str  # STR
    password:str  # STR
    bdate: datetime  # datetime
    bio:str # STR
    email:str  # STR


class ReadUser(CreateUser):
    pass
