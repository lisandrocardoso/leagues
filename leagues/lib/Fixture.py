# -*- coding: utf-8 -*-

import datetime

from BaseObject import BaseObject


class Fixture(BaseObject):

    def set_up(self, **kwargs):
        self.competitionId = kwargs.get('competitionId')
        self.stageId = kwargs.get('stageId')
        self.matches = []

    def add_match(self, matchId):
        self.matches.append(matchId)

    def del_match(self, matchId):
        if matchId in self.matches:
            self.matches.remove(matchId)

    def get_matches(self):
        return self.matches

