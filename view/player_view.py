import os


def get_player_info():
    name = input("Entrez le prénom du joueur : ")
    elo = input("Entrez le classement Elo du joueur : ")
    return name, elo


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