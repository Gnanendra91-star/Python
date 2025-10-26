def teacher_notes_word_count():
    # Step 1: Create a file and write student notes
    file_name = input("Enter the file name: ")
    with open(file_name, 'w') as file:
        print("Enter student notes (press Enter on an empty line to stop):")
        while True:
            line = input()
            if not line:
                break
            file.write(line + '\n')

    # Step 2: Display the content of the file
    print("\nFile Content:")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)

    # Step 3: Count occurrences of a chosen word
    word = input("Enter the word to count: ")
    count = content.split().count(word)
    print(f"\nThe word '{word}' occurs {count} times.")

# Run the program
teacher_notes_word_count()

output:
Enter the file name: helloo.txt
Enter student notes (press Enter on an empty line to stop):
Python is great
python is easy to learn
I Love Python


File Content:
Python is great
python is easy to learn
I Love Python

Enter the word to count: Python

The word 'Python' occurs 2 times.
