class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.total_power = 0

    def apply_armour(self) -> None:
        self.protection = sum(
            armour_element["protection"]
            for armour_element in self.armour
        )

    def apply_weapon(self) -> None:
        self.total_power = self.base_power + self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion["effect"].items():
                match stat:
                    case "hp":
                        self.hp += value
                    case "power":
                        self.total_power += value
                    case "protection":
                        self.protection += value

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def calculate_stats(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
