csv_content = """Id,Name,Grade,Attendance
101,Alice,A,90
102,Bob,B,85
103,Charlie,A,95
104,David,C,80
105,Eve,B,88
"""

# Write to a file named 'students.csv'
with open("students.csv", "w") as file:
    file.write(csv_content)
import csv

# Read CSV file
file_name = input("Enter CSV file name: ")
records = []

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        records.append(row)

# Display all records
print("\nStudent Records:")
for r in records:
    print(f"Id: {r[0]}, Name: {r[1]}, Grade: {r[2]}, Attendance: {r[3]}")

# Calculate average attendance
total = sum(int(r[3]) for r in records)
average = total / len(records)
print(f"\nAverage Attendance: {average:.2f}")

output:
Enter CSV file name: students.csv

Student Records:
Id: 101, Name: Alice, Grade: A, Attendance: 90
Id: 102, Name: Bob, Grade: B, Attendance: 85
Id: 103, Name: Charlie, Grade: A, Attendance: 95
Id: 104, Name: David, Grade: C, Attendance: 80
Id: 105, Name: Eve, Grade: B, Attendance: 88

Average Attendance: 87.60
