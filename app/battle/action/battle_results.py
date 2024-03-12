from typing import Dict, List

class KnightResult:
    def __init__(self, name: str, hp_remaining: int) -> None:
        self.name: str = name
        self.hp_remaining: int = hp_remaining

    def display_result(self) -> None:
        print(f"{self.name} has {self.hp_remaining} HP left after the battle.")

def store_results(knights: List[KnightResult]) -> Dict[str, int]:
    results: Dict[str, int] = {}
    for knight in knights:
        results[knight.name] = knight.hp_remaining
    return results

def display_battle_results(results: Dict[str, int]) -> None:
    for name, hp in results.items():
        print(f"{name} ended the battle with {hp} HP.")

# Example usage
if __name__ == "__main__":
    knights_results = [
        KnightResult("Arthur", 50),
        KnightResult("Lancelot", 0),  # Assume Lancelot is defeated
        KnightResult("Gawain", 30),
    ]

    results = store_results(knights_results)
    display_battle_results(results)
