import os


def enter_score():
    score = input("Veuillez renseigner le score \n(1 :"
                  "joueur 1 gagnant | 2 : joueur 2 gagnant |"
                  "3 : match nul) : ")
    return score


def print_match_result(match):
    print("--------------------")
    print(
        f"{match.player1.name} {match.player1.surname} : {match.score_player1}",
        f"\n{match.player2.name} {match.player2.surname} : {match.score_player2}"
        )
    input("Appuyez sur ENTRÉE pour continuer ...")
    os.system("cls")


def print_final_score(players, round_number):
    os.system("cls")
    print("-----------------------------------")
    print(f"SCORE FINAL -- ROUND #{round_number}")
    print("-----------------------------------")
    for player in players:
        print(f"{player.name} {player.surname} : {player.score}")
