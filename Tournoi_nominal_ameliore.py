#-------------------MODEL---------------------       
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
#-----------------------------------------------------  
class Player:
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
        
    def __str__(self):
        return self.name

#-----------------------------------------------------
class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0
        
#Victoire 1 points 0 pour l'autre
#Match nul 0.5 pour les deux

#-----------------------------------------------------
class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []
        
    def add_match(self, player1, player2): #1
        match = Match(player1, player2)
        self.matchs.append(match)
        
    def add_match2(self, match): #2
        self.matchs.append(match)
        
#-------------------VIEW----------------------       
def get_tournament_info():
    name = input("Enter the tournament name : ")
    time_control = input("Enter time control (Bullet/Splitz/Quick) : ")
    return name, time_control
    
def get_player_info():
    name = input("Enter the player name : ")
    elo = input("Enter the player elo : ")
    return name, elo
    
def print_player(players):
    for player in players:
        print(f"name : {player.name}")
        print(f"elo : {player.elo}")
        print("--------------------")
        
def enter_score():
    score = input("Enter score (1 / 2 / 0) : ")
    return score
    
def print_match_result(match):
    print(f"{match.player1.name} : {match.score_player1}", f"\n{match.player2.name} : {match.score_player2}")
    
#-------------------CONTROLER----------------------       
#from model.tournament import Tournament

players = [Player("Ranga", 34), Player("Grégory", 12), Player("Jean-Marie", 3), Player("toto", 100)]

class TournamentControler:
    def __init__(self):
        name, time_control = get_tournament_info()
        self.tournament = Tournament(name, time_control)
        
        """for i in range(2):
            name, elo = get_player_info()
            player = Player(name, elo)
            self.tournament.add_player(player)"""
        self.tournament.players = players
            
    def print_player(self):
        print_player(self.tournament.players)
        
    def run_first_round(self):
        #algorithme pour créer les premier round
        self.tournament.players.sort(key = lambda x : x.elo)
        round1 = Round("1")
        self.tournament.add_round(round1)
        for i in range(2):
            round1.add_match(self.tournament.players[i], self.tournament.players[2 + i])
            
        for match in self.tournament.rounds[0].matchs:
            """print(match.player1)
            print(match.player2)"""
            match.score_player1, match.score_player2 = self.handle_score()
            print_match_result(match)
            
            
    def handle_score(self):
        score = enter_score()
        if(score == "1"):
            return 1,0
        elif(score == "2"):
            return 0,1
        else:
            return 0.5,0.5
            
            
            
  
 
 #-----------------Main---------------
 #from controler.tournament_controler import TournamentControler
tournamentControler = TournamentControler()
tournamentControler.print_player()
tournamentControler.run_first_round()