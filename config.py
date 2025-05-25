import json, os
DEFAULT_CONFIG = {'email_notify': False, 'email_settings': {}}

def load_config(path=None):
    if path and os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return DEFAULT_CONFIG

