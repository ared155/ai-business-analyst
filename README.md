# AI Business Analyst (RAG-Powered SQL Agent)

Live Demo 👉 [Hugging Face Space](https://huggingface.co/spaces/Ared155/ai-business-analyst)

---

## Overview

AI Business Analyst is a Retrieval-Augmented Generation (RAG) system that converts natural language business questions into secure SQL queries, executes them on a database, and generates business insights.

This project demonstrates end-to-end AI system design including:

- Schema-aware SQL generation
- Vector-based retrieval (RAG)
- Cloud LLM integration (Google Gemini)
- Secure SQL execution with guardrails
- Public deployment on Hugging Face Spaces

---

## Architecture

User Question  
→ Schema Retrieval (FAISS + Embeddings)  
→ Gemini LLM (SQL Generation)  
→ SQL Guard (Security Layer)  
→ SQLite Execution  
→ Insight Generation  
→ Gradio UI

---

## Features

- Natural Language → SQL
- Join-aware query generation
- SQL safety guard (SELECT-only enforcement)
- Business insight generation
- Public cloud deployment
- Interactive example prompts

---

## Tech Stack

- Python
- Gradio (UI)
- Sentence-Transformers
- FAISS (Vector Search)
- Google Gemini API
- SQLite
- Hugging Face Spaces (Deployment)

---

## Example Queries

- Show total sales amount by product  
- Which region generated the highest revenue?  
- Show average order value  
- Show total sales by region  

---

## Setup Locally

```bash
pip install -r requirements.txt
python app.py
