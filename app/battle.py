"""The tournament battle logic."""

from app.factory import build_knights


def battle(knights_config: dict) -> dict:
    """Run the tournament and return each knight's remaining hp."""
    knights = build_knights(knights_config)

    for knight in knights.values():
        knight.prepare_for_battle()

    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
