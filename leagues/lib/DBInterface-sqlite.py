# -*- coding: utf-8 -*-

import sqlite3
import json

from Draft import Draft
from Fixture import Fixture
from Match import Match
from Team import Team

from pprint import pprint

class DBInterfaceSQLite():

    def __init__(self, dbfile):

        self.dbfile = dbfile
        self.connection = sqlite3.connect(dbfile)

        self.queries = {}

    def create_match(self):
        # Insert a new match entry, return last_inserted_id
        # Only for test purposes:
        for i in range(0, 99999):
            yield i

    def setup_tables(self):
        cursor = self.connection.cursor()

        with open('setup-sqlite.json') as qf:
            queries = json.load(qf)

            for query in queries:
                name = query.get('name')
                sql = ''.join(query.get('sql'))

                print sql

                cursor.execute(sql)

        self.connection.commit()

    def create_user(self, username, password):
        pass

    def test_tables(self):
        cursor = self.connection.cursor()

        for i in range(101, 200):
            cursor.execute("""
                INSERT INTO match VALUES(
                    NULL,
                    ?,
                    NULL,
                    NULL,
                    0,
                    0,
                    0)
            """, ("name" + str(i), ))

        for i in range(0, 100):
            cursor.execute("""
                INSERT INTO fixture VALUES(
                    NULL,
                    NULL)
            """)

        for fId in range(0, 100):
            for mId in range(101, 200):
                cursor.execute("""
                    INSERT INTO fixtureMatch VALUES(
                        ?,
                        ?)
            """, (fId, mId))

        self.connection.commit()

### Test suite

db = DBInterfaceSQLite('testdbp')

db.setup_tables()

#db.test_tables()
