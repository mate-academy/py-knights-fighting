from typing import Any


class Battle:
    def __init__(self, knight1: Any, knight2: Any) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def perform_battle(self) -> None:
        print("Fight!")
        print(f"{self.knight1.name} against {self.knight2.name}")

        damage_knight1 = max(self.knight1.power - self.knight2.defense, 0)
        damage_knight2 = max(self.knight2.power - self.knight1.defense, 0)

        self.knight1.hp -= damage_knight2
        self.knight2.hp -= damage_knight1

        print(f"{self.knight1.name} has {self.knight1.hp} life")
        print(f"{self.knight2.name} has {self.knight2.hp} life")

        if self.knight1.hp <= 0:
            print(f"{self.knight2.name} wins!")
        elif self.knight2.hp <= 0:
            print(f"{self.knight1.name} wins!")
        else:
            print("The battle continues!")
