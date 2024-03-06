from fastapi import FastAPI
from .routers import assets
from . import db_activation

app = FastAPI()
db_activation.activate()

app.include_router(assets.router)
