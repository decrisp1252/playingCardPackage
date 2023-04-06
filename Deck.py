from Card import *
import random


class Deck:
    """
    This is a class that represents a deck of the Cards class.

    Attributes:
    deck (list): a list containing the cards in the deck.

    Methods:
    init: initializes a deck instance.
    str: returns a string representation of a deck instance.
    show_entire_card_deck: prints the entire deck of cards.
    """
    deck = []

    def __init__(self, nof_card_packs, shuffled, value_list, suit_list):
        for pack in range(nof_card_packs):
            self.deck += [Card(suit, value) for value in value_list for suit in suit_list]

        if shuffled is True:
            random.shuffle(self.deck)

    def __str__(self):
        return f"{len(self.deck)} cards in deck."

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        return self.deck[index]

    def show_entire_card_deck(self):
        for i in range(len(self.deck)):
            print(self.deck[i])

    def draw_from_top(self, num_cards=1):
        drawn_cards = []
        for i in range(num_cards):
            if len(self.deck) > 0:
                drawn_cards.append(self.deck.pop(0))
            else:
                break
        return drawn_cards

    def draw_from_bottom(self, num_cards=1):
        drawn_cards = []
        for i in range(num_cards):
            if len(self.deck) > 0:
                drawn_cards.append(self.deck.pop(len(self.deck)))
            else:
                break
        return drawn_cards

    def show_top_card(self):
        return self.deck[0]
