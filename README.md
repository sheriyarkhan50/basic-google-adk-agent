# Basic Google ADK Gemini Agent

A beginner-friendly conversational AI agent built with **Python**, **Google Agent Development Kit (ADK)** and **Gemini**. This project is my first hands-on step in learning how to build LLM-powered agents.

> **Project level:** Beginner  
> **Status:** Learning project / local development  
> **Primary language:** Python

## What this project does

The agent accepts a user's message, sends it to the configured Gemini model with a set of instructions, and returns a generated response.

It demonstrates the foundations of an LLM agent:

- Creating an agent with Google ADK.
- Selecting a language model.
- Writing an agent description and behavioral instructions.
- Configuring response temperature and output-token limits.
- Running and manually testing an agent locally.

## Current capabilities and limitations

### Included

- General conversational question answering.
- Beginner-friendly explanations.
- Configurable model and generation settings.
- Local command-line and browser-based testing through the ADK CLI.

### Not included yet

- Custom tools or external API calls.
- Persistent memory across sessions.
- Retrieval-Augmented Generation (RAG).
- Multi-agent orchestration.
- Production authentication, monitoring or deployment.

These are intentionally left for future projects so the first implementation stays easy to understand.

## Architecture

```text
User message
    |
    v
Google ADK runtime
    |
    v
Basic assistant agent
    |-- name and description
    |-- behavioral instructions
    |-- generation configuration
    |
    v
Configured Gemini model
    |
    v
Generated response
```

This is a simple LLM-powered agent. It does not independently plan multi-step tasks or use external tools yet.

## Project structure

```text
basic-google-adk-agent/
├── basic_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── .env.example
├── docs/
│   └── learning-notes.md
├── screenshots/
│   └── README.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python version supported by the current Google ADK release (use Python 3.10 or newer as a practical starting point; check the ADK installation guide for the current supported versions).
- A Google AI Studio API key for Gemini API access.
- Internet access while calling the hosted model.
- Git (optional, for version control).

## Setup and installation

Commands below use Windows PowerShell. On macOS or Linux, use `source .venv/bin/activate` to activate the virtual environment.

### 1. Clone the repository

```powershell
git clone https://github.com/YOUR-USERNAME/basic-google-adk-agent.git
cd basic-google-adk-agent
```

If you have not created the GitHub repository yet, create an empty repository first, then use its clone URL.

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure your API key

Get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Copy the example environment file:

```powershell
Copy-Item basic_agent/.env.example basic_agent/.env
```

Open `basic_agent/.env` and replace the placeholder with your key:

```env
GOOGLE_API_KEY=your_actual_api_key
```

**Security:** `basic_agent/.env` is ignored by Git. Never paste your real key into source code, screenshots, README files, public issues or commits. If a key is exposed, revoke it and create a replacement.

### 5. Run the agent in the terminal

From the repository root:

```powershell
adk run basic_agent
```

Enter a question when prompted. Use the CLI's exit instruction (commonly `exit` or `quit`) to end the session; follow the prompt shown by your installed ADK version.

### 6. Run the browser development interface

```powershell
adk web
```

Open the local address printed in the terminal (commonly `http://localhost:8000`). Select `basic_agent` in the interface and send a message.

The web interface is for local development and testing. Do not expose it publicly as a production application.

## Example prompts for manual testing

Try these after starting the agent:

| Test | Prompt | What to check |
|---|---|---|
| General knowledge | `Explain what an API is in simple words.` | Clear and relevant explanation |
| Technical learning | `What is the difference between an LLM and an AI agent?` | Correct distinction |
| Step-by-step | `Explain how a Python virtual environment works in 5 steps.` | Useful ordered steps |
| Uncertainty | `Tell me a fact you cannot verify from the information available.` | Does not pretend certainty |
| Conciseness | `Explain Git in two sentences.` | Respects the request for brevity |

Record the actual results you observe. Do not claim a test passed unless you ran it.

## Understanding the code

The main implementation is in [`basic_agent/agent.py`](basic_agent/agent.py).

- `Agent`: creates the ADK LLM agent.
- `model`: chooses the model that generates responses. The configured model name must be available to your account and supported by your installed ADK version.
- `name`: stable identifier for the agent.
- `description`: short summary of the agent's purpose.
- `instruction`: behavioral guidance given to the model.
- `temperature`: influences response variability. A lower value generally produces more consistent responses; it does not guarantee factual accuracy.
- `max_output_tokens`: limits the maximum generated output length.

## Troubleshooting

### `adk` is not recognized

Confirm the virtual environment is active, then run:

```powershell
python -m pip install -r requirements.txt
python -m pip show google-adk
```

Close and reopen the terminal if the executable is still not found.

### API key or authentication error

- Confirm the key is valid and enabled for the Gemini API.
- Check that the file is named `.env`, not `.env.txt`.
- Confirm it is located inside `basic_agent/`.
- Restart the ADK command after changing environment variables.

### Model not found or unavailable

The model identifier in `agent.py` may not be available to your account or current ADK/provider configuration. Check the current Gemini model catalogue and replace `gemini-3.5-flash` with a model ID currently available to you.

### Import error

Activate the virtual environment and reinstall dependencies:

```powershell
python -m pip install --upgrade google-adk
```

## Learning outcomes

By completing this project, I am practicing how to:

1. Set up a Python project and isolated environment.
2. Initialize an LLM agent with Google ADK.
3. Configure model behavior using instructions and generation settings.
4. Authenticate to a hosted model API without hardcoding secrets.
5. Run and manually evaluate an agent locally.
6. Document an AI project so another developer can reproduce it.

## Roadmap

- [ ] Add and document a custom Python tool.
- [ ] Connect an external API through a tool.
- [ ] Explore ADK sessions and conversation state.
- [ ] Build a document question-answering RAG agent.
- [ ] Experiment with multi-agent workflows.
- [ ] Add automated evaluation and error handling.
- [ ] Expose the agent through an API and deploy it securely.

## References

- [Google ADK documentation](https://google.github.io/adk-docs/)
- [ADK Python quickstart](https://google.github.io/adk-docs/get-started/quickstart/)
- [Google AI Studio API keys](https://aistudio.google.com/app/apikey)
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)

## Author

**Your Name**  
Full Stack Developer | Learning AI Engineering

- GitHub: [@sheriyarkhan50](https://github.com/sheriyarkhan50)
- LinkedIn: [muhammad-sheriyar-khan-36669814b](https://www.linkedin.com/in/muhammad-sheriyar-khan-36669814b/)

---

*This is a learning project. The implementation and documentation will evolve as I explore more agent engineering concepts.*
