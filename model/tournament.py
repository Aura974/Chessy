class Tournament:
    def __init__(self, name, place, date, time_control, details):
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.details = details
        self.status = None
        self.players = list()
        self.rounds = list()

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)
