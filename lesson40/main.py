import logging
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.middleware.sessions import SessionMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SECRET_KEY = "super-secret-key-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

ADMIN_HASH = "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGGa31S2"
users_db = {
    "admin": {
        "username": "admin",
        "password_hash": ADMIN_HASH,
        "full_name": "Ivan Ivanov"
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/oauth2/login")

app = FastAPI(title="Auth Demo (Session, JWT, OAuth2)")
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

def verify_password(plain_password, hashed_password):
    logger.info(f"Сравниваем пароль: {plain_password}")
    return plain_password == "secret"

def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/auth/session/login")
async def login_session(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    request.session["user"] = user["username"]
    return {"message": "Logged in via Session"}

@app.get("/user/me/session")
async def get_me_session(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="No session found")
    return {"user": user, "method": "Session (Cookie)"}

@app.post("/auth/jwt/login")
async def login_jwt(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_jwt_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/user/me/jwt")
async def get_me_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"user": payload.get("sub"), "method": "Manual JWT"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/auth/oauth2/login")
async def login_oauth2(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"OAuth2 login attempt for: {form_data.username}")
    user = users_db.get(form_data.username)
    if not user:
        logger.warning("User not found")
        raise HTTPException(status_code=400, detail="User not found")
    if not verify_password(form_data.password, user["password_hash"]):
        logger.warning("Invalid password")
        raise HTTPException(status_code=400, detail="Invalid password")
    token = create_jwt_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/user/me/oauth2")
async def get_me_oauth2(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"user": payload.get("sub"), "method": "OAuth2 Flow"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

@app.post("/auth/logout")
async def logout(request: Request):
    request.session.clear()
    return {"message": "Logged out successfully"}
