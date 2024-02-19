class Pvp:
    def __init__(self,player_1, player_2) -> None:
        self.player_1 = player_1
        self.player_2 = player_2

    def fight(self):
        self.player_1["hp"] -= self.player_2["power"] - self.player_1["protection"]
        self.player_2["hp"] -= self.player_1["power"] - self.player_2["protection"]

    def check_if_someone_fell_in_battle(self):
        if self.player_1["hp"] <= 0:
            self.player_1["hp"] = 0

        if self.player_2["hp"] <= 0:
            self.player_2["hp"] = 0

    def player_vs_player(self):
        self.fight()
        self.check_if_someone_fell_in_battle()

def pvp(player_1, player_2):
    battle = Pvp(player_1, player_2)
    battle.player_vs_player()