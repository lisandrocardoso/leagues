# -*- coding: utf-8 -*-


from BaseObject import BaseObject


# BaseStage(id, name, < teams = [], competitionId > )
class BaseStage(BaseObject):

    def set_up(self, **kwargs):
        self.stype = kwargs.get('stype')

        self.fixtures = []
        self.teams = set()

        self.data['finished'] = False
        self.data['winners'] = []
        self.data['losers'] = []
        self.data['current_fixture'] = 0
        self.data['legs'] = kwargs.get('legs')

### Fixture handling toolset

    def add_fixture(self, fid):
        if not fid in self.fixtures:
            self.fixtures.append(fid)
            return True
        return False

    def get_fixture_by_order_id(self, oid):
        if oid >= len(self.fixtures) or oid < 0:
            return None
        return self.fixtures[oid]

    def get_fixtures(self):
        for i in self.fixtures:
            yield self.fixtures[i]

    def del_fixture(self, fid):
        if fid in self.fixtures:
            self.fixtures.remove(fid)

### Teams handling toolset

    def add_team(self, tid):
        if not tid in self.teams:
            self.teams.add(tid)
            return True
        return False

    def get_teams(self):
        for team in self.teams:
            yield team

### Placeholders

    def generate_fixture(self):
        return False
