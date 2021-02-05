""" Import parent and random method"""

import random
from Player import Player


class Historian(Player):
    """Historian plays moves based on opponents most frequent sequence of size r"""
    def __init__(self, name="Historian", r=1):
        if not isinstance(r, int):
            raise ValueError("Expected remember argument to be an integer")

        assert isinstance(r, int) & (r >= 1) & (r <= 3)
        super().__init__(name + " (" + str(r) + ")")
        self.opponents_choices = []
        self.remember = r

    def save_opponents_choice(self, action):
        """Save opponents action"""
        self.opponents_choices.append(str(action))

    def select_action(self, value=None):
        """Depending on remember length Historian have to play random until it has a sequence"""
        if len(self.opponents_choices) < self.remember + 1:
            return super().select_action(random.randint(0, 2))

        # if sequence not found before also return random choice
        action = self.__find_most_common_in_sequence__()
        if action is None:
            return super().select_action(random.randint(0, 2))

        # If the sequence is only one element, strip it and make it into a proper key.
        if len(action) == 1:
            action = str(action).strip("(),' ")
        else:
            # If it is a list get the first move after the most common sequence
            action = action[0]

        action = (Player.action_values[action] + 2) % 3

        return super().select_action(action)

    def __find_most_common_in_sequence__(self):
        """Find most common sequence"""

        # Depending on remember length look at most common choices after what the last choice is.

        # Get last r elements of the opponents sequence.
        last_sequence = list(self.opponents_choices[-self.remember:])

        # Save what sequence is followed after the opponents "last_sequence"
        # If the last_sequence is found, we know that we need to save the next sequence
        # Then found_sequence is True, go to next iteration with that sequence that we want to save
        played_after_last_sequence = []

        found_sequence = False
        for sequence in self.get_sub_sequence(self.opponents_choices):
            if found_sequence:
                played_after_last_sequence.append(sequence)

            if sequence == last_sequence:
                found_sequence = True
                continue
            found_sequence = False
        # If the sequence is still empty, then Historian has to choose a random choice.

        if len(played_after_last_sequence) == 0:
            return None

        # Turn list of sub_lists into list of sub_tuples so that we can use them as hashes
        played_after_last_sequence = [tuple(sub_list) for sub_list in played_after_last_sequence]
        # print(played_after_last_sequence)

        # Now we count how many of each sequence appears in the played_after_last_sequence list.
        counts = {}
        for played in played_after_last_sequence:
            if played in counts.keys():
                counts[played] += 1
            else:
                counts[played] = 1

        # Return the sub sequence with the most appearances.
        return max(counts, key=counts.get)

    def get_sub_sequence(self, sequence):
        """Generator that splits list into tuples of size self.remember"""
        for i in range(0, len(sequence), self.remember):
            yield sequence[i: i+self.remember]
