def apply(potion: str, knight_name: dict) -> None:
    if potion in knight_name["potion"]["effect"]:
        knight_name[potion] += knight_name["potion"]["effect"][potion]


def if_someone_fell(knight: str, data: dict) -> None:
    if data[knight]["hp"] <= 0:
        data[knight]["hp"] = 0


def fight(knight_1: str, knight_2: str, data: dict, attributes: list) -> None:
    data[knight_1][attributes[0]] -= \
        data[knight_2][attributes[1]] - data[knight_1][attributes[2]]

    data[knight_2][attributes[0]] -= \
        data[knight_1][attributes[1]] - data[knight_2][attributes[2]]
