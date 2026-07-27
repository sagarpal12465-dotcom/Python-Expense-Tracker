with open("expenses.txt", "r") as file:
    lines = file.readlines()

total_expenses = 0

max_expense = 0
max_item = ""

for line in lines:
    if ":" in line:
        parts = line.split(":")
        item_name = parts[0].strip()
        amount_str = parts[1].strip()
        amount = int(amount_str)

        total_expenses = total_expenses + amount

        if amount > max_expense:
            max_expense = amount
            max_item = item_name

print("-" * 30)
print(f"Total Monthly Expense: {total_expenses} INR")
print(f"Highest Expense: {max_item} ({max_expense} INR)")
print("-" * 30)


with open("summary .txt", "w") as summary_file:
    summary_file.write("___ EXPENSE SUMMARY REPORT ___\n")
    summary_file.write(f"Total Amount Spent: {total_expenses} INR\n")
    summary_file.write(f"Highest Expense: {max_item} {max_expense} INR\n")
    summary_file.write("Status: Processd Succesfully\n")