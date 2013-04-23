# -*- coding: utf-8 -*-


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
