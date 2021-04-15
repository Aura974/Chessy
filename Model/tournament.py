from player import Player
from match import Match
from round import Round
from datetime import datetime

class Tournament:
    def __init__(self, round_list, players_list, tournament_name, tournament_place, tournament_date, tournament_type, tournament_description):
        self.round_list = round_list()
        self.players_list = players_list()
        self.tournament_name = tournament_name()
        self.tournament_place = tournament_place()
        self.tournament_date = tournament_date()
        self.tournament_type = tour()
        self.tournament_description = tournament_description()

    def round_list():
        pass

    def players_list():
        pass

    def tournament_name():
        pass

    def tournament_place():
        pass

    def tournament_date():
        pass

    def tournament_type():
        pass

    def tournament_description():
        pass
   
