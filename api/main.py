from fastapi import FastAPI
from api.endpoints import read_card

app = FastAPI(title="Hotel Kiosk API")

app.include_router(read_card.router, prefix="/card", tags=["Card Reader"])
