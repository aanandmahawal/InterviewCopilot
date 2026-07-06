# Multi-Agent AI Resume & Interview Copilot

An AI-powered career assistant that analyzes resumes, evaluates ATS compatibility, compares candidates against job descriptions, generates interview questions, and provides personalized career guidance using a multi-agent architecture.

Unlike traditional resume analyzers that rely on a single prompt-response interaction, this system uses multiple specialized AI agents orchestrated through LangGraph. Each agent performs a dedicated task and passes structured outputs to the next stage, creating a recruiter-style evaluation workflow.

---

## Overview

Most resume review tools focus only on keyword matching or generic ATS scores. Recruiters, however, evaluate candidates across multiple dimensions including technical skills, project relevance, experience, role fit, interview readiness, and career growth potential.

This project simulates that process using a multi-agent workflow that:

- Analyzes resumes
- Evaluates ATS compatibility
- Matches resumes against job descriptions
- Identifies strengths and skill gaps
- Generates interview questions
- Provides personalized career guidance

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

Acts as the first-stage recruiter review.

Responsibilities:

- Extract technical skills
- Analyze projects and experience
- Identify strengths and weaknesses
- Summarize resume quality

Output:

- Resume Analysis Report

---

### ATS Scorer Agent

Simulates an Applicant Tracking System.

Responsibilities:

- Compare resume with job description
- Calculate ATS compatibility score
- Identify matching and missing skills
- Highlight strengths and improvement areas

Scoring Logic:

| Component | Weight |
|------------|---------|
| Technical Skills | 40% |
| Projects | 25% |
| Experience | 20% |
| Education | 15% |

Output:

- ATS Score
- Skills Match Analysis
- Recruiter Summary

---

### JD Matcher Agent

Acts as a hiring manager.

Responsibilities:

- Evaluate role suitability
- Compare candidate profile against requirements
- Identify project relevance
- Assess skill alignment

Output:

- Match Percentage
- Relevant Skills
- Skill Gaps
- Hiring Recommendation

---

### Interview Generator Agent

Acts as a technical interviewer.

Responsibilities:

Generate:

- Technical Questions
- Project-Based Questions
- Behavioral Questions
- HR Questions

Questions are customized using both the resume and job description.

Output:

- Personalized Interview Question Bank

---

### Career Advisor Agent

Acts as an AI career mentor.

Responsibilities:

- Suggest suitable roles
- Identify missing skills
- Recommend certifications
- Suggest future projects
- Generate learning roadmap

Output:

- Career Growth Plan

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
├── app.py
│
├── agents/
│   ├── resume_analyzer.py
│   │   └── Extracts skills, projects, strengths and weaknesses
│   │
│   ├── ats_scorer.py
│   │   └── Calculates ATS score and identifies skill gaps
│   │
│   ├── jd_matcher.py
│   │   └── Evaluates candidate fit against the job description
│   │
│   ├── interview_generator.py
│   │   └── Generates role-specific interview questions
│   │
│   └── career_advisor.py
│       └── Creates career roadmap and recommendations
│
├── graph/
│   ├── state.py
│   │   └── Shared state passed between all agents
│   │
│   └── interview_copilot_graph.py
│       └── LangGraph workflow orchestration
│
├── utils/
│   ├── llm.py
│   │   └── Groq LLM configuration, retries and JSON handling
│   │
│   └── parser.py
│       └── PDF text extraction using pdfplumber
│
├── requirements.txt
├── README.md
└── .env
```

---

## How It Works

### Step 1 — Resume Upload

User uploads a PDF resume.

### Step 2 — Resume Parsing

The PDF is parsed using pdfplumber and converted into plain text.

### Step 3 — Agent Execution

LangGraph orchestrates the workflow and sequentially executes all agents.

### Step 4 — ATS Evaluation

The ATS Agent compares the resume against the job description and calculates compatibility scores.

### Step 5 — Interview Preparation

Interview Agent generates role-specific interview questions.

### Step 6 — Career Guidance

Career Advisor Agent provides skill-gap analysis and roadmap recommendations.

### Step 7 — Dashboard Generation

Results are displayed through an interactive Streamlit dashboard.

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

1. Upload Resume
2. Paste Job Description
3. Click Analyze Resume
4. LangGraph executes all agents
5. View:
   - ATS Score
   - Resume Analysis
   - JD Match Report
   - Interview Questions
   - Career Advice
6. Download Generated Report

---

## Future Improvements

- Resume Chat Assistant
- Mock Interview Agent
- Multi-LLM Support (Groq + Gemini + OpenAI)
- Advanced RAG Pipeline
- Resume Version Comparison
- PDF Report Generation
- Job Recommendation Engine
- Vector Database Integration

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
- Multi-Agent Workflows

The project combines AI engineering, software engineering, and user-focused design into a production-style application that solves a real-world problem for job seekers.
