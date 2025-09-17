from typing import Dict
from app.models.knight import Knight

def fight(
        knight1: Knight,
        knight2: Knight
) -> Dict[str, int]:
    """
    Executa uma rodada de batalha entre dois cavaleiros.
    Atualiza os hp dos objetos Knight e retorna o resultado.
    """
    damage_to_knight1: int = max(0, knight2.power - knight1.protection)
    damage_to_knight2: int = max(0, knight1.power - knight2.protection)

    knight1.hp = max(knight1.hp - damage_to_knight1, 0)
    knight2.hp = max(knight2.hp - damage_to_knight2, 0)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
