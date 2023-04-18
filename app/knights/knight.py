class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armor: list[dict],
                 weapon: dict,
                 potion: dict[dict]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.apply_armor(armor)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def apply_armor(self, armor: list[dict]) -> list[dict]:
        self.protection += sum(part.get("protection") for part in armor)
        return armor

    def apply_weapon(self, weapon: dict) -> dict:
        self.power += weapon.get("power")
        return weapon

    def apply_potion(self, potion: dict[dict]) -> dict[dict]:
        if potion is not None and "effect" in potion:
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            elif "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            elif "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]
        return potion
