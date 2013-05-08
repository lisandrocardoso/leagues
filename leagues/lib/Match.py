# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class Match(BaseObject):
    def set_up(self, **kwargs):
        self.home_id = kwargs.get('home_id')
        self.away_id = kwargs.get('away_id')
        self.data = {}
        self.data['score'] = {'home': 0,
                              'away': 0}
        self.data['winner'] = 0
        self.data['home_win'] = False
        self.data['away_win'] = False
        self.data['drawn'] = True
        self.data['played'] = False
        self.data['point_diff'] = 0

    def add_team_home(self, teamId):
        self.home_id = teamId

    def add_team_away(self, teamId):
        self.away_id = teamId

    def add_score(self, home=0, away=0):
        self.data['score']['home'] += home
        self.data['score']['away'] += away

    def set_score(self, home, away):
        self.data['score']['home'] = home
        self.data['score']['away'] = away

    def end_match(self):
        self.data['played'] = True

        if self.data['score']['home'] > self.data['score']['away']:
            self.data['winner'] = self.home_id
            self.data['home_win'] = True
            self.data['away_win'] = self.data['drawn'] = False
            self.data['point_diff'] = (self.data['score']['home'] -
                                       self.data['score']['away'])
        elif self.data['score']['home'] < self.data['score']['away']:
            self.data['winner'] = self.away_id
            self.data['away_win'] = True
            self.data['home_win'] = self.data['drawn'] = False
            self.data['point_diff'] = (self.data['score']['away'] -
                                       self.data['score']['home'])
        else:
            self.data['winner'] = 0
            self.data['away_win'] = self.data['home_win'] = False
            self.data['drawn'] = True
            self.data['point_diff'] = 0

    def get_teams(self):
        return (self.home_id, self.away_id)

    def get_data(self):
        return self.data

