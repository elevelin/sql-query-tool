# SQL Query Tool (CLI - SQLite)

A Python CLI tool that lets you explore a sample e-commerce database using real SQL queries. Preloaded with data for users, orders, products, and order items — run predefined reports or custom SQL directly.

---

## ✅ Features

- Runs on SQLite (no setup required)
- Loads schema and data automatically
- Run interactive queries from a menu
- Supports custom SQL input
- Outputs results in clean tables using `tabulate`

---

## 📦 Setup

### 1. Clone the repo

```bash
git clone https://github.com/elevelin/sql-query-tool.git
cd sql-query-tool
```
2. Install dependencies
```bash

pip3 install tabulate
```
## ▶️ Run It
```bash

python3 main.py
```
You’ll see a menu like:
📊 SQL Query Tool Menu:
```mathematica
1. Top customers by total spend
2. Monthly revenue
3. List all users
4. Run custom SQL
0. Exit
```
Choose a number to run that query — or write your own with option 4.

## 🧪Schema Overview
```users (id, name, email, created_at)
products (id, name, price)

orders (id, user_id, order_date)

order_items (id, order_id, product_id, quantity)
```
## 📁 Project Structure
```graphql

sql-query-tool/
├── main.py           # CLI tool
├── schema.sql        # Table definitions
├── seed.sql          # Sample data
├── data/shop.db      # Auto-created SQLite DB
├── .gitignore        # Excludes db
└── REA.md
```
## 🚀 Why This Project?

This tool shows:

- Proficiency in raw SQL (joins, group by, aggregates)

- Understanding of database schema design

- Python + SQLite integration

- Real-world reporting use cases
