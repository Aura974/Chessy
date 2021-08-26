from model.match import Match


class Round:
    def __init__(self, round_number, start_time, end_time):
        self.round_number = round_number
        self.start_time = start_time
        self.end_time = end_time
        self.matches = []

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def add_reload_match(self, match):
        self.matches.append(match)
