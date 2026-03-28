from tools.terminal_tool import run_terminal
from tools.file_tool import read_file
from tools.file_tool import write_file
from tools.python_tool import run_python
from tools.search_tool import search_files

TOOLS = {
    "run_terminal": run_terminal,
    "read_file": read_file,
    "write_file": write_file,
    "run_python": run_python,
    "search_files": search_files,
}

def execute_action(action: dict):
    tool = action.get("tool")
    args = action.get("args", {})

    if tool == "none" or tool not in TOOLS:
        return "No valid action."

    try:
        return TOOLS[tool](**args)
    except Exception as e:
        return f"Execution error: {e}"
