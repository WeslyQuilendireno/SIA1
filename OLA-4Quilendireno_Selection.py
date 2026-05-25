# MACHINE PROBLEM:
#1. Write a program that will show the bonus of an employee by asking the employee’s years in service and office.
#2. The user will input number for years in service and initials for their department (IT, Acct, HR)

name = input("Enter employee name:")
years = int(input("Enter years-in-service: "))
office = input("Enter office: ")

office = office.lower()

if office == "it":
    if years >= 10:
        bonus = 1000
    else:
        bonus = 500

elif office == "acct":
    if years >= 10:
        bonus = 1200
    else:
        bonus = 6000

elif office == "hr":
    if years >= 10:
        bonus = 1500
    else:
        bonus = 7500


print (f"Hi {name}, your bonus is  {bonus}.")
