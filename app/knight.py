class Knight:
    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 protection: int = 0) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def apply_improvements(self, knight: dict) -> None:
        self.protection += \
            sum(part["protection"] for part in knight["armour"])
        self.power += knight["weapon"]["power"]
        if "potion" in knight and knight["potion"] is not None:
            for effect in knight["potion"]["effect"]:
                if effect == "hp":
                    self.hp += knight["potion"]["effect"]["hp"]
                    continue
                if effect == "power":
                    self.power += knight["potion"]["effect"]["power"]
                    continue
                if effect == "protection":
                    self.protection += \
                        knight["potion"]["effect"]["protection"]
                    continue
