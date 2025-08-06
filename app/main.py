from fastapi import FastAPI
from app.routes.api import router as api_router

app = FastAPI(title="Student Management API")
app.include_router(api_router)
