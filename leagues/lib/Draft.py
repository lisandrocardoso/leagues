# -*- coding: utf-8 -*-


from BaseStage import BaseStage

import Tools


class Draft(BaseStage):

#    def set_up(self, **kwargs):
#        self.teams = kwargs.get('teams', set())
#        self.fixtures = {}
#
#        self.data = {}
#
#        self.data['legs'] = kwargs.get('legs', 1)
#        self.data['finished'] = False
#        self.data['winners'] = []
#        self.data['losers'] = []
#        self.data['current_fixture'] = 0

#    def generate_fixtures(self):
#        if not self.teams:
#            return False

#        teams = self.teams

#        while len(teams):
#            (team, teams) = Tools.pick_random(teams, 2)
            


# Test set

D = Draft()

D.add_team(1)
D.add_team(2)
D.add_team(3)
D.add_team(4)
D.add_team(5)

for team in D.get_teams():
    print team

D.generate_fixtures()