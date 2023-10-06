class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:

        self.name = name
        self.potion = potion
        self.hp = hp
        self.power = power
        self.weapon = weapon
        self.protection = 0
        self.armour = armour

    def apply_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_armour(self) -> None:
        self.protection += sum(arm["protection"] for arm in self.armour)


def creation_of_knight_instances(knight_dict: dict) -> dict:
    knights_instances = {}
    for knight_name, knight_data in knight_dict.items():
        knight = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armour=knight_data["armour"],
            weapon=knight_data["weapon"],
            potion=knight_data["potion"]
        )
        knights_instances[knight_name] = knight

    return knights_instances
