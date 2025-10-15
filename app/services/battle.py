from app.models.knight import Knight


def create_knights(knights_data: dict) -> dict:
    """Cria instâncias de cavaleiros a partir dos dados."""
    knights = {}
    for key, data in knights_data.items():
        knight = Knight(**data)
        knight.apply_equipment()
        knights[key] = knight
    return knights


def battle(knights_data: dict) -> dict:
    """Executa a batalha e retorna o resultado final."""
    knights = create_knights(knights_data)

    # 1. Lancelot vs Mordred
    knights["lancelot"].attack(knights["mordred"])
    knights["mordred"].attack(knights["lancelot"])

    # 2. Arthur vs Red Knight
    knights["arthur"].attack(knights["red_knight"])
    knights["red_knight"].attack(knights["arthur"])

    # Resultado final
    return {k.name: k.hp for k in knights.values()}
