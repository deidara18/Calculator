expression = input("Введите математическое выражение: ")

numbers_and_operators = []

current_number = 0

for char in expression:

    if char.isdigit():
        current_number = current_number * 10 + int(char)
    elif char == "+" or char == "-" or char == "*" or char == "/":
        numbers_and_operators.append(current_number)
        numbers_and_operators.append(char)
        current_number = 0

numbers_and_operators.append(current_number)

i = 1
while i < len(numbers_and_operators) - 1:
    operator = numbers_and_operators[i]
    if operator == "*":
        numbers_and_operators[i - 1] = numbers_and_operators[i - 1] * numbers_and_operators[i + 1]
        del numbers_and_operators[i:i + 2]
    elif operator == "/":
        numbers_and_operators[i - 1] = numbers_and_operators[i - 1] / numbers_and_operators[i + 1]
        del numbers_and_operators[i:i + 2]
    else:
        i += 2

current_total = numbers_and_operators[0]
for i in range(1, len(numbers_and_operators), 2):
    operator = numbers_and_operators[i]
    number = numbers_and_operators[i + 1]
    if operator == "+":
        current_total += number
    elif operator == "-":
        current_total -= number

print("Результат: ", current_total)
