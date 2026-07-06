from typing import TypedDict, List, Dict


class InterviewCopilotState(TypedDict):
    resume_text: str
    job_description: str

    resume_analysis: str

    ats_report: str
    ats_score: int

    jd_match_report: str
    match_percentage: int

    interview_questions: str

    current_question: str
    candidate_answer: str
    interview_feedback: str

    career_advice: str