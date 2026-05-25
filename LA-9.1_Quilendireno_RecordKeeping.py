# 1. Create a Record Keeping App.
# 2. The app will display the following options
# A. Add a Record
# B. View All Records
# C. Clear All Records
# D. Exit
# 3. If A, the user will input the following information (Name, Email Address, Home Address).
# The app will save the information in a text file.
# 4. If B, the app will display all the records.
# 5. If C, the app will clear the text file (do not remove the file) and display “No records found!”
# 6. If D, display “Thank you!”


FILE_NAME = "records.txt"

def add_record():
    name = input("Enter Name: ")
    email = input("Enter Email Address: ")
    address = input("Enter Home Address: ")
    with open(FILE_NAME, "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email Address: {email}\n")
        file.write(f"Home Address: {address}\n")
        file.write("-" * 30 + "\n")
    print("\nRecord saved successfully!")

def view_records():
    with open(FILE_NAME, "r") as file:
        content = file.read()
    if content.strip() == "":
        print("\nNo records found!")
    else:
        print("\n===== ALL RECORDS =====")
        print(content)

def clear_records():
    with open(FILE_NAME, "w") as file:
        file.write("")
    print("\nNo records found!")
open(FILE_NAME, "a").close()

while True:
    print("\nRECORD KEEPING APP")
    print("A. Add a record")
    print("B. View all record")
    print("C. Clear all records")
    print("D. Exit")

    choice = input("Please enter your choice: ").strip().upper()

    if choice == "A":
        add_record()
    elif choice == "B":
        view_records()
    elif choice == "C":
        clear_records()
    elif choice == "D":
        print("\nThank you!")
        break
    else:
        print("\nInvalid choice. Please enter A, B, C, or D.")