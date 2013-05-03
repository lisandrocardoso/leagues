# -*- coding: utf-8 -*-


from BaseObject import BaseObject


class User(BaseObject):

    def set_up(self, **kwargs):
        self.tournaments = kwargs.get('tournaments', [])
        self.teams = kwargs.get('teams', [])