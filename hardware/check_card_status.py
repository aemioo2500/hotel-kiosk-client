import serial
import time
import configparser

def send_command(ser, hex_str):
    """Send a hex command and return the raw hex response."""
    cmd_bytes = bytes.fromhex(hex_str)
    print(f"[🔧] Sending: {cmd_bytes.hex().upper()}")
    ser.write(cmd_bytes)
    ser.flush()
    response = ser.read_until(expected=b'\x03', size=64)
    print(f"[🔁] Raw Response: {response}")
    return response.hex().upper()

def check_card_status():
    try:
        # Load COM port from config.ini
        config = configparser.ConfigParser()
        config.read("config.ini")
        port = config["thai_id_reader"]["port"]

        print(f"[⏳] Connecting to {port}...")
        ser = serial.Serial(port, baudrate=9600, timeout=1)
        print(f"[✅] Connected to {port}")

        # Initial command
        init_cmd = 'F2 00 00 03 43 30 33 03 B2'
        send_command(ser, init_cmd)
        time.sleep(0.5)

        # Status command
        status_cmd = 'F2 00 00 03 43 31 30 03 B0'
        response = send_command(ser, status_cmd)
        print(f"[📤] Status Response: {response}")
        print(f"[📏] Response Length: {len(response)} characters")

        ser.close()

        # Clean and parse response
        clean_response = response.replace("E5", "").replace("06", "")
        byte_data = bytes.fromhex(clean_response)

        pattern = b'\x50\x31\x30'  # 'P10'
        idx = byte_data.find(pattern)

        if idx == -1 or len(byte_data) < idx + 6:
            print("[⚠️] Card status pattern not found")
            return

        try:
            st0 = int(chr(byte_data[idx + 3]), 16)
            st1 = int(chr(byte_data[idx + 4]), 16)
            st2 = int(chr(byte_data[idx + 5]), 16)
        except Exception as e:
            print(f"[❌] Failed to parse st0-st2: {e}")
            return

        # Interpret values
        position = {
            0: "❌ No card in machine",
            1: "✅ Card at dispenser (not taken)",
            2: "📥 Card at RF/IC"
        }.get(st0, f"❓ Unknown (st0={st0})")

        card_stock = {
            0: "❌ No cards",
            1: "⚠️ Low cards (<10)",
            2: "✅ Sufficient cards"
        }.get(st1, f"❓ Unknown (st1={st1})")

        error_bin = "🗑 Full" if st2 == 1 else "🗑 Not full (<22 cards)"

        print("\n📋 Card Sensor Summary:")
        print(f"- Card Position: {position}")
        print(f"- Card Stock: {card_stock}")
        print(f"- Reject Bin: {error_bin}")

    except serial.SerialException as e:
        print(f"[❌] Cannot connect to serial port: {e}")

if __name__ == "__main__":
    check_card_status()
