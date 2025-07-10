from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
from typing import Optional

app = FastAPI()


@app.get("/hello")
def read_hello(request: Request):
    accept_headers = request.headers.get("Accept")
    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)
    return JSONResponse(content="Hello world", status_code=200)

class WelcomeRequest(BaseModel):
    name: str

@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {f"Bienvenue {request.name}"}

@app.post("/hello-custom")
def read_hello_custom(request: Request, name: Optional[str] = None, is_teacher: Optional[bool] = None ):
    accept_headers = request.headers.get("Accept")
    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)

    if name is None and is_teacher is None:
        return RedirectResponse(url="/hello", status_code=303)

    if name is not None and is_teacher is None:
        is_teacher = False

    if name is None and is_teacher is not None:
        name = "Non fournie"

    if is_teacher:
        return "Hello Teacher " + name + " !"
    else:
        return "Hello " + name + " !"




