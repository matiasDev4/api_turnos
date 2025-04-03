from fastapi.routing import APIRouter
from fastapi import Depends, Form , HTTPException
from fastapi.responses import FileResponse, JSONResponse
from typing import Annotated
from config.database import session
from sqlalchemy.orm import Session
from models.model_database import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.schema import userRegister
from jose import jwt
import jwt
from dotenv import load_dotenv
from datetime import timedelta
import datetime
import bcrypt
import os

app_login = APIRouter()
load_dotenv(".env")

SECRET_KEY = os.getenv("SECRET_KEY")


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

Oauth2 = OAuth2PasswordBearer(tokenUrl="login")


@app_login.post("/register")
def registerUser(form: Annotated[userRegister, Form(...)], db: Session  = Depends(get_db)):
    try:
        getPasswordHashed = passwordHashed(str(form.password))
        user = db.query(User).filter(form.email == User.user_email).first()
        if not user:
            addUser = User(
                user_name = form.username,
                user_email = form.email,
                user_password = getPasswordHashed,
                user_role = "usuarios"
            )
            db.add(addUser)
            db.commit()
            db.refresh(addUser)
            return JSONResponse(content={"message": "Registro exitoso"}, status_code=201)      
        else:
            raise HTTPException(status_code=401, detail={"message":"Usuario existente"})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})
        
# Funcion para codificacion del JWT 
def encode_token(payload: dict, exp: int = 1) -> str:

    # Copio el payload para evitar mutacion
    data = payload.copy()

    #Creamos el tiempo de expiración del token
    expire = datetime.datetime.utcnow() + timedelta(days=exp)

    data["exp"] = expire
    # Guardamos en una variable el JWT para despues retornarlo
    encode = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return encode

# Funcion para decodificacion del JWT
def decode_token(token: Annotated[str, Depends(Oauth2)]) -> dict:
    #Esperamos el token para decoficarlo, verificarlo y retornar los datos encriptados
    try:
        decode = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decode
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=500, detail="El token expiro")
    
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=500, detail="El token es Inválido")

def verificationPassword(PasswordPlane: str, HashedPassword: str) -> bool:
    passwordNotHashed = bcrypt.checkpw(PasswordPlane.encode('utf-8'), HashedPassword.encode('utf-8'))
    return passwordNotHashed

def passwordHashed(password:str) -> str:
    salt = bcrypt.gensalt()
    passwordHash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return passwordHash.decode('utf-8')

#Path para login y retornar el token
@app_login.post("/login")
def loginUser(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    try:
        #Consultamos a la DB si existe un usuario y contraseña indicados
        consult = db.query(User).filter(User.user_email == form.username).first()
        
        #Verificamos que no sea NONE, obtenemos token y retornamos el token
        if consult is None:    
            raise HTTPException(status_code=401, detail="Credenciales incorrectas!")
        
        passwordVerify = verificationPassword(form.password, consult.user_password)
        if not passwordVerify:
            raise HTTPException(status_code=401, detail="Credenciales incorrectas!")

        token = encode_token({"email":consult.user_email, "role":consult.user_role, "username":consult.user_name})
        return JSONResponse(content={"access_token": token, "token_type":"bearer"}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app_login.get("/admin/me")
def dataAdmin(user: Annotated[dict, Depends(decode_token)]):
    try:
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    