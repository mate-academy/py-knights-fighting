class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def is_armour(self, armour: list) -> int:
        for part in armour:
            self.hp += part["protection"]
        return self.hp

    def is_weapon(self, weapon_power: int) -> int:
        self.power += weapon_power
        return self.power

    def is_potion(self, potion: dict) -> callable:
        if potion:
            if potion["effect"].get("protection"):
                self.hp += potion["effect"]["protection"]
            if potion["effect"]["power"]:
                self.power += potion["effect"]["power"]
            if potion["effect"]["hp"]:
                self.hp += potion["effect"]["hp"]
        return self.hp, self.power
