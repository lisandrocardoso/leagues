# -*- coding: utf-8 -*-


from BaseObject import BaseObject


class StageGroup(BaseObject):

    def set_up(self, **kwargs):
        self.stages = set()

        self.data['finished'] = False
        self.data['winners'] = []
        self.data['losers'] = []
        self.data['current_stage'] = 0

### Stage handling toolset

    def add_stage(self, sid):
        self.stages.add(sid)

    def get_stages(self):
        for sid in self.stages:
            yield self.stages[sid]

    def del_stages(self, sid):
        if sid in self.stages:
            self.stages.remove(sid)
