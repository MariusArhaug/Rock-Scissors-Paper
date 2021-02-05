"""
    Inherits from player
"""
from Player import Player


class Sequential(Player):
    """
        Sequential player: Plays moves based on input sequence given at the start of the list.
    """

    def __init__(self, sequence, name="Sequential"):
        super().__init__(name)
        self.sequence = sequence
        self.index = 0

        if not all(isinstance(n, str) for n in self.sequence):
            raise ValueError("All values in sequence must be string or integer")
        if not all(n.lower() in ["rock", "paper", "scissors"] for n in self.sequence):
            raise ValueError("All string values must be typed correct: (Rock, Paper, Scissor)")
        # if it is a list of strings (Rock/Paper/Scissors) accept it and type it correct
        self.__handle_typo__()

    def __handle_typo__(self):
        """ Change into correct format, then change values from string to integers """

        self.sequence = list(map(lambda action: Player.action_values[action.strip().capitalize()], self.sequence))

    def select_action(self, value=None):
        """Get next action in the sequence"""
        seq_action = self.sequence[self.index]
        self.handle_sequence()
        return super().select_action(seq_action)

    def handle_sequence(self):
        """
        Iterate through the sequence list
        if index is greater than list length reset.
        """
        self.index = (self.index + 1) % len(self.sequence)
