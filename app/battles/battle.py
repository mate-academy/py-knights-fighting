from app.knights.knight_configs.config_tools import create_knights_from_config
from app.knights.knights import Knight


def get_battle_pairs(knights_config: dict) -> list:
    names = [value["name"] for value in knights_config.values()]
    if len(names) % 2 != 0:
        raise ValueError("Need even number of knights for battle.")
    pairs = []
    half = len(names) // 2
    for i in range(half):
        pairs.append((names[i], names[i + half]))
    return pairs


def find_knight(name: str) -> Knight:
    for knight in Knight.knights:
        if knight.name == name:
            return knight
    raise ValueError(f"Knight with name '{name}' not found!")


def battle(knights_config: dict) -> dict:
    create_knights_from_config(knights_config)
    for knight in Knight.knights:
        knight.prepare()
    battle_pairs = get_battle_pairs(knights_config)

    for knight1, knight2 in battle_pairs:
        find_knight(knight1).attack(find_knight(knight2))
        find_knight(knight2).attack(find_knight(knight1))

    return {knight.name: knight.hp for knight in Knight.knights}
