def apply_armour(fighter: dict) -> dict:
    fighter["protection"] = 0
    for armour in fighter["armour"]:
        fighter["protection"] += armour["protection"]
