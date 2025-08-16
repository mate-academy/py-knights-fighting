from app.config.knights import Knight


class BattleSimulator:
    def __init__(self, lancelot: Knight, arthur: Knight,
                 mordred: Knight, red_knight: Knight) -> None:
        self.lancelot = lancelot
        self.arthur = arthur
        self.mordred = mordred
        self.red_knight = red_knight

    def fight(self, fighter1: str, fighter2: str) -> None:
        k1 = getattr(self, fighter1)
        k2 = getattr(self, fighter2)

        protection2 = sum(item["protection"] for item in k2.armour)

        damage_to_k1 = max(0, k2.power - protection2)
        damage_to_k2 = max(0, k1.power - protection2)

        k1.hp = max(0, k1.hp - damage_to_k1)
        k2.hp = max(0, k2.hp - damage_to_k2)

    def start_fight(self) -> dict:
        self.fight("lancelot", "mordred")
        self.fight("arthur", "red_knight")

        return {
            self.lancelot.name: self.lancelot.hp,
            self.arthur.name: self.arthur.hp,
            self.mordred.name: self.mordred.hp,
            self.red_knight.name: self.red_knight.hp,
        }
