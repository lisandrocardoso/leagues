# -*- coding: utf-8 -*-


class DBInterface():

    def __init__(self):
        self.queries = {}

        # add_user
        sql = """
        INSERT INTO member(id, name, password) VALUES (NULL, ?, ?)
        """

        # add_member
        sql = """
        INSERT INTO member(id, name, teamID) VALUES (NULL, ?, ?)
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
