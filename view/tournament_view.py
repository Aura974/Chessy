from utils.utils import view_score


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
    choice = input("Entrez l'id du tournoi souhaité : ")
    return int(choice)


def print_tournaments_list(tournaments):
    print("-------------------------")
    print("-------------------------")
    print("LISTE DES TOURNOIS")
    print("-------------------------")
    for tournament in tournaments:
        print("-------------------------")
        print(f"ID : {tournament.index}")
        print(f"Nom : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Date : {tournament.date}")
        print(f"Type : {tournament.time_control}")
        print(f"Description : {tournament.details}")
        print(f"Statut : {tournament.status}")
        print("-------------------------")


def print_tournament_players_a_to_z():
    print("---------------------------------------")
    print("---------------------------------------")
    print("LISTE DES JOUEURS DU TOURNOI DEMANDÉ")
    print("ORDRE ALPHABÉTIQUE")


def print_tournament_players_elo():
    print("---------------------------------------")
    print("---------------------------------------")
    print("LISTE DES JOUEURS DU TOURNOI DEMANDÉ")
    print("CLASSEMENT")


def print_tournament_players_list(tournament):
    print(f"Nom : {tournament.name}")
    print("---------------------------------------")
    for player in tournament.players:
        print("-------------------------")
        print(f"NOM : {player.surname}")
        print(f"Prénom : {player.name}")
        print(f"Elo : {player.elo}")
        print(f"Score : {player.score}")
        print("-------------------------")


def print_tournament_rounds(tournament):
    print("---------------------------------------")
    print("---------------------------------------")
    print("LISTE DES TOURS DU TOURNOI DEMANDÉ")
    print(f"Nom : {tournament.name}")
    print("---------------------------------------")
    for round in tournament.rounds:
        print("-------------------------")
        print(f"Round n°{round.round_number}")
        print(f"Début : {round.start_time}")
        print(f"Fin : {round.end_time}")
        print(f"Nombre de matchs joués : {len(round.matches)}")
        print("-------------------------")


def print_tournament_matches_title(tournament):
    print("---------------------------------------")
    print("---------------------------------------")
    print("LISTE DES MATCHS DU TOURNOI DEMANDÉ")
    print(f"Nom : {tournament.name}")
    print("---------------------------------------")


def print_tournament_matches(rounds, matches):
    for round, match_list in zip(rounds, matches):
        for match in match_list:
            print("-------------------------")
            print(f"ROUND N° : {round.round_number}")
            print(" -- Joueur 1 --")
            print(f"Nom : {match.player1.surname}")
            print(f"Prénom : {match.player1.name}")
            print(f"Elo : {match.player1.elo}")
            print("-------------------------")
            print(" -- VS --")
            print("-------------------------")
            print(" -- Joueur 2 --")
            print(f"Nom : {match.player2.surname}")
            print(f"Prénom : {match.player2.name}")
            print(f"Elo : {match.player2.elo}")
            print("-------------------------")
            result = view_score(match.score_player1)
            print(f" -- Résultat :  {result} --")
            print("-------------------------")
