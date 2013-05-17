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
            t = oi.create_team('Team' + str(j) + '_User_' + str(i), i)
            print oi.get_team_by_name('Team' + str(j) + '_User_' +
                str(i))[0].get_name(),
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

    s = oi.create_stage('Stage 1', 'group', 1)
    for tid in range(1, 11):
        if oi.get_team_by_id(tid):
            oi.add_team_to_stage(s.get_ID(), tid)

    oi.generate_stage_fixture_matches(s.get_ID())

    oi.db.terminate(True)
