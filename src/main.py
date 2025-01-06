from fastapi import FastAPI
import uvicorn
from routers.app import app_route

mainApp = FastAPI()

mainApp.description = "API para turnos"

mainApp.include_router(app_route)

if __name__ == "__main__":
    
    uvicorn.run(mainApp, port=8000)