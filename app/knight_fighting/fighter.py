class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Weapon:
    def __init__(self, name: str, power: int | float) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int | float) -> None:
        self.part = part
        self.protection = protection


class Fighter:
    def __init__(
            self,
            name: str,
            power: int | float,
            hp: int | float,
            armour: list,
            weapon: dict,
            potion: dict,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [
            Armour(
                part=armour_item["part"],
                protection=armour_item["protection"]
            )
            for armour_item in armour
        ]
        self.weapon = Weapon(name=weapon["name"], power=weapon["power"])

        if potion is not None:
            self.potion = Potion(name=potion["name"], effect=potion["effect"])
        else:
            self.potion = None

    def apply_armour(self) -> None:
        self.protection = 0

        for arm in self.armour:
            self.protection += arm.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]

            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]

            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def reset_health_points(self) -> None:
        self.hp = 0
