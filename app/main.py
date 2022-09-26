from app.fighters.knights_сonfig import KNIGHTS
from app.fighters.сharacters import Knight
from app.battle_rules import fight


def participants_invite(name: dict) -> Knight:

    return Knight(name["name"], name["power"],
                  name["hp"], name["armour"],
                  name["weapon"], name["potion"])


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = participants_invite(knights_config["lancelot"])
    # apply armour
    lancelot.get_ready()

    # arthur
    arthur = participants_invite(knights_config["arthur"])
    #  apply armour
    arthur.get_ready()

    # # mordred
    mordred = participants_invite(knights_config["mordred"])
    #  apply armour
    mordred.get_ready()

    # # red_knight
    red_knight = participants_invite(knights_config["red_knight"])
    #  apply armour
    red_knight.get_ready()

    # ---------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
