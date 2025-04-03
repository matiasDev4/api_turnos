from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers.app import app_route
from routers.cursor import app_cursos
from routers.login import app_login

mainApp = FastAPI()

mainApp.description = "API para turnos"

mainApp.include_router(app_route)
mainApp.include_router(app_cursos)
mainApp.include_router(app_login)

origins = [
    "http://localhost:5173",
    ]

mainApp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

if __name__ == "__main__":
    
    uvicorn.run(mainApp, port=8000)