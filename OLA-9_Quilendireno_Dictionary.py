# MACHINE PROBLEM :

# 1. Create a Record Keeping App using Dictionary.
# 2. The application will ask the user to choose between:
# a. Add Data
# b. Delete Data
# c. End
# 3. If Add Data, the application will ask the user to input the key and its value:
# a. Enter key: Last Name
# b. Enter value: Doe
# ● The user may add different keys with its value
# ● Store the information in a Dictionary
# ● Display the result
# 4. If Delete Data, the application will ask for the key and its value then delete the value.
# a. Enter key: First Name
# b. Enter value: John
# ● Remove the item from the Dictionary.
# ● Display the result.
# 5. If End, display “Thank You”

record = {}

while True:
    print("\n===== Record Keeping App =====")
    print("1. Add Data")
    print("2. Delete Data")
    print("3. End")

    choice = input("Choose an option: ")
    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        if key in record:
            record[key].append(value)
        else:
            record[key] = [value]
        print("\nRecord updated:")
        for k, v in record.items():
            print(f"  {k}: {', '.join(v)}")

    elif choice == "2":
        key = input("Enter key: ")
        value = input("Enter value: ")
        if key in record and value in record[key]:
            record[key].remove(value)
            if not record[key]:
                del record[key]
            print(f"\n'{value}' removed from '{key}'.")
        else:
            print("\nKey or value not found in records.")
        print("\nRecord updated:")
        for k, v in record.items():
            print(f"  {k}: {', '.join(v)}")

    elif choice == "3":
        print("\nThank You")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

