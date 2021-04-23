from model.tournament import Tournament
from model.round import Round
from model.player import Player
from view.view import *

players = [Player("Ranga", 34), Player("Grégory", 12), Player("Jean-Marie", 3), Player("Steve", 100), Player("Aura", 18), Player("Mélanie", 27), Player("Vanessa", 7), Player("Anonymous", 57)]


class TournamentController:
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

    def run_first_round(self, scoreboard1=None):
        # algorithme pour créer les premiers rounds

        self.scoreboard1 = dict()
        self.tournament.players.sort(key=lambda x: x.elo)
        round1 = Round("1")
        self.tournament.add_round(round1)
        self.print_player()
        for i in range(4):
            round1.add_match(
                self.tournament.players[i],
                self.tournament.players[i + 4]
                            )

        for match in self.tournament.rounds[0].matches:
            print(match.player1)
            print(match.player2)
            match.score_player1, match.score_player2 = self.handle_score()
            print_match_result(match)
            self.scoreboard1[match.player1.name] = match.score_player1
            self.scoreboard1[match.player2.name] = match.score_player2

    def run_other_rounds(self, scoreboard2=None):
        self.scoreboard2 = dict(
            sorted(self.scoreboard1.items(), key=lambda item: item[1])
                                )
         
        print(self.scoreboard2)



        # round2 = Round("2")
        # self.tournament.add_round(round2)
        # for i in range(4):
        #     round1.add_match(self.tournament.players[i], self.tournament.players[i + 4])
            
        # for match in self.tournament.rounds[0].matches:
        #     print(match.player1)
        #     print(match.player2)
        #     match.score_player1, match.score_player2 = self.handle_score()
        #     print_match_result(match)

            
            
    def handle_score(self):
        score = enter_score()
        if(score == "1"):
            return 1,0
        elif(score == "2"):
            return 0,1
        else:
            return 0.5,0.5