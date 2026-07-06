from utils.llm import call_llm


def resume_analyzer_node(state):

    resume = state["resume_text"]

    prompt = f"""
You are a Senior Technical Recruiter.

Analyze the resume and return ONLY the following sections.

## Technical Skills
- List top technical skills

## Key Projects
- Project Name
- One-line description

## Strengths
- 5 bullet points

## Areas of Improvement
- 3 bullet points

Keep the response concise.
Maximum 250 words.

Resume:
{resume}
"""

    response = call_llm(prompt)

    return {
        **state,
        "resume_analysis": response
    }