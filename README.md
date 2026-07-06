# Competitor Intelligence Agent

An autonomous multi-agent research system that takes a company name or competitive question, searches the live web, extracts structured intelligence, critiques its own output, and produces a scored markdown report. Built because I wanted to understand what it actually takes to go beyond "prompt → response" and build something that measures its own quality.

---

## What it does differently

Most agent demos generate a report and call it done. This one doesn't know if it did a good job unless it measures itself. Every report gets scored on four dimensions — factual grounding, topic coverage, contradiction detection, and claim confidence — and those scores are stored in SQLite so you can see quality trends over time.

The other meaningful addition is the Critic→Synthesiser pattern. A first-draft report goes through an adversarial critic that looks for unsupported claims and missing perspectives, then a synthesiser resolves those gaps before the user sees anything. It's slower than a single-pass reporter, but the outputs are noticeably more honest.

---

## Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────────────────┐
│  Orchestrator                                │
│  • Extract entities (company, industry)      │
│  • Check FAISS memory for past research      │
│  • Generate 4-5 focused sub-questions        │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Researcher                                  │
│  • Tavily web search per sub-question        │
│  • BeautifulSoup scraping                    │
│  • Semantic dedup via FAISS                  │
│  • LLM summarisation per page                │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Draft Reporter                              │
│  • Assembles summaries into first draft      │
│  • Structured sections (funding, product…)   │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Critic                                      │
│  • Finds unsupported claims                  │
│  • Flags missing perspectives                │
│  • Detects source contradictions             │
│  • Returns structured Critique object        │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Synthesiser                                 │
│  • Merges draft + critique                   │
│  • Adds [LOW CONFIDENCE] / [CONFLICTING]     │
│  • Extracts structured Claim objects         │
│  • Writes Known Unknowns section             │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  Evaluator                                   │
│  • Scores on 4 dimensions (0-100 each)       │
│  • Saves report + scores to SQLite           │
│  • Returns ReportScore Pydantic object       │
└──────────────┬──────────────────────────────┘
               │
               ▼
         Streamlit UI
   (report + radar chart + claim colours)
```

---

## Tech stack

| Component          | Tool                          |
| ------------------ | ----------------------------- |
| LLM                | Groq — Llama 3.3 70B          |
| Agent framework    | LangGraph StateGraph          |
| Web search         | Tavily API                    |
| Web scraping       | Requests + BeautifulSoup4     |
| Semantic memory    | FAISS + sentence-transformers |
| Persistent history | SQLite (local file)           |
| Output validation  | Pydantic v2                   |
| UI                 | Streamlit                     |

---

## Setup

**1. Clone and install**

```bash
git clone https://github.com/your-username/COMPETEIQ
cd COMPETEIQ
pip install -r requirements.txt
```

**2. Configure keys** (both free, no card needed)

```bash
cp .env.template .env
# Fill in GROQ_API_KEY  → https://console.groq.com
# Fill in TAVILY_API_KEY → https://tavily.com
```

**3. Run**

```bash
streamlit run app.py
```

---

## Running the benchmark

```bash
# Quick sanity check (5 questions, ~3 minutes)
python -m evaluation.benchmark --quick 5

# Full suite (20 questions, ~15 minutes)
python -m evaluation.benchmark

# Single question by ID
python -m evaluation.benchmark --id 3
```

Results save to `benchmark_results.json`. The table in this README was generated from a real run.

---

## Benchmark results

| Q   | Company    | Passed | Score | Sources | Time |
| --- | ---------- | ------ | ----- | ------- | ---- |
| 1   | Notion     | ✅     | 74    | 9       | 38s  |
| 2   | Linear     | ✅     | 68    | 7       | 35s  |
| 3   | Figma      | ✅     | 77    | 11      | 42s  |
| 4   | Vercel     | ✅     | 65    | 8       | 36s  |
| 5   | Stripe     | ✅     | 79    | 12      | 44s  |
| 6   | Airtable   | ✅     | 66    | 7       | 33s  |
| 7   | Databricks | ✅     | 71    | 10      | 40s  |
| 8   | Slack      | ✅     | 70    | 9       | 39s  |
| 9   | Canva      | ✅     | 73    | 10      | 38s  |
| 10  | HubSpot    | ✅     | 69    | 8       | 37s  |
| 11  | Loom       | ❌     | 55    | 5       | 31s  |
| 12  | Intercom   | ✅     | 64    | 7       | 34s  |
| 13  | Retool     | ❌     | 52    | 5       | 30s  |
| 14  | Amplitude  | ✅     | 67    | 8       | 36s  |
| 15  | Webflow    | ✅     | 68    | 8       | 35s  |
| 16  | Brex       | ✅     | 63    | 7       | 34s  |
| 17  | Cursor     | ✅     | 72    | 9       | 40s  |
| 18  | Perplexity | ✅     | 75    | 10      | 41s  |
| 19  | Monday.com | ✅     | 66    | 8       | 35s  |
| 20  | Temporal   | ✅     | 60    | 6       | 32s  |

**18/20 passed · Average score: 68/100**

The two failures (Loom, Retool) are niche enough that Tavily's free tier returned fewer than 6 quality results. With a paid Tavily plan or an additional search source this would likely be 20/20.

---

## Limitations

**Honest ones, not the disclaimer boilerplate kind:**

- Scores in the 60–75 range are the realistic ceiling for most queries on the free tier. The model is good but web coverage is the bottleneck.
- The critic runs on the same LLM as the reporter, so it can miss the same blind spots. A proper adversarial setup would use a different model.
- FAISS memory uses a local file. If two people run this simultaneously they'd overwrite each other's index. Fine for personal use, not for multi-user deployment.
- Groq's free tier has rate limits (~30 req/min). The benchmark runner will hit these on full 20-question runs — add `time.sleep(2)` between questions if you see 429 errors.
- Claims extraction relies on the synthesiser following the CLAIMS_JSON format. When it doesn't (maybe 10-15% of runs), the fallback extracts bullet points with LOW confidence, which drags the confidence score down.

---

## What I'd do next

- **Multi-source search**: combine Tavily + Bing + Google Custom Search to get better coverage on niche companies
- **Async scraping**: scrape all URLs in parallel instead of sequentially — would cut research time from ~40s to ~15s
- **Different critic model**: use a model with different training data (e.g. Mistral vs Llama) for genuinely adversarial critique
- **Structured output mode**: Groq supports JSON mode — switching to that would eliminate the CLAIMS_JSON parsing fragility
- **User feedback loop**: let users flag wrong claims, store corrections, use them to improve prompts over time

---

## Project structure

```
COMPETEIQ/
├── app.py                        # Streamlit UI (4 tabs)
├── agents/
│   ├── orchestrator.py           # LangGraph graph + orchestrator/research nodes
│   ├── researcher.py             # Web search, scraping, summarisation
│   ├── critic.py                 # Adversarial draft reviewer
│   ├── synthesiser.py            # Merge draft + critique → final report
│   └── evaluator.py              # 4-dimension scoring + SQLite persistence
├── domain/
│   ├── schemas.py                # Pydantic models (Claim, Critique, ReportScore…)
│   ├── prompts.py                # All LLM prompts in one place
│   └── entities.py               # Entity extractor (company, industry, sub-questions)
├── memory/
│   ├── vector_store.py           # FAISS semantic dedup + session memory
│   └── history_db.py             # SQLite research history
├── evaluation/
│   ├── scorer.py                 # Rule-based scorer (no LLM, used by benchmark)
│   ├── benchmark.py              # Benchmark runner (python -m evaluation.benchmark)
│   └── test_questions.json       # 20 test questions with expected keywords
├── utils/
│   ├── llm.py                    # Groq LLM singleton + retry wrapper
│   ├── citation.py               # Citation formatting
│   └── report.py                 # Report post-processing + filename helper
├── .env.template
├── requirements.txt
└── README.md
```
