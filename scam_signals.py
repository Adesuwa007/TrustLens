# scam_signals.py
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "scam_signals.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    SCAM_SIGNALS = json.load(f)