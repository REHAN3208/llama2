import requests
import json

API_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "tinyllama"

print("TinyLlama Chat (type 'exit' to quit)\n")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    try:
        response = requests.post(API_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt
        }, stream=True)

        print("TinyLlama: ", end="")
        full_text = ""

        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    token = data.get("response", "")
                    print(token, end="", flush=True)
                    full_text += token
                except json.JSONDecodeError:
                    pass

        print("\n")
    except requests.exceptions.ConnectionError:
        print("❌ Ollama server not running. Run: ollama serve\n")
        break

