class Armour:

    def __init__(self, name, protection):
        self.name = name
        self.protection = protection

    def __repr__(self):
        return f"{self.name}"
