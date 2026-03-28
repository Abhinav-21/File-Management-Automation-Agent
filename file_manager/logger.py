from datetime import datetime
import json
import os

LOG_FILE = "agent/file_manager/file_log.txt"
UNDO_FILE = "agent/file_manager/last_run.json"

last_run = []

def log_move(src: str, dest: str):
    global last_run

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | MOVED | {src} -> {dest}\n")

    last_run.append({"src": src, "dest": dest})


def save_last_run():
    with open(UNDO_FILE, "w", encoding="utf-8") as f:
        json.dump(last_run, f, indent=2)


def undo_last_run():
    if not os.path.exists(UNDO_FILE):
        print("No undo data.")
        return

    with open(UNDO_FILE, "r") as f:
        moves = json.load(f)

    for m in reversed(moves):
        try:
            if os.path.exists(m["dest"]):
                os.rename(m["dest"], m["src"])
                print(f"Undo: {m['dest']} → {m['src']}")
        except Exception as e:
            print("Undo error:", e)
