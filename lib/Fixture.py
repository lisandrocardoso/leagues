# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class Fixture(BaseObject):

    def set_up(self, **kwargs):
        self.dates = {}

    def add_date(self, dateId, dateDate="", dateInfo=""):
        if self.dates.get(dateId, 0):
            return
        self.dates[dateId] = {'matches': [],
                              'dateDate': dateDate,
                              'dateInfo': dateInfo}

    def add_match_to_date(self, dateId, matchId):
        if self.dates.get(dateId, 0):
            if not matchId in self.dates[dateId]['matches']:
                self.dates[dateId]['matches'].append(matchId)

    def get_date(self, dateId):
        if self.dates.get(dateId):
            return self.dates[dateId]
        else:
            return {}
