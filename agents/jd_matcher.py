from utils.llm import call_llm


def jd_matcher_node(state):

    resume = state["resume_text"]
    jd = state["job_description"]

    prompt = f"""
You are a Senior Technical Recruiter.

Compare the candidate's resume against the job description.

Return ONLY:

# Match Percentage
XX%

# Matching Skills
- skill
- skill

# Missing Skills
- skill
- skill

# Relevant Projects
- project
- project

# Hiring Recommendation
One concise paragraph.

Keep response under 200 words.

Resume:
{resume}

Job Description:
{jd}
"""

    response = call_llm(prompt)

    return {
        **state,
        "jd_match_report": response
    }