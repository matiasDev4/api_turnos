from fastapi.routing import APIRouter


app_route = APIRouter()


@app_route.get("/date_time")
async def get_date():
    pass