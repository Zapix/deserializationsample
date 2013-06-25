# -*- coding: utf-8 -*-


class Point(object):

    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_dict(self):
        '''
        :return: dictionary with values for current object
        :rtype: dict
        '''
        return {
            'x': self.x,
            'y': self.y,
            'z': self.z
        }
