class Player:
    def __init__(self, name, surname, elo, score, birth_date, gender):
        self.name = name
        self.surname = surname
        self.elo = elo
        self.score = score
        self.birth_date = birth_date
        self.gender = gender
        self.opponent = list()

    def __str__(self):
        return self.name
