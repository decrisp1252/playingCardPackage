class CardProperties:
    """
    This is a class that represents a list of possible suits and values for a deck of cards.

    Attributes:
    suit_list (list): a list of possible suits for a card (e.g. "hearts", "diamonds", "clubs", "spades").
    value_list (list): a list of possible values for a card (e.g. "ace", "2", "3", ..., "10", "jack", "queen", "king").

    Methods:
    __init__: initializes a CardProperties instance with the specified suits and values.
    extract_suit_list_from_file: extracts a list of suits from a file.
    extract_value_list_from_file: extracts a list of values from a file.
    """
    suit_list = ["Hearts", "Diamonds", "Spades", "Clubs"]
    value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "Ace"]

    def __init__(self, suits=None, values=None):
        if suits is not None:
            self.suit_list = suits
        else:
            self.suit_list = ["Hearts", "Diamonds", "Spades", "Clubs"]

        if values is not None:
            self.value_list = values
        else:
            self.value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "Ace"]

    def extract_suit_list_from_file(self, filename):
        try:
            with open(filename, "r") as suit_list_file:
                self.suit_list = suit_list_file.readlines()
        except FileNotFoundError:
            print("ERROR: File not found.")

    def extract_value_list_from_file(self, filename):
        try:
            with open(filename, "r") as value_list_file:
                self.value_list = value_list_file.readlines()
        except FileNotFoundError:
            print("ERROR: File not found.")
