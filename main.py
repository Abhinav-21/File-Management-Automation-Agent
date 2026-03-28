from brain import decide_action
from tools.terminal_tool import run_terminal
from tools.file_tool import read_file
from tools.file_tool import write_file
from tools.python_tool import run_python
from tools.search_tool import search_files
from file_manager.watcher import start_watcher

while True:
    user_input = input("\n> ")

    if user_input == "exit":
        break

    if user_input == "start file watcher":
        start_watcher()
        continue

    action = decide_action(user_input)

    tool = action.get("tool")
    args = action.get("args", {})

    if tool == "run_terminal":
        result = run_terminal(args.get("command", ""))
        
    elif tool == "read_file":
        result = read_file(args.get("path", ""))
    
    elif tool == "write_file":
        result = write_file(
            args.get("path", ""),
            args.get("content", "")
        )
    
    elif tool == "run_python":
        result = run_python(args.get("file", ""))

    elif tool == "search_files":
        result = search_files(
            args.get("keyword", ""),
            args.get("path", ".")
        )
    else:
        result = "No valid tool selected."

    print("\n--- RESULT ---")
    print(result)
