import json
from modules.storage import HISTORY_FILE

def display_history():
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            history = json.load(f)
    except:
        print("No history found.")
        return
    for idx, entry in enumerate(history, 1):
        print(f"{idx}. Prefs: {entry['preferences']}")
        for i, o in enumerate(entry['suggestions'], 1):
            print(f"   {i}. {o['top']}, {o['bottom']}, {o['shoes']}")


