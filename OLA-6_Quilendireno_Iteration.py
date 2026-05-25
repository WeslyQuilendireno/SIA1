# 1. Create a program that computes a student’s average accepting four (4) parameters (Name, Math
# Grade, English Grade, Science Grade).
# 2. Display the output.
# 3. Use iteration structure to accept another input from user.

def compute_average(name, math, english, science):

    average = (math + english + science) / 3


    print(f"\n{name}")
    print(f"    Math = {math}, English = {english}, Science = {science}")
    print(f"    Average = {average:.2f}")



while True:
    print("\n--- Student Grade Entry ---")
    student_name = input("Enter Name: ")
    m_grade = float(input("Enter Math Grade: "))
    e_grade = float(input("Enter English Grade: "))
    s_grade = float(input("Enter Science Grade: "))

    compute_average(student_name, m_grade, e_grade, s_grade)


    again = input("\nDo you want to accept another input? (yes/no): ").lower()
    if again != 'yes':
        print("Program terminated.")
    break
