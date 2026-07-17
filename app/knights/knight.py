class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armor: list,
                 weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.protection = self.calculate_protection()
        self.potion_effect()

    def calculate_protection(self) -> int:
        protection = 0
        for item in self.armor:
            protection += item["protection"]
        return protection

    def damage(self) -> int:
        return self.power + self.weapon["power"]

    def potion_effect(self) -> None:
        if self.potion:
            for attribute, effect in self.potion["effect"].items():
                if attribute == "hp":
                    self.hp += effect
                elif attribute == "power":
                    self.power += effect
                elif attribute == "protection":
                    self.protection += effect

    def stats(self) -> dict:
        return {
            "power": self.damage(),
            "hp": self.hp,
            "protection": self.protection,
        }
