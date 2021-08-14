from model.player import Player
from model.round import Round
from model.tournament import Tournament
from view.player_view import get_player_info, print_match, print_player
from view.round_view import enter_score, print_final_score, print_match_result
from view.tournament_view import (get_tournament_name,
                                  get_tournament_time_control)
from tinydb import TinyDB, Query, where

players = [Player("Ranga", 34, 1), Player("Grégory", 12, 1),
           Player("Jean-Marie", 3, 0), Player("Steve", 100, 0.5),
           Player("Aura", 18, 0.5), Player("Mélanie", 27, 0),
           Player("Vanessa", 7, 1), Player("Anonymous", 57, 0)]


class TournamentController:
    def __init__(self):
        self.tournament = None
        self.db = TinyDB("tournament_serializer.json", indent=4)
        self.tournament_serializer = self.db.table("tournament_serializer")

    def new_tournament(self):
        name = self.get_and_check_name()
        time_control = self.get_and_check_time_control()
        self.tournament = Tournament(name, time_control)
        self.tournament.players = players

    def reload_tournament(self):
        db = TinyDB("tournament_serializer.json", indent=4)
        tournaments = Query()
        tournament = db.table('tournament_serializer')
        db_tournament = tournament.search(tournaments.name == "Abba")
        reloaded_tournament = db_tournament[0]
        self.tournament = None
        self.deserializer(reloaded_tournament)
        number_round_to_run = 4 - len(reloaded_tournament["rounds"])
        print(number_round_to_run)

        if number_round_to_run == 4:
            pass
            # run_first_round()
        else:
            for i in range(len(
                    reloaded_tournament["rounds"])
                    + 1, 5):
                pass
                # run_round(i)

    def deserializer(self, reloaded_tournament):
        self.tournament = Tournament(
            reloaded_tournament["name"],
            reloaded_tournament["time_control"])
        self.tournament.players = []

        for player in reloaded_tournament["players"]:
            reload_player = Player(player["name"],
                                   player["elo"],
                                   player["score"])
            self.tournament.add_player(reload_player)

        for round in reloaded_tournament["rounds"]:
            reload_round = Round(round["number"])
            for match in round["matches"]:
                player1 = Player(match["player1"]["name"],
                                 match["player1"]["elo"],
                                 match["player1"]["score"])
                player2 = Player(match["player2"]["name"],
                                 match["player1"]["elo"],
                                 match["player1"]["score"])

                reload_match = Match(player1, player2, match["score_player1"], match["score_player2"])

                reload_round.add_reload_match(reload_match)
            self.tournament.add_round(reload_round)

    def run_first_round(self):
        # algorithme pour créer les premiers rounds

        match_number = 1

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
        self.tournament_serializer.insert(self.tournament.serializer())

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
        self.tournament_serializer.update(self.tournament.serializer())

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
        while (time_control != "b" and time_control != "bz"
                and time_control != "r"):
            print("\033[38;5;1;88m"
                  "Le format du contrôle du temps est incorrect\033[0m")
            time_control = get_tournament_time_control()
            time_control = time_control.lower()
        else:
            if time_control == "b":
                time_control = "Bullet"
            elif time_control == "bz":
                time_control = "Blitz"
            elif time_control == "r":
                time_control = "Rapide"
        return time_control

    def update_tournament_score(self, match):
        match.player1.score += match.score_player1
        match.player2.score += match.score_player2
