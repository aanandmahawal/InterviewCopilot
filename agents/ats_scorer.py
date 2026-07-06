from utils.llm import call_llm_json


def ats_scorer_node(state):

    resume = state["resume_text"]
    jd = state["job_description"]

    prompt = f"""
You are an ATS (Applicant Tracking System) used by top technology companies
such as Qualcomm, Google, Microsoft, Amazon and NVIDIA.

Analyze the candidate resume against the job description.

Evaluate:

1. Technical Skills Match
2. Project Relevance
3. Experience Relevance
4. Education Fit
5. ATS Keyword Coverage

Return ONLY valid JSON.

Format:

{{
    "overall_score": 88,

    "technical_skills_score": 90,
    "projects_score": 85,
    "experience_score": 75,
    "education_score": 95,

    "matching_skills": [
        "Python",
        "FastAPI"
    ],

    "missing_skills": [
        "Kubernetes",
        "AWS"
    ],

    "strongest_projects": [
        "Project 1",
        "Project 2"
    ],

    "strengths": [
        "Strength 1",
        "Strength 2",
        "Strength 3"
    ],

    "improvements": [
        "Improvement 1",
        "Improvement 2",
        "Improvement 3"
    ],

    "recruiter_summary":
    "Short recruiter summary"
}}

Scoring Weights:

Technical Skills = 40%
Projects = 25%
Experience = 20%
Education = 15%

IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT wrap JSON inside ```json.
- All scores must be integers.
- Overall score must be realistic.
- matching_skills <= 10 items.
- missing_skills <= 10 items.
- strongest_projects <= 3 items.
- strengths must contain at least 3 items.
- improvements must contain at least 3 items.
- recruiter_summary <= 60 words.
- Never return empty arrays.

Resume:
{resume}

Job Description:
{jd}
"""

    ats_data = call_llm_json(prompt)

    if (
        not isinstance(ats_data, dict)
        or ats_data.get("error")
    ):

        ats_data = {
            "overall_score": 0,
            "technical_skills_score": 0,
            "projects_score": 0,
            "experience_score": 0,
            "education_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strongest_projects": [],
            "strengths": [
                "Unable to analyze strengths."
            ],
            "improvements": [
                "Unable to generate improvements."
            ],
            "recruiter_summary":
            "Unable to generate ATS report."
        }


    return {
        **state,
        "ats_report": ats_data
    }