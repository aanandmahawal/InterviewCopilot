from utils.llm import call_llm

def mock_interviewer_node(state):

    answer = state.get("candidate_answer", "")
    question = state.get("current_question", "")

    prompt = f"""
    Evaluate the candidate answer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Give:

    Score out of 10

    Strengths

    Weaknesses

    Improved Answer

    Confidence Rating
    """

    response = call_llm(prompt)

    return {
        **state,
        "interview_feedback": response
    }