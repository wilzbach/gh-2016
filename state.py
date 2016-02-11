# -*- coding: utf-8 -*-


class State:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def next_free_drone():
        return 0
