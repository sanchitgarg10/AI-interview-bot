import os
from env_config import OPENAI_API_KEY

# Set your preferred provider
PROVIDER = "openai"  # or "claude", "deepseek", "perplexity"

# Set your OpenAI model
#OPENAI_MODEL = "gpt-4"
OPENAI_MODEL = "gpt-3.5-turbo"  

# Extend here for Claude, DeepSeek, Perplexity, etc.
MODELS = {
    "openai": {
        "api_key": OPENAI_API_KEY,
        "model": OPENAI_MODEL,
        "client": "openai"  # used to route logic
    },
    # "claude": {...}
}
