from view.player_view import get_player_info, players_choice
from model.player import Player
from tinydb import TinyDB, Query
from controller.serializer_controller import player_list_serializer


class PlayerController:
    def __init__(self):
        self.player = None
        self.db = TinyDB("players_data.json", indent=4)
        self.players_data = self.db.table("players_data")

    def new_player(self):
        name, elo = get_player_info()
        self.player = Player(name, elo, score=0)
        self.players_data.insert(player_list_serializer(self.player))
        return self.player

    def existing_player(self):
        pass

    def handle_choice(self):
        choice = players_choice()
        while (choice != "1" and choice != "2"):
            print("Choisissez 1 ou 2 uniquement")
            choice = players_choice()
        else:
            if (choice == "1"):
                choice = self.new_player()
            elif (choice == "2"):
                choice = self.new_player()
        return choice
