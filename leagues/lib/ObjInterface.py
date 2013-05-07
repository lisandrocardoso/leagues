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
            'user' : {},
            'team' : {},
            'match' : {},
            'fixture' : {},
            'stage' : {},
            'competition' : {}
            }

        self.db = DBInterfaceSQLite('testdb')

# User interface toolset

    def create_user(self, name, password):
        sha1 = hashlib.sha1()
        sha1.update(password)

        enc_password = sha1.hexdigest()

        oid = self.db.run_query('create_user', (name, enc_password,))
        obj = User(oid, name)

        self.storage['user'][oid] = obj

    def load_user_name(self, name):
        ret = self.db.run_query('get_user_by_name', (name,))

        return User(ret[0][0], ret[0][1])


    def load_user_id(self, uid):
        ret = self.db.run_query('get_user_by_id', (uid,))

        return User(ret[0][0], ret[0][1])

    def get_user(self, uid):
        return self.storage['user'][uid]


oi = ObjInterface()

oi.db.setup_tables()

oi.create_user('pepe', 'password')

oi.load_user_name('pepe')

oi.load_user_id(1)

