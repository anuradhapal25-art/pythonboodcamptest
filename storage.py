
import csv
def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Amount"])

        for item, amount in expenses:
            writer.writerow([item, amount])

def load_expenses():
    expenses = []
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append((row["Item"], int(row["Amount"])))
    except FileNotFoundError:
        return []
    return expenses
