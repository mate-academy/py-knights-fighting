from app.battle_preparation.knights.list_knights import list_knights


def apply_armour(knight_config: dict) -> None:
    for i, knight in enumerate(knight_config):
        if knight == list_knights[i]:
            knight_config[knight]["protection"] = 0
            for armour in knight_config[knight]["armour"]:
                knight_config[knight]["protection"] += armour["protection"]
