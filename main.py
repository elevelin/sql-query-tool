import sqlite3
import os
from pathlib import Path
from tabulate import tabulate

DB_PATH = Path("data") / "shop.db"
SCHEMA_PATH = Path("schema.sql")
SEED_PATH = Path("seed.sql")

def init_db():
    if DB_PATH.exists():
        print("✅ Database already exists.")
        return
    print("🛠️ Initializing database...")
    os.makedirs(DB_PATH.parent, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    with open(SCHEMA_PATH, "r") as f:
        cur.executescript(f.read())
    with open(SEED_PATH, "r") as f:
        cur.executescript(f.read())

    conn.commit()
    conn.close()
    print("✅ Database created and seeded.")

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute(query)
        if query.strip().lower().startswith("select"):
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            conn.commit()
            print("✅ Query executed.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()

def show_menu():
    queries = {
        "1": ("Top customers by total spend", """
            SELECT u.name, SUM(p.price * oi.quantity) AS total_spent
            FROM users u
            JOIN orders o ON u.id = o.user_id
            JOIN order_items oi ON o.id = oi.order_id
            JOIN products p ON oi.product_id = p.id
            GROUP BY u.id
            ORDER BY total_spent DESC;
        """),
        "2": ("Monthly revenue", """
            SELECT substr(o.order_date, 1, 7) AS month, SUM(p.price * oi.quantity) AS revenue
            FROM orders o
            JOIN order_items oi ON o.id = oi.order_id
            JOIN products p ON oi.product_id = p.id
            GROUP BY month
            ORDER BY month;
        """),
        "3": ("List all users", "SELECT * FROM users;"),
        "4": ("Run custom SQL", None)
    }

    while True:
        print("\n📊 SQL Query Tool Menu:")
        for k, (desc, _) in queries.items():
            print(f"{k}. {desc}")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("👋 Goodbye!")
            break
        elif choice in queries:
            if choice == "4":
                query = input("Enter your custom SQL:\n")
                run_query(query)
            else:
                _, sql = queries[choice]
                run_query(sql)
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    init_db()
    show_menu()

