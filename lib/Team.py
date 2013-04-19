# -*- coding: utf-8 -*-

from BaseObject import BaseObject


class Team(BaseObject):

    def set_up(self, **kwargs):
        self.members = []

    def add_member(self, memberID):
        self.members.append(memberID)

    def del_member(self, memberID):
        self.members.remove(memberID)

    def get_members(self):
        return self.members
