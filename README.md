# vaibhav-gpt-chatbot
Free chatbot vaibhav sonar
# 💬 Vaibhav's GPT Chatbot (OpenRouter)

A simple chatbot using OpenRouter + Gradio, free to run locally.

## 🧠 Requirements

- Python 3.10+ installed
- Your OpenRouter API key from https://openrouter.ai/keys

## 🚀 Run the Bot

```bash
# 1. Clone this repository
git clone https://github.com/your-username/vaibhav-gpt-chatbot
cd vaibhav-gpt-chatbot

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install required libraries
pip install -r requirements.txt

# 4. Set your API key securely
export OPENROUTER_API_KEY="sk-or-your-key"  # Linux/macOS
# OR
set OPENROUTER_API_KEY=sk-or-your-key       # Windows CMD
# OR
$env:OPENROUTER_API_KEY="sk-or-your-key"    # PowerShell

# 5. Run the chatbot
python chatbot.py
