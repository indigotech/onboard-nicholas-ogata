from fastapi import FastAPI, Path, Query, HTTPException, status
from user import User, UserRequest

app = FastAPI()

USERS = [
    User(1, 'User1', 18, 'user1@gmail.com'),
    User(2, 'User2', 22, 'user2@gmail.com'),
    User(3, 'User3', 40, 'user3@gmail.com'),
]

@app.get('/')
async def welcome():
    return {'message': 'Hello World!'}

@app.get('/users', status_code=status.HTTP_200_OK)
async def get_all_users():
    return USERS

@app.post('/users', status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest):
    new_user = User(**user_request.model_dump())
    USERS.append(new_user)
    return new_user
