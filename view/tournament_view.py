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


def print_existing_tournaments(db_tour):
    print("-------------------------")
    print(f"Tournoi n° : {db_tour.doc_id}")
    print(f"Nom : {db_tour['name']}\n"
          f"Lieu : {db_tour['place']}\n"
          f"Date : {db_tour['date']}\n"
          f"Type : {db_tour['time_control']}\n"
          f"Description : {db_tour['details']}")


def print_number_round_to_run(number):
    print(f"Nombre de tours restant : {number}")
    print("-------------------------")


def tournament_choice():
    choice = input("Entrez le n° du tournoi souhaité : ")
    return int(choice)
