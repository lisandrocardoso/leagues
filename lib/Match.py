# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class Match(BaseObject):
    """ Internal status tracking:
        UNSET = 0,
        SET = 2
        PLAYING = 3
        FINISHED = 4"""

    def set_up(self, **kwargs):
        self.status = 0
        self.team_home = 0
        self.team_away = 0
        self.score_home = 0
        self.score_away = 0
        if kwargs.get('team_home', 0):
            self.add_team_home(kwargs.get('team_home'))
        if kwargs.get('team_away', 0):
            self.add_team_away(kwargs.get('team_away'))

    def add_team_home(self, teamID):
        if not self.team_home:
            self.team_home = teamID
            self.score_home = 0
            self.status += 1
            return True
        else:
            return False

    def add_team_away(self, teamID):
        if not self.team_away:
            self.team_away = teamID
            self.score_away = 0
            self.status += 1
            return True
        else:
            return False

    def start_match(self):
        if self.status == 2:
            self.status += 1
            return True
        else:
            return False

    def end_match(self):
        if self.status == 3:
            self.status += 1
            return True
        else:
            return False

    def add_score_home(self, points=1, memberID=0):
        """ Add member scoring tracking"""
        if self.status == 3:
            self.score_home += points
            return True
        else:
            return False

    def add_score_away(self, points=1, memberID=0):
        """ Add member scoring tracking"""
        if self.status == 3:
            self.score_away += points
            return True
        else:
            return False

    def get_teams(self):
        return (self.team_home, self.team_away)

    def get_score(self):
        if self.status >= 2:
            return (self.score_home, self.score_away)
        else:
            return (0, 0)
