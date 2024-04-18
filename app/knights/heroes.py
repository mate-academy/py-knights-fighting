class Hero:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


def init_hero(knights: dict) -> list[Hero]:
    result = []
    for knight in knights:
        heroes = {
            "name": knights[knight]["name"],
            "power": (knights[knight]["power"]
                      + knights[knight]["weapon"]["power"]),
            "hp": knights[knight]["hp"],
            "protection": sum(
                armours["protection"] for armours in knights[knight]["armour"]
            )
        }
        potion = knights[knight]["potion"]
        if potion:
            if "power" in potion["effect"]:
                heroes["power"] += potion["effect"]["power"]
            if "hp" in potion["effect"]:
                heroes["hp"] += potion["effect"]["hp"]
            if "protection" in potion["effect"]:
                heroes["protection"] += potion["effect"]["protection"]
        result.append(Hero(**heroes))
    return result
