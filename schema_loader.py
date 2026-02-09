from sqlalchemy import inspect
from db import engine

def load_schema_documents():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    documents = []

    for table in tables:
        columns = inspector.get_columns(table)

        schema_text = f"Table: {table}\nColumns:\n"

        for col in columns:
            schema_text += f"- {col['name']} ({col['type']})\n"

        documents.append(schema_text)

    return documents