# -*- coding: utf-8 -*-

import datetime

from BaseObject import BaseObject


class Match(BaseObject):
    """ Internal status tracking:
        # UNSET = 0,
        SET = 2
        # PLAYING = 3
        FINISHED = 4"""

    def set_up(self, **kwargs):
        self.fixtureId = kwargs.get('fixtureId')
        self.competitionId = kwargs.get('competitionId')
        self.fullDate = kwargs.get('fullDate')
        self.status = 0
        self.homeTeamId = kwargs.get('homeTeamId', 0)
        self.homeTeamScore = None
        self.awayTeamId = kwargs.get('awayTeamId', 0)
        self.awayTeamScore = None

        if self.homeTeamId and self.awayTeamId:
            self.status = 2

    def add_score(self, homeScore = 0, awayScore = 0):
        self.add_score_home(points = homeScore)
        self.add_score_away(points = awayScore)

    def add_score_home(self, points = 0):
        self.homeTeamScore = points

    def add_score_away(self, points = 0):
        self.awayTeamScore = points

    def get_match_data(self):
        return { "homeTeamId" : self.homeTeamId,
                 "homeTeamScore" : self.homeTeamScore,
                 "awayTeamId" : self.awayTeamId,
                 "awayTeamScore" : self.awayTeamScore,
                 "status" : self.status,
                 "fullDate" : self.get_date_string(self.fullDate)
               }

    def get_date(self):
        return self.fullDate

    def get_date_string(self):
        return fullDate.strftime("%Y-%m-%d %H:%M:%S")


