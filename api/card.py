from pydantic import BaseModel

class CardResponse(BaseModel):
    name: str
    id_number: str
