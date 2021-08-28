from tinydb import TinyDB
from controller.player_controller import player_list_deserializer
from controller.serializer_controller import tournament_deserializer
from view.player_view import (print_players_a_to_z,
                              print_players_elo_ascending,
                              print_players_elo_descending,
                              print_players_list)
from view.tournament_view import (print_tournament_matches,
                                  print_tournament_matches_title,
                                  print_tournament_players_a_to_z,
                                  print_tournament_players_elo,
                                  print_tournament_players_list,
                                  print_tournament_rounds,
                                  print_tournaments_list,
                                  tournament_choice)
from utils.utils import get_age, get_tournament_matches


def get_players_list():
    db = TinyDB("players_data.json", indent=4)
    player_data = db.table('players_data')
    db_players = player_data.all()
    players = list()

    for player in db_players:
        player = player_list_deserializer(player)
        player.age = get_age(player.birthday)
        players.append(player)

    return players


def get_players_a_to_z(players):

    players.sort(key=lambda x: x.surname)

    print_players_a_to_z()
    print_players_list(players)

    return players


def get_players_elo_ascending(players):

    players.sort(key=lambda x: x.elo)

    print_players_elo_ascending()
    print_players_list(players)

    return players


def get_players_elo_descending(players):

    players.sort(key=lambda x: x.elo, reverse=True)

    print_players_elo_descending()
    print_players_list(players)

    return players


def get_tournaments_list():
    db = TinyDB("tournament_data.json", indent=4)
    tournament_data = db.table('tournament_data')
    db_tournament = tournament_data.all()
    tournaments = list()

    for tournament in db_tournament:
        tournament = tournament_deserializer(tournament)
        tournaments.append(tournament)

    tournaments.sort(key=lambda x: x.date, reverse=True)
    tournaments.sort(key=lambda x: x.status)

    for my_index, tournament in enumerate(tournaments, start=1):
        tournament.index = my_index

    print_tournaments_list(tournaments)

    return tournaments


def get_tournament_players_list():
    tournaments = get_tournaments_list()

    choice = tournament_choice()

    chosen_tournament = tournaments[(choice-1)]

    return chosen_tournament


def get_tournament_players_a_to_z(tournament):

    tournament.players.sort(key=lambda x: x.surname)

    print_tournament_players_a_to_z()
    print_tournament_players_list(tournament)

    return tournament


def get_tournament_players_elo(tournament):

    tournament.players.sort(key=lambda x: x.elo, reverse=True)

    print_tournament_players_elo()
    print_tournament_players_list(tournament)

    return tournament


def get_tournament_rounds_list():
    tournaments = get_tournaments_list()

    choice = tournament_choice()

    chosen_tournament = tournaments[(choice-1)]

    print_tournament_rounds(chosen_tournament)

    return chosen_tournament


def get_tournament_matches_list():
    tournaments = get_tournaments_list()

    choice = tournament_choice()

    chosen_tournament = tournaments[(choice-1)]

    tournament_rounds, round_matches = get_tournament_matches(chosen_tournament)

    print_tournament_matches_title(chosen_tournament)
    print_tournament_matches(tournament_rounds, round_matches)

    return tournament_rounds, round_matches
