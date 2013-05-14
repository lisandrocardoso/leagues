# -*- coding: utf-8 -*-

import hashlib
import logging
import re

from DBInterfaceSQLite import DBInterfaceSQLite

from Draft import Draft
from Fixture import Fixture
from Match import Match
from Team import Team
from User import User

from pprint import pprint

import Tools


def oilogger(func):
    def inner(*args, **kwargs):
        name = func.__name__
        params = ",".join(map(str, args[1:]))
        msg = "OI " + name + ": " + params
        if re.search('^get_', name):
            logging.debug(msg)
        elif re.search('^load_', name):
            logging.info(msg)
        else:
            logging.debug(msg)
        return func(*args, **kwargs)
    return inner


class ObjInterface():

    def __init__(self, configuration):
        logging.debug('OI Initiating Object Interface')
        self.storage = {
            'user': {},
            'team': {},
            'match': {},
            'fixture': {},
            'stage': {},
            'competition': {}
            }

        self.dbtype = configuration.get('db_type')
        print 'test'
        if self.dbtype == 'sqlite':
            logging.debug('OI Using sqlite interface')
            self.db = DBInterfaceSQLite(configuration.get('sqlite'))

    def save_to_storage(self, objtype, obj):
        if objtype in self.storage:
            oid = obj.get_ID()
            if oid in self.storage[objtype]:
                logging.debug('OI storage ' + objtype +
                 " " + str(oid) + " exists")
                return True
            self.storage[objtype][oid] = obj
            logging.debug('OI stored ' + objtype + " " + str(oid))
            return True
        else:
            logging.error('OI storage: wrong type ' + objtype)
            return False

    def load_from_storage(self, objtype, oid):
        if objtype in self.storage:
            obj = self.storage[objtype].get(oid, None)
            if not obj:
                logging.debug('OI storage: not found ' +
                 objtype + " " + str(oid))
                return None
            else:
                logging.debug('OI storage load: ' + objtype + " " + str(oid))
                return obj
        else:
            logging.error('OI storage: wrong type ' + objtype)
            return None

# - A 'get' function with specified parameter, i.e. 'get_team_by_id',
# will query DB for the specified by id object.
# - A 'get' function without specified parameter will query local
# storage (self.storage dictionary). If not found will return None.
# - A 'load' function will check storage, and then query DB, while also
# loading every referenced object, i.e., load_fixture will call
# load_match for every matchId in fixtureMatch table.
# A load_competition will load EVERYTHING

# User interface toolset

    @oilogger
    def create_user(self, name, password):
        sha1 = hashlib.sha1()
        sha1.update(password)
        enc_password = sha1.hexdigest()

        uid = self.db.run_query('create_user', (name, enc_password,))
        u = User(uid, name)

        self.save_to_storage('user', u)

        return u

    @oilogger
    def get_user_by_name(self, name):
        ret = self.db.run_query('get_user_by_name', (name,))
        if not ret:
            logging.debug('OI get_user_by_name: not found')
            return None

        row = ret[0]
        u = User(row['id'], row['name'])

        self.save_to_storage('user', u)

        return u

    @oilogger
    def get_user_by_id(self, uid):
        ret = self.db.run_query('get_user_by_id', (uid,))
        if not ret:
            logging.debug('OI get_user_by_id: not found')
            return None

        row = ret[0]
        u = User(uid, row['name'])

        self.save_to_storage('user', u)

        return u

    @oilogger
    def auth_user(self, name, password):
        sha1 = hashlib.sha1()
        sha1.update(password)
        enc_password = sha1.hexdigest()

        ret = self.db.run_query('get_user_by_name', (name,))
        if not ret:
            logging.debug('OI auth_user: not found')
            return None

        row = ret[0]
        if row['password'] == enc_password:
            u = User(row['id'], row['name'])

            self.save_to_storage('user', u)

            return u
        else:
            logging.debug('OI auth_user: password mismatch')
            return None

    @oilogger
    def create_user_competition(self, uid, cid):
        rid = self.db.run_query('create_user_competition',
            (uid, cid, ))

    @oilogger
    def create_user_team(self, uid, tid):
        rid = self.db.run_query('create_user_team',
            (uid, tid, ))

    @oilogger
    def get_user_competition_ids(self, uid):
        ret = self.db.run_query('get_user_competitions', (uid,))
        competitions = []
        for row in ret:
            competitions.append(row['competitionId'])

    @oilogger
    def get_user_team_ids(self, uid):
        ret = self.db.run_query('get_user_teams', (uid,))
        teams = []
        for row in ret:
            teams.append(row['teamId'])

    @oilogger
    def get_user(self, uid):
        return self.load_from_storage('user', uid)

    @oilogger
    def load_user(self, uid):
        u = self.get_user(uid)
        if not u:
            u = self.get_user_by_id(uid)

        if not u:
            logging.debug('OI user not found ' + str(uid))
            return None

        cids = self.get_user_competition_ids(uid)
        tids = self.get_user_team_ids(uid)

# Team interface toolset

    @oilogger
    def create_team(self, name, userId):
        oid = self.db.run_query('create_team', (name, userId,))
        t = Team(oid, name, user_id=userId)

        self.save_to_storage('team', t)

        return t

    @oilogger
    def get_team_by_id(self, tid):
        ret = self.db.run_query('get_team_by_id', (tid,))[0]
        t = Team(tid, ret['name'], ret['ownerId'])

        self.save_to_storage('team', t)

        return t

    @oilogger
    def get_team_by_name(self, name):
        ret = self.db.run_query('get_team_by_name', (name,))
        teams = []
        for row in ret:
            t = Team(row['id'], row['name'], row['ownerId'])
            teams.append(t)

            self.save_to_storage('team', t)

        return teams

    @oilogger
    def get_team(self, tid):
        return self.load_from_storage('team', tid)

# Match interface toolset

    @oilogger
    def create_match(self, name, homeTeamId, awayTeamId):
        mid = self.db.run_query('create_match',
            (name, homeTeamId, awayTeamId,))
        m = Match(mid, name, home_id=homeTeamId, away_id=awayTeamId)

        self.save_to_storage('match', m)

        return m

    @oilogger
    def get_match_by_id(self, mid):
        ret = self.db.run_query('get_match_by_id', (mid,))[0]
        m = Match(mid, ret['name'],
            home_id=ret['homeTeamId'],
            away_id=ret['awayTeamId'])

        self.save_to_storage('match', m)

        return m

    @oilogger
    def get_match_by_team(self, tid):
        ret = self.db.run_query('get_match_by_team', (tid, tid, ))
        matches = []
        for row in ret:
            m = Match(row['id'], row['name'],
                home_id=row['homeTeamId'],
                away_id=row['awayTeamId'])
            matches.append(m)

            self.save_to_storage('match', m)

        return matches

    @oilogger
    def get_match(self, mid):
        return self.load_from_storage('match', mid)

# Fixture interface toolset

    @oilogger
    def create_fixture(self, name):
        fid = self.db.run_query('create_fixture',
            (name, ))
        f = Fixture(fid, name)

        self.save_to_storage('fixture', f)

        return f

    @oilogger
    def get_fixture_by_id(self, fid):
        ret = self.db.run_query('get_fixture_by_id', (fid, ))[0]
        f = Fixture(fid, ret['name'])

        self.save_to_storage('fixture', fid)

        return f

    @oilogger
    def create_fixture_match(self, fid, mid):
        rid = self.db.run_query('create_fixture_match',
            (fid, mid, ))

    @oilogger
    def get_fixture_match_ids(self, fid):
        ret = self.db.run_query('get_fixture_matches',
            (fid, ))
        matches = []
        for row in ret:
            matches.append(row['matchId'])

        return matches

    @oilogger
    def get_fixture(self, fid):
        return self.load_from_storage('fixture', fid)

    def add_matches_to_fixture(self, fid, matches=[]):
        logging.debug('OI add_matches_to_fixture ' + str(fid))
        f = self.get_fixture(fid)
        if not f:
            return None

        for mid in matches:
            # If in local storage
            if self.get_match(mid):
                self.create_fixture_match(fid, mid)
            # If not we'll check in DB
            else:
                mobj = self.get_match_by_id(mid)
                if mobj:
                    self.create_fixture_match(fid, mid)

# Stage interface toolset

    @oilogger
    def create_stage(self, name, stype):
        sid = self.db.run_query('create_stage',
            (name, stype, ))
        s = Stage(sid, name, stype)

        self.save_to_storage('stage', s)

        return s

    @oilogger
    def get_stage_by_id(self, sid):
        ret = self.db.run_query('get_stage_by_id', (sid, ))[0]
        stype = ret['type']
        if stype == 'draft':
            s = Draft(sid, ret['name'], stype=stype)
        elif stype == 'group':
            s = Group(sid, ret['name'], stype=stype)

        self.save_to_storage('stage', s)

        return s

    @oilogger
    def create_stage_fixture(self, sid, fid):
        rid = self.db.run_query('create_stage_fixture',
            (sid, fid, ))

    @oilogger
    def get_stage_fixture_ids(self, sid):
        ret = self.db.run_query('get_stage_fixtures',
            (sid, ))
        fixtures = []
        for row in ret:
            fixtures.append(row['fixtureId'])

        return fixtures

    @oilogger
    def create_stage_team(self, sid, tid):
        rid = self.db.run_query('create_stage_team',
            (sid, tid, ))

    @oilogger
    def get_stage_team_ids(self, sid):
        ret = self.db.run_query('get_stage_teams',
            (sid, ))
        teams = []
        for row in ret:
            teams.append(ret['teamId'])

        return teams

# Competition interface toolset

    @oilogger
    def create_competition(self, name):
        cid = self.db.run_query('create_competition',
            (name, ))
        c = Competition(cid, name)

        self.save_to_storage('stage', c)

        return c
