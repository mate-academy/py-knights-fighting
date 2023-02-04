from typing import List

from app.players.knight import Knight
from app.setup_game.setup_knights import KnightSetup


def battle_setup(knight_config: dict) -> List[Knight]:
    knights_instances_list: List[Knight] = []

    def knights_instances(knights: dict) -> None:
        for knight in knights.keys():
            knight_instance = KnightSetup.get_knight_instance(
                knights[knight]["name"],
                knights[knight]
            )
            knights_instances_list.append(knight_instance)

    knights_instances(knight_config)

    for knight in knights_instances_list:
        knight.apply_weapon_power()
        knight.apply_potion()
        knight.apply_protection()

    return knights_instances_list


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights: List[Knight] = battle_setup(knight_config=knights)

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    knights[0].fight_knight(knights[2])
    knights[2].fight_knight(knights[0])
    # # 2 Arthur vs Red Knight:
    knights[1].fight_knight(knights[3])
    knights[3].fight_knight(knights[1])
    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp,
    }
