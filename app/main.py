from typing import Dict
from app.models.knight import Knight
from app.services.battle import fight
from app.data.knights import KNIGHTS


def battle() -> Dict[str, int]:
    """
    Cria instâncias dos cavaleiros e executa as batalhas definidas.
    Retorna os resultados finais.
    """
    knights: Dict[str, Knight] = {
        key: Knight(**config) for key, config in KNIGHTS.items()
    }

    results: Dict[str, int] = {}

    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for k1, k2 in pairs:
        outcome = fight(knights[k1], knights[k2])
        results.update(outcome)

    return results


if __name__ == "__main__":
    final_results = battle()
    for name, hp in final_results.items():
        print(f"{name}: {hp} HP")
