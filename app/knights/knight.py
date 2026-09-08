class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def arm_knight(self) -> Knight:
        power = self.power
        health = self.hp
        defence = 0

        if self.armour:
            for piece in self.armour:
                defence += piece["protection"]

        power += self.weapon["power"]

        if self.potion:

            potion_effect = self.potion.get("effect", {})

            additional_hp = potion_effect.get("hp", 0)
            additional_power = potion_effect.get("power", 0)
            additional_protection = potion_effect.get("protection", 0)

            if additional_hp :
                health += additional_hp
            if additional_protection:
                defence += additional_protection
            if additional_power:
                power += additional_power

        armed_knight = Knight(self.name, power, health,
                              self.armour, self.weapon, self.potion)
        armed_knight.protection = defence
        return armed_knight


def create_knight(knight_config: dict) -> dict:

    return {name: Knight(knight["name"], knight["power"], knight["hp"],
                         knight["armour"], knight["weapon"], knight["potion"])
            for name, knight in knight_config.items()}
