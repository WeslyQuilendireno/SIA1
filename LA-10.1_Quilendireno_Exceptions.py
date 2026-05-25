# MACHINE PROBLEM :
# 1. Create a calculator app
# 2. The user will choose between the 4 math operations (Add, Subtract, Multiply and Divide)
# 3. The application will ask for 2 numbers
# 4. Display the result
# 5. The application will ask if the user wants to try again
# 6. Use the appropriate Exceptions (ex: Invalid input such as text and zero division)
# 7. If not, display “Thank You”



while True:
    print("\n===== CALCULATOR APP ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        operation = int(input("\nChoose an operation (1-4): "))

        if operation not in [1, 2, 3, 4]:
            print("Error: Please choose a valid operation (1-4).")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == 1:
            result = num1 + num2
            symbol = "+"
        elif operation == 2:
            result = num1 - num2
            symbol = "-"
        elif operation == 3:
            result = num1 * num2
            symbol = "*"
        elif operation == 4:
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
            symbol = "/"

        print(f"\nResult: {num1} {symbol} {num2} = {result}")

    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")
        continue
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        continue

    again = input("\nDo you want to try again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThank You!")
        break