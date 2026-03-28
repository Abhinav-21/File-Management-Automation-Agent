import shutil
import os
import yaml
from pathlib import Path
from .logger import log_move

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

DRY_RUN = config.get("dry_run", False)


def move_file(src: str, dest_folder: str):
    try:
        os.makedirs(dest_folder, exist_ok=True)

        filename = os.path.basename(src)
        dest = os.path.join(dest_folder, filename)

        base, ext = os.path.splitext(filename)
        counter = 1

        while os.path.exists(dest):
            dest = os.path.join(dest_folder, f"{base}_{counter}{ext}")
            counter += 1

        if DRY_RUN:
            print(f"[DRY RUN] {src} → {dest}")
            return

        shutil.move(src, dest)
        log_move(src, dest)

        print(f"Moved: {filename} → {dest}")

    except Exception as e:
        print("Move error:", e)
