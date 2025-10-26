# Create and write content to files
file_list = ['file1.txt', 'file2.txt', 'file3.txt']

contents = [
    "This is the content of file1.",
    "Hello from file2!",
    "Sample line for file3."
]

for file_name, text in zip(file_list, contents):
    with open(file_name, 'w') as f:
        f.write(text)
import os

def copy_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, 'r') as original_file:
                original_content = original_file.read()
                base, ext = os.path.splitext(file_path)
                copy_file_path = f"{base}_copy{ext}"
                with open(copy_file_path, 'w') as copy_file:
                    copy_file.write(original_content)
                print(f"Contents copied from {file_path} to {copy_file_path} successfully.")
        else:
            print(f"Error: File '{file_path}' not found.")

copy_files(file_list)

output:
Contents copied from file1.txt to file1_copy.txt successfully.
Contents copied from file2.txt to file2_copy.txt successfully.
Contents copied from file3.txt to file3_copy.txt successfully.
