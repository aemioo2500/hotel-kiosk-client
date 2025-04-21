# main.py

import sys
from modules.thai_id import read_name_en, read_name_th, check_card_status, wait_for_card, reject_card
from modules.passport import scan_passport

def show_menu():
    print("\n========== Hotel Kiosk Client ==========")
    print("1. Read Thai ID (English Name)")
    print("2. Read Thai ID (Thai Name)")
    print("3. Check Card Status")
    print("4. Wait for Thai ID Card")
    print("5. Reject Card to Bin")
    print("6. Scan Passport (MRZ)")
    print("0. Exit")
    print("========================================")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("[📤] Reading English Name...")
            print(read_name_en.main())
        elif choice == "2":
            print("[📤] Reading Thai Name...")
            print(read_name_th.main())
        elif choice == "3":
            print("[📦] Checking Card Status...")
            print(check_card_status.main())
        elif choice == "4":
            print("[⏳] Waiting for Card...")
            print(wait_for_card.main())
        elif choice == "5":
            print("[🗑] Rejecting Card to Bin...")
            print(reject_card.main())
        elif choice == "6":
            print("[🌐] Scanning Passport MRZ...")
            print(scan_passport.main())
        elif choice == "0":
            print("Goodbye.")
            sys.exit()
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
