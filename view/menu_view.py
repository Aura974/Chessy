from controller.tournament_controller import TournamentController


def print_home_menu():
    print("1: Lancer un nouveau tournoi")
    print("2: Charger un tournoi")
    print("3: Afficher les rapports des joueurs")
    print("4: Afficher les rapports des tournois")
    print("5: Changer le classement Elo")
    print("6: Quitter")


def print_players_reports_menu():
    print("1: Liste des joueurs par ordre alphabétique")
    print("2: Liste des joueurs par classement Elo ascendant")
    print("3: Liste des joueurs par classement Elo descendant")
    # liste joueurs d'un tournoi
    print("4: Retour au menu principal")


def print_tournaments_reports_menu():
    # liste tournois
    # liste tours
    # liste matchs
    pass


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
        if input == 4:
            is_menu_report = False


def tournaments_reports_menu():
    pass


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
