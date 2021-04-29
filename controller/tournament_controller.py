from model.tournament import Tournament
from model.round import Round
from model.player import Player
from view.player_view import get_player_info, print_player
from view.round_view import enter_score, print_match_result, print_final_score
from view.tournament_view import (
    get_tournament_name, get_tournament_time_control)


players = [
    Player("Ranga", 34), Player("Grégory", 12), Player("Jean-Marie", 3),
    Player("Steve", 100), Player("Aura", 18), Player("Mélanie", 27),
    Player("Vanessa", 7), Player("Anonymous", 57)]


class TournamentController:
    def __init__(self):
        name = self.get_and_check_name()
        time_control = self.get_and_check_time_control()
        self.tournament = Tournament(name, time_control)
        """for i in range(4):
            #Créer une controleur de player
            #appeler la méthode qui permet de créer un player
            #retourner le player terminer
            #ensuite tu l'ajouter à la liste "self.tournament.add_player(player)"
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
            self.update_tournament_score(match)
        print_final_score(self.tournament.players, round1.number)

    def get_and_check_name(self):
        name = get_tournament_name()
        while not name.isalpha():
            print("Le format du nom est incorrect")
            name = get_tournament_name()
        return name

    def get_and_check_time_control(self):
        time_control = get_tournament_time_control()
        time_control = time_control.lower()
        while (time_control != "bullet" and time_control != "blitz"
                and time_control != "speed"):
            print("Le format du time control est incorrect")
            time_control = get_tournament_time_control()
            time_control = time_control.lower()

    def run_round(self, round_number):
        round = Round(str(round_number))
        self.tournament.add_round(round)

        self.tournament.players.sort(key=lambda x: x.elo)
        self.tournament.players.sort(key=lambda x: x.score, reverse=True)
        """for player in self.tournament.players:
            print(player.name, player.score, player.elo)"""

    def update_tournament_score(self, match):
        match.player1.score += match.score_player1
        match.player2.score += match.score_player2

    def handle_score(self):
        score = enter_score()
        if(score == "1"):
            return 1, 0
        elif(score == "2"):
            return 0, 1
        else:
            return 0.5, 0.5
