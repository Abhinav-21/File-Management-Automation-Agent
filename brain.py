import ollama
import json

SYSTEM_PROMPT = """
You are a local Windows coding assistant.

The system is Windows, not Linux.

Available tools:
1. run_terminal(command)
2. read_file(path)
3. write_file(path, content)
4. run_python(file)
5. search_files(keyword, path)

When listing files, use Windows commands like:
- dir
- dir /s

Return ONLY JSON:

{
  "tool": "...",
  "args": {...}
}
"""

def decide_action(user_input: str):
    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ],
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {"tool": "none", "args": {}}
