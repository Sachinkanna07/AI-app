# Sachin AI Chat

A small Streamlit app for asking Gemini one question at a time. The whole request path fits in [one Python file](app.py).

[Run the interface](#run-the-interface) · [Try a question](#try-a-question) · [Project roadmap](#project-roadmap)

## Try a question

Enter **“Explain a Python dictionary with a two-line example”** in **Ask a question**, then select **Generate**. The app checks for blank input, shows a spinner while Gemini responds, and displays the returned text. Each submission starts with an empty chat history, so include any context in the question itself.

> **Model compatibility**  
> This version targets `gemini-pro` through the legacy `google-generativeai` package. The interface can launch independently of model availability. If the API rejects the model ID, the integration needs a supported model and SDK. [Google’s migration guide](https://ai.google.dev/gemini-api/docs/migrate)

## Run the interface

From a local checkout, install the two packages listed in [requirements.txt](requirements.txt).

```sh
python -m pip install -r requirements.txt
```

Set `GEMINI_API_KEY` in the environment that starts Streamlit, or add an entry with that name to your deployment’s Streamlit secrets. Keep the value out of source control. If a key was ever committed, revoke it with the provider and issue a replacement.

```sh
python -m streamlit run app.py
```

Open the local address printed by Streamlit. A missing key produces a configuration message before the question field appears.

## Project roadmap

The planned next steps are conversation memory, tool and API integration, structured responses, evaluation checks, and a more complete deployment workflow and interface.

Built by [Sachin Kanna M](https://github.com/Sachinkanna07).
