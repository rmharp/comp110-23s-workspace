"""Calls methods from river.py used to simulate time passing in the river."""

from exercises.ex09.river import River

my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()