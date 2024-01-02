from os import name
from typing import List
from fastapi import responses
from fastapi import websockets
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse
from starlette.responses import HTMLResponse
from exceptions import StoryException
from fastapi import FastAPI
from router import user
from auth import authentication
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
from client import html
from fastapi.websockets import WebSocket

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)

@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
  return JSONResponse(
    status_code=418,
    content={'detail': exc.name}
  )


@app.get("/")
async def get():
  return HTMLResponse(html)

clients = []
messages: List[str] = []

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Send past messages to the new user
    for message in messages:
        await websocket.send_text(message)
    
    clients.append(websocket)
    
    while True:
        data = await websocket.receive_text()
        messages.append(data)
        
        # Broadcast the message to all connected clients
        for client in clients:
            await client.send_text(data)

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#   return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)


@app.middleware("http")
async def add_middleware(request: Request, call_next):
  start_time = time.time()
  response = await call_next(request)
  duration = time.time() - start_time
  response.headers['duration'] = str(duration)
  return response


origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)
