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

#2

side = 7

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = (2 * side) ** 0.5
    return (perimeter, area, diagonal)

print(square(side))