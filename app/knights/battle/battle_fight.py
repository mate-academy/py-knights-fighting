from app.knights.knights_config import KNIGHTS


def fighting_function(knights_ready: dict) -> None:
    lancelot_hp = knights_ready["lancelot"].hp - (
            knights_ready["mordred"].power
            - knights_ready["lancelot"].armour)
    KNIGHTS["lancelot"]["hp"] = 0 if lancelot_hp < 0 else lancelot_hp

    mordred_hp = knights_ready["mordred"].hp - (
            knights_ready["lancelot"].power
            - knights_ready["mordred"].armour)
    KNIGHTS["mordred"]["hp"] = 0 if mordred_hp < 0 else mordred_hp

    arthur_hp = knights_ready["arthur"].hp - (
            knights_ready["red_knight"].power
            - knights_ready["arthur"].armour)
    KNIGHTS["arthur"]["hp"] = 0 if arthur_hp < 0 else arthur_hp

    red_knight_hp = knights_ready["red_knight"].hp - (
            knights_ready["arthur"].power
            - knights_ready["red_knight"].armour)
    KNIGHTS["red_knight"]["hp"] = 0 if red_knight_hp < 0 else red_knight_hp
