class Player:
    def __init__(self, name, elo, score):
        self.name = name
        # self.surname = surname
        # self.birth_date = None
        # self.gender = None
        self.elo = elo
        self.score = score
        self.opponent = list()

    def __str__(self):
        return self.name

    def serializer(self):
        self.data = {"name": self.name, "elo": self.elo, "score": self.score}
        return self.data

    def serializer_player(self):
        self.data = {"name": self.name, "elo": self.elo}
        return self.data
