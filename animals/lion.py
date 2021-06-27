"""A lion."""

import animal

class Lion(anima.Animal):

    def __init__(self):
        self.kind = 'lion'

    def get_kind(self):
        return self.kind
