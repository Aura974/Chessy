from model.match import Match


class Round:
    def __init__(self, number):
        self.number = number
        self.matches = []

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)
