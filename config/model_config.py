import os
from config import OPENAI_API_KEY

# Set your preferred provider
PROVIDER = "openai"  # or "claude", "deepseek", "perplexity"

# Set your OpenAI model
OPENAI_MODEL = "gpt-4"

# Extend here for Claude, DeepSeek, Perplexity, etc.
MODELS = {
    "openai": {
        "api_key": OPENAI_API_KEY,
        "model": OPENAI_MODEL,
        "client": "openai"  # used to route logic
    },
    # "claude": {...}
}
