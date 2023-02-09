from __future__ import annotations


class TheKnight:

    @staticmethod
    def stats(stats: dict) -> list:
        list_of_knights = []
        for knight in stats.values():
            name = knight["name"]
            hp = knight["hp"]
            power = knight["power"]
            for armour in knight["armour"]:
                protection = armour["protection"]
                if knight["potion"] is not None:
                    eff = knight["potion"]["effect"]
                    hp += eff["hp"]
                    power += eff["power"]
                list_of_knights.append({"name": name,
                                        "hp": hp,
                                        "power": power,
                                        "protection": protection})
        return list_of_knights
