# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class BaseCompetition(BaseObject):

    def set_up(self, **kwargs):

        #self.stages = [ [1,2,3 (groups)], [4, (draft) ] ]
        self.stages = []
        self.teams = []

    def add_team(self, teamId):
        self.teams.add(teamId)

    def del_team(self, teamId):
        try:
            self.teams.remove(teamId)
        except:
            # Fail silently
            pass

    def add_stage(self, stageIdList):
        self.stages.append[stageId]
