import subprocess
import platform

ALLOWED = [
    "dir",
    "echo",
    "type",
    "mkdir",
    "copy",
    "move",
    "del",
    "rename",
    "python",
]

BLOCKED_PATTERNS = [
    "format",
    "shutdown",
    "taskkill",
    "reg",
    "powershell",
]


def run_terminal(command: str) -> str:
    try:
        cmd = command.strip().lower()

        # -------------------------
        # Hard block dangerous stuff
        # -------------------------
        if any(b in cmd for b in BLOCKED_PATTERNS):
            return "Command blocked for safety."

        # -------------------------
        # Allow-list enforcement
        # -------------------------
        if not any(cmd.startswith(c) for c in ALLOWED):
            return "Command not allowed."

        # -------------------------
        # Linux → Windows mapping
        # -------------------------
        if platform.system() == "Windows":
            if cmd == "ls":
                command = "dir"
            if cmd.startswith("ls "):
                command = command.replace("ls", "dir", 1)

        # -------------------------
        # Execute
        # -------------------------
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )

        return result.stdout + result.stderr

    except Exception as e:
        return str(e)
