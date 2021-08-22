import os


def get_player_info():
    name = input("Entrez le prénom du joueur : ")
    # surname = input("Entrez le nom de famille du joueur : ")
    # birth_date = input("Entrez la date de naissance du joueur : ")
    # gender = input("Entrez le sexe du joueur (F/M) : ")
    elo = int(input("Entrez le classement Elo du joueur : "))
    return name, elo


def get_existing_player():
    name = input("Entrez le prénom du joueur : ")
    # surname = input("Entrez le nom de famille du joueur : ")
    elo = int(input("Entrez le classement Elo du joueur : "))
    return name, elo


def players_choice():
    choice = input("Nouveau joueur : \033[1m1\033[0m / "
                   "Joueur existant : \033[1m2\033[0m : ")
    return choice


def print_player(players):
    print("-------------------------")
    print("CLASSEMENT DES JOUEURS")
    print("-------------------------")
    for player in players:
        print(f"Prénom : {player.name}")
        print(f"Score : {player.score}")
        print(f"Elo : {player.elo}")
        print("--------------------")
    input("Appuyez sur ENTRÉE pour continuer...")
    os.system("cls")


def print_match(matches):
    print("--------------------")
    print(f"1.{matches.player1.name}\n\n2.{matches.player2.name}\n")
