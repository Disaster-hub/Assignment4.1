import json

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def ensure_user(data, user_id):
    if user_id not in data:
        data[user_id] = {
            "income": 0,
            "budgets": {},
            "transactions": [],
            "notifications": False
        }

def get_balance_summary(user_data):
    total_income = user_data.get("income", 0)
    expenses = sum(t["amount"] for t in user_data["transactions"] if t["type"] == "expense")
    current_balance = total_income + sum(t["amount"] for t in user_data["transactions"])

    summary = f"💰 Income: ${total_income:.2f}\n"
    summary += f"📉 Expenses: ${-expenses:.2f}\n"
    summary += f"📊 Balance: ${current_balance:.2f}\n\n"
    summary += "🗂️ Budgets:\n"
    for cat, amt in user_data.get("budgets", {}).items():
        spent = sum(t["amount"] for t in user_data["transactions"] if t["category"] == cat and t["type"] == "expense")
        summary += f" - {cat}: ${amt:.2f} | Spent: ${-spent:.2f}\n"
    return summary
