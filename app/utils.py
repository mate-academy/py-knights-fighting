def apply_armor(knight: dict) -> None:
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]


def apply_weapon(knight: dict) -> None:
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        for effect in ("power", "protection", "hp"):
            if effect in knight["potion"]["effect"]:
                knight[effect] += knight["potion"]["effect"][effect]


def make_preparations(*args: dict) -> None:
    for arg in args:
        apply_armor(arg)
        apply_weapon(arg)
        apply_potion(arg)


def make_fight(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]


def check_health(knight1: dict, knight2: dict) -> None:
    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0
