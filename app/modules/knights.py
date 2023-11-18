from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def make_knight(knight: dict) -> Knight:

        name = knight["name"]
        power = knight["power"]
        hp = knight["hp"]
        protection = 0

        if knight["armour"]:
            for armour in knight["armour"]:
                protection += armour["protection"]

        power += knight["weapon"]["power"]

        if knight["potion"]:
            effect_from_potion = knight["potion"]["effect"]

            if "protection" in effect_from_potion:
                protection += effect_from_potion["protection"]

            if "power" in effect_from_potion:
                power += effect_from_potion["power"]

            if "hp" in effect_from_potion:
                hp += effect_from_potion["hp"]

        return Knight(name, power, hp, protection)

    def fight(self: Knight, opponent: Knight) -> None:

        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)
