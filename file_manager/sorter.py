import yaml
import os
from pathlib import Path
from .ai_classifier import classify_file

CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

def decide_destination(file_path: str) -> str:
    ext = file_path.split(".")[-1].lower()

    # RULE-BASED FIRST
    for category, exts in config["rules"].items():
        if ext in exts:
            return config["destinations"][category]

    # IF AI DISABLED → send to others
    if not config.get("ai_enabled", True):
        return config["destinations"]["others"]

    # AI FALLBACK
    print(f"[AI fallback] {file_path}")
    ai_category = classify_file(file_path)

    if ai_category in config["destinations"]:
        return config["destinations"][ai_category]

    return config["destinations"]["others"]


