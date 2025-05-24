# dict_examples.py

# Define a dictionary
student = {
    "name": "John",
    "age": 21,
    "courses": ["Math", "Physics"]
}

# Accessing values
print("Student name:", student["name"])

# Add new key-value pair
student["grade"] = "A"

# Update existing value
student["age"] = 22

# Loop through dictionary
print("\nStudent info:")
for key, value in student.items():
    print(f"{key}: {value}")
