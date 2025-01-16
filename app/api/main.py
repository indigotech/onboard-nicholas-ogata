from fastapi import APIRouter, FastAPI
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from app.api.contact import router as contact_router
from app.api.chat import router as chat_router

app = FastAPI()

api_router = APIRouter()

api_router.include_router(user_router.router, prefix='/users')
api_router.include_router(auth_router.router, prefix='/login')
api_router.include_router(contact_router.router, prefix='/contacts')
api_router.include_router(chat_router.router, prefix='/chats')

app.include_router(api_router)
