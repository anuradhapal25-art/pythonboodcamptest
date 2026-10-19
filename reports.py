
def total_spent(expenses):
    total = 0
    for item, amount in expenses:
        total = total + amount
    return total


def biggest_expense(expenses):
    return sorted(expenses, key=lambda x: x[1])[-1]
