class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def sum_protection(self) -> int:
        protection = 0
        for item in self.armour:
            protection += item.get("protection", 0)
        if self.potion is not None:
            protection += self.potion.get("effect", {}).get("protection", 0)
        return protection

    def sum_power(self) -> int:
        total_power = self.power + self.weapon.get("power")
        if self.potion is not None:
            total_power += self.potion.get("effect", {}).get("power", 0)
        return total_power

    def sum_hp(self) -> int:
        total_hp = self.hp
        if self.potion is not None:
            total_hp += self.potion.get("effect", {}).get("hp", 0)
        return total_hp

    def stats(self) -> dict:
        return {
            "hp" : self.sum_hp(), "power" : self.sum_power(),
            "protection" : self.sum_protection()
        }
