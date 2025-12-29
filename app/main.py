from app.knight import Knight

def battle(knights_config: dict) -> dict:
    # 1. Criação dinâmica (DRY): cria um objeto Knight para cada chave no dicionário
    knights = {
        name: Knight(config) 
        for name, config in knights_config.items()
    }

    # 2. Executar as batalhas usando as instâncias do dicionário
    # Lancelot vs Mordred
    knights["lancelot"].receive_damage(knights["mordred"].power)
    knights["mordred"].receive_damage(knights["lancelot"].power)

    # Arthur vs Red Knight
    knights["arthur"].receive_damage(knights["red_knight"].power)
    knights["red_knight"].receive_damage(knights["arthur"].power)

    # 3. Retornar os HPs finais em um dicionário
    return {
        knight.name: knight.hp 
        for knight in knights.values()
    }
