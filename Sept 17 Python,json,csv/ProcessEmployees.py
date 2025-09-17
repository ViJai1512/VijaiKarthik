import csv
# Read CSV file
with open("employees.csv", "r") as file:
	reader = csv.DictReader(file)
	employees = list(reader)
# Print all employees
print("Employees:")
for e in employees:
	print(f"- {e['name']} ({e['department']}) - Salary: {e['salary']} ₹")
 
# calculate total and average salary
salaries = [float(e['salary']) for e in employees]
total_salary = sum(salaries)
average_salary = total_salary / len(salaries)
print(f"\nTotal Salary: ₹{total_salary:.2f}")
print(f"Average Salary: ₹{average_salary:.2f}")