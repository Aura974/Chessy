from match import Match
from datetime import datetime

class Round:
    def __init__(self, match_name, round_name, begin_datetime, end_datetime):
        self.match_name = Match.match_name()
        self.round_name = round_name()
        self.begin_datetime = begin_datetime()
        self.end_datetime = end_datetime()

    def round_name(self):
        pass

    def begin_datetime(self):
        pass

    def end_datetime(self):
        pass

    

