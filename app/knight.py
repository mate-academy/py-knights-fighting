class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:

        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def equip(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:

            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def attack(self, defender: "Knight") -> None:
        incoming_damage = max(0, self.power - defender.protection)
        defender.hp = max(0, defender.hp - incoming_damage)


def prepare_knights(config: dict) -> dict:
    knights = {}

    for knight_key, knight_data in config.items():
        knights[knight_key] = Knight(
            name=knight_data["name"],
            hp=knight_data["hp"],
            power=knight_data["power"],
            armour=knight_data["armour"],
            weapon=knight_data["weapon"],
            potion=knight_data["potion"]
        )

    for knight in knights.values():
        knight.equip()
    return knights
