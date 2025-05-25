import json, os
HISTORY_FILE = 'data/history.json'

def save_history(prefs, suggestions):
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    entry = {'preferences': prefs, 'suggestions': suggestions}
    history = []
    if os.path.isfile(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except:
            history = []
    history.append(entry)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

