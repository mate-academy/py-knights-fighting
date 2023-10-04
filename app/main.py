from app.arenas.camelot import Camelot
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    battle_arena = Camelot()
    [Knight(name=knight["name"],
            hp=knight["hp"],
            power=knight["power"],
            armour=knight["armour"],
            weapon=knight["weapon"],
            potion=knight["potion"])
        for knight in knights_config.values()]

    battle_arena.knight_battle(Knight.knights_for_battle
                               .get("Lancelot")
                               .prepare_for_battle(),
                               Knight.knights_for_battle
                               .get("Mordred")
                               .prepare_for_battle())
    battle_arena.knight_battle(Knight.knights_for_battle
                               .get("Arthur")
                               .prepare_for_battle(),
                               Knight.knights_for_battle
                               .get("Red Knight")
                               .prepare_for_battle())

    return battle_arena.battles_results
