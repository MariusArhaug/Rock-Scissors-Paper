"""Action class"""


class Action:
    """Action class that overrides operator when a user calls an action"""
    action_values = {'Rock': 0, 'Scissors': 1, 'Paper': 2}
    action_names = {val: name for name, val in action_values.items()}

    def __init__(self, value):
        if isinstance(value, str):
            value = self.action_values[value]
        assert isinstance(value, int) & (value >= 0) & (value < 3)
        self.value = value

    def __eq__(self, other):
        """ If "equal sign" operator is used (==), do this method"""
        return self.value == other.value

    def __gt__(self, other):
        """ If "greater than"  operator is used (>), do this method"""
        return (self.value + 1) % 3 == other.value

    def __str__(self):
        """To string method, when printing an action, return the String value not the digit."""
        return self.action_names[self.value]

    def who_beats_me(self):
        """Return who beats self.value"""
        return (self.value + 2) % 3

