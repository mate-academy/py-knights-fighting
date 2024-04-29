from app.variables.variables_knIghts import KNIGHTS


def apply_armor_and_weapon(knight: dict) -> None:
    knight["protection"] = sum(armor["protection"]
                               for armor in knight["armour"])
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"]:
        for effect, value in knight["potion"]["effect"].items():
            if effect in knight:
                knight[effect] += value


def battle(knights_c: dict) -> dict:
    for knight in knights_c.values():
        apply_armor_and_weapon(knight)
        apply_potion(knight)
    for attacker, defender in [("lancelot", "mordred"),
                               ("arthur", "red_knight")]:
        knights_c[attacker]["hp"] -= (knights_c[defender]["power"]
                                      - knights_c[attacker]["protection"])
        knights_c[defender]["hp"] -= (knights_c[attacker]["power"]
                                      - knights_c[defender]["protection"])

        for knight in [attacker, defender]:
            if knights_c[knight]["hp"] <= 0:
                knights_c[knight]["hp"] = 0

    return {knight["name"]: knight["hp"] for knight in knights_c.values()}


print(battle(KNIGHTS))
