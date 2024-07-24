def apply_skills(participants: dict, participating_knights: dict) -> None:
    for nickname in participating_knights:
        knight = participating_knights[nickname]
        if participants[nickname]["armour"]:
            knight.apply_armour(participants[nickname]["armour"])
        knight.apply_weapon(participants[nickname]["weapon"])
        if participants[nickname]["potion"]:
            knight.apply_potion(participants[nickname]["potion"]["effect"])
