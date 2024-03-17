from fastapi import FastAPI

from app.api.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)


@app.get("/testing/")
def read_root():
    return {"message": "Hello World"}
