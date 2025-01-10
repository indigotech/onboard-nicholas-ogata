from fastapi import APIRouter, FastAPI
from app.api.user import router as user_router

app = FastAPI()

api_router = APIRouter()

api_router.include_router(user_router.router, prefix='/users')

app.include_router(api_router)
