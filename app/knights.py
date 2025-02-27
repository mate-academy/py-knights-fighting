import collections


class Knight:
    def __init__(self, name: str, base_hp: int, base_power: int,
                 armour: int, weapon: collections.Iterable, potion=None) -> None:
        self.name = name
        self.hp = base_hp
        self.power = base_power + weapon["power"]
        self.protection = sum(item["protection"] for item in armour) if armour else 0
        self.weapon = weapon["name"]
        self.potion = potion["name"] if potion else None

        if potion and "effect" in potion:
            self.apply_potion(potion["effect"])

    def apply_potion(self, effect: str) -> None:
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = max(opponent_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)

    def __repr__(self):
        return f"{self.name}(HP: {self.hp}, Power: {self.power}, Protection: {self.protection})"
