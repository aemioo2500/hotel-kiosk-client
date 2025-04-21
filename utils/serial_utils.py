def hex_to_tis620(hex_data: str) -> str:
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

def send_command(ser, hex_str, delay=0.3):
    cmd = bytes.fromhex(hex_str)
    ser.write(cmd)
    ser.flush()
    import time
    time.sleep(delay)
    response = ser.read(64)
    return response.hex().upper()