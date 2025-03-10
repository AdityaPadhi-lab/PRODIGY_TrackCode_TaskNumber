from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import uuid

app = FastAPI()

# In-memory storage
users = {}

# User Model
class User(BaseModel):
    name: str
    email: EmailStr
    age: int

# Create a User
@app.post("/users/", status_code=201)
def create_user(user: User):
    user_id = str(uuid.uuid4())  # Generate unique ID
    users[user_id] = user
    return {"id": user_id, **user.dict()}

# Read a User
@app.get("/users/{user_id}")
def get_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **users[user_id].dict()}

# Update a User
@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user
    return {"id": user_id, **user.dict()}

# Delete a User
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}
