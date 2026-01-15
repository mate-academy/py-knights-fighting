# Class initialisation
class Knight:
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


def init_knights(knights: dict) -> list[Knight]:
    result = []
    for knight in knights:
        knight_stats = {
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
                knight_stats["power"] += potion["effect"]["power"]
            if "hp" in potion["effect"]:
                knight_stats["hp"] += potion["effect"]["hp"]
            if "protection" in potion["effect"]:
                knight_stats["protection"] += potion["effect"]["protection"]
        result.append(Knight(**knight_stats))
    return result


# Battle initialisation
def battle_between_knights(pair_of_knights: list[list[Knight]]) -> None:
    for opponents in pair_of_knights:
        opponents[0].hp -= opponents[1].power - opponents[0].protection
        opponents[1].hp -= opponents[0].power - opponents[1].protection
        for opponent in opponents:
            if opponent.hp <= 0:
                opponent.hp = 0


def make_pair(knights: list[Knight]) -> list[list[Knight]]:
    result = [
        [
            knights[index], knights[len(knights) // 2 + index]
        ] for index in range(len(knights) // 2)
    ]
    if len(result) % 2 != 0:
        result.remove(result[-1])
        print("The last participant is eliminated because he has no opponent.")
    return result
