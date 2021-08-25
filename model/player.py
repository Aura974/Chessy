class Player:
    def __init__(self, name, surname, elo, birth_date, gender, score):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
        self.elo = elo
        self.score = score
        self.opponent = list()

    def __str__(self):
        return self.name
