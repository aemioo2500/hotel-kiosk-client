import serial
import time
import configparser

def send_command(ser, hex_str, delay=0.3):
    """ส่งคำสั่งแบบ Hex String และอ่านค่าจาก Serial"""
    cmd = bytes.fromhex(hex_str)
    ser.write(cmd)
    time.sleep(delay)
    response = ser.read(64)
    print(f"[📤] ส่ง: {hex_str}")
    print(f"[📥] ตอบกลับ: {response.hex().upper()}")
    return response.hex().upper()

def eject_id_card():
    """สั่งให้เครื่องจ่ายบัตรประชาชนออก"""
    # โหลดค่าพอร์ต COM จาก config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")
    port = config["thai_id_reader"]["port"]

    try:
        ser = serial.Serial(port, baudrate=57600, timeout=1)
        print(f"[🔄] เชื่อมต่อกับ {port}...")

        # ตั้งค่าการเชื่อมต่อ COM
        print("\n▶️ ตั้งค่าการเชื่อมต่อ COM")
        set_com_cmd = 'F2 00 00 03 43 30 31 03 B0'
        send_command(ser, set_com_cmd)

        # ย้ายบัตรไปตำแหน่งพัก
        print("\n▶️ ย้ายบัตรไปตำแหน่งพัก")
        move_to_parking_cmd = 'F2 00 00 03 43 30 30 03 B1'
        send_command(ser, move_to_parking_cmd)

        # สั่งให้เครื่องจ่ายบัตรออก
        print("\n⏳ กำลังจ่ายบัตรประชาชนออก...")
        eject_cmd = 'F2 00 00 03 43 DC 31 03 5C'
        send_command(ser, eject_cmd)

        ser.close()
        print("[✅] จ่ายบัตรประชาชนออกเรียบร้อยแล้ว.")

    except serial.SerialException as e:
        print(f"[❌] ไม่สามารถเชื่อมต่อพอร์ต {port} ได้: {e}")

if __name__ == "__main__":
    eject_id_card()
