"""File to define Fish class."""


class Fish:
    """Animal type Fish."""

    age: int

    def __init__(self):
        """Initializes age to be 0."""
        self.age = 0
        return None
    
    def one_day(self):
        """Defines how one day of time passing affects the bear's age."""
        self.age += 1
        return None