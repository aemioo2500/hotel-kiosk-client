from api.utils.serial_utils import send_command
from api.models.card import CardResponse

def read_thai_id_card() -> CardResponse:
    # Example: Send command to hardware and receive response
    command = "F2 00 00 03 43 31 30 03 B0"
    response = send_command(command)
    # TODO: Parse the response to extract actual name and ID number
    return CardResponse(name="Sample Name", id_number="1234567890123")
