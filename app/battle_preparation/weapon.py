from app.battle_preparation.knights.list_knights import list_knights


def apply_weapon(knight_config: dict) -> None:
    for i, knight in enumerate(knight_config):
        if knight == list_knights[i]:
            knight_config[knight]["power"] += \
                knight_config[knight]["weapon"]["power"]
