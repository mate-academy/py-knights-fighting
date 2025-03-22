from app.total import Power
from app.globale import KNIGHTS


def battle(knights_config: dict) -> dict:
    def fight(knight1: str, knight2: str) -> None:
        knights_config[knight1]["hp"] -= max(
            0,
            knights_config[knight2]["power"]
            - knights_config[knight1]["protection"]
        )
        knights_config[knight2]["hp"] -= max(
            0,
            knights_config[knight1]["power"]
            - knights_config[knight2]["protection"]
        )

    def tot() -> dict:
        knight_names = list(knights_config.keys())

        for name in knight_names:
            knight_power = Power(
                armour=knights_config[name]["armour"],
                weapon=knights_config[name]["weapon"],
                potion=knights_config[name]["potion"]
            )

            sum_hp, sum_power, sum_protection = knight_power.total_power()

            knights_config[name]["hp"] += sum_hp
            knights_config[name]["power"] += sum_power
            knights_config[name]["protection"] = (
                knights_config[name].get("protection", 0) + sum_protection
            )

        fight(knight_names[0], knight_names[2])
        fight(knight_names[1], knight_names[3])

        return {
            knights_config[name]["name"]: max(0, knights_config[name]["hp"])
            for name in knight_names
        }

    return tot()


print(battle(KNIGHTS))
