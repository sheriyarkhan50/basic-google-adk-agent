# Learning Notes — Basic Google ADK Gemini Agent

These notes explain the concepts used in the first agent in plain language. Add your own observations as you experiment.

## 1. What is an LLM?

A Large Language Model (LLM) is a machine-learning model trained to process and generate language. It can answer questions, summarize text, explain code and generate content.

An LLM by itself does not automatically have access to your database, files or external services. Those capabilities need to be provided through tools, integrations or retrieval systems.

## 2. What is an AI agent?

An AI agent is an application that uses a model and additional components to work toward a task. Depending on its design, it may use instructions, tools, state, workflows and other agents.

The first project is intentionally simple: it is an LLM-powered conversational agent with no custom tools.

## 3. What is Google ADK?

Google Agent Development Kit (ADK) is a framework for developing, testing and deploying AI agents. It provides agent abstractions and runtime/development tools.

Official documentation: https://google.github.io/adk-docs/

## 4. Understanding the implementation

```python
from google.genai import types
from google.adk.agents.llm_agent import Agent
```

- `google.genai.types` provides typed configuration objects for Google GenAI.
- `Agent` is the ADK class used to define this LLM agent.

### Model

```python
model="gemini-3.5-flash"
```

The model is the language model used to generate the response. Model IDs and availability can change. If this ID is unavailable, use a currently supported Gemini model ID from the official model documentation.

### Name

```python
name="basic_assistant"
```

A code-friendly identifier for this agent.

### Description

```python
description="A basic conversational AI assistant..."
```

A short explanation of what the agent is designed to do. It helps developers and agent workflows understand the agent's purpose.

### Instruction

```python
instruction="You are a helpful and reliable AI assistant..."
```

Instructions define the agent's role and response guidelines. They influence behavior but are not a substitute for code-level validation, authorization or security controls.

### Temperature

```python
temperature=0.3
```

Temperature controls the variability of generated output. Lower values generally make outputs more predictable; higher values allow more variation. It does not make an answer more truthful.

### Maximum output tokens

```python
max_output_tokens=800
```

A limit on generated output length. Tokens are pieces of text; they are not exactly the same as words or characters.

## 5. Agent versus tool

An instruction tells the model how to respond. A tool gives the agent a way to invoke a defined capability, such as calling a Python function or an API.

Example future tool ideas:

- Look up a vehicle by VIN in an authorized API.
- Retrieve current weather from a weather API.
- Search a set of company documents.
- Query an approved database through a controlled backend function.

Never give an agent unrestricted database or shell access. Validate inputs and enforce permissions in the application.

## 6. How a request flows through this project

1. A user submits a message.
2. The ADK runtime sends the message to the agent.
3. The agent's instructions and generation configuration are applied.
4. The configured Gemini model generates a response.
5. The runtime returns the response to the user.

## 7. Experiments to perform

Change one setting at a time and compare outputs:

| Experiment | Change | Observation to record |
|---|---|---|
| A | Temperature `0.1` vs `0.8` | How does wording vary? |
| B | Output limit `200` vs `800` | How does response length change? |
| C | Concise instruction vs detailed instruction | Does response structure change? |
| D | Ask an ambiguous question | Does the agent ask for clarification or state uncertainty? |

Run each experiment more than once. Model output can vary, so avoid drawing conclusions from a single response.

## 8. Testing checklist

- [ ] Agent starts without import errors.
- [ ] A simple question receives a response.
- [ ] A technical question receives a relevant explanation.
- [ ] A request for a short answer is handled concisely.
- [ ] An ambiguous question does not lead to invented certainty.
- [ ] Invalid or missing API credentials produce a diagnosable error.
- [ ] No API key is committed to Git.

Write down the date, model ID, prompt and observed result for important experiments.

## 9. Glossary

- **LLM:** Large Language Model.
- **Prompt:** Input sent to a model.
- **Instruction / system guidance:** High-level behavioral guidance for an agent.
- **Token:** A unit of text processed by a model.
- **Temperature:** A generation setting that influences variability.
- **Tool calling:** A model-driven request for an application to execute a defined function.
- **Session:** A conversation context managed by an application or agent runtime.
- **RAG:** Retrieval-Augmented Generation; retrieving relevant information and supplying it to a model to help answer a question.
- **Evaluation:** Measuring an agent's behavior against defined criteria.

## 10. My reflection

Complete these after running the project:

- What I understood:
- What confused me:
- What error I faced and how I fixed it:
- One experiment I performed:
- What I want to build next:
