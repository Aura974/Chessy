from tinydb import TinyDB


def player_serializer(player):
    data = {"name": player.name, "elo": player.elo, "score": player.score}
    return data


def player_list_serializer(player):
    data = {"name": player.name, "elo": player.elo}
    # "surname": Player.surname, "birth_date": Player.birth_date,
    # "gender": Player.gender
    return data


def match_serializer(match):
    data = {"player1": player_serializer(match.player1),
            "player2": player_serializer(match.player2),
            "score_player1": match.score_player1,
            "score_player2": match.score_player2}
    return data


def round_serializer(round):
    data = {"round_number": round.round_number,
            "matches": [match_serializer(match) for match in round.matches]}
    return data


def tournament_serializer(tournament):
    data = {"name": tournament.name,
            "time_control": tournament.time_control,
            "players": [player_serializer(player)
                        for player in tournament.players],
            "rounds": [round_serializer(round) for round in tournament.rounds]}
    return data
