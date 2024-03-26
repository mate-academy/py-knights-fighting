class Battle:
    def __init__(self, knight1, knight2):
        self.knight1 = knight1
        self.knight2 = knight2

    def perform_battle(self):
        print("Fight!")
        print(f"{self.knight1.name} against {self.knight2.name}")

        while self.knight1.hp > 0 and self.knight2.hp > 0:
            print(f"{self.knight1.name} has {self.knight1.hp} life")
            print(f"{self.knight2.name} has {self.knight2.hp} life")

            damage_knight1 = self.knight1.power - self.knight2.defense
            damage_knight2 = self.knight2.power - self.knight1.defense

            self.knight1.hp -= damage_knight2
            self.knight2.hp -= damage_knight1

        winner = self.knight1 if self.knight1.hp > 0 else self.knight2
        print(f"Finished! {winner.name} winner!")