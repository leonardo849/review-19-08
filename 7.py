def calculateBalance(salary, expensesList):
    expensesValue = 0
    for ex in expensesList:
        expensesValue += ex
    return f"salary: {salary}, expenses: {expensesValue}, balance: {salary - expensesValue}"

print(calculateBalance(5000, [5500]))