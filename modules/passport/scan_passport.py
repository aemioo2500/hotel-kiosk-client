# modules/passport/scan_passport.py

import serial
import time
from utils.serial_utils import PASSPORT_PORT, BAUDRATE_PASS, TIMEOUT_PASS

# Command for IDE237
CMD_ENABLE_TRIGGER = bytes.fromhex("7E01303030304053434E544345313B03")
CMD_BEGIN_DECODE   = bytes.fromhex("7E01303030304053434E545247313B03")

def is_valid_mrz(text):
    """
    Check whether the scanned text is a valid MRZ (starts with 'P<')
    """
    return text.startswith("P<") and len(text.splitlines()) >= 2

def main():
    try:
        with serial.Serial(PASSPORT_PORT, BAUDRATE_PASS, timeout=TIMEOUT_PASS) as ser:
            print("[🔗] Connected to IDE237 passport scanner.")

            # Step 1: Enable scanner trigger
            ser.write(CMD_ENABLE_TRIGGER)
            time.sleep(0.3)

            # Step 2: Start decoding
            ser.write(CMD_BEGIN_DECODE)
            print("[⏳] Waiting for MRZ data...")

            buffer = ""
            timeout = 10
            start_time = time.time()

            while time.time() - start_time < timeout:
                if ser.in_waiting:
                    data = ser.read(ser.in_waiting)
                    text = data.decode(errors='ignore').strip()
                    buffer += text
                    print("📥 Received:", text)

                    if is_valid_mrz(buffer):
                        print("\n✅ MRZ Data Received:\n")
                        print(buffer)
                        return buffer

                time.sleep(0.2)

            print("⚠️ Timeout: No MRZ data received.")
            return None

    except Exception as e:
        print("❌ Error while reading passport:", str(e))
        return None

if __name__ == "__main__":
    main()
