from pydantic import BaseModel

# This is from User
class UserBase(BaseModel):
    username: str
    email: str
    password: str

# This is to User, therefore don't have password!
class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    class Config():
        orm_mode = True