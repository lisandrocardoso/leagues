# -*- coding: utf-8 -*-

import logging
import re

from lib.ObjInterface import ObjInterface

if __name__ == "__main__":

    logformat = '%(asctime)s %(levelname)s %(message)s'
    logging.basicConfig(format=logformat, level=logging.DEBUG)

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

    oi.create_user('pepe', 'password')

    u1 = oi.get_user_by_name('pepe')
    u2 = oi.get_user_by_name('pepe')

    print oi.auth_user('pepe', 'password').get_name()

    t1 = oi.create_team('Equipin', 1)
    t2 = oi.create_team('Sacachispas', 1)
    t3 = oi.create_team('Papichulo', 1)

    print t1.get_name()
    print t2.get_name()
    print t3.get_name()

    m1 = oi.create_match('Match1vs2', t1.get_ID(), t2.get_ID())
    m2 = oi.create_match('Match1vs3', t1.get_ID(), t3.get_ID())
    m3 = oi.create_match('Match2vs3', t2.get_ID(), t3.get_ID())
    m4 = oi.create_match('Match3vs2', t3.get_ID(), t2.get_ID())
    m5 = oi.create_match('Match3vs1', t3.get_ID(), t1.get_ID())
    m6 = oi.create_match('Match2vs1', t2.get_ID(), t1.get_ID())

    print oi.get_match_by_id(1).get_name()

    for match in oi.get_match_by_team(2):
        print match.get_name()

    f1 = oi.create_fixture('Fecha 1')
    oi.add_matches_to_fixture(f1.get_ID(),
        [m1.get_ID(), m2.get_ID(), m3.get_ID(), ])

    f2 = oi.create_fixture('Fecha 2')
    oi.add_matches_to_fixture(f2.get_ID(),
        [m4.get_ID(), m5.get_ID(), m6.get_ID(), ])

    print oi.get_fixture_match_ids(f1.get_ID())
    print oi.get_fixture_match_ids(f2.get_ID())

    #f2 = oi.create_fixture('Fecha 2')

    U = oi.load_user(1)

    oi.db.terminate(True)

