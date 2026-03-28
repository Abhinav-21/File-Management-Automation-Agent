import ollama

query = input("What do you want to ask?")

response = ollama.chat(
    model="qwen3:4b",
    messages=[{"role": "user", "content": query}]
)

print(response["message"]["content"])
