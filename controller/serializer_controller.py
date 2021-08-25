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
            "birthday": player.birth_date,
            "gender": player.gender,
            "score": player.score}
    return data


def player_list_deserializer(reloaded_player):
    player = Player(reloaded_player["name"],
                    reloaded_player["surname"],
                    reloaded_player["elo"],
                    reloaded_player["birthday"],
                    reloaded_player["gender"],
                    score=0)
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
            "matches": [match_serializer(match) for match in round.matches]}
    return data


def round_deserializer(reloaded_round):
    round = Round(reloaded_round["round_number"])
    for match in reloaded_round["matches"]:
        player1 = player_deserializer(match["player1"])
        player2 = player_deserializer(match["player2"])
        reload_match = Match(player1, player2)
        round.add_reload_match(reload_match)
    return round


def tournament_serializer(tournament):
    data = {"name": tournament.name,
            "place": tournament.place,
            "time_control": tournament.time_control,
            "details": tournament.details,
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
    tournament.players = list()
    tournament.rounds = list()

    for player in reloaded_tournament["players"]:
        player = player_deserializer(player)
        tournament.add_player(player)

    for round in reloaded_tournament["rounds"]:
        round_deserializer(round)
        tournament.add_round(round)
    return tournament
