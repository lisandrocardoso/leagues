# -*- coding: utf-8 -*-

import hashlib

from DBInterfaceSQLite import DBInterfaceSQLite

from Draft import Draft
from Fixture import Fixture
from Match import Match
from Team import Team
from User import User

from pprint import pprint

import Tools


class ObjInterface():

    def __init__(self):
        self.storage = {
            'user': {},
            'team': {},
            'match': {},
            'fixture': {},
            'stage': {},
            'competition': {}
            }

        self.db = DBInterfaceSQLite('testdb')

# User interface toolset

    def create_user(self, name, password):
        sha1 = hashlib.sha1()
        sha1.update(password)
        enc_password = sha1.hexdigest()

        oid = self.db.run_query('create_user', (name, enc_password,))
        u = User(oid, name)

        self.storage['user'][oid] = u

    def load_user_name(self, name):
        ret = self.db.run_query('get_user_by_name', (name,))[0]
        u = User(ret['id'], ret['name'])
        self.storage['user'][u.get_ID()] = u

        return u

    def load_user_id(self, uid):
        ret = self.db.run_query('get_user_by_id', (uid,))[0]
        u = User(uid, ret['name'])
        self.storage['user'][uid] = u

        return u

    def get_user(self, uid):
        return self.storage['user'].get(uid, None)

    def auth_user(self, name, password):
        sha1 = hashlib.sha1()
        sha1.update(password)
        enc_password = sha1.hexdigest()

        ret = self.db.run_query('get_user_by_name', (name,))[0]
        if ret['password'] == enc_password:
            u = User(ret['id'], ret['name'])
            self.storage['user'][ret['id']] = u

            return u

        return None

# Team interface toolset

    def create_team(self, name, userId):
        oid = self.db.run_query('create_team', (name, userId,))
        t = Team(oid, name, user_id=userId)

        self.storage['team'][oid] = t

        return t

    def load_team_id(self, tid):
        ret = self.db.run_query('get_team_by_id', (tid,))[0]
        t = Team(tid, ret['name'], ret['ownerId'])
        self.storage['team'][tid] = t

        return t

    def load_team_name(self, name):
        ret = self.db.run_query('get_team_by_name', (name,))
        teams = []
        for row in ret:
            t = Team(row['id'], row['name'], row['ownerId'])
            self.storage['team'][row['id']] = t
            teams.append(t)

        return teams

    def get_team(self, tid):
        return self.storage['team'].get('tid', None)

# Match interface toolset

    def create_match(self, name, homeTeamId, awayTeamId):
        oid = self.db.run_query('create_match',
            (name, homeTeamId, awayTeamId,))
        m = Match(oid, name, home_id=homeTeamId, away_id=awayTeamId)

        self.storage['match'][oid] = m

        return m

    def load_match_id(self, mid):
        ret = self.db.run_query('get_match_by_id', (mid,))[0]
        m = Match(mid, ret['name'],
            home_id=ret['homeTeamId'],
            away_id=ret['awayTeamId'])
        self.storage['match'][mid] = m

        return m

    def load_match_team(self, tid):
        ret = self.db.run_query('get_match_by_team', (tid, tid, ))
        matches = []
        for row in ret:
            m = Match(row['id'], row['name'],
                home_id=row['homeTeamId'],
                away_id=row['awayTeamId'])
            self.storage['match'][m.get_ID()] = m
            matches.append(m)

        return matches

    def get_match(self, mid):
        return self.storage['match'].get('mid', None)

if __name__ == "__main__":
    oi = ObjInterface()

    oi.db.setup_tables()

    oi.create_user('pepe', 'password')

    u1 = oi.load_user_name('pepe')

    u2 = oi.load_user_name('pepe')

    print oi.auth_user('pepe', 'milangas')
    print oi.auth_user('pepe', 'password')

    t1 = oi.create_team('Equipin', 1)
    t2 = oi.create_team('Sacachispas', 1)
    t3 = oi.create_team('Papichulo', 1)

    print t1
    print t2

    m1 = oi.create_match('Match1vs2', t1.get_ID(), t2.get_ID())
    m2 = oi.create_match('Match1vs3', t1.get_ID(), t3.get_ID())
    m3 = oi.create_match('Match2vs3', t2.get_ID(), t3.get_ID())
    m4 = oi.create_match('Match3vs2', t3.get_ID(), t2.get_ID())
    m5 = oi.create_match('Match3vs1', t3.get_ID(), t1.get_ID())
    m6 = oi.create_match('Match2vs1', t2.get_ID(), t1.get_ID())

    print oi.load_match_id(1)

    for match in oi.load_match_team(2):
        print match.get_name()
