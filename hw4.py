def calculate_expenses(expenses):
    total_amount = 0
    categories = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        total_amount += amount
        if category not in categories:
            categories[category] = 0
        categories[category] += amount
    max_category = max(categories, key=categories.get)
    return f"Total: {total_amount}, Max category: {max_category}"

expenses = [
    {"category": "food", "amount": 120.5},
    {"category": "transport", "amount": 55.3},
    {"category": "food", "amount": 80.2},
    {"category": "entertainment", "amount": 200},
    {"category": "transport", "amount": 45.1},
]

result = calculate_expenses(expenses)
print(result) 
