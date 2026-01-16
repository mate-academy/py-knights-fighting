def apply(participant: dict) -> dict:
    changed_participant = participant

    changed_participant["protection"] = 0
    for armour in changed_participant["armour"]:
        changed_participant["protection"] += armour["protection"]

    changed_participant["power"] += changed_participant["weapon"]["power"]

    if changed_participant["potion"] is not None:
        for skill in ["power", "protection", "hp"]:
            if skill in changed_participant["potion"]["effect"]:
                changed_participant[skill] += changed_participant["potion"]["effect"][skill]

    return changed_participant
