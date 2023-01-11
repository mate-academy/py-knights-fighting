class ModifiedKnight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def mod_armour(self, armour_list: list) -> int:
        for armor in armour_list:
            self.hp += armor["protection"]

        return self.hp

    def mod_weapon(self, weapon: dict) -> int:
        self.power += weapon["power"]

        return self.power

    def mod_potion(self, potion: dict) -> int:
        if potion is not None:

            if potion["effect"].get("protection"):
                self.hp += potion["effect"]["protection"]

            if potion["effect"]["power"] is not None:
                self.power += potion["effect"]["power"]

            if potion["effect"]["hp"] is not None:
                self.hp += potion["effect"]["hp"]

        return self.power, self.hp
