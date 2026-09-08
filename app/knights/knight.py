from app.knights import knights_list

class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: dict, potion: dict | None):
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
            self.potion.get("effect")
            additional_hp = self.potion.get("effect").get("hp")
            additional_power = self.potion.get("effect").get("power")
            additional_protection = self.potion.get("effect").get("protection")

            if additional_hp :
                health += additional_hp
            if additional_protection:
                defence += additional_protection
            if additional_power:
                power += additional_power

        armed_knight = Knight(self.name,power,health,self.armour,self.weapon,self.potion)
        armed_knight.protection = defence
        return armed_knight

def create_knight(knight_config):

    return {name: Knight(knight["name"], knight["power"], knight["hp"],
                            knight["armour"], knight["weapon"], knight["potion"])
               for name, knight in knights_list.KNIGHTS.items()}



