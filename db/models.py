from sqlalchemy import Column, Integer, String
from db.database import Base

# Its datas and values are using '=' equal sign, not ':' colon sign
class DBUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)