from fastapi import FastAPI
from db import models
from db.database import engine
from routes import user

app = FastAPI()

app.include_router(user.router)

@app.get('/')
def index():
    return {"message":"Welcome to the API!"}

models.Base.metadata.create_all(engine)