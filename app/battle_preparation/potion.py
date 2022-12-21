from app.battle_preparation.knights.list_knights import list_knights


def apply_potion(knight_config: dict) -> None:
    for i, knight in enumerate(knight_config):
        if knight == list_knights[i]:
            if knight_config[knight]["potion"] is not None:
                if "power" in knight_config[knight]["potion"]["effect"]:
                    knight_config[knight]["power"] += \
                        knight_config[knight]["potion"]["effect"]["power"]

                if "protection" in knight_config[knight]["potion"]["effect"]:
                    knight_config[knight]["protection"] += \
                        knight_config[knight]["potion"]["effect"]["protection"]

                if "hp" in knight_config[knight]["potion"]["effect"]:
                    knight_config[knight]["hp"] += \
                        knight_config[knight]["potion"]["effect"]["hp"]
