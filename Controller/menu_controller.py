import os
from tinydb import TinyDB, Query
from controller.tournament_controller import TournamentController
from controller.player_controller import player_list_deserializer
from controller.serializer_controller import tournament_deserializer
from view.player_view import (existing_player_choice, get_existing_player,
                              get_new_elo, print_existing_players,
                              print_players_a_to_z,                           print_players_elo_ascending,
                              print_players_elo_descending,
                              print_players_list, print_players_title)
from view.tournament_view import (print_tournament_matches,
                                  print_tournament_matches_title,
                                  print_tournament_players_a_to_z,
                                  print_tournament_players_elo,
                                  print_tournament_players_list,
                                  print_tournament_rounds,
                                  print_tournaments_list,
                                  tournament_choice)
from view.menu_view import (print_home_menu,
                            print_players_reports_menu, print_tournaments_reports_menu)
from utils.utils import (get_age,
                         get_tournament_matches,
                         is_elo_valid,
                         error_message, is_query_empty, print_text)


def get_user_input(range):
    input_user = input("Entrer votre choix  : ")
    while not int(input_user) > 0 or not int(input_user) <= range:
        input_user = input("Entrer votre choix  : ")
    return int(input_user)


def players_reports_menu():
    is_menu_report = True
    while is_menu_report:
        print_players_reports_menu()
        input = get_user_input(4)
        if input == 1:
            players = get_players_list()
            get_players_a_to_z(players)
        elif input == 2:
            players = get_players_list()
            get_players_elo_ascending(players)
        elif input == 3:
            players = get_players_list()
            get_players_elo_descending(players)
        elif input == 4:
            is_menu_report = False


def tournaments_reports_menu():
    is_menu_report = True
    while is_menu_report:
        print_tournaments_reports_menu()
        input = get_user_input(6)
        if input == 1:
            get_tournaments_list()
        elif input == 2:
            tournament = get_tournament_players_list()
            get_tournament_players_a_to_z(tournament)
        elif input == 3:
            tournament = get_tournament_players_list()
            get_tournament_players_elo(tournament)
        elif input == 4:
            get_tournament_rounds_list()
        elif input == 5:
            get_tournament_matches_list()
        elif input == 6:
            is_menu_report = False


def home_menu():
    tournamentController = TournamentController()
    is_app_run = True
    while is_app_run:
        print_home_menu()
        input = get_user_input(6)
        if input == 1:
            tournamentController.new_tournament()
        elif input == 2:
            tournamentController.reload_tournament()
        elif input == 3:
            players_reports_menu()
        elif input == 4:
            tournaments_reports_menu()
        elif input == 5:
            update_player_elo()
        elif input == 6:
            break


def get_players_list():
    db = TinyDB("players_data.json", indent=4)
    player_data = db.table('players_data')
    db_players = player_data.all()
    players = list()

    for player in db_players:
        player = player_list_deserializer(player)
        player.age = get_age(player.birthday)
        players.append(player)

    return players


def update_player_elo():
    db = TinyDB("players_data.json", indent=4)
    players = Query()
    player_data = db.table('players_data')

    existing_player = get_existing_player()

    db_players = player_data.search(players.name == existing_player)

    while is_query_empty(db_players):
        error_message("Aucun joueur trouvé")
        existing_player = get_existing_player()
        db_players = player_data.search(players.name == existing_player)

    print_players_title()
    for db_play in db_players:
        print_existing_players(db_play)

    choice = existing_player_choice()

    new_elo = get_new_elo()

    while not is_elo_valid(new_elo):
        error_message("Veuillez entrer un nombre")
        new_elo = get_new_elo()
    else:
        new_elo = int(new_elo)
        os.system("cls")
        print_text("Changement validé !")
        player_data.update({"elo": new_elo}, doc_ids=[choice])
        uploaded_player = player_data.get(doc_id=choice)
        print_existing_players(uploaded_player)

    return new_elo


def get_players_a_to_z(players):

    players.sort(key=lambda x: x.surname)

    print_players_a_to_z()
    print_players_list(players)

    return players


def get_players_elo_ascending(players):

    players.sort(key=lambda x: x.elo)

    print_players_elo_ascending()
    print_players_list(players)

    return players


def get_players_elo_descending(players):

    players.sort(key=lambda x: x.elo, reverse=True)

    print_players_elo_descending()
    print_players_list(players)

    return players


def get_tournaments_list():
    db = TinyDB("tournament_data.json", indent=4)
    tournament_data = db.table('tournament_data')
    db_tournament = tournament_data.all()
    tournaments = list()

    for tournament in db_tournament:
        tournament = tournament_deserializer(tournament)
        tournaments.append(tournament)

    tournaments.sort(key=lambda x: x.date, reverse=True)
    tournaments.sort(key=lambda x: x.status)

    for my_index, tournament in enumerate(tournaments, start=1):
        tournament.index = my_index

    print_tournaments_list(tournaments)

    return tournaments


def get_tournament_players_list():
    tournaments = get_tournaments_list()

    choice = tournament_choice()

    chosen_tournament = tournaments[(choice-1)]

    return chosen_tournament


def get_tournament_players_a_to_z(tournament):

    tournament.players.sort(key=lambda x: x.surname)

    print_tournament_players_a_to_z()
    print_tournament_players_list(tournament)

    return tournament


def get_tournament_players_elo(tournament):

    tournament.players.sort(key=lambda x: x.elo, reverse=True)

    print_tournament_players_elo()
    print_tournament_players_list(tournament)

    return tournament


def get_tournament_rounds_list():
    tournaments = get_tournaments_list()

    choice = tournament_choice()

    chosen_tournament = tournaments[(choice-1)]

    print_tournament_rounds(chosen_tournament)

    return chosen_tournament


def get_tournament_matches_list():
    tournaments = get_tournaments_list()

    choice = tournament_choice()

    chosen_tournament = tournaments[(choice-1)]

    tournament_rounds, round_matches = get_tournament_matches(chosen_tournament)

    print_tournament_matches_title(chosen_tournament)
    print_tournament_matches(tournament_rounds, round_matches)

    return tournament_rounds, round_matches
