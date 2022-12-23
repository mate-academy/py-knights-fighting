from app.knights_dict import LIST_KNIGHT


def apply_weapon(knight_config: dict) -> None:
    for i, knight in enumerate(knight_config):
        if knight == LIST_KNIGHT[i]:
            knight_config[knight]["power"] += \
                knight_config[knight]["weapon"]["power"]
