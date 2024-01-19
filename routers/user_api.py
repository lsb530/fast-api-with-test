from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

user = APIRouter(prefix='/api')
class User(BaseModel):
    name: str
    age: int

users = [
    {
        'id': 1,
        'name': 'LEE',
        'age': 30
    },
    {
        'id': 2,
        'name': 'KIM',
        'age': 25
    }
]

@user.get("/users", tags=['user'])
async def get_users():
    return {"data": users}

@user.get("/users/{user_id}", tags=['user'])
async def get_user(user_id: int):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user.post("/users", tags=['user'])
async def create_user(user: User):
    new_id = max(user['id'] for user in users) + 1
    new_user = user.model_dump()
    new_user['id'] = new_id
    users.append(new_user)
    return {"data": users}

@user.patch("/users/{user_id}", tags=['user'])
async def update_user(user_id: int, update_info: User):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.update(update_info)
    return user

@user.delete("/users/{user_id}", tags=['user'])
async def delete_user(user_id: int):
    global users
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    users = [user for user in users if user['id'] != user_id]
    return {"detail": "User deleted"}
