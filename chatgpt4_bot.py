import gradio as gr
import requests

# ✅ Use your real OpenRouter API key here
API_KEY = "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"

def chat_with_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # ✅ Correct formatting
        "Content-Type": "application/json"
    }

    model = "mistralai/mistral-7b-instruct"  # ✅ Free, fast, and stable

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

gr.Interface(
    fn=chat_with_openrouter,
    inputs="text",
    outputs="text",
    title="Vaibhav's Free GPT Chatbot (OpenRouter)"
).launch(share=True)
