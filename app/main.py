from typing import Dict, List, Tuple
from battle.preparation.knight_preparation import prepare_knight
from battle.action.battle_act import simulate_battle
from battle.action.battle_results import aggregate_results
from battle.knight import KNIGHTS

def main() -> None:
    # Prepare knights for battle
    prepared_knights: Dict[str, dict] = {
        k: prepare_knight(v) for k, v in KNIGHTS.items()
    }

    # Define battle pairs
    battle_pairs: List[Tuple[str, str]] = [
        ('lancelot', 'mordred'),
        ('arthur', 'red_knight'),
    ]

    # Simulate battles and collect outcomes
    battle_outcomes: List[dict] = []
    for knight1, knight2 in battle_pairs:
        result: dict = simulate_battle(prepared_knights[knight1], 
                                       prepared_knights[knight2])
        battle_outcomes.append(result)

    # Aggregate and display results
    final_results: Dict[str, dict] = aggregate_results(battle_outcomes)
    for knight, result in final_results.items():
        print(f"{knight}: {result}")

if __name__ == "__main__":
    main()
