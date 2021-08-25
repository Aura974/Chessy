import os


def get_player_name():
    name = input("Entrez le prénom du joueur : ")
    return name


def get_player_surname():
    surname = input("Entrez le nom de famille du joueur : ")
    return surname


def get_player_birthday():
    birth_date = input("Entrez la date de naissance du joueur\n"
                       "(format jj/mm/aaaa) : ")
    return birth_date


def get_player_gender():
    gender = input("Entrez le sexe du joueur (f/m) : ")
    return gender


def get_player_elo():
    elo = input("Entrez le classement Elo du joueur : ")
    return elo


def get_existing_player():
    name = input("Entrez le prénom du joueur : ")
    surname = input("Entrez le nom de famille du joueur : ")
    elo = input("Entrez le classement Elo du joueur : ")
    return name, surname, int(elo)


def players_choice():
    choice = input("Nouveau joueur : \033[1m1\033[0m\n"
                   "Joueur existant : \033[1m2\033[0m : ")
    return choice


def print_player(players):
    print("-------------------------")
    print("CLASSEMENT DES JOUEURS")
    print("-------------------------")
    for player in players:
        print(f"Prénom : {player.name}")
        print(f"NOM : {player.surname}")
        print(f"Score : {player.score}")
        print(f"Elo : {player.elo}")
        print("--------------------")
    input("Appuyez sur ENTRÉE pour continuer...")
    os.system("cls")


def print_match(matches):
    print("--------------------")
    print(f"1.{matches.player1.name} {matches.player1.surname}\n\n"
          f"VS\n\n"
          f"2.{matches.player2.name} {matches.player2.surname}\n")
