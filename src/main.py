from fastapi import FastAPI
from routers.app import app_route

mainApp = FastAPI()

mainApp.description = "API para turnos"

mainApp.include_router(app_route)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mainApp, port=8000)