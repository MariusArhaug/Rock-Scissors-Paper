"""Import player and random method"""
import random
from Player import Player


class RandomPlayer(Player):
    """Player randomly selects rock/paper/scissors"""
    def __init__(self, name="Random"):
        super().__init__(name)

    def select_action(self, value=None):
        """
        Select random action
        """
        action = random.randint(0, 2)
        return super().select_action(action)
