import yaml
import os

from file_manager.logger import save_last_run
from .sorter import decide_destination
from .mover import move_file
from .logger import save_last_run

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def run_scan():
    print("Starting scheduled scan...")

    for folder in config["watch_folders"]:
        for f in os.listdir(folder):
            path = os.path.join(folder, f)

            if os.path.isfile(path):
                try:
                    dest = decide_destination(path)
                    move_file(path, dest)
                except Exception as e:
                    print("Error:", e)

    print("Scan complete.")
    save_last_run()
