from app.contestants.list_of_contestants import Contestants
from app.contestants.knight import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion
from app.battle.battle_start import Battle


def battle(knights_list: dict) -> dict:

    list_of_knights = {}

    # KNIGHTS INITIATION
    for contestant, value in knights_list.items():
        list_of_knights[contestant] = Knight(
            name=value["name"],
            power=value["power"],
            hp=value["hp"],
            armour=value["armour"],
            weapon=value["weapon"],
            potion=value["potion"]
        )

    # BATTLE PREPARATIONS:
    for knight in list_of_knights.values():
        armour = Armour(knight.armour)
        armour.apply_armour(knight)

        weapon = Weapon(knight.weapon["power"])
        weapon.apply_weapon(knight)

        if knight.potion is not None:
            potion = Potion(knight.potion["effect"])
            potion.apply_potion(knight)

    print(list_of_knights["lancelot"].name)

    # BATTLE:
    # 1 Lancelot vs Mordred:
    battle_1 = Battle(list_of_knights["lancelot"], list_of_knights["mordred"])
    battle_1.battle_start()
    battle_1.check_if_fell()

    # 2 Arthur vs Red Knight:
    battle_2 = Battle(list_of_knights["arthur"], list_of_knights["red_knight"])
    battle_2.battle_start()
    battle_2.check_if_fell()

    # Return battle results:
    return {
        list_of_knights[knights].name: list_of_knights[knights].health_points
        for knights in list_of_knights
    }


print(battle(Contestants.KNIGHTS))
