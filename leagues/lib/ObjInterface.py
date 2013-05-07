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
        u = User(oid, name)

        self.storage['user'][oid] = u

    def load_user_name(self, name):
        ret = self.db.run_query('get_user_by_name', (name,))
        u = User(ret['id'], ret['name'])
        self.storage['user'][u.get_ID()] = u

        return u

    def load_user_id(self, uid):
        ret = self.db.run_query('get_user_by_id', (uid,))
        u = User(ret['id'], ret['name'])
        self.storage['user'][u.get_ID()] = u

        return u

    def get_user(self, uid):
        return self.storage['user'][uid]

    def auth_user(self, name, password):
        sha1 = hashlib.sha1()
        sha1.update(password)
        enc_password = sha1.hexdigest()

        ret = self.db.run_query('get_user_by_name', (name,))
        if ret['password'] == enc_password:
            u = User(ret['id'], ret['name'])
            self.storage['user'][ret['id']] = u

            return u

        return None


if __name__ == "__main__":
    oi = ObjInterface()

    oi.db.setup_tables()

    oi.create_user('pepe', 'password')

    u1 = oi.load_user_name('pepe')

    u2 = oi.load_user_name('pepe')

    print oi.auth_user('pepe', 'milangas')
    print oi.auth_user('pepe', 'password')

