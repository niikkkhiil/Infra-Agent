***Building an autonomous, self-healing AI infrastructure agent that:***

 Accepts natural language commands

 Retrieves real-time AWS & Terraform knowledge using RAG + live web search

 Plans, validates, and executes infrastructure changes safely

 Runs through a production-grade CI/CD + Terraform workflow

 Can detect failures and auto-remediate (self-healing)   

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