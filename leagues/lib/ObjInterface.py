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

    def generate_draft_fixtures(self, draftId):
        # Load object from DB with ID
        draft = DBInterface.load_draft(draftId)
        
        if not draft.teams:
            return False

        if draft.fixtures:
            return False

        legs = draft.data.get('legs')
#        self.data['current_fixture'] = 0

        teams = draft.teams

        while len(teams):
            (team, teams) = Tools.pick_random(teams, 2)
    

        