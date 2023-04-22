"""File to define Bear class."""


class Bear:
    """Animal type Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger_score to be 0."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Defines how one day of time passing affects the bear's age and hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Defines how eating fish replenishes a bear's hunger."""
        self.hunger_score += num_fish