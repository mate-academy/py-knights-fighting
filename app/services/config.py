from app.models.models import Knight


def prepare_models(raw_models: dict) -> list:
    applied_modifier_list = [
        Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data["potion"]
        )
        for knight, data in raw_models.items()
    ]
    for knight in applied_modifier_list:
        knight.apply_modifiers()
    return applied_modifier_list
