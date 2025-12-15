"""
this module create heroes stats objects
"""


class Stats:
    def __init__(self, name, protection, power, hp):
        self.name = name
        self.protection = protection
        self.power = power
        self.hp = hp

    def battle(self):
        return self
