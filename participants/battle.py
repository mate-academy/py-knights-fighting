def after_battle(participant: dict, opposite: dict) -> dict:
    renewed_participant = participant
    renewed_participant["hp"] -= opposite["power"] - renewed_participant["protection"]
    if renewed_participant["hp"] <= 0:
        renewed_participant["hp"] = 0

    return renewed_participant
