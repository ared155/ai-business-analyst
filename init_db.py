from sqlalchemy import text
from db import engine

with engine.connect() as conn:

    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        region TEXT,
        signup_date TEXT
    );
    """))

    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product TEXT,
        amount FLOAT,
        order_date TEXT
    );
    """))

    conn.execute(text("""
    INSERT INTO customers (name, region, signup_date)
    VALUES
    ('Alice', 'North', '2024-01-01'),
    ('Bob', 'South', '2024-02-15'),
    ('Charlie', 'West', '2024-03-20');
    """))

    conn.execute(text("""
    INSERT INTO orders (customer_id, product, amount, order_date)
    VALUES
    (1, 'Laptop', 1200, '2024-04-01'),
    (2, 'Phone', 800, '2024-04-05'),
    (1, 'Tablet', 400, '2024-05-01'),
    (3, 'Laptop', 1300, '2024-05-10');
    """))

    conn.commit()

print("Database initialized.")