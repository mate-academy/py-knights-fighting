from app.participants.Config import KNIGHTS
from app.participants.Knight import Knight
from app.Battle import fight


def participants_invite(name: dict) -> Knight:

    return Knight(name["name"], name["power"],
                  name["hp"], name["armour"],
                  name["weapon"], name["potion"])


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = participants_invite(knightsConfig["lancelot"])
    # apply armour
    lancelot.get_ready()

    # arthur
    arthur = participants_invite(knightsConfig["arthur"])
    #  apply armour
    arthur.get_ready()

    # # mordred
    mordred = participants_invite(knightsConfig["mordred"])
    #  apply armour
    mordred.get_ready()

    # # red_knight
    red_knight = participants_invite(knightsConfig["red_knight"])
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
