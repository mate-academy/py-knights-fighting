def apply(participant: dict) -> dict:
    changed_participant = participant

    changed_participant["protection"] = 0
    for a in changed_participant["armour"]:
        changed_participant["protection"] += a["protection"]

    # apply weapon
    changed_participant["power"] += changed_participant["weapon"]["power"]

    # apply potion if exist
    if changed_participant["potion"] is not None:
        if "power" in changed_participant["potion"]["effect"]:
            changed_participant["power"] += changed_participant["potion"]["effect"]["power"]

        if "protection" in changed_participant["potion"]["effect"]:
            changed_participant["protection"] += changed_participant["potion"]["effect"]["protection"]

        if "hp" in changed_participant["potion"]["effect"]:
            changed_participant["hp"] += changed_participant["potion"]["effect"]["hp"]

    return changed_participant
