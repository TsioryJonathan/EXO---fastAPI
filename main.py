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
def read_hello_custom(request: Request, name: Optional[str] = None, is_teacher: Optional[bool] = False ):
    accept_headers = request.headers.get("Accept")
    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported Media Type"}, status_code=400)

    if name is None and is_teacher is False:
        return JSONResponse(content= "Hello World !" , status_code=200)

    if name is None and is_teacher is not None:
        name = "Non fournie"

    if is_teacher:
        return JSONResponse("Hello Teacher " + name + " !" , status_code=200)
    else:
        return JSONResponse("Hello " + name + " !" , status_code=200)

@app.put("/top-secret")
async def read_top_secret(request : Request):
    authorization_headers = request.headers.get("Authorization")

    if not authorization_headers or authorization_headers != "my-secret-key":
        return JSONResponse({"Incorrect key" : authorization_headers} ,status_code=403)

    body = await request.json()
    secret_code = body.get("secret_code")

    if not secret_code or len(secret_code) != 4:
        return JSONResponse({"Incorrect secret code" : "Must be 4 digits"} ,status_code=400)

    return JSONResponse(
        content={"message": "Welcome to the top secret area !"},
        status_code=200
    )


