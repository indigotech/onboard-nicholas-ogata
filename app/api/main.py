from fastapi import APIRouter, FastAPI
from app.api.user import router as user_router
from app.api.auth import router as auth_router

app = FastAPI()

api_router = APIRouter()

api_router.include_router(user_router.router, prefix='/users')
api_router.include_router(auth_router.router, prefix='/login')

app.include_router(api_router)
