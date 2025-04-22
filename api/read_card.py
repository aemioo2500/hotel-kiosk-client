from fastapi import APIRouter
from api.services.card_reader import read_thai_id_card
from api.models.card import CardResponse

router = APIRouter()

@router.get("/read", response_model=CardResponse)
def read_card():
    return read_thai_id_card()
