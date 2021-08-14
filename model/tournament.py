from model.player import Player


class Tournament:
    def __init__(self, name, time_control):
        self.name = name
        self.time_control = time_control
        self.players = []
        self.rounds = []

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def serializer(self):
        data = {"name": self.name,
                "time_control": self.time_control,
                "players": [player.serializer() for player in self.players],
                "rounds": [round.serializer() for round in self.rounds]}
        return data
