import os


def enter_score():
    os.system("clear")
    score = input("Enter score (1 : player 1 win / 2 : player 2 win / 3 : draw) ")
    return score


def print_match_result(match):
    print(
        f"{match.player1.name} : {match.score_player1}",
        f"\n{match.player2.name} : {match.score_player2}"
        )
    input("Appuyez sur ENTER pour continuer ...")


def print_final_score(players, number):
    os.system("clear")
    print(f"FINAL SCORE -- ROUND #{number}")
    for player in players:
        print(f"{player.name} : {player.score}")
