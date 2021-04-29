def get_player_info():
    name = input("Enter the player name : ")
    elo = input("Enter the player elo : ")
    return name, elo


def print_player(players):
    for player in players:
        print(f"name : {player.name}")
        print(f"elo : {player.elo}")
        print("--------------------")
