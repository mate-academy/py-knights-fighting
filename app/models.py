class Item:
    def __init__(
            self, name: str, power: int = 0, protection: int = 0, hp: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.protection = protection
        self.hp = hp


class Knight:
    def __init__(
            self, name: str,
            base_power: int,
            base_hp: int,
            armour: int,
            weapon: str,
            potion: int = None
    ) -> None:
        self.name = name
        self.power = base_power + weapon.power
        self.hp = base_hp
        self.protection = sum(a["protection"] for a in armour)
        self.apply_potion(potion)

    def apply_potion(self, potion: int) -> None:
        if not potion:
            return
        self.power += potion["effect"].get("power", 0)
        self.protection += potion["effect"].get("protection", 0)
        self.hp += potion["effect"].get("hp", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = max(opponent_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)
