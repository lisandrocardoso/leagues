# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class Team(BaseObject):

    def set_up(self, **kwargs):
        # ownerID = userID
        self.userID = kwargs.get(['userID'], None)