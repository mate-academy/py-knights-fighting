from typing import Dict
from app.models.knight import Knight
from app.services.battle import fight


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    """
    Cria instâncias dos cavaleiros a partir de knights_config
    e executa as batalhas definidas.
    Retorna os resultados finais.
    """
    # Cria todas as instâncias de cavaleiros (DRY)
    knights: Dict[str, Knight] = {
        key: Knight(**config) for key, config in knights_config.items()
    }

    results: Dict[str, int] = {}

    # Pares de batalhas fixos
    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    # Executa batalhas com loop
    for k1, k2 in pairs:
        outcome = fight(knights[k1], knights[k2])
        results.update(outcome)

    return results


if __name__ == "__main__":
    # exemplo manual (não roda nos testes)
    from app.data.knights import KNIGHTS

    final_results = battle(KNIGHTS)
    for name, hp in final_results.items():
        print(f"{name}: {hp} HP")
