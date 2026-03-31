class Armour:
    def __init__(self, armor: list) -> None:
        self.armor = armor

    def use_armor(self, knight) -> None:
        knight.protection += sum(thing['protection'] for thing in self.armor)
