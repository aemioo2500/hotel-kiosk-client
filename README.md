# hotel-kiosk

A Python-based hotel self check-in kiosk system that integrates Thai National ID card reading, passport scanning, and backend API services.

---

## 📌 Features

-🔍 Read full name in **English** (`read_name_en.py)
 🔍 Read full name in **Thai** (`read_name_th.p`)- 📤 Decode `APDU` responses using `TIS-620` encoing
- ⚙️ Connects via **Serial COM** with IC card reader (CRT-91)
- 🧩 Modular: Easy to integrate into other systems (e.g., FastAPI, Hotel Kosk
- 🛂 Scan and parse passport MRZ data (`scan_passpor.py)
- 🖥️ Backend API using FastAPI frmework

---

## 🧰 Tech Sack

- Pyhon3.x
- ySeial
- FasAPI
- TIS-620 Encodin (Thai)

---

## 🚀 How to Run

### 1. Install depenencies


```bash
pip install -r requirementstxt
```

---

### 2. Run Thai or English namereader

```bash
# For English name
python hardware/read_name_en.py

# For Thai name
python hardware/read_name_t.py
```

📝 *Default COM port is `COM4`. Modify in script if needed.*

---

### 3. Run PassportScanner

```bash
python hardware/scan_passpot.py
```

---

### 4. Run Bacend API

```bash
uvicorn api.main:app --rload
```

---

## 📂 File tructure

```plaintext
hotel-kiosk/
├── hardware/
│   ├── read_name_en.py
│   ├── read_name_th.py
│   ├── check_card_status.py
│   ├── move_card_to_stacker.py
│   ├── wait_for_id_card.py
│   └── scan_passport.py
├── api/
│   ├── main.py
│   ├── endpoints/
│   │   └── read_card.py
│   └── models.py
├── utils/
│   └── serial_utils.py
├── config.ini
├── requirements.txt
├── README.md
└── LCENSE

---

## Use Case

This module is part of a **Hotel Self Check-in Kiosk** system to verify identity by reading name data directly from a Thai National ID card or passport, replacing mnual entry.

---

📢 Created by **Nipon Aemioo** | 2025  
🔗 For more info or integration support, contact via GitHub or LinkedIn

--- 
