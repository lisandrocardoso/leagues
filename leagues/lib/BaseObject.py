# -*- coding: utf-8 -*-


class BaseObject(object):

    def __init__(self, ID=-1, name="NoName", **kwargs):
        self.name = name
        self.ID = ID
        self.data = {}

        self.set_up(**kwargs)

    def set_up(self, args):
        pass

    def get_name(self):
        return self.name

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def has_ID(self, ID):
        if (ID == self.ID):
            return True
        else:
            return False

    def set_data(self, data, value):
        if data in self.data:
            self.data[data] = value

    def get_data(self):
        return self.data

