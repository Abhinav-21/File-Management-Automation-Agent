import ollama
import os

MODEL = "gemma3:1b"

PROMPT = """
Classify this file into ONE category from this list:

images
documents
code
archives
video
audio
others

Filename: {name}

Return ONLY the category word.
"""

def classify_file(file_path: str) -> str:
    name = os.path.basename(file_path)

    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{
                "role": "user",
                "content": PROMPT.format(name=name)
            }]
        )

        result = response["message"]["content"].strip().lower()

        allowed = [
            "images","documents","code",
            "archives","video","audio","others"
        ]

        if result not in allowed:
            return "others"

        print(f"[AI] {name} → {result}")
        return result

    except Exception as e:
        print("AI error:", e)
        return "others"
