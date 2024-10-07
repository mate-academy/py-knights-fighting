class KnightsStats:
    def __init__(self, knight: dict) -> None:
        self.knight_dict = knight
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0


def knight_stats(knights) -> dict:
    knights_attr = {}
    for knight, stats in knights.items():
        knights_attr.update({knight: KnightsStats(stats)})
    return knights_attr