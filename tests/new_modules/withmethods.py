class Person:
    """Base class representing a person."""

    def __init__(self, name: str, age: int):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute

    def introduce(self) -> str:
        """Public method to introduce the person."""
        return f"My name is {self.name} and I am {self._age} years old."

    def celebrate_birthday(self):
        """Public method to increment age and return a message."""
        self._age += 1
        return f"Happy Birthday, {self.name}! You are now {self._age} years old."
