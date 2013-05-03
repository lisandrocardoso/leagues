# -*- coding: utf-8 -*-

from Draft import Draft
from Fixture import Fixture
from Match import Match
from Team import Team


class DBInterface():

    def __init__(self):
        self.queries = {}

        # add_user
        sql = """
        INSERT INTO member(id, name, password) VALUES (NULL, ?, ?)
        """
        self.queries['add_user'] = sql

        # add_team
        sql = """
        INSERT INTO team(id, name)
        """


        # get_member_list
        sql = """
        SELECT * FROM member WHERE id in ?
        """
        self.queries['get_member_list'] = {'params': 'memberId_list',
                                           'sql': sql}

        # get_team_list
        sql = """
        SELECT * FROM team WHERE id in ?
        """
        self.queries['get_team_list'] = {'params': 'teamId_list',
                                         'sql': sql}

        # get_fixture_list
        sql = """
        SELECT * FROM fixture WHERE id in ?
         """

    def run_query(self, query_name, **kwargs):
        q = self.queries.get(query_name, None)
        if not q:
            return False

        #get last insert id and return it
        pass

    def load_draft(self, draftId):
        # Load draft data from DB
        return Draft()


    def create_match(self):
        # Insert a new match entry, return last_inserted_id
        # Only for test purposes:
        for i in range (0, 99999):
            yield i
