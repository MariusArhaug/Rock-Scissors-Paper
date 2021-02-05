"""
    Import action here so other child classes dont have to import it.
"""
from Action import Action


class Player:
    """
    Basic player is parent class, could be abstract
    """
    action_values = Action.action_values
    action_names = Action.action_names
    player_types = ["Random", "Sequential", "MostCommon", "Historian"]

    def __init__(self, name, *arg):
        self.__name__ = name
        self.__stats__ = {"Points": 0, "Games": 0}

    def select_action(self, value):
        """ Select which action to perform"""
        if not isinstance(value, int):
            raise ValueError(f"Expected action_type to be integer, got: {type(value)}")

        return Action(value) if value in self.action_names else print("Not valid action")

    def receive_result(self, result):
        """Increase points based on result"""
        if result == "draw":
            self.__stats__["Points"] += 0.5
        elif result == "winner":
            self.__stats__["Points"] += 1

    def update_number_of_games(self):
        """Update number of games"""
        self.__stats__["Games"] += 1

    def get_win_percentage(self):
        """Return win percentage"""
        return self.__stats__["Points"]/self.__stats__["Games"]

    def enter_name(self, name):
        """Make it possilble to change names"""
        self.__name__ = name

    def __str__(self):
        return self.__name__
