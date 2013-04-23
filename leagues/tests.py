# -*- coding: utf-8 -*-

import lib.Member
import lib.Team
import lib.Match
import lib.Fixture

# tentativo:

members = {}
teams = {}
matches = {}
fixtures = {}
leagues = {}

for i in range(0, 100):
    members[i] = lib.Member.Member(i, 'nombre' + str(i), points=0, teamID=0)

for i in range(1, 10, 2):
    teams[i] = lib.Team.Team(i, 'team' + str(i))

for i in range(2, 11, 2):
    teams[i] = lib.Team.Team(i, 'team' + str(i))

for i in range(0, 10):
    for j in range(0, 10):
        teams[i + 1].add_member((i * 10) + j)

for i in range(0, 5):
    matches[i] = lib.Match.Match(i, 'match' + str(i), team_home=(i + 1),
                                 team_away=(i + 6))
    matches[i].start_match()
    matches[i].add_score_home()
    matches[i].add_score_home()
    matches[i].add_score_away()

fixt = lib.Fixture.Fixture(1)
fixt.add_date(1)
for i in range(0, 5):
    fixt.add_match_to_date(1, i, 'date Date', 'date Info')

#for i in matches:
#    print matches[i].get_name()
#    (j, k) = matches[i].get_teams()
#    print teams[j].get_name() + ' ' + teams[k].get_name()
#    print matches[i].get_score()
