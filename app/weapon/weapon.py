def apply_weapon(knights_data: dict) -> None:
    for skills in knights_data.values():
        skills["power"] += skills["weapon"]["power"]
