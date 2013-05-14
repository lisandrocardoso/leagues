# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class BaseCompetition(BaseObject):

    def set_up(self, **kwargs):
        self.ctype = kwargs.get('ctype')
        self.userID = kwargs.get('user_id')

        self.teams = set()
        #self.stages = [ [1,2,3 (groups)], [4, (draft) ] ]
        self.stages = []

        self.data['finished'] = 0
        self.data['current_stage'] = 0

# Team handling toolset

    def add_team(self, tid):
        self.teams.add(tid)

    def del_team(self, tid):
        if tid in self.teams:
            self.teams.remove(tid)

# Stage handling toolset

    def add_stage_group(self, sid_list):
        if not sid in self.stages:
            self.stages.append(sid)
