# hotel-kiosk-client

A Python-based control system for hotel kiosk machines.

Supports:
- Reading Thai National ID cards via the CRT-591 reader (APDU over Serial)
- Reading passport MRZ data via the IDE237 passport scanner (COM2 connection)

Designed for direct hardware integration. No external API is required.  
Ideal for hotel self check-in kiosks.

---

## ภาษาไทย (Thai)

ระบบควบคุมตู้ Kiosk สำหรับโรงแรม พัฒนาด้วย Python

รองรับการทำงาน:
- อ่านบัตรประชาชนไทยผ่านเครื่องอ่านรุ่น CRT-591 (ส่งคำสั่ง APDU ผ่าน Serial)
- อ่านข้อมูล MRZ จากหนังสือเดินทางผ่านเครื่องสแกนพาสปอร์ต IDE237 (เชื่อมต่อ COM2)

สามารถรันได้โดยตรงบนเครื่อง Kiosk โดยไม่ต้องเชื่อมต่อ API หรืออินเทอร์เน็ต เหมาะสำหรับระบบเช็คอินด้วยตนเองในโรงแรม