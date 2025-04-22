import serial
import time
import configparser

def send_command(ser, hex_str, delay=0.3):
    """Send a hex command to the card reader and return the response."""
    cmd = bytes.fromhex(hex_str)
    ser.write(cmd)
    time.sleep(delay)
    response = ser.read(64)
    print(f"[📤] Sent: {hex_str}")
    print(f"[📥] Response: {response.hex().upper()}")
    return response.hex().upper()

def move_card_to_stacker():
    """Move a stuck card to the stacker (reject bin)."""
    # Load COM port from config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")
    port = config["thai_id_reader"]["port"]

    try:
        ser = serial.Serial(port, baudrate=57600, timeout=1)
        print(f"[🔄] Connecting to {port}...")

        # Set COM connection
        print("\n▶️ Setting COM connection")
        set_com_cmd = 'F2 00 00 03 43 30 31 03 B0'
        send_command(ser, set_com_cmd)

        # Move card to stacker bin
        print("\n🗑 Moving card to stacker...")
        move_cmd = 'F2 00 00 03 43 DC 01 03 5E'
        send_command(ser, move_cmd)

        ser.close()
        print("[✅] Card moved to stacker successfully.")

    except serial.SerialException as e:
        print(f"[❌] Cannot connect to serial port: {e}")

if __name__ == "__main__":
    move_card_to_stacker()
