from model.match import Match


class Round:
    def __init__(self, number):
        self.number = number
        self.matches = []

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def serializer(self):
        data = {"number": self.number,
                "matches": [match.serializer() for match in self.matches]}
        return data
