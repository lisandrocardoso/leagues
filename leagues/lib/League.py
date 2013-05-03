# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class  League(BaseObject):

    def set_up(self, **kwargs):
        self.type = ""
        self.teams = set()
        self.fixtures = {}

    def add_team(self, teamId):
        pass

    def del_team(self, teamId):
        pass

    def add_fixture(self, fixtureId):
        pass
