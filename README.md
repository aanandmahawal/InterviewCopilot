# Multi-Agent AI Resume & Interview Copilot

An AI-powered career assistant that analyzes resumes, evaluates ATS compatibility, compares candidates against job descriptions, generates interview questions, and provides personalized career guidance using a multi-agent architecture.

Instead of relying on a single prompt-response interaction, this system uses multiple specialized AI agents coordinated through LangGraph. Each agent performs a dedicated task and passes structured outputs to the next stage, creating a recruiter-style evaluation workflow.

---

## Overview

Most resume analyzers focus only on keyword matching or generate generic ATS scores. Recruiters, however, evaluate candidates across multiple dimensions including skills, projects, experience, role fit, and interview readiness.

This project simulates that process through a multi-agent workflow that:

- Analyzes resumes
- Evaluates ATS compatibility
- Matches resumes against job descriptions
- Identifies strengths and skill gaps
- Generates interview questions
- Provides career recommendations

---

## Architecture

```text
User Uploads Resume + Job Description
                │
                ▼
          PDF Parser
                │
                ▼
        LangGraph Workflow
                │
                ▼
┌─────────────────────────────┐
│ Resume Analyzer Agent       │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ ATS Scorer Agent            │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ JD Matcher Agent            │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Interview Generator Agent   │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Career Advisor Agent        │
└─────────────┬───────────────┘
              │
              ▼
          Streamlit UI
```

---

## Agent Workflow

### Resume Analyzer Agent

Acts as the first-level recruiter review.

Responsibilities:

- Extract technical skills
- Identify projects and experience
- Evaluate resume strengths
- Highlight potential weaknesses
- Generate structured resume insights

Output:

- Resume summary
- Skills overview
- Strengths and weaknesses
- Project evaluation

---

### ATS Scorer Agent

Simulates an Applicant Tracking System used by modern companies.

Responsibilities:

- Compare resume against the job description
- Evaluate skill alignment
- Evaluate project relevance
- Assess experience and education fit
- Identify missing keywords

Scoring Logic:

| Component | Weight |
|------------|---------|
| Technical Skills | 40% |
| Projects | 25% |
| Experience | 20% |
| Education | 15% |

Output:

- Overall ATS Score
- Technical Skills Score
- Projects Score
- Experience Score
- Education Score
- Matching Skills
- Missing Skills
- Recruiter Summary

---

### JD Matcher Agent

Acts as a hiring manager evaluating role suitability.

Responsibilities:

- Compare candidate profile with role requirements
- Measure overall job fit
- Identify matching and missing skills
- Highlight relevant projects
- Provide suitability analysis

Output:

- Match Percentage
- Relevant Skills
- Skill Gaps
- Relevant Projects
- Hiring Recommendation

---

### Interview Generator Agent

Acts as a technical interviewer.

Responsibilities:

Generate role-specific:

- Technical Questions
- Project-Based Questions
- Behavioral Questions
- HR Questions

Questions are tailored using:

- Candidate Resume
- Job Description
- Skills
- Projects

Output:

- Personalized Interview Question Bank
- Suggested Answers

---

### Career Advisor Agent

Acts as an AI career mentor.

Responsibilities:

- Recommend suitable career paths
- Identify skill gaps
- Suggest certifications
- Recommend future projects
- Create a learning roadmap

Output:

- Suitable Roles
- Skill Gap Analysis
- Certification Recommendations
- Project Suggestions
- 3-Month Roadmap

---

## Key Features

- Multi-Agent AI Workflow
- LangGraph State Management
- ATS Scoring Engine
- Resume Intelligence
- Job Description Matching
- Interview Question Generation
- Career Guidance System
- Structured JSON Outputs
- Interactive Dashboard
- Recruiter-Style Evaluation
- PDF Resume Parsing

---

## Tech Stack

| Component | Technology |
|------------|------------|
| LLM | Groq Llama 3.3 70B |
| Agent Framework | LangGraph |
| LLM Orchestration | LangChain |
| Frontend | Streamlit |
| PDF Parsing | pdfplumber |
| Visualization | Plotly |
| State Management | LangGraph StateGraph |
| Programming Language | Python |

---

## Project Structure

```text
InterviewCopilot/
│
├── agents/
│   ├── resume_analyzer.py
│   ├── ats_scorer.py
│   ├── jd_matcher.py
│   ├── interview_generator.py
│   └── career_advisor.py
│
├── graph/
│   ├── state.py
│   └── interview_copilot_graph.py
│
├── utils/
│   ├── llm.py
│   └── parser.py
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd InterviewCopilot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your free API key from:

https://console.groq.com

---

## Run Application

```bash
streamlit run app.py
```

Application launches at:

```text
http://localhost:8501
```

---

## Example Workflow

1. Upload Resume (PDF)
2. Paste Job Description
3. Click Analyze Resume
4. System Executes Multi-Agent Workflow
5. View:

- ATS Score
- Resume Analysis
- JD Match Report
- Interview Questions
- Career Advice

6. Download Complete Report

---

## Future Improvements

- Resume Chat Assistant
- Multi-LLM Support (Groq + Gemini + OpenAI)
- Resume Version Comparison
- Vector Database Integration
- Advanced RAG Pipeline
- Interview Simulation Mode
- PDF Report Generation
- Job Recommendation Engine

---

## Why This Project?

This project demonstrates practical applications of:

- Agentic AI
- Generative AI
- LangGraph
- LLM Orchestration
- Prompt Engineering
- AI System Design
- Resume Intelligence
- Career Recommendation Systems

It combines AI engineering, software engineering, and user-focused design into a production-style application that solves a real-world problem.
