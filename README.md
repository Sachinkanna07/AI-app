# Sachin AI Chat

A lightweight conversational AI application built with **Python** and **Streamlit**, using Google's Gemini API for response generation.

> **Project status:** this repository is the current lightweight baseline. A broader upgrade is planned, so the project is intentionally kept simple and easy to inspect.

## Current capabilities

- Streamlit-based chat interface
- Gemini-powered text generation
- API credentials loaded from environment variables or Streamlit secrets
- Basic input validation and loading feedback
- Minimal dependency footprint

## Tech stack

- Python
- Streamlit
- Google Generative AI SDK

## Run locally

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your Gemini API key:

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

4. Start the app:

```bash
streamlit run app.py
```

## Planned upgrade

The next version is intended to move beyond a basic chat demo. Planned areas include:

- stronger product UI and interaction design
- conversation memory and context management
- tool / API integration
- structured prompt and response handling
- evaluation and reliability checks
- production-ready deployment workflow

These are roadmap items, not current capabilities.

## Security

Never commit API keys or other credentials to source control. If a key has ever been committed publicly, revoke it and generate a new one even after removing it from the current code.

## Author

**Sachin Kanna M**  
Computer Science Engineering student focused on full-stack/backend development and applied AI.
