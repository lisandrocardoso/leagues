# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class Team(BaseObject):

    def set_up(self, **kwargs):
        self.userID = kwargs.get('user_id')

        self.matches = set()
        self.competitions = set()

    def add_competition(self, cid):
        self.competitions.add(cid)

    def del_competition(self, cid):
        if cid in self.competitions:
            self.competitions.remove(cid)

    def get_competitions(self):
        for cid in self.competitions:
            yield cid 

    def add_match(self, mid):
        self.matches.add(mid)

    def del_match(self, mid):
        if mid in self.matches:
            self.matches.remove(mid)

    def get_matches(self, mid):
        for mid in self.matches:
            yield mid 

