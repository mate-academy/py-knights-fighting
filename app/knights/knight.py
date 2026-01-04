from __future__ import annotations


class Knight:
    def __init__(self, info: dict) -> None:
        self.info = info

    def knight_stats(self) -> dict:
        knight_protection = 0
        knight_power = self.info["power"] + self.info["weapon"]["power"]
        knight_hp = self.info["hp"]
        for armour in self.info["armour"]:
            knight_protection += armour["protection"]
        if self.info["potion"] is not None:
            for effect, value in self.info["potion"]["effect"].items():
                if effect == "power":
                    knight_power += value
                if effect == "protection":
                    knight_protection += value
                if effect == "hp":
                    knight_hp += value
        return dict(
            name=self.info["name"],
            hp=knight_hp,
            power=knight_power,
            protection=knight_protection
        )

    @staticmethod
    def battle(knight1: dict, knight2: dict) -> list:
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]

        if knight1["hp"] <= 0:
            knight1["hp"] = 0
        if knight2["hp"] <= 0:
            knight2["hp"] = 0

        return [knight1, knight2]
