#1
def arithmetic_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return f"Not known operation: {operation}"

print(arithmetic_operation(8, 2, '*'))
print(arithmetic_operation(8, 2, '+'))
print(arithmetic_operation(8, 2, '#'))