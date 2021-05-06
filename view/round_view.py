import os


def enter_score():
    score = input("Veuillez renseigner le score \n(\033[1m1\033[0m :"
                  "joueur 1 gagnant |\033[1m2\033[0m : joueur 2 gagnant |"
                  "\033[1m3\033[0m : match nul) : ")
    return score


def print_match_result(match):
    print("--------------------")
    print(
        f"{match.player1.name} : {match.score_player1}",
        f"\n{match.player2.name} : {match.score_player2}"
        )
    input("Appuyez sur ENTRÉE pour continuer ...")
    os.system("cls")


def print_final_score(players, number):
    os.system("cls")
    print("-----------------------------------")
    print(f"SCORE FINAL -- TOUR #{number}")
    print("-----------------------------------")
    for player in players:
        print(f"{player.name} : {player.score}")
