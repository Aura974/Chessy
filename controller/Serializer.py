from tinydb import TinyDB
from model.tournament import Tournament


class Serializer:
    def __init__(self, data):
        self.data = Tournament.serializer

