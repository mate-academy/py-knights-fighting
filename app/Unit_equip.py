from __future__ import annotations


class Knight:
    def __init__(self,
                 knights: dict
                 ) -> None:
        self.name = knights["name"]
        self.power = knights["power"] + knights["weapon"].get("power")
        self.hp = knights["hp"]
        self.protection = sum([protec["protection"]
                               for protec in knights["armour"]])
        self.potion = knights["potion"]

        if knights["potion"] is not None:
            self.power += knights["potion"].get("effect").get("power", 0)
            self.hp += knights["potion"].get("effect").get("hp", 0)
            self.protection += knights["potion"].get("effect").get(
                "protection", 0
            )

    @staticmethod
    def duel(knight1: Knight, knight2: Knight) -> dict:

        shot1 = knight1.power - knight2.protection
        shot2 = knight2.power - knight1.protection
        knight1.hp -= shot2
        knight2.hp -= shot1

        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0
        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        }
