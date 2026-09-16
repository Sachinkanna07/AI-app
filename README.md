# Sachin AI Chat

A lightweight AI chat application built with Python and Streamlit, using Google's Gemini API for response generation.

## Features

- Simple Streamlit chat interface
- Gemini-powered text generation
- API credentials loaded securely from environment variables or Streamlit secrets
- Input validation and loading feedback

## Tech Stack

- Python
- Streamlit
- Google Generative AI SDK

## Run Locally

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your Gemini API key as an environment variable:

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

4. Start the app:

```bash
streamlit run app.py
```

## Security

Never commit API keys or other credentials to source control. If a key has ever been committed publicly, revoke it and generate a new one even after removing it from the current code.

## Author

Sachin Kanna M — Computer Science Engineering student interested in full-stack development, AI, and building practical software products.
