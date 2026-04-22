def apply_armour(knights_data: dict) -> None:
    for skills in knights_data.values():
        skills["protection"] = 0
        for armour in skills["armour"]:
            skills["protection"] += armour["protection"]
