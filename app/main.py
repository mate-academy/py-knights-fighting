from app.config.knight import Knight
from app.config.battlekit import BattleKit


def battle(knights_config: dict) -> dict:
    """
    Simulates a battle between pairs of knights
    based on the given configuration

    Args:
        knights_config (dict):
            A dictionary containing knight configurations.

    Returns:
        dict:
            A dictionary with battle results.
    """

    # BATTLE PREPARATIONS:
    knights = []

    # Create knight instances and equip them with battle kits
    for knight in knights_config.values():
        knight_instance = Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"]
        )

        knight_battle_kit = BattleKit(
            weapon=knight["weapon"],
            armour=knight["armour"],
            potion=knight["potion"]
        )

        # Equip the knight with the battle kit
        knight_instance.equip(knight_battle_kit)
        knights.append(knight_instance)

    # -------------------------------------------------------------------------------
    # BATTLE:
    battle_results = {}

    # Divide the knights into pairs for battle
    knights_half = len(knights) // 2

    for index in range(knights_half):
        # Perform battle between two knights and update battle results
        battle_results.update(
            knights[index].battle(knights[index + knights_half])
        )

    return battle_results
