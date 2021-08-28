class Player:
    def __init__(self, name, surname, elo, score):
        self.name = name
        self.surname = surname
        self.elo = elo
        self.score = score
        self.birthday = None
        self.gender = None
        self.opponent = list()

    def __str__(self):
        return self.name
