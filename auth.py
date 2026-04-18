from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException
from database import db

router = APIRouter()

users_collection = db["users"]
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_token(username: str):
    expire = datetime.utcnow() + timedelta(hours=2)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except:
        return None
# Signup
@router.post("/signup")
def signup(user: dict):
    if users_collection.find_one({"username": user["username"]}):
        raise HTTPException(status_code=400, detail="User already exists")

    users_collection.insert_one(user)
    return {"message": "User created successfully"}

# Login
@router.post("/login")
def login(user: dict):
    db_user = users_collection.find_one({
        "username": user["username"],
        "password": user["password"]
    })

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user["username"])   # ✅ ADD THIS

    return {"token": token}   # ✅ RETURN TOKEN