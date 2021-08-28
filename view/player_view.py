import os


def get_player_name():
    name = input("Entrez le prénom du joueur : ")
    return name


def get_player_surname():
    surname = input("Entrez le nom de famille du joueur : ")
    return surname


def get_player_birthday():
    birthday = input("Entrez la date de naissance du joueur\n"
                     "(format jj/mm/aaaa) : ")
    return birthday


def get_player_gender():
    gender = input("Entrez le sexe du joueur (f/m) : ")
    return gender


def get_player_elo():
    elo = input("Entrez le classement Elo du joueur : ")
    return elo


def get_existing_player():
    name = input("Entrez le prénom du joueur : ")
    name = name.strip().title()
    return name


def players_choice():
    choice = input("Nouveau joueur : \033[1m1\033[0m\n"
                   "Joueur existant : \033[1m2\033[0m : ")
    return choice


def print_existing_players(db_play):
    print("-------------------------")
    print(f"Joueur id : {db_play.doc_id}")
    print(f"Nom : {db_play['surname']}\n"
          f"Prénom : {db_play['name']}\n"
          f"Elo : {db_play['elo']}\n")


def existing_player_choice():
    choice = input("Entrez l'id du joueur souhaité : ")
    return int(choice)


def print_player(players):
    print("-------------------------")
    print("CLASSEMENT DES JOUEURS")
    print("-------------------------")
    for player in players:
        print(f"NOM : {player.surname}")
        print(f"Prénom : {player.name}")
        print(f"Score : {player.score}")
        print(f"Elo : {player.elo}")
        print("--------------------")
    input("Appuyez sur ENTRÉE pour continuer...")
    os.system("cls")


def print_match(matches):
    print("--------------------")
    print(f"1.{matches.player1.surname} {matches.player1.name}\n\n"
          f"VS\n\n"
          f"2.{matches.player2.surname} {matches.player2.name}\n")


def print_players_a_to_z():
    print("-------------------------")
    print("-------------------------")
    print("LISTE DES JOUEURS")
    print("ORDRE ALPHABÉTIQUE")
    print("-------------------------")


def print_players_elo_ascending():
    print("-------------------------")
    print("-------------------------")
    print("LISTE DES JOUEURS")
    print("CLASSEMENT ASCENDANT")
    print("-------------------------")


def print_players_elo_descending():
    print("-------------------------")
    print("-------------------------")
    print("LISTE DES JOUEURS")
    print("CLASSEMENT DESCENDANT")
    print("-------------------------")


def print_players_list(players):
    for player in players:
        print("-------------------------")
        print(f"NOM : {player.surname}")
        print(f"Prénom : {player.name}")
        print(f"Elo : {player.elo}")
        print(f"Âge : {player.age} ans")
        print(f"Date de naissance : {player.birthday}")
        print(f"Sexe : {player.gender}")
        print("-------------------------")
