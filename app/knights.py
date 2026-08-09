class Knight:

    # __init__ method creates Knight object,
    # implements basic stats and then applies armour, weapon and potion
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list | None,
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
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    # applies armour
    def apply_armour(self) -> None:
        if self.armour:
            for item in self.armour:
                self.protection += item["protection"]

    # applies weapon
    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    # applies potion
    def apply_potion(self) -> None:
        if self.potion:
            for effect, value in self.potion["effect"].items():
                if effect == "power":
                    self.power += value
                elif effect == "hp":
                    self.hp += value
                elif effect == "protection":
                    self.protection += value

    # here we apply rules how battle between two knights change their hp stats
    @staticmethod
    def battle(knight1: Knight, knight2: Knight) -> None:
        damage_to_1 = max(knight2.power - knight1.protection, 0)
        damage_to_2 = max(knight1.power - knight2.protection, 0)
        knight1.hp = max(knight1.hp - damage_to_1, 0)
        knight2.hp = max(knight2.hp - damage_to_2, 0)

    # here we create dict with knights' names and hp stats
    # to return it as our result
    @staticmethod
    def battle_result(knights_dict: dict) -> dict:
        result_dict = {}
        for knight in knights_dict.values():
            result_dict[knight.name] = knight.hp
        return result_dict
