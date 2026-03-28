from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import yaml
from .sorter import decide_destination
from .mover import move_file
import os

def scan_existing():
    print("Scanning existing files...")

    for folder in config["watch_folders"]:
        for f in os.listdir(folder):
            path = os.path.join(folder, f)

            if os.path.isfile(path):
                try:
                    dest = decide_destination(path)
                    move_file(path, dest)
                except Exception as e:
                    print("Scan error:", e)


with open("agent/config.yaml", "r") as f:
    config = yaml.safe_load(f)

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        path = str(event.src_path)
        time.sleep(1)

        dest = decide_destination(path)
        move_file(path, dest)

def start_watcher():
    scan_existing()
    observer = Observer()
    handler = Handler()

    for folder in config["watch_folders"]:
        observer.schedule(handler, folder, recursive=False)

    observer.start()
    print("File watcher running...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
