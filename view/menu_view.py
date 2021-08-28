from controller.menu_controller import (get_players_a_to_z,
                                        get_players_elo_ascending,
                                        get_players_elo_descending,
                                        get_players_list,
                                        get_tournament_matches_list,
                                        get_tournament_players_a_to_z,
                                        get_tournament_players_elo,
                                        get_tournament_players_list,
                                        get_tournament_rounds_list,
                                        get_tournaments_list)
from controller.tournament_controller import TournamentController


def print_home_menu():
    print("1: Lancer un nouveau tournoi")
    print("2: Reprendre un tournoi")
    print("3: Afficher les rapports des joueurs")
    print("4: Afficher les rapports des tournois")
    print("5: Changer le classement Elo d'un joueur")
    print("6: Quitter")


def print_players_reports_menu():
    print("1: Liste des joueurs par ordre alphabétique")
    print("2: Liste des joueurs par classement Elo ascendant")
    print("3: Liste des joueurs par classement Elo descendant")
    print("4: Retour au menu principal")


def print_tournaments_reports_menu():
    print("1: Liste des tournois")
    print("2: Liste des joueurs d'un tournoi -- Orde alphabétique")
    print("3: Liste des joueurs d'un tournoi -- Classement")
    print("4: Liste des tours d'un tournoi")
    print("5: Liste des matchs d'un tournoi")
    print("6: Retour au menu principal")


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
            pass
        elif input == 6:
            break
