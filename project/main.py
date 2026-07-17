# pakage is (utils) -> (add __init__) forlder theat contains that has many modules 

from utils.calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
)

from utils.fformatter import display_result


while True:
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Thank you!")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        display_result("Addition", add(a, b))

    elif choice == "2":
        display_result("Subtraction", subtract(a, b))

    elif choice == "3":
        display_result("Multiplication", multiply(a, b))

    elif choice == "4":
        display_result("Division", divide(a, b))

    elif choice == "5":
        display_result("Modulus", modulus(a, b))

    elif choice == "6":
        display_result("Power", power(a, b))

    else:
        print("Invalid Choice")