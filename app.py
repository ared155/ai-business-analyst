import gradio as gr
import pandas as pd

from schema_loader import load_schema_documents
from rag import SchemaRAG
from llm import generate_sql, generate_insight
from db import execute_query
from sql_guard import is_safe


# -------------------------
# Load RAG once
# -------------------------

documents = load_schema_documents()
rag = SchemaRAG(documents)


# -------------------------
# Main Logic
# -------------------------

def analyze(question):

    if not question.strip():
        return "Please enter a question.", "", ""

    try:
        # Retrieve relevant schema
        relevant_schema = rag.retrieve(question)
        schema_text = "\n".join(relevant_schema)

        # Generate SQL
        sql = generate_sql(question, schema_text)

        if not is_safe(sql):
            return "Unsafe query generated.", "", ""

        # Execute
        result = execute_query(sql)
        insight = generate_insight(question, result)

        df = pd.DataFrame(result)

        return sql, df, insight

    except Exception as e:
        return f"Error: {str(e)}", "", ""


# -------------------------
# Gradio UI
# -------------------------

with gr.Blocks() as demo:

    gr.Markdown("# 📊 AI Business Analyst (RAG Version)")
    gr.Markdown("Ask business questions in natural language.")

    question_input = gr.Textbox(label="Enter your question")

    analyze_btn = gr.Button("Analyze")

    sql_output = gr.Code(label="Generated SQL", language="sql")
    result_output = gr.Dataframe(label="Query Result")
    insight_output = gr.Textbox(label="Business Insight")

    analyze_btn.click(
        analyze,
        inputs=question_input,
        outputs=[sql_output, result_output, insight_output]
    )


demo.launch()
