class Armour:
    def __init__(self, armour: list[dict]) -> None:
        self.armour = armour
        self.parts = [part["part"] for part in armour]

    def put_on(self, knight: object) -> None:
        knight.protection += sum(part["protection"] for part in self.armour)


class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon["name"]
        self.power = weapon["power"]

    def take(self, knight: object) -> None:
        knight.power += self.power


class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = potion["name"]
        self.effect = potion["effect"]

    def drink(self, knight: object) -> None:
        knight.power += self.effect.get("power", 0)
        knight.hp += self.effect.get("hp", 0)
        knight.protection += self.effect.get("protection", 0)
