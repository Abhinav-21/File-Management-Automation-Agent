import time
import yaml
import signal
import sys
from file_manager.scan_runner import run_scan

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

INTERVAL = config.get("schedule_hours", 12) * 3600
running = True


def stop_handler(sig, frame):
    global running
    print("\nStopping scheduler gracefully...")
    running = False


signal.signal(signal.SIGINT, stop_handler)
signal.signal(signal.SIGTERM, stop_handler)


def start_scheduler():
    print(f"File sorter running every {INTERVAL/3600} hours")
    print("Press Ctrl+C to stop.\n")

    while running:
        run_scan()

        if not running:
            break

        print(f"Sleeping for {INTERVAL/3600} hours...\n")

        for _ in range(int(INTERVAL)):
            if not running:
                break
            time.sleep(1)

    print("Scheduler stopped.")
    sys.exit(0)
