from typing import Dict
from app.models.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    """
    Executa a batalha entre dois cavaleiros.

    Retorna um dicionário com o hp final de cada cavaleiro.
    """
    knight1.hp -= max(0, knight2.power - knight1.protection)
    knight2.hp -= max(0, knight1.power - knight2.protection)

    return {
        knight1.name: max(knight1.hp, 0),
        knight2.name: max(knight2.hp, 0),
    }
