import ollama

query = input("What do you want to ask?")

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[{"role": "user", "content": query}]
)

print(response["message"]["content"])
