import sys
from scheduler import start_scheduler
from file_manager.scan_runner import run_scan
from file_manager.logger import undo_last_run
from brain import decide_action
from executor import execute_action


def natural_language_mode(user_input: str):
    action = decide_action(user_input)
    result = execute_action(action)
    print(result)


if __name__ == "__main__":

    # -----------------------------
    # 1. Natural language mode
    # -----------------------------
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        user_input = " ".join(sys.argv[1:])
        natural_language_mode(user_input)
        sys.exit()

    # -----------------------------
    # 2. Existing flags (unchanged)
    # -----------------------------
    if "--once" in sys.argv:
        print("Running single scan...\n")
        run_scan()
        print("Done.")

    elif "--undo" in sys.argv:
        undo_last_run()
        sys.exit()

    # -----------------------------
    # 3. Default → scheduler
    # -----------------------------
    else:
        start_scheduler()
