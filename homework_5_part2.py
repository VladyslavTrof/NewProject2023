
answer = "yes"

while answer == "yes" or answer == "y":
  number_1 = float(input("Enter first number: "))
  number_2 = float(input("Enter second number: "))

  operation = input("Choose your operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

  if operation == "1":
    result = number_1 + number_2
    print(f"{number_1} + {number_2} = {result}")
  elif operation == "2":
    result = number_1 - number_2
    print(f"{number_1} - {number_2} = {result}")
  elif operation == "3":
    result = number_1 * number_2
    print(f"{number_1} * {number_2} = {result}")
  elif operation == "4":
    result = number_1 / number_2
    print(f"{number_1} / {number_2} = {result}")
  else:
    print("Wrong action selected")

  answer = input("Would you like to continue using calculator (yes/y or no/n): ")

  answer = answer.lower()

print("Thank you for using calculator! Have a nice day!")
