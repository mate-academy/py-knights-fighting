from app.types.knight_type import KnightType


class Knight:
    def __init__(self, knight: KnightType, protection: int) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.power = knight["power"]
        self.potion = knight["potion"]
        self.protection = protection

    def apply_armor(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()
