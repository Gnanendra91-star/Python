import os

# 1. Define custom exception
class EmptyFileError(Exception):
    pass

filename = input("Enter the filename: ")

file = None
try:
    # 3. Try opening the file
    file = open(filename, "r")

    # 4. Check if file is empty
    if os.path.getsize(filename) == 0:
        raise EmptyFileError("The file is empty.")

    # 5. Read and process content
    content = file.read()
    words = content.split()
    print(f"The file has {len(words)} words.")

# 6. Handle exceptions
except FileNotFoundError:
    print("Error: The specified file was not found.")
except EmptyFileError as e:
    print(f"Error: {e}")

# 7. Finally block
finally:
    if file:
        file.close()
    print("File operation completed")

output:
TestCase-1
Enter the filename: python.txt
Error: The specified file was not found.
File operation completed

TestCase-2
Enter the filename: file1.txt
The file has 6 words.
File operation completed

TestCase-3
Enter the filename: empty.txt
Error: The file is empty.
File operation completed
