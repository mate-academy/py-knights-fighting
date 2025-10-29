from typing import Dict, Any, TYPE_CHECKING


if TYPE_CHECKING:
    from app.barracks.knight_preparation import Knight


def apply_equipment(knight: "Knight") -> None:
    """Apply armour and weapon bonuses to the knight."""
    knight.protection = sum(item["protection"] for item in knight.armour)
    knight.power = knight.base_power + knight.weapon["power"]


def apply_potion(knight: "Knight") -> None:
    """Apply potion effects to the knight, if any."""
    if knight.potion is None:
        return

    effect: Dict[str, Any] = knight.potion.get("effect", {})
    knight.hp += effect.get("hp", 0)
    knight.power += effect.get("power", 0)
    knight.protection += effect.get("protection", 0)
