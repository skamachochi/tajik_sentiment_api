from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.auth import router as auth_router
from app.routers.predictions import router as pred_router
from app.core import database

app = FastAPI()
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(pred_router)

@app.get("/")
def root():
    return {"message": "hello"}

