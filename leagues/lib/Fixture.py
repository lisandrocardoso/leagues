# -*- coding: utf-8 -*-

from BaseObject import BaseObject


# Fixture(name, < matches = [], stageId = 0 >)
class Fixture(BaseObject):

    def set_up(self, **kwargs):
        self.matches = set(kwargs.get('matches', []))

        self.stage_id = kwargs.get('stageId', 0)
        
        self.unmatched_teams = set()

    def add_match(self, matchId):
        self.matches.add(matchId)

    def del_match(self, matchId):
        try:
            self.matches.remove(matchId)
        except:
            pass

