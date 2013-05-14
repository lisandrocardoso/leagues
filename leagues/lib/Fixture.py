# -*- coding: utf-8 -*-

from BaseObject import BaseObject


# Fixture(name, < matches = [], stageId = 0 >)
class Fixture(BaseObject):

    def set_up(self, **kwargs):
        self.matches = set()

        self.data['finished'] = False

        self.unmatched_teams = set()

    def add_match(self, mid):
        self.matches.add(mid)

    def del_match(self, mid):
        if mid in self.matches:
            self.matches.remove(matchId)

    def get_matches(self):
        for mid in self.matches:
            yield mid

