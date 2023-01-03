def apply_weapon(fighter: list[dict]) -> None:
    fighter["power"] += fighter["weapon"]["power"]
