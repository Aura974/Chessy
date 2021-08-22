class Tournament:
    def __init__(self, name, time_control):
        self.name = name
        # self.place = place
        self.time_control = time_control
        self.players = list()
        self.rounds = list()

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)
