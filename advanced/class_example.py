# class_example.py

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Testing
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())
