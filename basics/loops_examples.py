# loops_examples.py

# For loop
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop
print("\nWhile loop until counter reaches 5:")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# Nested loop
print("\nNested loop (3x3 grid):")
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()
