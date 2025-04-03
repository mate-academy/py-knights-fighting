from typing import Any


def display_knight_stats(knight: Any) -> None:
    print(f"Knight: {knight.name}")
    print(f"HP: {knight.get_hp()}")
    print(f"Power: {knight.get_power()}")
    print(f"Protection: {knight.get_protection()}")
    print("-" * 20)
