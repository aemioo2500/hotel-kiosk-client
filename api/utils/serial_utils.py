import serial

def send_command(command: str) -> str:
    with serial.Serial('COM4', baudrate=9600, timeout=1) as ser:
        ser.write(bytes.fromhex(command))
        response = ser.read(64)
        return response.hex().upper()
