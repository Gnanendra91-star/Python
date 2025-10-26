from functools import reduce

# Sample data
student_names = ["Alice", "Bob", "Charlie", "Diana"]
student_grades = [65, 72, 58, 70]

print("Original Grades:")
print(list(zip(student_names, student_grades)))

# 1. Scale grades using map and lambda (e.g., add 20 internal points to each grade)
scaled_grades = list(map(lambda x: x + 20, student_grades))
print("\nScaled Grades (+20 points):")
print(list(zip(student_names, scaled_grades)))

# 2. Filter students with grades above 90 using filter and lambda
high_achievers = list(filter(lambda x: x > 90, scaled_grades))
print("\nStudents with grades above 90:", high_achievers)

# 3. Calculate total and average using reduce
total = reduce(lambda a, b: a + b, scaled_grades)
average = total / len(scaled_grades)
print("\nTotal of scaled grades:", total)
print("Average of scaled grades:", average)

# 4. Sort grades in ascending order using sorted and lambda
sorted_grades = sorted(scaled_grades)
print("\nSorted Grades (Ascending):", sorted_grades)


# 5. Sort grades in descending order using sorted and lambda
sorted_desc = sorted(scaled_grades, reverse=True)
print("\nSorted Grades (Descending):",sorted_desc)

output:
Original Grades:
[('Alice', 65), ('Bob', 72), ('Charlie', 58), ('Diana', 70)]

Scaled Grades (+20 points):
[('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 90)]

Students with grades above 90: [92]

Total of scaled grades: 345
Average of scaled grades: 86.25

Sorted Grades (Ascending): [78, 85, 90, 92]

Sorted Grades (Descending): [92, 90, 85, 78]
