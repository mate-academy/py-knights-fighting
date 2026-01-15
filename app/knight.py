class Knight:

    def __init__(self, stats: dict) -> None:
        self.name = stats.get("name")
        self.power = stats.get("power")
        self.hp = stats.get("hp")
        self.protection = 0
        self.put_armour(stats.get("armour"))
        self.take_weapon(stats.get("weapon"))
        self.drink_potion(stats.get("potion"))

    def put_armour(self, armour: list | None) -> None:
        if armour is not None:
            for item in armour:
                self.protection += item.get("protection", 0)

    def take_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power")

    def drink_potion(self, potion: dict | None) -> None:
        if potion is not None:
            effect = potion.get("effect")
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)
