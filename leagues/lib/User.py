# -*- coding: utf-8 -*-


from BaseObject import BaseObject


class User(BaseObject):

    def set_up(self, **kwargs):
        self.competitions = kwargs.get('competitions', [])
        self.teams = kwargs.get('teams', [])
