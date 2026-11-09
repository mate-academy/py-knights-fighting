"""Combat rules for resolving a duel."""

from .knight import Knight


def resolve_duel(first_knight: Knight, second_knight: Knight) -> None:
    """Resolve one simultaneous exchange between two knights."""
    first_knight.receive_attack(second_knight.power)
    second_knight.receive_attack(first_knight.power)
