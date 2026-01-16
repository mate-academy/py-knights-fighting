from time import sleep

from app.knights.knights_data import KNIGHTS
from app.knights.knights import Knight


def battle(knights: dict) -> dict:
    battle_participants = []

    print("Welcome to the Kingdom of Camelot "
          "the greatest championship of knights.\n"
          "Today ours participants:")

    for knight in knights.values():
        battle_participants.append(Knight(knight))
        print(knight["name"])
        sleep(0.5)
    print("Let`s congratulate them!!!")
    sleep(1)
    # BATTLE PREPARATIONS:
    print("Knights are preparing for the battle.")

    for knight in battle_participants:
        knight.equip_armour()
        sleep(1)
        knight.equip_weapon()
        sleep(1)
        knight.drink_potion()
        sleep(1)
    print("Knights are ready for the battle.So, let`s get started.")
    # -------------------------------------------------------------------------------
    # BATTLE:
    print(f"The first battle between {battle_participants[0].name} "
          f"and {battle_participants[2].name}.")
    # 1 Lancelot vs Mordred:
    battle_participants[0].knights_battle(battle_participants[2])
    sleep(1)
    # 2 Arthur vs Red Knight:
    print(f"The second battle between {battle_participants[1].name} "
          f"and {battle_participants[3].name}.")
    battle_participants[1].knights_battle(battle_participants[3])
    sleep(1)
    print("Results today battles:")
    # Return battle results:
    result = {
        knight.name: knight.hp for knight in battle_participants
    }
    return result


print(battle(KNIGHTS))
