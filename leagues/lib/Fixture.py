# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class Fixture(BaseObject):

    def set_up(self, **kwargs):
        self.matches = set()
        self.unmatched_teams = set()

    def add_match(self, matchId):
        self.matches.add(matchId)

    def del_match(self, matchId):
        try:
            self.matches.remove(matchId)
        except:
            pass

