# -*- coding: utf-8 -*-


from BaseObject import BaseObject


class User(BaseObject):

    def set_up(self, **kwargs):
        self.competitions = set()
        self.teams = set()

    def add_competition(self, cid):
        self.competitions.add(cid)

    def del_competition(self, cid):
        if cid in self.competitions:
            self.competitions.remove(cid)

    def get_competitions(self):
        for cid in self.competitions:
            yield cid

    def add_team(self, tid):
        self.teams.add(tid)

    def del_team(self, cid):
        if tid in self.teams:
            self.teams.remove(tid)

    def get_teams(self, cid):
        for tid in self.teams:
            yield tid

