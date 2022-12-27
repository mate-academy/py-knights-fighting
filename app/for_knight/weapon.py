def apply_weapon(fighter: dict) -> dict:
    fighter["power"] += fighter["weapon"]["power"]
