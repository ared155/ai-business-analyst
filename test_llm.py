from schema_loader import load_schema_documents
from rag import SchemaRAG
from llm import generate_sql
from db import execute_query
from sql_guard import is_safe

documents = load_schema_documents()
rag = SchemaRAG(documents)

question = "Show total sales amount by product"

relevant_schema = rag.retrieve(question)
schema_text = "\n".join(relevant_schema)

sql = generate_sql(question, schema_text)

print("\nGenerated SQL:\n")
print(sql)

if not is_safe(sql):
    print("Unsafe query detected!")
else:
    result = execute_query(sql)
    print("\nQuery Result:\n")
    print(result)
