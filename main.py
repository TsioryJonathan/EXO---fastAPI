from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def read_hello():
    return JSONResponse(content="Hello world", status_code=200)

class WelcomeRequest(BaseModel):
    name: str

@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {f"Bienvenue {request.name}"}