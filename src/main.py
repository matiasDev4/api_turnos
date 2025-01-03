from fastapi import FastAPI

mainApp = FastAPI()

mainApp.description = "API para turnos"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mainApp, port=8000)