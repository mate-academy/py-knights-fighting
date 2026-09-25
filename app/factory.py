"""Build Knight objects out of the raw KNIGHTS configuration."""

from app.models import Armour, Knight, Potion, Weapon


def build_knight(data: dict) -> Knight:
    """Create one Knight instance from a dict of raw stats."""
    armour = [Armour(a["part"], a["protection"]) for a in data["armour"]]
    weapon = Weapon(data["weapon"]["name"], data["weapon"]["power"])

    potion = None
    if data["potion"] is not None:
        potion = Potion(data["potion"]["name"], data["potion"]["effect"])

    return Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def build_knights(config: dict) -> dict:
    """Create a dict of Knight instances from the raw KNIGHTS config."""
    return {key: build_knight(value) for key, value in config.items()}
