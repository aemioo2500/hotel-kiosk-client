import serial
import time
import configparser

def send_command(ser, command_bytes, delay=0.5):
    """ส่งคำสั่งแบบ Byte และอ่านค่าจาก Serial"""
    ser.write(command_bytes)
    ser.flush()
    time.sleep(delay)
    return ser.read_all()

def is_valid_mrz(text):
    """ตรวจสอบว่าเป็นข้อมูล MRZ หรือไม่"""
    return text.startswith("P<") and len(text.splitlines()) >= 2

def scan_passport():
    """สแกนข้อมูล MRZ จากหนังสือเดินทาง"""
    # โหลดค่าพอร์ต COM จาก config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")
    port = config["passport_scanner"]["port"]

    try:
        with serial.Serial(port, baudrate=115200, timeout=2) as ser:
            print(f"🔗 เชื่อมต่อกับสแกนเนอร์ที่พอร์ต {port}")

            # คำสั่งเปิด Trigger
            CMD_ENABLE_TRIGGER = bytes.fromhex("7E01303030304053434E544345313B03")
            send_command(ser, CMD_ENABLE_TRIGGER)

            # คำสั่งเริ่มการสแกน
            CMD_BEGIN_DECODE = bytes.fromhex("7E01303030304053434E545247313B03")
            send_command(ser, CMD_BEGIN_DECODE)

            print("⏳ รอรับข้อมูล MRZ ...")

            buffer = ""
            timeout = 10  # วนลูปอ่านสูงสุด 10 วินาที
            start_time = time.time()

            while time.time() - start_time < timeout:
                if ser.in_waiting:
                    data = ser.read(ser.in_waiting)
                    text = data.decode(errors='ignore')
                    buffer += text
                    print("📥 รับข้อมูล:", text.strip())

                    if is_valid_mrz(buffer):
                        print("\n✅ ได้รับข้อมูล MRZ:\n", buffer.strip())
                        break

                time.sleep(0.2)

            else:
                print("⚠️ หมดเวลา: ไม่ได้รับข้อมูล MRZ")

    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    scan_passport()
