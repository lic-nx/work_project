from typing import Union

from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Models
from sqlalchemy import Column, BIGINT, VARCHAR

class Emplyee(Base):
    pass

@app.get("/users")
def get_users()-> JSONResponse:
    pass


