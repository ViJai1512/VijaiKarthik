import json

# Open and load JSON file
with open("students.json", "r") as file:
	students = json.load(file)

# Print all student names
print("Students:")
for s in students:
	print(s['name'])
 
# Calculate total & average marks for each student
print("\nMarks Summary:")
for s in students:
	total = sum(s['marks'].values())
	avg = total / len(s['marks'])
	print(f"{s['name']} - Total: {total}, Average: {avg:.2f}")