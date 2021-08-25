def get_tournament_name():
    name = input("Entrez le nom du tournoi : ")
    return name


def get_tournament_place():
    place = input("Entrez le lieu du tournoi : ")
    return place


def get_tournament_time_control():
    time_control = input("Entrez le contrôle du temps : "
                         "\n(\033[1mb\033[0m = Bullet / "
                         "\033[1mbz\033[0m = Blitz / "
                         "\033[1mr\033[0m = Rapide) : ")
    return time_control


def get_tournament_details():
    details = input("Entrez la description du tournoi (facultatif) : ")
    return details


def get_existing_tournament():
    name = input("Entrez le nom du tournoi : ")
    place = input("Entrez le lieu du tournoi : ")
    date = input("Entrez la date du tournoi : ")
    time_control = input("Entrez le contrôle du temps : "
                         "\n(\033[1mb\033[0m = Bullet / "
                         "\033[1mbz\033[0m = Blitz / "
                         "\033[1mr\033[0m = Rapide) : ")
    return name, place, date, time_control
