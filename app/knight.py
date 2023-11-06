class Knight:
    def __init__(
            self, name: str,
            power: int,
            hp: int,
            weapon: dict,
            potion: dict,
            armour: list = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.protection = sum(a["protection"] for a in armour)

        if potion:
            self.apply_potion(potion)

        self.equip_weapon()

    def apply_potion(self, potion: dict) -> None:
        if "power" in potion["effect"]:
            self.power += potion["effect"]["power"]
        if "protection" in potion["effect"]:
            self.protection += potion["effect"]["protection"]
        if "hp" in potion["effect"]:
            self.hp += potion["effect"]["hp"]

    def equip_weapon(self) -> None:
        self.power += self.weapon["power"]

    def attack(self, other: "Knight") -> None:
        other.hp -= self.power - other.protection
        if other.hp < 0:
            other.hp = 0
