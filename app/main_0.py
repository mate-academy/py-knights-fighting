from app.total import Power
from app.main import KNIGHTS


def fight(knight1: str, knight2: str) -> None:
    KNIGHTS[knight1]["hp"] -= max(0, KNIGHTS[knight2]["power"]
                                  - KNIGHTS[knight1]["protection"])
    KNIGHTS[knight2]["hp"] -= max(0, KNIGHTS[knight1]["power"]
                                  - KNIGHTS[knight2]["protection"])


def tot() -> dict:

    knights_name = list(KNIGHTS.keys())

    for name in knights_name:

        knight_power = Power(
            armour=KNIGHTS[name]["armour"],
            weapon=KNIGHTS[name]["weapon"],
            potion=KNIGHTS[name]["potion"])

        sum_hp, sum_power, sum_protection = knight_power.total_power()

        KNIGHTS[name]["hp"] += sum_hp
        KNIGHTS[name]["power"] += sum_power
        KNIGHTS[name]["protection"] = (
            KNIGHTS[name].get("protection", 0) + sum_protection
        )

    fight(knights_name[0], knights_name[2])
    fight(knights_name[1], knights_name[3])

    return {name: max(0, KNIGHTS[name]["hp"]) for name in knights_name}


print(tot())
