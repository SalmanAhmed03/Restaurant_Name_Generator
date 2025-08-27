# llm.py
from __future__ import annotations
import os
from typing import Optional
from langchain_openai import ChatOpenAI

# --- HARD-CODED API KEY (for local testing only) ---
# ⚠️ Replace the placeholder below with your real key.
# ⚠️ Do NOT commit this file to Git, and rotate the key if it has been exposed anywhere.
OPENAI_API_KEY = "POST_YOUR_KEY"

def get_llm(
    model: str = "gpt-4o-mini",
    temperature: float = 0.6,
    timeout: Optional[float] = None,
) -> ChatOpenAI:
    if not OPENAI_API_KEY or OPENAI_API_KEY == "sk-proj-REPLACE_ME":
        raise RuntimeError(
            "OPENAI_API_KEY is not set in llm.py. Put your real key in the OPENAI_API_KEY variable."
        )

    # Ensure downstream libs see it
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # Return a ready ChatOpenAI client
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        timeout=timeout,
    )
