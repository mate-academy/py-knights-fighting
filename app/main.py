from app.members.person import create_knight


def battle(knights_config: dict) -> dict:
    knights = {knight_name: create_knight(knight_info)
               for knight_name, knight_info
               in knights_config.items()}
    knights["lancelot"].battle(knights["mordred"])
    knights["arthur"].battle(knights["red_knight"])
    return {knight.name: knight.hp for knight in knights.values()}
