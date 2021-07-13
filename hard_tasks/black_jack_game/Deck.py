from itertools import product
from random import shuffle
from const import RANKS, SUITS, PRINTED


class BlackJack:
    """
    The class of the card itself with certain parameters
    """

    def __init__(self, suit, rank, picture, points):
        self.suit = suit  # масть карты
        self.rank = rank  # ранг карты
        self.picture = picture # отображение карты
        self.points = points  # вес карты(сколько очков)

    def __str__(self):
        """
        :return: Drawing a playing card and the number of points
        """
        message = self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck:
    """
    Generating and calling up a deck of cards
    """
    def __init__(self):
        """
        Function - Initiator for creating and shuffling a deck
        """
        self.cards = self._generate_deck()
        shuffle(self.cards)

    @staticmethod
    def _generate_deck():
        """
        creating and shuffling a deck
        :return: Returns a finished, shuffled deck of cards
        """
        cards = []
        for suit, rank in product(SUITS, RANKS): # Double cycle for shuffling suit and rank cards
            if rank == 'A':
                points = 11
            elif rank.isdigit(): # if rank card has no 'str' val
                points = int(rank) # reverse this value in int
            else:
                points = 10 # else this card has 10 points
            picture = PRINTED.get(rank) #render picture card
            c = BlackJack(suit=suit, rank=rank, points=points, picture=picture)#creating a class instance
            cards.append(c)
        return cards

    def get_card(self):
        """
        :return: get one random card
        """
        return self.cards.pop()

    def __len__(self):
        """
        :return: length of deck card
        """
        return len(self.cards)
