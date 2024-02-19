from __future__ import annotations


class Pvp:
    # p1 and p2 is player_1 and player_2
    def __init__(self, p1: dict, p2: dict) -> None:
        self.p1 = p1
        self.p2 = p2

    def fight(self) -> None:
        self.p1["hp"] -= self.p2["power"] - self.p1["protection"]
        self.p2["hp"] -= self.p1["power"] - self.p2["protection"]

    def check_if_someone_fell_in_battle(self) -> None:
        if self.p1["hp"] <= 0:
            self.p1["hp"] = 0

        if self.p2["hp"] <= 0:
            self.p2["hp"] = 0

    def player_vs_player(self) -> None:
        self.fight()
        self.check_if_someone_fell_in_battle()


def pvp(p1: dict, p2: dict) -> None:
    battle = Pvp(p1, p2)
    battle.player_vs_player()
