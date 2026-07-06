from utils.llm import call_llm


def career_advisor_node(state):

    resume = state["resume_text"]

    prompt = f"""
Act as a Senior AI Career Coach.

Analyze the resume and provide:

# Best-Fit Roles
- role
- role

# Skill Gaps
- gap
- gap

# Recommended Certifications
- certification
- certification

# Next Project Ideas
- idea
- idea

# 3-Month Learning Roadmap

Month 1:
...

Month 2:
...

Month 3:
...

Keep response concise.
Maximum 250 words.

Resume:
{resume}
"""

    response = call_llm(prompt)

    return {
        **state,
        "career_advice": response
    }