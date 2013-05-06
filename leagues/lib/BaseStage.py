# -*- coding: utf-8 -*-


from BaseObject import BaseObject


# BaseStage(id, name, < teams = [], competitionId > )
class BaseStage(BaseObject):

    def set_up(self, **kwargs):
        self.teams = set(kwargs.get('teams', []))
        self.fixtures = {}

        self.competitionID = kwargs.get('competitionId', 0)

        self.data = {}

        self.data['legs'] = kwargs.get('legs', 1)
        self.data['finished'] = False
        self.data['winners'] = []
        self.data['losers'] = []
        self.data['current_fixture'] = 0

### Fixture handling toolset

    def get_new_key(self):
        return len(self.fixtures.keys())

    def get_order_id_by_fixture_id(self, fixtureId):
        for orderId in self.fixtures.keys():
            if fixtureId == self.fixtures[orderId]:
                return orderId

    def get_fixtures(self):
        for i in self.fixtures.keys():
            yield self.fixtures[i]

    def add_fixture(self, fixtureId):
        self.fixtures[self.get_new_key()] = fixtureId

    def del_fixture_by_fixture_id(self, fixtureId):
        orderId = self.get_order_id_by_fixture_id(fixtureId)
        self.del_fixture_by_order_id(orderId)

    def del_fixture_by_order_id(self, orderId):
        if self.fixtures.get(orderId, None):
            del self.fixtures[orderId]

### Teams handling toolset

    def add_team(self, teamId):
        self.teams.add(teamId)

    def get_teams(self):
        for team in self.teams:
            yield team

### Data handling

    def get_data(self):
        return self.data

### Placeholders

    def generate_fixture(self):
        return False
