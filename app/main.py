from app.knights.knights import unformated_knights
from app.battle.knights_creation import creating_knights
from app.battle.battle import battle_fight


def battle(knights_to_format: dict) -> dict:
    knights = creating_knights(knights_to_format)

    battle_fight(knights["lancelot"], knights["mordred"])
    battle_fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.total_hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(unformated_knights))
