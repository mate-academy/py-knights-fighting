class Fighters(object):
    def __init__(self, fighter: dict) -> None:
        for key in fighter:
            setattr(self, key, fighter[key])
        self.protection = 0
