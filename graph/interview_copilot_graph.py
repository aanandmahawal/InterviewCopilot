from langgraph.graph import StateGraph, START, END

from graph.state import InterviewCopilotState

from agents.resume_analyzer import resume_analyzer_node
from agents.ats_scorer import ats_scorer_node
from agents.jd_matcher import jd_matcher_node
from agents.interview_generator import interview_generator_node
from agents.career_advisor import career_advisor_node

builder = StateGraph(InterviewCopilotState)

builder.add_node(
    "resume_analyzer",
    resume_analyzer_node
)

builder.add_node(
    "ats_scorer",
    ats_scorer_node
)

builder.add_node(
    "jd_matcher",
    jd_matcher_node
)

builder.add_node(
    "interview_generator",
    interview_generator_node
)

builder.add_node(
    "career_advisor",
    career_advisor_node
)

builder.add_edge(
    START,
    "resume_analyzer"
)

builder.add_edge(
    "resume_analyzer",
    "ats_scorer"
)

builder.add_edge(
    "ats_scorer",
    "jd_matcher"
)

builder.add_edge(
    "jd_matcher",
    "interview_generator"
)

builder.add_edge(
    "interview_generator",
    "career_advisor"
)

builder.add_edge(
    "career_advisor",
    END
)

compiled_graph = builder.compile()