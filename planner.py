import json
import subprocess

MODEL = "gemma3:1b"

SYSTEM_PROMPT = """
You are a local filesystem agent.
You must respond ONLY in JSON.

Available tools:
- create_text_file(path, content)
- list_files(path)
- delete_file(path)

Return format:
{
  "tool": "...",
  "args": {...}
}
"""

def ask_llm(prompt: str) -> dict:
    full_prompt = SYSTEM_PROMPT + "\nUser: " + prompt

    result = subprocess.run(
        ["ollama", "run", MODEL, full_prompt],
        capture_output=True,
        text=True,
    )

    try:
        return json.loads(result.stdout.strip())
    except:
        return {"tool": None}
