"""File to define River class."""

__author__ = "730470865"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class serves as a habit to both Bear and Fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish older than 3 days and bears older than 5 days."""
        fish_result: list[Fish] = []
        bears_result: list[Bear] = []
        for item in self.fish:
            if item.age <= 3:
                fish_result.append(item)
        for item in self.bears:
            if item.age <= 5:
                bears_result.append(item)
        self.fish = fish_result
        self.bears = bears_result
        return None

    def remove_fish(self, amount: int):
        """Used in the eating function to remove fish."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1

    def bears_eating(self):
        """Simulates bears eating fish, which increases a nears hunger score and decreases the total number of fish."""
        i: int = 0
        while i < len(self.bears) and len(self.fish) > 5:
            self.bears[i].eat(3)
            self.remove_fish(3)
            i += 1
        return None
    
    def check_hunger(self):
        """Removes bears with negative hunger scores."""
        bears_result: list[Bear] = []
        for item in self.bears:
            if item.hunger_score >= 0:
                bears_result.append(item)
        self.bears = bears_result
        return None
        
    def repopulate_fish(self):
        """Reproduces 4 fish for every pair of fish."""
        i: int = 1
        num_fish = len(self.fish)
        while i <= num_fish // 2:
            i2: int = 0
            while i2 < 4:
                self.fish.append(Fish())
                i2 += 1
            i += 1
        return None
    
    def repopulate_bears(self):
        """Reproduces 1 bear for every pair of bears."""
        i: int = 1
        num_bears = len(self.bears)
        while i <= num_bears // 2:
            self.bears.append(Bear())
            i += 1
        return None
    
    def view_river(self):
        """Visualizes the number of bears and fish on the current day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulates one week passing in the river."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1