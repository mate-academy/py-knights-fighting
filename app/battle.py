class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict | None,
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare(self) -> None:
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

    def fight_with(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp <= 0:
            self.hp = 0

        if opponent.hp <= 0:
            opponent.hp = 0


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(**knight_data)
        for key, knight_data in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare()

    knights["lancelot"].fight_with(knights["mordred"])
    knights["arthur"].fight_with(knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
