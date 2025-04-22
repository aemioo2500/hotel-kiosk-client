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

def wait_for_id_card():
    """Prepare the reader to wait for ID card insertion."""
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

        # Clear any stuck card (move to reject bin)
        print("\n▶️ Clearing any stuck card")
        clear_cmd = 'F2 00 00 03 43 DC 31 03 5C'
        send_command(ser, clear_cmd)

        # Wait for new card insertion
        print("\n⏳ Waiting for ID card insertion...")
        wait_cmd = 'F2 00 00 03 43 33 30 03 B2'
        send_command(ser, wait_cmd)

        ser.close()
        print("[✅] Reader is ready for ID card insertion.")

    except serial.SerialException as e:
        print(f"[❌] Cannot connect to serial port: {e}")

if __name__ == "__main__":
    wait_for_id_card()
