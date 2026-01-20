***Building an autonomous, self-healing AI infrastructure agent that:***

 Accepts natural language commands
 Retrieves real-time AWS & Terraform knowledge using RAG + live web search
 Plans, validates, and executes infrastructure changes safely
 Runs through a production-grade CI/CD + Terraform workflow
 Can detect failures and auto-remediate (self-healing)   

 🧠 What Is This Project?

    This project builds an autonomous AI DevOps engineer that can:
    Understand natural language infrastructure requests
    Fetch up-to-date AWS & Terraform knowledge
    Generate and safely apply Terraform code
    Monitor infrastructure health
    Automatically fix issues when something breaks
    All of this runs on AWS ECS with CI/CD, just like a real production system.

    1. Why This Project Exists (The Problem)

    Modern infrastructure management is painful because:

    ❌ Too Much Manual Work

    Engineers read hundreds of pages of AWS docs and Terraform guides
    Knowledge becomes outdated very quickly

    ❌ No Context Awareness

    Systems forget past actions
    No memory of previous scaling, failures, or fixes

    ❌ Unsafe Infrastructure Changes

    Terraform changes are risky
    One wrong apply can break production

    ❌ No Self-Healing

    CloudWatch alarms trigger
    Humans wake up
    Problems stay broken until fixed manually

    ❌ Most AI Demos Never Reach Production

    Run locally
    No CI/CD
    No real AWS deployment
    No monitoring

 ✅ What This Project Solves

    This project delivers a production-ready AI infrastructure agent that:

    ✔ Understands natural language
    ✔ Uses real AWS knowledge
    ✔ Applies Terraform safely
    ✔ Heals infrastructure automatically
    ✔ Runs on ECS with CI/CD

**System Components Explained**

 *1. Streamlit UI (Chat Interface)*

    Path: src/main.py

    Natural language interface (e.g.
    “Scale ECS service to 4 tasks”)

    Shows:

    AI reasoning
    Terraform plan preview
    Approval step before apply

    📌 Why Streamlit?

    Fast UI
    Easy local + ECS deployment
    Great for demos

*2. Agent Layer (Agentic Brain)*

Directory: src/agents/

Agent	                           Responsibility

Planner Agent	                    Converts user intent → structured infra plan
Coder Agent	                        Generates Terraform HCL
Validator Agent	                    Runs terraform plan, policy & safety checks
Executor Agent	                    Applies infra via Terraform / AWS APIs

🔹 Key design choice
You separated reasoning, generation, validation, execution → this is exactly how real autonomous systems are built.