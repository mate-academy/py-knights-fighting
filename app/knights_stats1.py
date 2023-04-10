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
            name = knight.get("name")
            hp = knight.get("hp")
            power = 0
            if knight["weapon"] is not None:
                weapon = knight["weapon"]
                power = knight.get("power") + weapon.get("power")
            protection = 0
            for armour in knight.get("armour"):
                protection += armour.get("protection")
            if knight["potion"] is not None:
                eff = knight["potion"]["effect"]
                hp += eff.get("hp")
                power += eff.get("power")
                if "protection" in eff:
                    protection += eff.get("protection")
            contenders.append(TheKnight(name, hp, power, protection))
        return contenders
