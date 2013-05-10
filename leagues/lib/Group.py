# -*- coding: utf-8 -*-


from BaseStage import BaseStage

import Tools


class Group(BaseStage):

    def generate_fixtures(self):
        if not self.teams:
            return False

        teams = self.teams
        while len(teams):
            (team, teams) = Tools.pick_random(teams, 2)

# Test set

#D = Draft()

#D.add_team(1)
#D.add_team(2)
#D.add_team(3)
#D.add_team(4)
#D.add_team(5)

#for team in D.get_teams():
#    print team

#D.generate_fixtures()
