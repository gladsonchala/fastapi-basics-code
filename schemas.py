from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
  username: str
  password: str

class UserDisplay(BaseModel):
  id: int
  username: str
  class Config():
    orm_mode = True
