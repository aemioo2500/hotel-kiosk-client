# utils/serial_utils.py

import configparser
import time

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Thai National ID reader settings
THAI_PORT = config["thai_id_reader"]["port"]
BAUDRATE_THAI = int(config["thai_id_reader"]["baudrate"])
TIMEOUT_THAI = int(config["thai_id_reader"]["timeout"])

# Passport scanner settings
PASSPORT_PORT = config["passport_scanner"]["port"]
BAUDRATE_PASS = int(config["passport_scanner"]["baudrate"])
TIMEOUT_PASS = int(config["passport_scanner"]["timeout"])

def send_command(ser, hex_str, delay=0.3):
    """
    Send a HEX string command via Serial and receive a response.
    """
    cmd = bytes.fromhex(hex_str)
    ser.write(cmd)
    ser.flush()
    time.sleep(delay)
    response = ser.read(64)
    print(f"Sent:     {hex_str}")
    print(f"Received: {response.hex().upper()}")
    return response.hex().upper()

def hex_to_tis620(hex_data: str) -> str:
    """
    Convert HEX response from Thai ID card (APDU) to readable TIS-620 text.
    """
    try:
        if hex_data.endswith("9000"):
            hex_data = hex_data[:-4]
        hex_data = hex_data.upper()
        if "505139" in hex_data:
            hex_data = hex_data.split("505139")[-1]
        data_bytes = bytes.fromhex(hex_data)
        text = data_bytes.decode('tis-620', errors='replace').strip()
        return text.replace('#', ' ')
    except Exception as e:
        return f"[decode error: {e}]"
