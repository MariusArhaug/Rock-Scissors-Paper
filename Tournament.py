"""
    Import Single game, player and plotting tools
"""
from matplotlib.pyplot import plot, figure, xlabel, ylabel, title, legend, show
from SingleGame import SingleGame, Player


class Tournament:
    """
        Tournament class that runs multiple single games.
    """

    def __init__(self, player1, player2, number_of_games=100):
        """
            Start up the tournament with players and number of games.
        """
        # Proof check variables.
        if not isinstance(number_of_games, int):
            raise ValueError("Expected number_of_games to be an integer!")

        SingleGame.check_type(player1, Player)
        SingleGame.check_type(player2, Player)

        self.__player1__ = player1
        self.__player2__ = player2
        self.__single_game__ = SingleGame(player1, player2)
        self.__number_of_games__ = number_of_games

    def arrange_single_game(self):
        """
            Perform a single game
        :return:
        """
        self.__single_game__.perform_game()

    def arrange_tournament(self):
        """
            Run n single games and collect their statistics
        :return:
        """

        # Collect the players win percentage per game and use it to plot a graph.
        values_1 = []
        values_2 = []
        x = []
        for x_i in range(1, self.__number_of_games__ + 1):
            self.__single_game__.perform_game()

            x.append(x_i)
            values_1.append(self.__player1__.get_win_percentage())
            values_2.append(self.__player2__.get_win_percentage())

        self.create_figure(x, values_1, values_2)

    # Graph the final graph of the two players results and see how it evolves.
    # The graphs will be mirrored of each other
    def create_figure(self, x_values, y_values_1, y_values_2):
        """
            Use the final results from the games to plot a graph with their scores.
        :param x_values:
        :param y_values_1:
        :param y_values_2:
        :return:
        """
        print("Final results:")
        figure()

        plot(x_values, y_values_1)
        plot(x_values, [0.5]*len(x_values), linestyle="dashed", color="grey")
        plot(x_values, y_values_2)

        xlabel("Number of games")
        ylabel("Score per game")
        title(f"Tournament with {self.__player1__} vs. {self.__player2__} with a {self.__number_of_games__} of games")
        legend([f'{self.__player1__}', f'{self.__player2__}'], loc=2)
        show()
