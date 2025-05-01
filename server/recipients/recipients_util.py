import json
import os

PHONE_FILE = os.path.join(os.path.dirname(__file__), "phone_numbers.json")

def load_phone_numbers():
    if not os.path.exists(PHONE_FILE):
        return []
    
    with open(PHONE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_phone_number(number):
    number = load_phone_numbers()
    if number not in number:
        number.append(number)
    with open(PHONE_FILE, "w") as f:
        json.dump(number, f, indent=2)
