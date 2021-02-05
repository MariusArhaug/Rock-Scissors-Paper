"""
    Modules for players, and Tournament
"""
from Player import Player
from Historian import Historian
from MostCommon import MostCommon
from Sequential import Sequential
from RandomPlayer import RandomPlayer
from Tournament import Tournament


class Controller:
    """
        Main controller class that user interacts with
    """
    def __init__(self):
        self.__choices__ = []
        self.__players__ = []

    def run_interface(self):
        """
            Main interface that a user interacts with
        """
        print("--------------------------Rock-Paper-Scissors--------------------------")

        self.get_player_types()
        self.declare_player_types()
        number_of_games = int(input("Number of games to be played: "))
        player_one = self.__players__[0]
        player_two = self.__players__[1]
        tournament = Tournament(player_one, player_two, number_of_games)
        tournament.arrange_tournament()

        print("-----------------------------------------------------------------------")

    def get_player_types(self):
        """
         Ask the user what types of players he wants to play against each other.
         :return:
        """
        for i in range(2):
            while True:
                answer = input(f"Choose player {i + 1}: (Random, Sequential, MostCommon, Historian): ").lower()
                if answer not in map(str.lower, Player.player_types):
                    raise ValueError(f"Expected one of the four player types {Player.player_types}")
                break
            self.__choices__.append(answer)

    def declare_player_types(self):
        """
         # After the choices have been made for P1 and P2, do the appropriate init for them.
        :return:
        """
        player = None
        for i, choice in enumerate(self.__choices__):
            if choice == "random":
                player = RandomPlayer()

            elif choice == "sequential":
                print(f"Player {i+1} chose Sequential, decide your sequence")
                sequence = [action for action in input("Sequence: ").split(", ")]
                player = Sequential(sequence)

            elif choice == "mostcommon":
                player = MostCommon()

            elif choice == "historian":
                print(f"Player {i+1} chose Sequential, decide your remembering (1,2,3)")
                r = int(input("Remembering: "))
                player = Historian(r=r)

            self.__players__.append(player)


def main():
    """
        main method
    :return:
    """
    controller = Controller()
    controller.run_interface()


if __name__ == '__main__':
    main()
