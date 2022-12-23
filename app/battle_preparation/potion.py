
def apply_potion(knight_config: dict) -> None:
    for knight in knight_config:
        if knight_config[knight]["potion"] is not None:
            for potion_effect in knight_config[knight]["potion"]["effect"]:
                knight_config[knight][potion_effect] += \
                    knight_config[knight]["potion"]["effect"][potion_effect]
