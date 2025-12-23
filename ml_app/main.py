from fastapi import FastAPI
from app.routes import peak_shaving

app = FastAPI(title="Solar Health API")

app.include_router(
    peak_shaving.router,
    prefix="/peak-shaving",
    tags=["Peak Shaving"]
)
