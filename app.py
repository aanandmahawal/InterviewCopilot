# python -m streamlit run app.py

import json
from datetime import datetime

import streamlit as st
import plotly.graph_objects as go

from agents.resume_analyzer import resume_analyzer_node
from agents.ats_scorer import ats_scorer_node
from agents.jd_matcher import jd_matcher_node
from agents.interview_generator import interview_generator_node
from agents.career_advisor import career_advisor_node
from utils.parser import extract_pdf_text

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="AI Resume & Interview Copilot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------
# SIDEBAR
# ---------------------------------

with st.sidebar:

    st.title("🤖 AI Resume Copilot")

    st.markdown("---")

    st.markdown("""
### Features

✅ ATS Score Analysis

✅ Resume Analysis

✅ JD Matching

✅ Interview Questions

✅ Career Guidance

✅ Multi-Agent Workflow

✅ LangGraph Powered

✅ Recruiter Style Evaluation
""")

    st.markdown("---")

    st.info(
        """
Upload a Resume and compare it against a Job Description.

Perfect for:

• AI Engineer  
• ML Engineer  
• Data Scientist  
• Software Engineer  
• GenAI Roles
"""
    )

# ---------------------------------
# HEADER
# ---------------------------------

st.title("🤖 Multi-Agent AI Resume & Interview Copilot")

st.caption(
    "Analyze resumes, evaluate ATS compatibility, generate interview questions and receive personalized career guidance."
)

st.markdown("---")

# ---------------------------------
# INPUTS
# ---------------------------------

col1, col2 = st.columns(2)

with col1:

    resume_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

    if resume_file:
        st.success("Resume Uploaded")

with col2:

    jd = st.text_area(
        "💼 Paste Job Description",
        height=250,
        placeholder="Paste complete Job Description..."
    )

    if jd.strip():
        st.success("Job Description Added")

# ---------------------------------
# ANALYZE
# ---------------------------------

if st.button(
    "🚀 Analyze Resume",
    use_container_width=True
):

    missing = []

    if resume_file is None:
        missing.append("Resume")

    if not jd.strip():
        missing.append("Job Description")

    if missing:

        if len(missing) == 2:

            st.warning(
                "⚠ Please upload a Resume and provide a Job Description."
            )

        else:

            st.warning(
                f"⚠ Missing: {missing[0]}"
            )

        st.stop()

    # ---------------------------------
    # SAVE PDF
    # ---------------------------------

    with open("resume.pdf", "wb") as f:
        f.write(resume_file.getbuffer())

    # ---------------------------------
    # LOADING
    # ---------------------------------

    progress = st.progress(0)

    status = st.empty()

    status.info("📄 Parsing Resume...")
    progress.progress(10)

    resume_text = extract_pdf_text(
        "resume.pdf"
    )

    state = {
        "resume_text": resume_text,
        "job_description": jd
    }

    # Resume Analysis
    status.info("📄 Analyzing Resume...")
    progress.progress(20)

    state = resume_analyzer_node(state)

    # ATS Analysis
    status.info("🎯 Calculating ATS Score...")
    progress.progress(40)

    state = ats_scorer_node(state)

    # JD Matching
    status.info("💼 Matching Resume with JD...")
    progress.progress(60)

    state = jd_matcher_node(state)

    # Interview Questions
    status.info("🎤 Generating Interview Questions...")
    progress.progress(80)

    state = interview_generator_node(state)

    # Career Advice
    status.info("🚀 Generating Career Roadmap...")
    progress.progress(95)

    state = career_advisor_node(state)

    progress.progress(100)

    result = state

    status.success(
        "✅ Analysis Completed Successfully"
    )

    st.markdown("---")

    # ---------------------------------
    # ATS DATA
    # ---------------------------------

    ats = result["ats_report"]

    ats_score = ats.get(
        "overall_score",
        0
    )

    # ---------------------------------
    # ATS SCORE
    # ---------------------------------

    st.subheader(
        "📊 ATS Compatibility Score"
    )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=ats_score,
            title={
                "text": "ATS Match Score"
            },
            gauge={
                "axis": {"range": [0, 100]},
                "steps": [
                    {"range": [0, 50]},
                    {"range": [50, 75]},
                    {"range": [75, 100]}
                ],
                "threshold": {
                    "line": {"width": 4},
                    "value": ats_score
                }
            }
        )
    )

    fig.update_layout(
        height=320
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # ---------------------------------
    # KPI CARDS
    # ---------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "ATS Score",
        f"{ats.get('overall_score',0)}%"
    )

    c2.metric(
        "Skills Match",
        f"{ats.get('technical_skills_score',0)}%"
    )

    c3.metric(
        "Projects Match",
        f"{ats.get('projects_score',0)}%"
    )

    c4.metric(
        "Experience Match",
        f"{ats.get('experience_score',0)}%"
    )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.success("⭐ Key Strengths")

        strengths = ats.get("strengths", [])

        if strengths:

            for item in strengths:

                st.markdown(
                    f"- ✅ {item}"
                )

        else:

            st.info(
                "No strengths identified."
            )

    with right:

        st.warning("🔧 Improvement Areas")

        improvements = ats.get("improvements", [])

        if improvements:

            for item in improvements:

                st.markdown(
                    f"- 🔧 {item}"
                )

        else:

            st.info(
                "No improvement areas identified."
            )

    st.markdown("---")

    # ---------------------------------
    # EXTRA STATS
    # ---------------------------------

    s1, s2, s3 = st.columns(3)

    s1.metric(
        "Matching Skills",
        len(
            ats.get(
                "matching_skills",
                []
            )
        )
    )

    s2.metric(
        "Missing Skills",
        len(
            ats.get(
                "missing_skills",
                []
            )
        )
    )

    s3.metric(
        "Generated",
        datetime.now().strftime("%H:%M")
    )

    st.markdown("---")

    # ---------------------------------
    # RECRUITER SUMMARY
    # ---------------------------------

    st.subheader(
        "📝 Recruiter Summary"
    )

    st.info(
        ats.get(
            "recruiter_summary",
            "No summary available."
        )
    )

    st.markdown("---")

    # ---------------------------------
    # TABS
    # ---------------------------------

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📄 Resume Analysis",
            "🎯 ATS Report",
            "💼 JD Match",
            "🎤 Interview Questions",
            "🚀 Career Advice"
        ]
    )

    # ---------------------------------
    # TAB 1
    # ---------------------------------

    with tab1:

        st.markdown(
            result["resume_analysis"]
        )

    # ---------------------------------
    # TAB 2
    # ---------------------------------

    with tab2:

        col1, col2 = st.columns(2)

        with col1:

            st.success(
                "Matching Skills"
            )

            for skill in ats.get(
                "matching_skills",
                []
            ):
                st.write(
                    f"✅ {skill}"
                )

        with col2:

            st.warning(
                "Missing Skills"
            )

            for skill in ats.get(
                "missing_skills",
                []
            ):
                st.write(
                    f"❌ {skill}"
                )

        st.markdown("---")

        st.subheader(
            "🚀 Strongest Projects"
        )

        for project in ats.get(
            "strongest_projects",
            []
        ):
            st.write(
                f"🚀 {project}"
            )

    # ---------------------------------
    # TAB 3
    # ---------------------------------

    with tab3:

        st.markdown(
            result["jd_match_report"]
        )

    # ---------------------------------
    # TAB 4
    # ---------------------------------

    with tab4:

        st.markdown(
            result["interview_questions"]
        )

    # ---------------------------------
    # TAB 5
    # ---------------------------------

    with tab5:

        st.markdown(
            result["career_advice"]
        )

    # ---------------------------------
    # DOWNLOAD REPORT
    # ---------------------------------

    report = f"""
Resume Analysis

{result['resume_analysis']}

ATS Report

{json.dumps(ats, indent=2)}

JD Match

{result['jd_match_report']}

Interview Questions

{result['interview_questions']}

Career Advice

{result['career_advice']}
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )