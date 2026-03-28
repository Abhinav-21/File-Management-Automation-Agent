import ollama

query = input("What do you want to ask?")

response = ollama.chat(
    model="gemma3:1b",
    messages=[{"role": "user", "content": query}]
)

print(response["message"]["content"])
