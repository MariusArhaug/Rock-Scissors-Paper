"""
    Imports
"""

from MostCommon import MostCommon
from Historian import Historian
from Player import Player


class SingleGame:
    """
    A single game between two players
    """

    @staticmethod
    def check_type(var, obj):
        """Check that input is right instance"""
        if not isinstance(var, obj):
            raise ValueError(f"Inappropriate type: {type(var)} for constructor")

    def __init__(self, player1, player2):
        self.check_type(player1, Player)
        self.check_type(player2, Player)

        self.__player1__ = player1
        self.__player2__ = player2
        self.__number_of_games__ = 0

    def perform_game(self):
        """ Ask player for their choice of action"""
        self.__number_of_games__ += 1
        self.__player1__.update_number_of_games()
        self.__player2__.update_number_of_games()

        action_one = self.__player1__.select_action()
        action_two = self.__player2__.select_action()

        # Draw
        if action_one == action_two:
            self.__player1__.receive_result("draw")
            self.__player2__.receive_result("draw")
            self.__show_result__("Draw", "Draw", action_one, action_two)

        # Player1 wins
        elif action_one > action_two:
            self.__player1__.receive_result("winner")
            self.__show_result__(self.__player1__, self.__player2__, action_one, action_two)

        # Player2 wins
        elif action_two > action_one:
            self.__player2__.receive_result("winner")
            self.__show_result__(self.__player2__, self.__player1__, action_two, action_one)

        # If one of our players are MostCommon or Historian we need to save the opponents moves.
        if isinstance(self.__player1__, (MostCommon, Historian)):
            self.__player1__.save_opponents_choice(action_two)
        elif isinstance(self.__player2__, (MostCommon, Historian)):
            self.__player2__.save_opponents_choice(action_one)

    def __show_result__(self, winner, looser, action_win, action_loose):
        """Print out a final result between two players and their moves."""
        print(f"--------------------Game Number: {self.__number_of_games__}--------------------")
        if winner == "Draw" and looser == "Draw":
            print(f"The game ended in a draw. Both chose {action_win}")
        else:
            print(f"{winner} won over {looser} with the {action_win} vs {action_loose}")
        print(" ")
