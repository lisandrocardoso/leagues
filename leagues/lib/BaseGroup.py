# -*- coding: utf-8 -*-

from BaseObject import BaseObject
from BaseCompetition import BaseCompetition


class BaseGroup(BaseObject, BaseCompetition):

    def set_up(self, **kwargs):
        self.type = ""

        self.competitionId = kwargs.get('competitionId')

        self.teams = set()
        self.fixtures = {}

