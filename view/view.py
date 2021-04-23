def get_tournament_info():
    name = input("Enter the tournament name : ")
    time_control = input("Enter time control (Bullet/Splitz/Quick) : ")
    return name, time_control


def get_player_info():
    name = input("Enter the player name : ")
    elo = input("Enter the player elo : ")
    return name, elo


def print_player(players):
    for player in players:
        print(f"name : {player.name}")
        print(f"elo : {player.elo}")
        print("--------------------")


def enter_score():
    score = input("Enter score (1 / 2 / 0) : ")
    return score


def print_match_result(match):
    print(
        f"{match.player1.name} : {match.score_player1}",
        f"\n{match.player2.name} : {match.score_player2}"
        )
