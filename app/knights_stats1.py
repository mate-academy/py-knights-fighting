from __future__ import annotations


class TheKnight:
    list_of_knights = []

    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 protection: int
                 ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
        TheKnight.list_of_knights.append(self)

    @staticmethod
    def count_stats(stats: dict) -> list:
        contenders = []
        for knight in stats.values():
            name = knight["name"]
            hp = knight["hp"]
            power = knight["power"] + knight["weapon"]["power"]
            protection = 0
            for armour in knight["armour"]:
                protection += armour["protection"]
            if knight["potion"] is not None:
                eff = knight["potion"]["effect"]
                hp += eff["hp"]
                power += eff["power"]
                if "protection" in eff:
                    protection += eff["protection"]
            contenders.append(TheKnight(name, hp, power, protection))
        return contenders
