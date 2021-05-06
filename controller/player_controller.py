from view.player_view import get_player_info
from model.player import Player


class PlayerController:
    def __init__(self):
        name, elo = get_player_info()
        self.player = Player(name, elo, score=0)
