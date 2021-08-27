from model.player import Player
from model.tournament import Tournament
from model.round import Round
from model.match import Match


def player_serializer(player):
    data = {"name": player.name,
            "surname": player.surname,
            "elo": player.elo,
            "score": player.score}
    return data


def player_list_serializer(player):
    data = {"name": player.name,
            "surname": player.surname,
            "elo": player.elo,
            "score": player.score,
            "birthday": player.birth_date,
            "gender": player.gender}
    return data


def player_list_deserializer(reloaded_player):
    player = Player(reloaded_player["name"],
                    reloaded_player["surname"],
                    reloaded_player["elo"],
                    reloaded_player["score"])
    player.birth_date = reloaded_player["birthday"]
    player.gender = reloaded_player["gender"]
    return player


def player_deserializer(reloaded_player):
    player = Player(reloaded_player["name"],
                    reloaded_player["surname"],
                    reloaded_player["elo"],
                    reloaded_player["score"])
    return player


def match_serializer(match):
    data = {"player1": player_serializer(match.player1),
            "player2": player_serializer(match.player2),
            "score_player1": match.score_player1,
            "score_player2": match.score_player2}
    return data


def round_serializer(round):
    data = {"round_number": round.round_number,
            "start_time": round.start_time,
            "end_time": round.end_time,
            "matches": [match_serializer(match) for match in round.matches]}
    return data


def round_deserializer(reloaded_round):
    reload_round = Round(reloaded_round["round_number"],
                         reloaded_round["start_time"],
                         reloaded_round["end_time"])
    for match in reloaded_round["matches"]:
        player1 = player_deserializer(match["player1"])
        player2 = player_deserializer(match["player2"])
        reload_match = Match(player1, player2)
        reload_round.add_reload_match(reload_match)
    return reload_round


def tournament_serializer(tournament):
    data = {"name": tournament.name,
            "place": tournament.place,
            "date": tournament.date,
            "time_control": tournament.time_control,
            "details": tournament.details,
            "status": tournament.status,
            "players": [player_serializer(player)
                        for player in tournament.players],
            "rounds": [round_serializer(round) for round in tournament.rounds]}
    return data


def tournament_deserializer(reloaded_tournament):
    tournament = Tournament(reloaded_tournament["name"],
                            reloaded_tournament["place"],
                            reloaded_tournament["date"],
                            reloaded_tournament["time_control"],
                            reloaded_tournament["details"])
    tournament.status = reloaded_tournament["status"]
    tournament.players = list()
    tournament.rounds = list()

    for player in reloaded_tournament["players"]:
        player = player_deserializer(player)
        tournament.add_player(player)

    for round in reloaded_tournament["rounds"]:
        reload_round = round_deserializer(round)
        tournament.add_round(reload_round)

    return tournament
