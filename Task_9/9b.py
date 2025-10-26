# Custom Exception
class NegativeNumberError(Exception):
    pass  

try:
    # Take user input
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    # Check for negative numbers
    if num1 < 0 or num2 < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

    # Perform division
    result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except NegativeNumberError as e:
    print(f"Error: {e}")

finally:
    print("Calculation Attempt Finished")
  
output:
TestCase-1
Enter the numerator: 10
Enter the denominator: 0
Error: Division by zero is not allowed.
Calculation Attempt Finished

TestCase-2
Enter the numerator: 20
Enter the denominator: 10
Result: 20 / 10 = 2.0
Calculation Attempt Finished

TestCase-3
Enter the numerator: y
Error: Please enter valid numeric values.
Calculation Attempt Finished

TestCase-4
Enter the numerator: -5
Enter the denominator: 2
Error: Negative numbers are not allowed
Calculation Attempt Finished
