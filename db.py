from sqlalchemy import create_engine, text

DATABASE_URL = "sqlite:///business.db"

engine = create_engine(DATABASE_URL)

def execute_query(query: str):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]