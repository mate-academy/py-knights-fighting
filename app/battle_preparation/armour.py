from app.knights_dict import LIST_KNIGHT


def apply_armour(knight_config: dict) -> None:
    for i, knight in enumerate(knight_config):
        if knight == LIST_KNIGHT[i]:
            knight_config[knight]["protection"] = 0
            for armour in knight_config[knight]["armour"]:
                knight_config[knight]["protection"] += armour["protection"]
