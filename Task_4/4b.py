# Input list of integers
numbers = [2, 8, 3, 4, 5, 6]

# List comprehension to get squares of even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]

# List comprehension with formatted descriptions
descriptions = [f"Square of {x} is {x**2}" for x in numbers if x % 2 == 0]

# Display the results
print("Even Squares:", even_squares)
print("Descriptions:", descriptions)

output:
Even Squares: [4, 64, 16, 36]
Descriptions: ['Square of 2 is 4', 'Square of 8 is 64', 'Square of 4 is 16', 'Square of 6 is 36']
