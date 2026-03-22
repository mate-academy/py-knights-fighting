from app.warrior.stats import Stats


class Armour:
    def __init__(self, armour_list: list[dict]) -> None:
        self.armour_list = []
        self.stats = Stats()
        for armour in armour_list:
            self.armour_list.append(armour.get("part"))
            self.stats.protection += armour.get("protection")
