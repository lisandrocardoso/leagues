# -*- coding: utf-8 -*-


from BaseObject import BaseObject


class Member(BaseObject):

    def set_up(self, **kwargs):
        self.points = kwargs['points']
        self.teamID = kwargs['teamID']
