# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class BaseCompetition(BaseObject):

    def set_up(self, **kwargs):
        self.ctype = kwargs.get('ctype')
        self.userID = kwargs.get('user_id')

        self.teams = set()
        #self.stagegroups = [ StageGroup, StageGroup, ...]
        self.stage_groups = []

        self.data['finished'] = 0
        self.data['current_stage'] = 0

# Team handling toolset

    def add_team(self, tid):
        self.teams.add(tid)

    def del_team(self, tid):
        if tid in self.teams:
            self.teams.remove(tid)

# Stage handling toolset

    def add_stage_group(self, sgid):
        if not sgid in self.stages:
            self.stages.append(sgid)

    def del_stage_group(self, sgid):
        if sgid in self.stages:
            self.stages.remove(sgid)
