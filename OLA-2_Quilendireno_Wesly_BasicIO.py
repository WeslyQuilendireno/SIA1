# MACHINE PROBLEM:
# Ask the user to input the student’s name, grade in Math, Science, and English. Then compute the average.


name = input("Enter student name: (LN, FN MI:)")
print ("Enter student's grade in\n")

math = float(input("math: "))
science = float(input("science: "))
english = float(input("english: "))

average = (math + science + english) / 3

print (f"Average grade of {name} is {average:.2f}.")

