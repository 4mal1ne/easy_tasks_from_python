import abc
from Deck import Deck
import random


class AbstractPLayer(abc.ABC):
    """
    PLayer class. We can see his value cards, his position on the table, his rate and points value
    """
    def __init__(self, position):
        self.cards = []
        self.position = position
        self.rate = 0
        self.full_points = 0

    def change_points(self):
        """
        :return: Check Method for player points, when he take a new card
        """
        self.full_points = sum([card.points for card in self.cards])

    def ask_card(self, deck, card_count):
        """
        :param deck: take a deck
        :param card_count: check a card count
        :return:
        """
        for _ in range(card_count):
            card = deck.get_card()
            self.cards.append(card)
        self.change_points()
        return True

    @abc.abstractmethod
    def change_rate(self, max_rate, min_rate):# change rate
        pass

    def print_cards(self):
        """
        Print our cards
        :return:
        """
        for card in self.cards:
            print(card)


class Player(AbstractPLayer):
    """

    """
    def change_rate(self, max_rate, min_rate):
        while True:
            value = int(input('Make your rate: '))
            if value < max_rate and value > min_rate:
                self.rate = value
                break
        print(f'Your rate is {self.rate}')


# to do is it needed ?
# class Dealler(AbstractPLayer):
#     pass


class Bot(AbstractPLayer):
    def change_rate(self, max_rate, min_rate):
        self.rate = random.randint(min_rate, max_rate)
        print(f'{self} give {self.rate}')
