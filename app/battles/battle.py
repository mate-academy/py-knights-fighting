





class BattleSimulator:

    def __init__(self, lancelot: object, arthur: object, mordred: object,
                 red_knight: object) -> None:
        self.lancelot = lancelot
        self.mordred = mordred
        self.arthur = arthur
        self.red_knight = red_knight

    def fight(self, knight1: object,
                                      knight2: object) -> None:
        damage_to_k1 = max(0, knight2.power - knight1.protection)
        damage_to_k2 = max(0, knight1.power - knight2.protection)

        knight1.hp -= damage_to_k1
        knight2.hp -= damage_to_k2


        if knight1.hp < 0:
            knight1.hp = 0

        if knight2.hp < 0:
            knight2.hp = 0

    def start_fight(self) -> dict:
        self.conduct_one_on_one_battle(self.lancelot, self.mordred)

        self.conduct_one_on_one_battle(self.arthur, self.red_knight)

        return {
            self.lancelot.name: self.lancelot.hp,
            self.arthur.name: self.arthur.hp,
            self.mordred.name: self.mordred.hp,
            self.red_knight.name: self.red_knight.hp,
        }
