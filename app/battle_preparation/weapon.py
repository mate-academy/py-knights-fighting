
def apply_weapon(knight_config: dict) -> None:
    for knight in knight_config:
        knight_config[knight]["power"] += \
            knight_config[knight]["weapon"]["power"]
