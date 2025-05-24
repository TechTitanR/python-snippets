# file_handling_example.py

# Write to a file
with open("sample.txt", "w") as file:
    file.write("Hello from file handling in Python!")

# Read from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)
