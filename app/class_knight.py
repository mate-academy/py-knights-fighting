class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def knight_puts_on_armor(self) -> int | None:
        if self.armour == []:
            return
        for element_armor in self.armour:
            self.protection += element_armor["protection"]
        return self.protection

    def knight_takes_weapon(self) -> None:
        self.power += self.weapon["power"]

    def knight_drinks_the_potion(self) -> None:
        if self.potion is not None:
            for attribute, effect_value in self.potion["effect"].items():
                if attribute in ["power", "protection", "hp"]:
                    setattr(
                        self, attribute,
                        getattr(self, attribute) + effect_value
                    )
