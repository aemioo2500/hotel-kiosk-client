# hotel-kiosk-client

Python-based backend module for interfacing with Thai National ID card readers (CRT-591) and passport scanners (IDE237) in hotel self check-in kiosks.

---

## 📌 Features

### Thai ID Card (CRT-591)
- 🔍 Read full **English name** from Thai National ID
- 🔍 Read full **Thai name** from Thai National ID
- 📦 Check **card status** (position, stock, reject bin)
- ⏳ Wait for card insertion
- 🗑 Move stuck card to stacker (reject bin)
- ⏏️ Eject card from reader

### Passport (IDE237)
- 🌐 Scan and extract **MRZ data**
- ✅ Verify full name matching from OCR scan

---

## 🧰 Tech Stack

- Python 3.x
- PySerial
- TIS-620 decoding
- ConfigParser
- Modular Script Design

---

## 🚀 Getting Started

### 1. Clone and Install
```bash
git clone https://github.com/your-username/hotel-kiosk-client.git
cd hotel-kiosk-client
pip install -r requirements.txt
```

---

### 2. Run a Module

#### 🪪 Read English name from Thai ID
```bash
python hardware/read_name_en.py
```

#### 🪪 Read Thai name from Thai ID
```bash
python hardware/read_name_th.py
```

#### 📦 Check Card Reader Status
```bash
python hardware/check_card_status.py
```

#### ⏳ Wait for Thai ID Card
```bash
python hardware/wait_for_id_card.py
```

#### ⏏️ Eject Thai ID Card
```bash
python hardware/eject_id_card.py
```

#### 🗑 Move Card to Reject Bin
```bash
python hardware/move_card_to_stacker.py
```

#### 🛂 Scan Passport (IDE237)
```bash
python hardware/scan_passport.py
```

---

## ⚙️ File Structure

```
hotel-kiosk-client/
├── api/
│   ├── card.py              # API model (Pydantic)
│   ├── card_reader.py       # Logic interface for reading card
│   ├── main.py              # FastAPI entrypoint
│   └── read_card.py         # Route for reading Thai ID
│
├── hardware/
│   ├── check_card_status.py     # Card dispenser status checker
│   ├── eject_id_card.py         # Eject ID card from reader
│   ├── move_card_to_stacker.py  # Move card to reject bin
│   ├── read_name_en.py          # Read English name
│   ├── read_name_th.py          # Read Thai name
│   ├── scan_passport.py         # MRZ scanner via passport
│   └── wait_for_id_card.py      # Wait for card insertion
│
├── utils/
│   ├── serial_utils.py          # Serial communication functions
│   └── __init__.py              # Python package marker
│
├── LICENSE
├── README.md
├── config.ini                   # COM port configuration
└── requirements.txt
```

---

## 🔧 Configuration

Edit the `config.ini` file to match your COM ports:

```ini
[thai_id_reader]
port = COM4

[passport_scanner]
port = COM2
```

---

## 💼 Use Case

This code is a key component in a **hotel self-service kiosk system**, designed to replace manual check-in by verifying guest identity via their government-issued ID or passport.

---

## 🪪 Devices Supported

- Thai National ID Reader: **CRT-591**
- Passport Scanner: **IDE237** (MRZ OCR)

---

## 📜 License

MIT License. Feel free to use, modify, and integrate.

---

📢 Created by **Nipon Eiamoo** | 2025  
🔗 Contact via GitHub or LinkedIn for collaboration
