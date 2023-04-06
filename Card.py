class Card:
    """
    This class represents a playing card with a suit and a value.

    Attributes:
    suit (str): the suit of the card (e.g. "hearts", "diamonds", "clubs", "spades").
    value (str): the value of the card (e.g. "ace", "2", "3", ..., "10", "jack", "queen", "king").

    Methods:
    __str__: returns a string representation of the card in the format "value of suit".
    __repr__: returns a string representation of the card,
    which is the same as the string representation returned by __str__.
    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return self.__str__()

