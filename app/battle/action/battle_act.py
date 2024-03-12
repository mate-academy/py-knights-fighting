from typing import Tuple

class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp

    def receive_attack(self, attack_power: int) -> None:
        self.hp -= attack_power

    def is_alive(self) -> bool:
        return self.hp > 0


def conduct_battle(knight1: Knight, knight2: Knight) -> Tuple[str, int]:
    while knight1.is_alive() and knight2.is_alive():
        knight1.receive_attack(knight2.power)
        knight2.receive_attack(knight1.power)
    
    winner = knight1 if knight1.is_alive() else knight2
    return winner.name, winner.hp


# Example usage
if __name__ == "__main__":
    knight_a = Knight("Arthur", 30, 100)
    knight_b = Knight("Lancelot", 25, 120)

    winner_name, winner_hp = conduct_battle(knight_a, knight_b)
    print(f"The winner is {winner_name} with {winner_hp} HP remaining.")
