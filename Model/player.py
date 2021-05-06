class Player:
    def __init__(self, name, elo, score):
        self.name = name
        # self.surname = surname
        # self.gender = None
        # self.birth_date = None
        self.elo = elo
        self.score = score
        self.opponent = list()

    def __str__(self):
        return self.name
