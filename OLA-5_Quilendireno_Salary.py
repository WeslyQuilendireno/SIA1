<<<<<<< HEAD

#MACHINE PROBLEM:
# 1. Ask the user to input employee name, number of hours rendered, SSS contribution, PhilHealth
# contribution, and Housing Loan.
# 2. Display the salary computation as payslip.

employee_name = input("Employee Name: ")
rendered_hours = float(input("Enter number of hours: "))
SSS_contribution = float(input("SSS contribution: "))
PhilHealth_contribution = float(input("Phil health: "))
Housing_Loan = float(input("Housing loan: "))

hourly_rate = 500
gross_salary = rendered_hours * hourly_rate
tax = gross_salary * 0.10
total_deductions = SSS_contribution + PhilHealth_contribution + Housing_Loan + tax
net_salary = gross_salary - total_deductions


print(f"""
==========PAYSLIP==========
==========EMPLOYEE INFORMATION===
Employee Name: {employee_name.upper()}
Rendered Hours: {rendered_hours}
Rate per Hour: {hourly_rate}
Gross Salary: {gross_salary}
==========DEDUCTIONS==========
SSS: {SSS_contribution}
PhilHealth: {PhilHealth_contribution}
Other Loan: {Housing_Loan}
Tax: {tax}
Total Deductions: {total_deductions}
Net Salary: {net_salary}
""")
=======

#MACHINE PROBLEM:
# 1. Ask the user to input employee name, number of hours rendered, SSS contribution, PhilHealth
# contribution, and Housing Loan.
# 2. Display the salary computation as payslip.

employee_name = input("Employee Name: ")
rendered_hours = float(input("Enter number of hours: "))
SSS_contribution = float(input("SSS contribution: "))
PhilHealth_contribution = float(input("Phil health: "))
Housing_Loan = float(input("Housing loan: "))

hourly_rate = 500
gross_salary = rendered_hours * hourly_rate
tax = gross_salary * 0.10
total_deductions = SSS_contribution + PhilHealth_contribution + Housing_Loan + tax
net_salary = gross_salary - total_deductions


print(f"""
==========PAYSLIP==========
==========EMPLOYEE INFORMATION===
Employee Name: {employee_name.upper()}
Rendered Hours: {rendered_hours}
Rate per Hour: {hourly_rate}
Gross Salary: {gross_salary}
==========DEDUCTIONS==========
SSS: {SSS_contribution}
PhilHealth: {PhilHealth_contribution}
Other Loan: {Housing_Loan}
Tax: {tax}
Total Deductions: {total_deductions}
Net Salary: {net_salary}
""")
>>>>>>> 0e24f6a61b5ebe0de3ed9817783479a27d9c7133
