from datetime import date, timedelta
from typing import List, Dict

# Updated Start Date: Monday, Feb 23, 2026
START_DATE = date(2026, 2, 23)

WEEKLY_PLANS: List[Dict] = [
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 1A – Python Proficiency (Weeks 1-4)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 1: Modified - No setup, 1 lecture per day
        "week": 1,
        "phase": "Phase 1: Python & DSA",
        "theme": "Python Foundations – CS50P Fast Track",
        "days": [
            {"topic": "CS50P Lecture 0: Functions, Variables",
             "tasks": ["Watch CS50P Lecture 0", "Complete Problem Set 0", "Create GitHub repo 'fde-journey'"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 1: Conditionals",
             "tasks": ["Watch CS50P Lecture 1", "Complete Problem Set 1"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 2: Loops",
             "tasks": ["Watch CS50P Lecture 2", "Complete Problem Set 2"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 3: Exceptions",
             "tasks": ["Watch CS50P Lecture 3", "Complete Problem Set 3"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "Python Practice – Strings & Lists",
             "tasks": ["Solve 3 easy string manipulation exercises", "LeetCode Easy: Two Sum (#1)", "Review week 1 code"],
             "resources": ["https://leetcode.com/problems/two-sum/"]},
            {"topic": "Weekend Deep Dive: Dictionaries & Sets",
             "tasks": ["Practice dict/set operations", "LeetCode Easy: Contains Duplicate (#217)", "Build a word frequency counter script"],
             "resources": ["https://leetcode.com/problems/contains-duplicate/"]},
            {"topic": "Weekend Review & File I/O Intro",
             "tasks": ["Read/write CSV files with Python", "LeetCode Easy: Best Time to Buy and Sell Stock (#121)", "Push all code to GitHub"],
             "resources": ["https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"]},
        ],
    },
    {   # Week 2: CS50P Lectures 4-6
        "week": 2,
        "phase": "Phase 1: Python & DSA",
        "theme": "Python Intermediate – CS50P Lectures 4-6",
        "days": [
            {"topic": "CS50P Lecture 4: Libraries",
             "tasks": ["Watch CS50P Lecture 4", "Complete Problem Set 4", "Explore: requests, json, csv modules"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 5: Unit Tests",
             "tasks": ["Watch CS50P Lecture 5", "Complete Problem Set 5", "Learn pytest basics"],
             "resources": ["https://docs.pytest.org/"]},
            {"topic": "CS50P Lecture 6: File I/O ⭐",
             "tasks": ["Watch CS50P Lecture 6", "Complete Problem Set 6", "LeetCode Easy: Valid Anagram (#242)"],
             "resources": ["https://leetcode.com/problems/valid-anagram/"]},
            {"topic": "File I/O Deep Dive",
             "tasks": ["Practice: parse a large CSV with error handling", "LeetCode Medium: Group Anagrams (#49)"],
             "resources": ["https://leetcode.com/problems/group-anagrams/"]},
            {"topic": "JSON & API Data Processing",
             "tasks": ["Fetch data from a public API", "Parse and transform nested JSON"],
             "resources": ["https://jsonplaceholder.typicode.com/"]},
            {"topic": "Unit Testing Practice",
             "tasks": ["Write comprehensive tests for File I/O scripts", "Learn pytest fixtures"],
             "resources": ["https://docs.pytest.org/en/stable/fixture.html"]},
            {"topic": "Week 2 Review & LeetCode",
             "tasks": ["Review Problem Sets 4-6", "LeetCode Medium: Top K Frequent Elements (#347)"],
             "resources": ["https://leetcode.com/problems/top-k-frequent-elements/"]},
        ],
    },
    {   # Week 3: CS50P Lectures 7-8 + Project Start
        "week": 3,
        "phase": "Phase 1: Python & DSA",
        "theme": "Python Advanced – Regex & OOP",
        "days": [
            {"topic": "CS50P Lecture 7: Regular Expressions ⭐",
             "tasks": ["Watch CS50P Lecture 7", "Complete Problem Set 7"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 8: OOP (Part 1)",
             "tasks": ["Watch CS50P Lecture 8", "Build: DataRecord class with validation"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 8: OOP (Part 2)",
             "tasks": ["Complete Problem Set 8", "Practice: class composition"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "PII Redaction Project – Design",
             "tasks": ["Design pipeline architecture", "Write regex patterns for PII detection"],
             "resources": ["https://microsoft.github.io/presidio/"]},
            {"topic": "PII Redaction Project – Implementation",
             "tasks": ["Implement PII scanner class", "LeetCode Medium: Product of Array Except Self (#238)"],
             "resources": ["https://leetcode.com/problems/product-of-array-except-self/"]},
            {"topic": "Weekend: PII Project Testing",
             "tasks": ["Write unit tests for PII detection", "Test edge cases"],
             "resources": []},
            {"topic": "Weekend Review & LeetCode",
             "tasks": ["Review OOP and Regex", "LeetCode Medium: Maximum Subarray (#53)"],
             "resources": ["https://leetcode.com/problems/maximum-subarray/"]},
        ],
    },
    {   # Week 4: Project Complete + Pandas
        "week": 4,
        "phase": "Phase 1: Python & DSA",
        "theme": "Advanced Python & Phase 1A Checkpoint",
        "days": [
            {"topic": "CS50P Lecture 9: Et Cetera",
             "tasks": ["Watch CS50P Lecture 9", "Learn: dataclasses and enums"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "PII Redaction Project – SQL Output",
             "tasks": ["Add SQLite output to pipeline", "LeetCode Medium: 3Sum (#15)"],
             "resources": ["https://leetcode.com/problems/3sum/"]},
            {"topic": "Python Advanced – Environments",
             "tasks": ["Learn venv and requirements.txt", "LeetCode Medium: Merge Intervals (#56)"],
             "resources": ["https://leetcode.com/problems/merge-intervals/"]},
            {"topic": "Pandas Fundamentals (Part 1)",
             "tasks": ["Install pandas, learn DataFrame basics"],
             "resources": ["https://pandas.pydata.org/docs/getting_started/"]},
            {"topic": "Pandas Fundamentals (Part 2)",
             "tasks": ["Data cleaning with pandas (nulls, dtypes)"],
             "resources": ["https://pandas.pydata.org/docs/user_guide/merging.html"]},
            {"topic": "Weekend: Phase 1A Checkpoint",
             "tasks": ["Review all CS50P concepts", "Verify PII project is on GitHub"],
             "resources": []},
            {"topic": "Weekend Review & LeetCode",
             "tasks": ["LeetCode Medium: Search in Rotated Sorted Array (#33)"],
             "resources": ["https://leetcode.com/problems/search-in-rotated-sorted-array/"]},
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 1B – DSA Deep Dive (Weeks 5-8)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 5: HashMaps & Strings
        "week": 5,
        "phase": "Phase 1: Python & DSA",
        "theme": "DSA – HashMaps & Strings",
        "days": [
            {"topic": "HashMap Patterns",
             "tasks": ["Study: hash table internals in Python (dict)", "LeetCode Medium: Longest Consecutive Sequence (#128)"]},
            {"topic": "String Manipulation Deep Dive",
             "tasks": ["Study: sliding window, two pointers", "LeetCode Medium: Minimum Window Substring (#76)"]},
            {"topic": "Advanced Python – Itertools",
             "tasks": ["Practice itertools (combinations, permutations)", "Build: memory-efficient file processor"]},
            {"topic": "DSA – Two Pointer Technique",
             "tasks": ["Study two-pointer patterns", "LeetCode Medium: Trapping Rain Water (#42)"]},
            {"topic": "Python – Error Handling",
             "tasks": ["Custom exception classes", "Logging best practices"]},
            {"topic": "Weekend: Data Pipeline Script",
             "tasks": ["Design a multi-step data pipeline (API -> SQLite)"]},
            {"topic": "Weekend Review + Networking",
             "tasks": ["Review HashMaps", "Reach out to 2 FDEs on LinkedIn"]},
        ],
    },
    {   # Week 6: Arrays & Sliding Window
        "week": 6,
        "phase": "Phase 1: Python & DSA",
        "theme": "DSA – Arrays & Sliding Window",
        "days": [
            {"topic": "Sliding Window Pattern",
             "tasks": ["LeetCode Medium: Longest Repeating Character Replacement (#424)"]},
            {"topic": "Array Manipulation + Sorting",
             "tasks": ["Study: merge sort, quick sort", "LeetCode Medium: Kth Largest Element (#215)"]},
            {"topic": "Binary Search Applications",
             "tasks": ["Study binary search patterns", "LeetCode Medium: Search a 2D Matrix (#74)"]},
            {"topic": "Python – Collections Module",
             "tasks": ["Learn: Counter, defaultdict, deque", "Refactor previous solutions"]},
            {"topic": "Build: ETL Pipeline with Pandas",
             "tasks": ["Design ETL for Kaggle dataset (Extract -> Pandas -> SQLite)"]},
            {"topic": "Weekend: ETL Testing",
             "tasks": ["Write tests for ETL pipeline", "Add CLI arguments with argparse"]},
            {"topic": "Weekend Review",
             "tasks": ["Review sliding window", "Update GitHub portfolio"]},
        ],
    },
    {   # Week 7: Stacks, Queues & Trees
        "week": 7,
        "phase": "Phase 1: Python & DSA",
        "theme": "DSA – Stacks, Queues & Trees",
        "days": [
            {"topic": "Stack & Queue Patterns",
             "tasks": ["LeetCode Medium: Daily Temperatures (#739)"]},
            {"topic": "Tree Fundamentals",
             "tasks": ["Study BFS/DFS", "LeetCode Medium: Validate Binary Search Tree (#98)"]},
            {"topic": "Graph Basics",
             "tasks": ["Study graph representations", "LeetCode Medium: Number of Islands (#200)"]},
            {"topic": "Python – Async Basics",
             "tasks": ["Learn asyncio fundamentals", "Practice: async HTTP requests"]},
            {"topic": "Build: Async Data Fetcher",
             "tasks": ["Build async multi-API data aggregator"]},
            {"topic": "Weekend: Type Hints & Mypy",
             "tasks": ["Run mypy on all projects", "Fix type errors"]},
            {"topic": "Weekend Review",
             "tasks": ["Review trees and graphs"]},
        ],
    },
    {   # Week 8: Consolidation & Phase 1 Wrap-up
        "week": 8,
        "phase": "Phase 1: Python & DSA",
        "theme": "Phase 1 Consolidation",
        "days": [
            {"topic": "LeetCode Sprint (Arrays/Strings)",
             "tasks": ["Solve 3 medium problems", "Focus on clean code"]},
            {"topic": "LeetCode Sprint (HashMaps/Mixed)",
             "tasks": ["Solve 3 medium hashmaps", "Review 30 problems solved so far"]},
            {"topic": "Portfolio Review Day",
             "tasks": ["Update GitHub READMEs", "Write 1 LinkedIn post about journey"]},
            {"topic": "Phase 1 -> 2 Transition",
             "tasks": ["Install LangChain", "Read LangChain quickstart docs"]},
            {"topic": "LangChain Setup",
             "tasks": ["Set up OpenAI API key", "Understand: Models, Prompts, Chains"]},
            {"topic": "Weekend: Prompt Engineering",
             "tasks": ["Study: zero-shot, few-shot, chain-of-thought"]},
            {"topic": "Weekend: Phase 1 Complete 🎉",
             "tasks": ["Final review", "Update resume with Python skills"]},
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 2A – Agentic AI & Frameworks (Weeks 9-14)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 9: LangChain Fundamentals
        "week": 9,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "LangChain – Core",
        "days": [
            {"topic": "Models & Prompts", "tasks": ["Build: multi-prompt chatbot"]},
            {"topic": "Chains & Output Parsers", "tasks": ["Build: structured output chain (JSON)"]},
            {"topic": "Memory Systems", "tasks": ["Implement: ConversationSummaryMemory"]},
            {"topic": "LCEL", "tasks": ["Convert chains to LCEL pipe syntax"]},
            {"topic": "Tools & Agents Intro", "tasks": ["Study: ReAct agent pattern"]},
            {"topic": "Weekend: Research Agent", "tasks": ["Build agent that searches web + summarizes"]},
            {"topic": "Weekend: Review", "tasks": ["Push projects to GitHub", "LeetCode maintenance"]},
        ],
    },
    {   # Week 10: RAG Foundations
        "week": 10,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "Retrievers & RAG",
        "days": [
            {"topic": "Document Loaders", "tasks": ["Learn PDF/CSV/SQL loaders"]},
            {"topic": "Vector Stores", "tasks": ["Set up ChromaDB", "Build embedding pipeline"]},
            {"topic": "RAG Pipeline", "tasks": ["Build RAG: load -> split -> embed -> retrieve"]},
            {"topic": "Advanced Retrieval", "tasks": ["Learn: MMR, hybrid search"]},
            {"topic": "RAG Evaluation", "tasks": ["Build evaluation dataset (10 Q&A pairs)"]},
            {"topic": "Weekend: Vector DB", "tasks": ["Explore Pinecone", "Learn metadata filtering"]},
            {"topic": "Weekend: Review", "tasks": ["Draw RAG architecture diagram"]},
        ],
    },
    {   # Week 11: Production RAG
        "week": 11,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "RAG System – Production Build",
        "days": [
            {"topic": "Architecture", "tasks": ["Design production RAG ingestion pipeline"]},
            {"topic": "Conversation History", "tasks": ["Add memory to RAG", "Contextual compression"]},
            {"topic": "UI with Streamlit", "tasks": ["Build chat interface", "Add document upload"]},
            {"topic": "Error Handling", "tasks": ["Handle: no documents found", "Token limits"]},
            {"topic": "Optimization", "tasks": ["Caching for embeddings", "Optimize chunk size"]},
            {"topic": "Weekend: Documentation", "tasks": ["Write README", "Record demo video"]},
            {"topic": "Weekend: System Design", "tasks": ["Draw architecture using RADIO framework"]},
        ],
    },
    {   # Week 12: SQL Agents ⭐
        "week": 12,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "SQL Agents – LLM + SQL Integration",
        "days": [
            {"topic": "SQL Agent Basics", "tasks": ["Build basic SQL agent for Northwind DB"]},
            {"topic": "Advanced Queries", "tasks": ["Handle: complex JOINs via natural language"]},
            {"topic": "Error Correction ⭐", "tasks": ["Build: auto-correction loop (retry with error)"]},
            {"topic": "Schema Understanding", "tasks": ["Teach agent about table relationships"]},
            {"topic": "Security Layer", "tasks": ["SQL injection prevention", "Read-only enforcement"]},
            {"topic": "Weekend: Integration Testing", "tasks": ["Test edge cases (empty results)"]},
            {"topic": "Weekend: Review", "tasks": ["Push SQL Agent to GitHub"]},
        ],
    },
    {   # Week 13: LangGraph
        "week": 13,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "LangGraph – State Machines",
        "days": [
            {"topic": "LangGraph Fundamentals", "tasks": ["Study nodes, edges, state"]},
            {"topic": "Complex Workflows", "tasks": ["Human-in-the-loop pattern"]},
            {"topic": "Multi-Agent Collaboration", "tasks": ["Supervisor agent pattern"]},
            {"topic": "Error Correction Loops ⭐", "tasks": ["Self-correcting SQL agent with LangGraph"]},
            {"topic": "Streaming & Persistence", "tasks": ["Add checkpoint persistence (SQLite)"]},
            {"topic": "Weekend: Integrated Project", "tasks": ["SQL gen -> validation -> correction graph"]},
            {"topic": "Weekend: Review", "tasks": ["Networking: reach out to 2 FDEs"]},
        ],
    },
    {   # Week 14: FastAPI & Deployment
        "week": 14,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "Advanced Agents & FastAPI",
        "days": [
            {"topic": "FastAPI Fundamentals", "tasks": ["Build REST API with CRUD"]},
            {"topic": "FastAPI + LangChain", "tasks": ["Expose SQL agent as API endpoint"]},
            {"topic": "Deployment Patterns", "tasks": ["Dockerize your agent app"]},
            {"topic": "Observability", "tasks": ["Add LangSmith tracing"]},
            {"topic": "Prompt Engineering", "tasks": ["Few-shot examples for SQL agent"]},
            {"topic": "Weekend: Project Polish", "tasks": ["Code review all Phase 2 projects"]},
            {"topic": "Weekend: Phase 2A Review", "tasks": ["Update READMEs", "LeetCode maintenance"]},
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 2B – Modern Data Stack (Weeks 15-16)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 15: Snowflake
        "week": 15,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "Snowflake – Cloud Data Warehouse",
        "days": [
            {"topic": "Snowflake Fundamentals", "tasks": ["Snowflake free trial", "Web UI"]},
            {"topic": "Data Loading", "tasks": ["Practice: COPY INTO", "Load sample TPC-H data"]},
            {"topic": "Advanced Features", "tasks": ["Time Travel, Cloning", "Snowpark Python"]},
            {"topic": "Python Integration", "tasks": ["Use snowflake-connector-python"]},
            {"topic": "Architecture", "tasks": ["Study multi-cluster shared data"]},
            {"topic": "Weekend: SQL Agent", "tasks": ["Connect SQL agent to Snowflake"]},
            {"topic": "Weekend: Review", "tasks": ["Document Snowflake interview points"]},
        ],
    },
    {   # Week 16: dbt
        "week": 16,
        "phase": "Phase 2: Agentic AI & Modern Data Stack",
        "theme": "dbt – Data Transformation",
        "days": [
            {"topic": "dbt Fundamentals", "tasks": ["Install dbt-core + snowflake adapter"]},
            {"topic": "Models & Testing", "tasks": ["Build staging/mart models", "dbt tests"]},
            {"topic": "Macros & Jinja", "tasks": ["Write custom dbt macros"]},
            {"topic": "Snowflake Integration", "tasks": ["Run dbt models against Snowflake"]},
            {"topic": "Lineage", "tasks": ["Generate dbt docs", "Lineage graph"]},
            {"topic": "Weekend: Integration", "tasks": ["Connect dbt -> Snowflake -> SQL Agent"]},
            {"topic": "Weekend: Phase 2 Complete 🎉", "tasks": ["Update resume with AI/Agent skills"]},
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 3A – Security & Compliance (Weeks 17-19)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 17: OWASP for LLMs
        "week": 17,
        "phase": "Phase 3: Security, Evals & Production",
        "theme": "OWASP LLM Top 10",
        "days": [
            {"topic": "OWASP Overview", "tasks": ["Study Prompt Injection, Output Handling"]},
            {"topic": "Injection & Data", "tasks": ["Build prompt injection test suite"]},
            {"topic": "Access & Denial", "tasks": ["Document security checklist"]},
            {"topic": "Input Validation", "tasks": ["Build validation middleware", "Rate limiting"]},
            {"topic": "Guardrails", "tasks": ["Implement topic restriction guardrails"]},
            {"topic": "Weekend: Security Audit", "tasks": ["Audit RAG and SQL agent projects"]},
            {"topic": "Weekend: Review", "tasks": ["Networking: engage in LangChain discussions"]},
        ],
    },
    {   # Week 18: Presidio – PII Redaction
        "week": 18,
        "phase": "Phase 3: Security, Evals & Production",
        "theme": "Microsoft Presidio",
        "days": [
            {"topic": "Presidio Fundamentals", "tasks": ["Run PII detection on sample text"]},
            {"topic": "Custom Recognizers", "tasks": ["Build recognizer for healthcare data"]},
            {"topic": "SQL Agent Integration", "tasks": ["Add PII redaction to agent input/output"]},
            {"topic": "RAG Integration", "tasks": ["Redact PII before embedding docs"]},
            {"topic": "Privacy Patterns", "tasks": ["Study HIPAA/GDPR requirements"]},
            {"topic": "Weekend: PII Testing", "tasks": ["Write detection tests", "Accuracy metrics"]},
            {"topic": "Weekend: Review", "tasks": ["Push PII updates to GitHub"]},
        ],
    },
    {   # Week 19: Security Integration
        "week": 19,
        "phase": "Phase 3: Security, Evals & Production",
        "theme": "Security Compliance",
        "days": [
            {"topic": "Architecture Docs", "tasks": ["Threat model for SQL agent"]},
            {"topic": "LLM Firewalls", "tasks": ["Build moderation chain for output"]},
            {"topic": "Adversarial Testing", "tasks": ["Test SQL injection via natural language"]},
            {"topic": "Secrets Management", "tasks": ["Audit secrets in Git history"]},
            {"topic": "Mock Interview", "tasks": ["Practice AI data privacy questions"]},
            {"topic": "Weekend: Portfolio Review", "tasks": ["Add security sections to READMEs"]},
            {"topic": "Weekend: Phase 3A Review", "tasks": ["Security skills checkpoint"]},
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 3B – Evals & Observability (Weeks 20-22)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 20: Ragas
        "week": 20,
        "phase": "Phase 3: Security, Evals & Production",
        "theme": "Ragas Evaluation",
        "days": [
            {"topic": "Ragas Setup", "tasks": ["Faithfulness and relevancy metrics"]},
            {"topic": "Dataset Creation", "tasks": ["Create ground truth Q&A (20+ pairs)"]},
            {"topic": "Advanced Metrics", "tasks": ["Context precision and recall"]},
            {"topic": "RAG Optimization", "tasks": ["Optimize based on eval scores"]},
            {"topic": "Automation", "tasks": ["Build automated eval pipeline"]},
            {"topic": "Weekend: Human Eval", "tasks": ["Build human evaluation interface"]},
            {"topic": "Weekend: Review", "tasks": ["Compare human vs Ragas scores"]},
        ],
    },
    {   # Week 21: Observability
        "week": 21,
        "phase": "Phase 3: Security, Evals & Production",
        "theme": "Monitoring",
        "days": [
            {"topic": "LangSmith Deep Dive", "tasks": ["Set up project tags and datasets"]},
            {"topic": "Feedback Loops", "tasks": ["Capture user feedback in Streamlit UI"]},
            {"topic": "Cost Monitoring", "tasks": ["Build token usage tracker"]},
            {"topic": "Alerting", "tasks": ["Set up alerts for high latency/error rate"]},
            {"topic": "Trace Analysis", "tasks": ["Identify bottlenecks in multi-agent graph"]},
            {"topic": "Weekend: A/B Testing", "tasks": ["Test two prompt versions with LangSmith"]},
            {"topic": "Weekend: Review", "tasks": ["Document observability strategy"]},
        ],
    },
    {   # Week 22: Capstone Design
        "week": 22,
        "phase": "Phase 3: Security, Evals & Production",
        "theme": "Capstone Project Planning",
        "days": [
            {"topic": "Problem Definition", "tasks": ["Select high-value FDE use case"]},
            {"topic": "Architecture Design", "tasks": ["Draft RADIO framework diagram"]},
            {"topic": "Data Strategy", "tasks": ["Select source datasets (SQL + Docs)"]},
            {"topic": "Tech Stack", "tasks": ["LangGraph + Snowflake + Presidio + Ragas"]},
            {"topic": "MVP Scoping", "tasks": ["Define core features for week 23-25"]},
            {"topic": "Weekend: Project Setup", "tasks": ["Initialize GitHub repo", "Infra setup"]},
            {"topic": "Weekend: Review", "tasks": ["Capstone pitch for LinkedIn"]},
        ],
    },
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 4 – Capstone & Career (Weeks 23-26)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 23: Capstone – Build Phase 1
        "week": 23,
        "phase": "Phase 4: Capstone & Career",
        "theme": "Capstone – Core Build",
        "days": [
            {"topic": "Data Ingestion", "tasks": ["Build Snowflake/dbt pipeline"]},
            {"topic": "RAG/SQL Implementation", "tasks": ["Implement core agent logic"]},
            {"topic": "Agent State Graph", "tasks": ["Build LangGraph workflow"]},
            {"topic": "UI Integration", "tasks": ["Connect logic to Streamlit frontend"]},
            {"topic": "Security Layer", "tasks": ["Add PII and injection protection"]},
            {"topic": "Weekend: Initial Evals", "tasks": ["Run Ragas against first draft"]},
            {"topic": "Weekend: Career Prep", "tasks": ["Update LinkedIn with Capstone progress"]},
        ],
    },
    {   # Week 24: Capstone – Build Phase 2
        "week": 24,
        "phase": "Phase 4: Capstone & Career",
        "theme": "Capstone – Refinement",
        "days": [
            {"topic": "Edge Case Handling", "tasks": ["Improve error correction loops"]},
            {"topic": "Performance", "tasks": ["Reduce latency via caching/async"]},
            {"topic": "Advanced UI", "tasks": ["Add data visualization/lineage to UI"]},
            {"topic": "Testing", "tasks": ["End-to-end integration tests"]},
            {"topic": "Observability", "tasks": ["Full LangSmith integration"]},
            {"topic": "Weekend: Documentation", "tasks": ["Write comprehensive project guide"]},
            {"topic": "Weekend: Career Prep", "tasks": ["FDE-specific resume updates"]},
        ],
    },
    {   # Week 25: Career – Interview Prep
        "week": 25,
        "phase": "Phase 4: Capstone & Career",
        "theme": "Career Readiness",
        "days": [
            {"topic": "Project Demo", "tasks": ["Record high-quality video walkthrough"]},
            {"topic": "System Design", "tasks": ["Practice FDE system design mocks"]},
            {"topic": "Technical Prep", "tasks": ["Review SQL, Python, Agent patterns"]},
            {"topic": "Behavioral Prep", "tasks": ["STAR stories for FDE roles"]},
            {"topic": "Networking", "tasks": ["Reach out to hiring managers"]},
            {"topic": "Weekend: Mock Interviews", "tasks": ["Conduct 2 mock technical rounds"]},
            {"topic": "Weekend: Review", "tasks": ["Final portfolio polish"]},
        ],
    },
    {   # Week 26: Graduation & Job Search
        "week": 26,
        "phase": "Phase 4: Capstone & Career",
        "theme": "Go to Market",
        "days": [
            {"topic": "Portfolio Launch", "tasks": ["Publish capstone blog post"]},
            {"topic": "Job Applications", "tasks": ["Apply to 10 target FDE/Solutions roles"]},
            {"topic": "Networking", "tasks": ["Informational interviews"]},
            {"topic": "Continued Learning", "tasks": ["Read 2 new AI research papers"]},
            {"topic": "LeetCode Maintenance", "tasks": ["Daily medium problem"]},
            {"topic": "Weekend: Review", "tasks": ["Plan continuing education goals"]},
            {"topic": "Weekend: Celebrate! 🎉", "tasks": ["Reflect on 26-week journey"]},
        ],
    },
]

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def generate_schedule() -> List[Dict]:
    """Generate the full day-by-day schedule."""
    schedule = []
    for week_plan in WEEKLY_PLANS:
        week_num = week_plan["week"]
        # Cycle starts every Monday
        week_start = START_DATE + timedelta(weeks=week_num - 1)
        
        for i, day_plan in enumerate(week_plan["days"]):
            day_date = week_start + timedelta(days=i)
            weekday = day_date.weekday() 
            is_weekend = weekday >= 5 
            # Updated weekday hours to 3.5
            hours = 7.0 if is_weekend else 3.5
            
            schedule.append({
                "date": day_date.strftime("%Y-%m-%d"),
                "day": DAY_NAMES[weekday],
                "week": week_num,
                "topic": day_plan["topic"],
                "tasks": day_plan.get("tasks", []),
                "hours": hours,
            })
    return schedule

# Output first week for verification
FULL_SCHEDULE = generate_schedule()
print(f"{'DATE':<12} | {'DAY':<10} | {'HOURS':<5} | {'TOPIC'}")
print("-" * 65)
for day in FULL_SCHEDULE[:7]:
    print(f"{day['date']:<12} | {day['day']:<10} | {day['hours']:<5.1f} | {day['topic']}")