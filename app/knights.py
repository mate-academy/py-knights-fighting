class Knight:
    knights = dict()

    def __init__(self, name: str, power: int, hp: int, weapon: dict) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = weapon["name"]
        Knight.knights[name] = self

    def knight_armour(self, armours: list[dict]) -> None:
        for armour in armours:
            self.armour.append(armour["part"])
            self.protection += armour["protection"]

    def knight_potion(self, potion: dict) -> None:
        self.potion = potion["name"]
        for effect, value in potion["effect"].items():
            if effect == "power":
                self.power += value
            elif effect == "hp":
                self.hp += value
            elif effect == "protection":
                self.protection += value
