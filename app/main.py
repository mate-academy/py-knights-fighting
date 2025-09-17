from typing import Dict
from app.data.knights import KNIGHTS
from app.models.knight import Knight
from app.services.battle import fight


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    """
    Executa as batalhas pré-definidas do torneio.

    Retorna um dicionário com o hp final de cada cavaleiro.
    """
    lancelot = Knight(**knights_config["lancelot"])
    mordred = Knight(**knights_config["mordred"])
    arthur = Knight(**knights_config["arthur"])
    red_knight = Knight(**knights_config["red_knight"])

    results: Dict[str, int] = {}
    results.update(fight(lancelot, mordred))
    results.update(fight(arthur, red_knight))

    return results


if __name__ == "__main__":
    final_results = battle(KNIGHTS)
    for name, hp in final_results.items():
        print(f"{name}: {hp} HP")
