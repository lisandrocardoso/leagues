# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class BaseLeague(BaseObject):

    def set_up(self, **kwargs):
        self.type = ""
        # stage type = group, draft
        # stage order
        # stage date ?
        # stage rules ?

        self.stages = {} 
        self.teams = []

    def add_team(self, teamId):
        pass

    def del_team(self, teamId):
        pass

    def add_fixture(self, fixtureId):
        pass
