import Player
from const import MESSAGES
from Deck import Deck


class Game:
    def __init__(self):
        self.players = []
        self.player = None
        # self.dealler = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_rate, self.min_rate = 20, 0

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        bots_count = int(input(MESSAGES.get("ask_bot_value")))
        self.all_players_cont = bots_count + 1
        for i in range(bots_count):
            # TO DO : should be random pos
            b = Player.Bot(position=i)
            self.players.append(b)
            print(b, ' is created')
            # TO DO : should be random pos
        self.player = Player.Player(position=bots_count + 1)
        self.players.append(self.player)

    def ask_rate(self):
        for player in self.players:
            player.change_rate(self.max_rate, self.min_rate)

    def first_distribution_cards(self):
        for player in self.players:
            player.ask_card(self.deck, 2)

    def start_game(self):
        message = MESSAGES.get("ask_start")
        if not self._ask_starting(message=message):
            exit(1)
        self._launching()

        self.ask_rate()

        self.first_distribution_cards()
        for p in self.players:
            for c in p.cards:
                print(c)
        pass
