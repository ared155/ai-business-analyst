import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def generate_sql(question, schema):

    prompt = f"""
You are an expert SQLite SQL generator.

User Question:
{question}

Relevant Database Schema:
{schema}

Rules:
- Only generate SELECT queries.
- Do NOT explain anything.
- Return only pure SQL.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    sql = response.text.strip()

    if "```" in sql:
        sql = sql.split("```")[1]

    # Remove leading language tag
    lines = sql.split("\n")

    if lines[0].lower() in ["sql", "sqlite"]:
        lines = lines[1:]

    sql = "\n".join(lines)

    return sql.strip()



def generate_insight(question, result):

    prompt = f"""
You are a business analyst.

User Question:
{question}

SQL Result:
{result}

Explain the result in simple business terms.
Keep it short and professional.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )


    return response.text.strip()
