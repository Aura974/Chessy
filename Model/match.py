from player import Player

class Match:
    def __init__(self, match_name, match_result):
        self.match_name = match_name()
        self.match_result = (self.player_one_result,self.player_two_result)    

    def match_name(self):
        pass   
    
    def player_one_score(self, player_one, player_one_score):
        self.player_one = Player.Player(name, surname)
        self.player_one_score = input(f"Entrez le score de {self.player_one.name} : ")
        
    def player_two_score(self, player_two, player_two_score):
        self.player_two = Player(name, surname)
        self.player_two_score = input(f"Entrez le score de {self.player_two.name} : ")

    def player_one_result(self, player_one_result):
        self.player_one_result = [self.player_one.name, self.player_one_score]

    def player_two_result(self, player_two_result):
        self.player_two_result = [self.player_two.name, self.player_two_score]

        


        

