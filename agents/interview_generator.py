from utils.llm import call_llm


def interview_generator_node(state):

    resume = state["resume_text"]
    jd = state["job_description"]

    prompt = f"""
Act as a Senior Interviewer.

Generate:

## Technical Questions
5 questions

## Project Questions
3 questions

## Behavioral Questions
1 questions

## HR Questions
1 questions

Only generate questions.

DO NOT generate answers.

Focus on:
- Resume projects
- AI/ML
- GenAI
- RAG
- System Design
- Job Description requirements

Resume:
{resume}

Job Description:
{jd}
"""

    response = call_llm(prompt)

    return {
        **state,
        "interview_questions": response
    }
