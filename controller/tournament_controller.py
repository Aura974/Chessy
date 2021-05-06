from model.tournament import Tournament
from model.round import Round
from model.player import Player
from view.player_view import get_player_info, print_player, print_match
from view.round_view import enter_score, print_match_result, print_final_score
from view.tournament_view import (
    get_tournament_name, get_tournament_time_control)

players = [Player("Ranga", 34, 1), Player("Grégory", 12, 1),
           Player("Jean-Marie", 3, 0), Player("Steve", 100, 0.5),
           Player("Aura", 18, 0.5), Player("Mélanie", 27, 0),
           Player("Vanessa", 7, 1), Player("Anonymous", 57, 0)]


class TournamentController:
    def __init__(self):
        name = self.get_and_check_name()
        time_control = self.get_and_check_time_control()
        self.tournament = Tournament(name, time_control)
        """for i in range(4):
            # Créer une controleur de player
            # appeler la méthode qui permet de créer un player
            # retourner le player terminer
            # ensuite tu l'ajoute à la liste "
            # self.tournament.add_player(player)"
            name, elo = get_player_info()
            player = Player(name, elo)
            self.tournament.add_player(player)"""
        self.tournament.players = players

    def run_first_round(self):
        # algorithme pour créer les premiers rounds

        match_number = 1
        # self.tournament.players.sort(key=lambda x: x.elo)

        round1 = Round("1")
        self.tournament.add_round(round1)

        player_for_round = self.get_players()
        print_player(player_for_round)

        for i in range(4):
            round1.add_match(
                player_for_round[i],
                player_for_round[i + 4]
                            )

        for match in round1.matches:
            match.player1.opponent.append(match.player2.elo)
            match.player2.opponent.append(match.player1.elo)

        for match in self.tournament.rounds[0].matches:
            print(f"\nTOUR #1 - MATCH #{match_number}")
            print_match(match)
            match.score_player1, match.score_player2 = self.handle_score()
            print(f"\nRÉSULTAT DU MATCH #{match_number}")
            match_number += 1
            print_match_result(match)
            self.update_tournament_score(match)
        print_final_score(self.tournament.players, round1.number)

    def run_round(self, round_number):
        match_number = 1

        round = Round(str(round_number))
        self.tournament.add_round(round)

        player_for_round = self.get_players()
        print_player(player_for_round)

        index_player = 0

        while len(player_for_round) != 0:
            player1 = player_for_round[index_player]
            player1_index = index_player
            player2 = player_for_round[index_player + 1]
            player2_index = index_player + 1

            while player2.elo in player1.opponent:
                index_player += 1
                player2 = player_for_round[index_player + 1]
                player2_index = index_player + 1
            round.add_match(player1, player2)
            del player_for_round[player1_index]
            del player_for_round[player2_index - 1]
            index_player = 0

        for match in round.matches:
            match.player1.opponent.append(match.player2.elo)
            match.player2.opponent.append(match.player1.elo)

        for i in range(1, 2):
            for match in self.tournament.rounds[round_number-1].matches:
                print(f"\nTOUR #{round_number} - MATCH #{match_number}")
                print_match(match)
                match.score_player1, match.score_player2 = self.handle_score()
                print(f"\nRÉSULTAT DU MATCH #{match_number}")
                match_number += 1
                print_match_result(match)
                self.update_tournament_score(match)
        print_final_score(self.tournament.players, round.number)

    def get_players(self):
        player_for_round = list()
        for player in self.tournament.players:
            player_for_round.append(player)
        player_for_round.sort(key=lambda x: x.elo)
        player_for_round.sort(key=lambda x: x.score, reverse=True)
        return player_for_round

    def handle_score(self):
        score = enter_score()
        if(score == "1"):
            return 1, 0
        elif(score == "2"):
            return 0, 1
        else:
            return 0.5, 0.5

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
                and time_control != "rapide"):
            print("Le format du contrôle du temps est incorrect")
            time_control = get_tournament_time_control()
            time_control = time_control.lower()

    def update_tournament_score(self, match):
        match.player1.score += match.score_player1
        match.player2.score += match.score_player2
