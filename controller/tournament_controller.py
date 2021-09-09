from utils.utils import (is_query_empty, is_tournament_name_valid,
                         is_place_valid, is_time_control_valid,
                         is_continue_or_quit,
                         is_update_player_elo_valid,
                         time_control_def, error_message,
                         set_date, set_round_time,
                         print_text)
from model.round import Round
from model.tournament import Tournament
from view.player_view import print_match, print_player
from view.round_view import enter_score, print_final_score, print_match_result
from view.tournament_view import (get_tournament_name,
                                  get_tournament_time_control,
                                  get_tournament_place,
<<<<<<< HEAD
                                  get_tournament_details, print_update_player_elo,
=======
                                  get_tournament_details,
>>>>>>> 5a271ff50d91018f53d7351118691416620579e4
                                  tournament_choice, print_existing_tournaments,
                                  print_current_tournaments,
                                  print_number_round_to_run,
                                  get_continue_or_quit)
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
        date = set_date()
        time_control = self.get_and_check_time_control()
        details = get_tournament_details()
        self.tournament = Tournament(name, place, date, time_control, details)
        self.tournament.status = "En cours"
        self.tournament.players = list()
        self.tournament_data.insert(tournament_serializer(self.tournament))
        tournament_get = self.tournament_data.get(
            (tournaments.name == self.tournament.name) &
            (tournaments.place == self.tournament.place))
        tournament_id = tournament_get.doc_id
        for i in range(1, 9):
            playerController = PlayerController()
            print_text(f"Joueur {i} : ")
            player = playerController.handle_players_choice()
            self.tournament.add_player(player)
            self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[tournament_id])
        self.run_first_round()
        self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[tournament_id])
        quit = self.get_and_check_continue_or_quit()
        if quit == "q":
            return
        else:
            pass
        for round_number in range(2, 5):
            self.run_round(round_number)
<<<<<<< HEAD
            self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[tournament_id])
=======
>>>>>>> 5a271ff50d91018f53d7351118691416620579e4
            quit = self.get_and_check_continue_or_quit()
            if quit == "q":
                return
            else:
                pass
        self.tournament.status = "Terminé"
        self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[tournament_id])

        update_elo = self.check_update_player_elo()

        while True:
            if update_elo == "o":
                PlayerController.update_player_elo()
                update_elo = self.check_update_player_elo()
            else:
                return

    def reload_tournament(self):
        self.db = TinyDB("tournament_data.json", indent=4)
        tournaments = Query()
        self.tournament_data = self.db.table("tournament_data")

        db_tournament = self.tournament_data.search(tournaments.status == "En cours")

<<<<<<< HEAD
        while is_query_empty(db_tournament):
            error_message("Aucun tournoi en cours")
            return

=======
>>>>>>> 5a271ff50d91018f53d7351118691416620579e4
        print_current_tournaments()

        for db_tour in db_tournament:
            number_round_to_run = 4 - len(db_tour["rounds"])
            print_existing_tournaments(db_tour)
            print_number_round_to_run(number_round_to_run)

        choice = tournament_choice()

        reloaded_tournament = self.tournament_data.get(doc_id=choice)

        self.tournament = None
        self.tournament = tournament_deserializer(reloaded_tournament)
        self.tournament.date = set_date()

        nb_of_players = len(self.tournament.players)

        if nb_of_players < 8:
            for i in range(1, (9 - nb_of_players)):
                playerController = PlayerController()
                print_text(f"Joueur {i + nb_of_players} : ")
                player = playerController.handle_players_choice()
                self.tournament.add_player(player)
                self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[choice])

        number_round_to_run = 4 - len(self.tournament.rounds)

        if number_round_to_run == 4:
            self.run_first_round()
            self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[choice])
            quit = self.get_and_check_continue_or_quit()
            if quit == "q":
                return
            else:
                pass
            for i in range(2, 5):
                self.run_round(i)
                self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[choice])
                quit = self.get_and_check_continue_or_quit()
                if quit == "q":
                    return
                else:
                    pass
        else:
            for i in range(len(self.tournament.rounds) + 1, 5):
                self.run_round(i)
                self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[choice])
                quit = self.get_and_check_continue_or_quit()
                if quit == "q":
                    return
                else:
                    pass
        self.tournament.status = "Terminé"
        self.tournament_data.update(tournament_serializer(self.tournament), doc_ids=[choice])

        update_elo = self.check_update_player_elo()

        while True:
            if update_elo == "o":
                PlayerController.update_player_elo()
                update_elo = self.check_update_player_elo()
            else:
                return

    def run_first_round(self):
        # algorithme pour créer les premiers rounds

        match_number = 1

        start_time = set_round_time()
        end_time = None
        round1 = Round("1", start_time, end_time)
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
            print_text(f"\nROUND #1 - MATCH #{match_number}")
            print_match(match)
            match.score_player1, match.score_player2 = self.handle_score()
            print_text(f"\nRÉSULTAT DU MATCH #{match_number}")
            match_number += 1
            print_match_result(match)
            self.update_tournament_score(match)
        self.tournament.players.sort(key=lambda x: x.elo, reverse=True)
        self.tournament.players.sort(key=lambda x: x.score, reverse=True)
        print_final_score(self.tournament.players, round1.round_number)
        round1.end_time = set_round_time()

    def run_round(self, round_number):
        match_number = 1

        start_time = set_round_time()
        end_time = None
        round = Round(str(round_number), start_time, end_time)
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
                print_text(f"\nROUND #{round_number} - MATCH #{match_number}")
                print_match(match)
                match.score_player1, match.score_player2 = self.handle_score()
                print_text(f"\nRÉSULTAT DU MATCH #{match_number}")
                match_number += 1
                print_match_result(match)
                self.update_tournament_score(match)
        self.tournament.players.sort(key=lambda x: x.elo, reverse=True)
        self.tournament.players.sort(key=lambda x: x.score, reverse=True)
        print_final_score(self.tournament.players, round.round_number)
        round.end_time = set_round_time()

    def get_players(self):
        player_for_round = list()
        for player in self.tournament.players:
            player_for_round.append(player)
        player_for_round.sort(key=lambda x: x.elo, reverse=True)
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
        name = name.strip().capitalize()
        while not is_tournament_name_valid(name):
            error_message("Le format du nom est incorrect")
            name = get_tournament_name()
            name = name.strip().capitalize()
        return name

    def get_and_check_place(self):
        place = get_tournament_place()
        place = place.strip().capitalize()
        while not is_place_valid(place):
            error_message("Le format du lieu est incorrect")
            place = get_tournament_place()
            place = place.strip().capitalize()
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

    def get_and_check_continue_or_quit(self):
        quit = get_continue_or_quit()
        quit = quit.lower()

        while not is_continue_or_quit(quit):
            error_message("Aucune commande correspondante")
            quit = get_continue_or_quit()
            quit = quit.lower()
        return quit

    def update_tournament_score(self, match):
        match.player1.score += match.score_player1
        match.player2.score += match.score_player2

    def check_update_player_elo(self):
        update_elo = print_update_player_elo()
        update_elo = update_elo.lower()

        while not is_update_player_elo_valid(update_elo):
            error_message("Entrez uniquement ""O"" ou ""N""")
            update_elo = print_update_player_elo()
            update_elo = update_elo.lower()
        return update_elo
