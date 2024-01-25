number1 = float(input("Enter the first digit: "))

number2 = float(input("Eneter the second digit: "))

operation = input("Enter your action (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
if operation == "-":
    result = number1 - number2
if operation == "*":
    result = number1 * number2
if operation == "/":
    if number2 != 0:
        result = number1 / number2
    else:

        print("Error: division 0!")

        exit()
else:

    print("Error: wrong operation!")

    exit()

print(f"{number1} {operation} {number2} = {result}")
