from fastapi import FastAPI
from .routers import assets,metrics, insights
from . import db_activation

app = FastAPI()
db_activation.activate()

app.include_router(assets.router)
app.include_router(metrics.router)
app.include_router(insights.router)