# -*- coding: utf-8 -*-

import sqlite3
import json

from Draft import Draft
from Fixture import Fixture
from Match import Match
from Team import Team

from pprint import pprint


class DBInterfaceSQLite():

    def __init__(self, dbfile, configuration={}):
        self.dbfile = dbfile
        self.connection = sqlite3.connect(dbfile)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        self.queries = self.load_queries(configuration.get('dbfile',
            './queries-sqlite.json'))

    def load_queries(self, queries_file):
        qr = []
        with open(queries_file) as qf:
            queries = json.load(qf)
            # Remove 'comment' queries
            for q in queries:
                if 'name' in q:
                    qr.append(q)

        return qr

    def find_query(self, query_name):
        for q in self.queries:
            if q.get('name', '') == query_name:
                return q

        return {}

    def return_headed(self):
        result = self.cursor.fetchall()
        hr = self.cursor.description

        headers = [h[0] for h in hr]

        d = []
        for r in result:
            d.append(dict(zip(headers, r)))

        return d

    def run_query(self, query_name, qargs):
        query = self.find_query(query_name)
        sql = ' '.join(query.get('sql', ''))
        qtype = query.get('type')

        self.cursor.execute(sql, qargs)

        if qtype == 'select':
            return self.return_headed()
        elif qtype == 'insert':
            self.connection.commit()
            return self.cursor.lastrowid

    def setup_tables(self):
        cursor = self.connection.cursor()

        with open('setup-sqlite.json') as qf:
            queries = json.load(qf)

            for query in queries:
                name = query.get('name')
                sql = ' '.join(query.get('sql'))

                cursor.execute(sql)

        self.connection.commit()


