from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.user import router as user_router

app = FastAPI(title="FastAPI-timeseries", description="Analyze Timeseries API")

app.include_router(auth_router)
app.include_router(user_router)


@app.get("/testing/")
def read_root():
    return {"message": "Hello World"}
