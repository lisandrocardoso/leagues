# -*- coding: utf-8 -*-

from DBInterface import DBInterface

from Draft import Draft
from Fixture import Fixture
from Match import Match
from Team import Team

import Tools

class ObjInterface():

    def __init__(self):
        super(ObjInterface, self).__init__()

   #def generate_seeded_draft_fixtures
    def generate_random_draft_fixtures(self, draftId):
        # Load object from DB with ID
        draft = DBInterface.load_draft(draftId)

        if not draft.teams:
            return False

        if draft.fixtures:
            return False

        fixtures = {}

        for i in range(0, draft.data.get('legs')):

#        self.data['current_fixture'] = 0

        result_teams = draft.teams

        while len(result_teams):
            (picked_teams, result_teams) = Tools.pick_random(teams, 2)
            if len(picked_teams) == 1:
                unmatched_team = picked_teams[0]
            else:
                matchId = DBInterface.create_match()


