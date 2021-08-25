from utils.checks import (is_tournament_name_valid,
                          is_place_valid, is_time_control_valid,
                          time_control_def, error_message)
from model.round import Round
from model.tournament import Tournament
from view.player_view import print_match, print_player
from view.round_view import enter_score, print_final_score, print_match_result
from view.tournament_view import (get_tournament_name,
                                  get_tournament_time_control,
                                  get_tournament_place,
                                  get_tournament_details,
                                  get_existing_tournament)
from controller.serializer_controller import tournament_serializer, tournament_deserializer
from controller.player_controller import PlayerController
from tinydb import TinyDB, Query


class TournamentController:
    def __init__(self):
        self.tournament = None
        self.db = TinyDB("tournament_data.json", indent=4)
        self.tournament_data = self.db.table("tournament_data")

    def new_tournament(self):
        tournaments = Query()
        name = self.get_and_check_name()
        place = self.get_and_check_place()
        time_control = self.get_and_check_time_control()
        details = get_tournament_details()
        self.tournament = Tournament(name, place, time_control, details)
        self.tournament.players = list()
        self.tournament_data.insert(tournament_serializer(self.tournament))
        tournament_get = self.tournament_data.get(
            (tournaments.name == self.tournament.name) &
            (tournaments.place == self.tournament.place))
        tournament_id = tournament_get.doc_id
        for i in range(1, 9):
            playerController = PlayerController()
            print(f"Joueur {i} : ")
            player = playerController.handle_choice()
            self.tournament.add_player(player)
            self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[tournament_id])
        self.run_first_round()
        for round_number in range(2, 5):
            self.run_round(round_number)

    def reload_tournament(self):
        self.db = TinyDB("tournament_data.json", indent=4)
        tournaments = Query()
        self.tournament_data = self.db.table('tournament_data')

        existing_tournament = get_existing_tournament()
        while True:
            try:
                db_tournament = self.tournament_data.search(
                    (tournaments.name == existing_tournament[0]) &
                    (tournaments.place == existing_tournament[1]) &
                    (tournaments.date == existing_tournament[2]) &
                    (tournaments.time_control == existing_tournament[3]))
                reloaded_tournament = db_tournament[0]
                break
            except IndexError:
                error_message("Tournoi non trouvé")
                existing_tournament = get_existing_tournament()

        self.tournament = None
        self.tournament = tournament_deserializer(reloaded_tournament)

        number_round_to_run = 4 - len(reloaded_tournament["rounds"])
        print(f"Nombre de tours restant : {number_round_to_run}")

        tournament_get = self.tournament_data.get(tournaments.name == self.tournament.name)
        tournament_id = tournament_get.doc_id

        nb_of_players = len(reloaded_tournament["players"])

        if nb_of_players < 8:
            for i in range(1, (9 - nb_of_players)):
                playerController = PlayerController()
                print(f"Joueur {i + nb_of_players} : ")
                player = playerController.handle_choice()
                self.tournament.add_player(player)
                self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[tournament_id])

        if number_round_to_run == 4:
            self.run_first_round()
        else:
            for i in range(len(reloaded_tournament["rounds"]) + 1, 5):
                self.run_round(i)

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
                player_for_round[i + 4])

        for match in round1.matches:
            match.player1.opponent.append(match.player2.elo)
            match.player2.opponent.append(match.player1.elo)

        for match in self.tournament.rounds[0].matches:
            print(f"\nROUND #1 - MATCH #{match_number}")
            print_match(match)
            match.score_player1, match.score_player2 = self.handle_score()
            print(f"\nRÉSULTAT DU MATCH #{match_number}")
            match_number += 1
            print_match_result(match)
            self.update_tournament_score(match)
        print_final_score(self.tournament.players, round1.round_number)
        self.tournament_data.update(tournament_serializer(self.tournament))

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
                print(f"\nROUND #{round_number} - MATCH #{match_number}")
                print_match(match)
                match.score_player1, match.score_player2 = self.handle_score()
                print(f"\nRÉSULTAT DU MATCH #{match_number}")
                match_number += 1
                print_match_result(match)
                self.update_tournament_score(match)
        print_final_score(self.tournament.players, round.round_number)
        self.tournament_data.update(tournament_serializer(self.tournament))

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
        name = name.split().capitalize()
        while not is_tournament_name_valid(name):
            error_message("Le format du nom est incorrect")
            name = get_tournament_name()
        return name

    def get_and_check_place():
        place = get_tournament_place()
        while not is_place_valid(place):
            error_message("Le format du lieu est incorrect")
            place = get_tournament_place()
        return place

    def get_and_check_time_control(self):
        time_control = get_tournament_time_control()
        time_control = time_control.lower()
        while is_time_control_valid(time_control):
            error_message("\033[38;5;1;88m Le format du contrôle du temps est incorrect\033[0m")
            time_control = get_tournament_time_control()
            time_control = time_control.lower()
        else:
            time_control = time_control_def(time_control)
        return time_control

    def update_tournament_score(self, match):
        match.player1.score += match.score_player1
        match.player2.score += match.score_player2
