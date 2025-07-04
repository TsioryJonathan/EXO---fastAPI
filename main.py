from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def read_hello():
    return JSONResponse(content="Hello world", status_code=200)
