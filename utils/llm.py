import os
import json
import time
import re

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# =====================================
# API KEY VALIDATION
# =====================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found in .env file"
    )

# =====================================
# LLM CONFIG
# =====================================
# llama-3.3-70b-versatile was deprecated by Groq (June 2026) for
# free/developer tiers. openai/gpt-oss-120b is Groq's recommended
# replacement. Override without code changes by setting GROQ_MODEL
# in .env if Groq deprecates this one too:
#   GROQ_MODEL=qwen/qwen3.6-27b

GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

llm = ChatGroq(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY,
    temperature=0.2,
)

# =====================================
# SYSTEM PROMPT
# =====================================

SYSTEM_PROMPT = """
You are an expert:

- ATS Specialist
- Technical Recruiter
- Resume Reviewer
- AI Career Coach
- Interviewer

Rules:
1. Be concise and professional.
2. Use markdown formatting.
3. Prefer bullet points.
4. Give recruiter-style feedback.
5. Focus on technical hiring standards.
6. Provide actionable suggestions.
7. Avoid unnecessary explanations.
"""

# =====================================
# TEXT RESPONSE
# =====================================

def call_llm(prompt: str, retries: int = 3):

    final_prompt = f"""
{SYSTEM_PROMPT}

{prompt}
"""

    for attempt in range(retries):

        try:

            response = llm.invoke(
                final_prompt
            )

            return response.content.strip()

        except Exception as e:

            if attempt == retries - 1:

                return f"""
### Error

Unable to generate response.

Reason:
{str(e)}
"""

            time.sleep(2)

# =====================================
# JSON RESPONSE
# =====================================

def call_llm_json(
    prompt: str,
    retries: int = 3
):

    final_prompt = f"""
{SYSTEM_PROMPT}

IMPORTANT:

Return ONLY valid JSON.

Do NOT:

- Use markdown
- Use ```json
- Add explanations
- Add comments

{prompt}
"""

    for attempt in range(retries):

        try:

            response = llm.invoke(
                final_prompt
            )

            text = response.content.strip()

            # Remove markdown wrappers

            text = text.replace(
                "```json",
                ""
            )

            text = text.replace(
                "```",
                ""
            )

            text = text.strip()

            # Extract JSON safely

            match = re.search(
                r"\{.*\}",
                text,
                re.DOTALL
            )

            if match:

                text = match.group()

            data = json.loads(text)

            return data

        except Exception as e:

            if attempt == retries - 1:

                return {
                    "error": True,
                    "message": str(e),
                    "raw_response": text if "text" in locals() else ""
                }

            time.sleep(2)

# =====================================
# CONNECTION TEST
# =====================================

def test_connection():

    try:

        response = llm.invoke(
            "Reply only with OK"
        )

        return response.content.strip()

    except Exception as e:

        return str(e)

# =====================================
# LOCAL TEST
# =====================================

if __name__ == "__main__":

    print(
        "\nGroq Connection Test:"
    )

    print(
        test_connection()
    )
