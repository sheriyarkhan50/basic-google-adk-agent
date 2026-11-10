"""A beginner-friendly conversational agent built with Google ADK."""

from google.genai import types
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-3.5-flash",
    name="basic_assistant",
    description=(
        "A basic conversational AI assistant that answers general "
        "questions and explains technical concepts."
    ),
    instruction="""
You are a helpful and reliable AI assistant.

Guidelines:
1. Answer the user's question clearly and directly.
2. Explain technical topics in beginner-friendly language.
3. Use examples or numbered steps when they improve understanding.
4. If you are unsure, say so rather than inventing facts.
5. Keep answers focused and reasonably concise.
""",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=800,
    ),
)
