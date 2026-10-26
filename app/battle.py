from typing import Any


def fight(
    first_knight: dict[str, Any],
    second_knight: dict[str, Any],
) -> None:
    """Resolve simultaneous damage and clamp defeated knights to zero HP."""
    first_damage = second_knight["power"] - first_knight["protection"]
    second_damage = first_knight["power"] - second_knight["protection"]

    first_knight["hp"] = max(0, first_knight["hp"] - first_damage)
    second_knight["hp"] = max(0, second_knight["hp"] - second_damage)
