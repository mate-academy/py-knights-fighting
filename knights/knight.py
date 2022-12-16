class Knight:
    def __init__(self, name: str, power: int, hp: int) -> callable:
        self.name = name
        self.power = power
        self.hp = hp

    def using_armour(self, armour: list, weapon_power: int) -> callable:
        self.power += weapon_power
        if len(armour) > 0:
            for part in armour:
                self.hp += part["protection"]
        return self.hp, self.power

    def using_potion(self, potion: dict) -> callable:
        if potion is not None:
            if potion["effect"].get("protection"):
                self.hp += potion["effect"]["protection"]
            if potion["effect"]["power"] is not None:
                self.power += potion["effect"]["power"]
            if potion["effect"]["hp"] is not None:
                self.hp += potion["effect"]["hp"]
        return self.hp, self.power
