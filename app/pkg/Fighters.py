class Fighters:
    list_fighters = []

    def __init__(self, name: str, hp: int, power: int,
                 protection: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
        Fighters.list_fighters.append(self)

    @staticmethod
    def check_damage() -> None:
        for i in range(4):
            fighter = Fighters.list_fighters[i]
            if fighter.hp <= 0:
                fighter.hp = 0

    @staticmethod
    def battle_vs() -> dict:
        lancelot = Fighters.list_fighters[0]
        arthur = Fighters.list_fighters[1]
        mordred = Fighters.list_fighters[2]
        red_knight = Fighters.list_fighters[3]

        # 1 Lancelot vs Mordred:
        lancelot.hp -= mordred.power - lancelot.protection
        mordred.hp -= lancelot.power - mordred.protection

        # 2 Arthur vs Red Knight:
        arthur.hp -= red_knight.power - arthur.protection
        red_knight.hp -= arthur.power - red_knight.protection

        # Check hp
        Fighters.check_damage()

        # result
        return {
            lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp
        }
