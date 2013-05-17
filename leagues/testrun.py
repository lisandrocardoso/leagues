# -*- coding: utf-8 -*-

import logging
import re
import sys
import random
from pprint import pprint

from lib import Tools

from lib.ObjInterface import ObjInterface

if __name__ == "__main__":

    logformat = '%(asctime)s %(levelname)s %(message)s'
    logging.basicConfig(format=logformat, level=logging.INFO)

    config = {
        'sqlite': {},
        'db_type': 'sqlite'
        }

    config['sqlite'] = {
        'db_file': 'tmp/dbfile',
        'queries_file': 'sql/queries-sqlite.json',
        'setup_queries_file': 'sql/setup-sqlite.json'
        }

    oi = ObjInterface(config)

    oi.db.setup_tables()

    print " -------------------------------- "
    print " -- User & Team creation tests -- "
    print " -------------------------------- "
    for i in range(1, 11):
        oi.create_user('user' + str(i), 'password')
        print oi.get_user_by_name('user' + str(i)).get_name(),
        print oi.get_user_by_id(i).get_ID()

        for j in range(1, 3):
            t = oi.create_team('team' + str(j) + '_User' + str(i), i)
            print oi.get_team_by_name('team' + str(j) +
                '_User' + str(i))[0].get_name(),
            print oi.get_team_by_id(t.get_ID()).get_ID()

    print " -------------------------- "
    print " -- Match creation tests -- "
    print " -------------------------- "
    #for i in range(1, 21, 2):
    #    home_team = oi.get_team_by_id(i)
    #    away_team = oi.get_team_by_id(i + 1)
    #    match_name = home_team.get_name() + " vs " + away_team.get_name()
 #    m = oi.create_match(match_name, home_team.get_ID(), away_team.get_ID())
    #    mid = m.get_ID()
    #    m = oi.update_match_data(mid, random.randrange(0, 5),
    #        random.randrange(0, 5))
    #    nm = oi.get_match_by_id(mid)
    #    print nm.get_name(), m.get_ID()
    #    print nm.get_teams()
    #    pprint(nm.get_data())

    print " ------------------------------------ "
    print " -- Match & Fixture creation tests -- "
    print " ------------------------------------ "

    teams = []
    for i in oi.storage.get('team').keys():
        teams.append(oi.storage.get('team')[i].get_ID())

    fixture_lists = Tools.combinations(set(teams))

    for idx in range(0, len(fixture_lists)):
        print "--------------" + str(idx)
        fixture = oi.create_fixture('Fecha ' + str(idx + 1))
        for pair in fixture_lists[idx]:
            print pair
            h_team = pair[0]
            h_name = oi.get_team_by_id(h_team).get_name()
            a_team = pair[1]
            a_name = oi.get_team_by_id(a_team).get_name()
            match_name = h_name + " vs " + a_name

            match = oi.create_match(match_name, h_team, a_team)
            fixture.add_match(match.get_ID())

    print oi.storage.get('fixture')

    for fixtid in oi.storage.get('fixture').keys():
        fixture = oi.storage.get('fixture')[fixtid]
        print " --------------------- "
        print fixture.get_name()
        for mid in fixture.get_matches():
            print oi.get_match(mid).get_name()

    oi.db.terminate(True)
