"""Import player and random method"""
import random
from Player import Player


class MostCommon(Player):
    """Based on opponents choices, choose the best attack for their most common choice"""
    def __init__(self, name="MostCommon"):
        super().__init__(name)
        self.opponents_choices = []

    def select_action(self, value=None):
        """First round it chooses randomly an attack, then do find most common"""
        if len(self.opponents_choices) == 0:
            return super().select_action(random.randint(0, 2))

        # Find the opponents most common action and choose an action that wins over it
        action = (Player.action_values[self.__find_most_common__()] + 2) % 3

        return super().select_action(action)

    def save_opponents_choice(self, action):
        """Save choices"""
        self.opponents_choices.append(str(action))

    def __find_most_common__(self):
        """Find most common"""
        return max(set(self.opponents_choices), key=self.opponents_choices.count)
