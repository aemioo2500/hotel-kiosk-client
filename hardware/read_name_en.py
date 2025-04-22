import serial
import time
import configparser
from utils.serial_utils import hex_to_tis620

def send_and_receive(ser, cmd, read_len=50, delay=0.5):
    ser.write(cmd)
    time.sleep(delay)
    return ser.read(read_len)

def read_english_name():
    # Load COM port from config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")
    port = config["thai_id_reader"]["port"]

    ser = serial.Serial(port, baudrate=57600, timeout=1)

    commands = [
        'F2 00 00 03 43 31 30 03 B0',
        'F2 00 00 03 43 30 33 03 B2',
        'F2 00 00 03 43 32 31 03 B2',
        'F2 00 00 03 43 50 30 03 D1',
        'F2 00 00 04 43 51 30 33 03 E4',
        'F2 00 00 03 43 51 38 03 D8',
        'F2 00 00 10 43 51 39 00 A4 04 00 08 A0 00 00 00 54 48 00 01 03 DF',
        'F2 00 00 0A 43 51 39 80 B0 00 75 02 00 64 03 F3',
        'F2 00 00 07 43 51 39 00 C0 00 00 03 1D',
    ]

    hex_response = ""
    for hex_cmd in commands:
        cmd = bytes.fromhex(hex_cmd)
        response = send_and_receive(ser, cmd, read_len=120 if 'B0' in hex_cmd or 'C0' in hex_cmd else 50)
        hex_response += response.hex().upper()

    ser.close()
    return hex_to_tis620(hex_response)

if __name__ == "__main__":
    name = read_english_name()
    print("📤 Result (English Name):", name)
