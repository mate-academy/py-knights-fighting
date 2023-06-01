class Inventory:
    def __init__(self,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_protection(self) -> int:
        protection = sum([item["protection"] for item in self.armour])
        if self.potion:
            protection += self.potion["effect"].get("protection", 0)
        return protection

    def get_power(self) -> int:
        power = self.weapon["power"]
        if self.potion:
            power += self.potion["effect"]["power"]
        return power

    def get_hp(self) -> int:
        if self.potion:
            return self.potion["effect"]["hp"]
        return 0
