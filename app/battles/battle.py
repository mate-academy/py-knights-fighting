from app.knights.knight import Knight


class Battle:
    def __init__(self, knights_config: dict) -> None:
        self.knight1 = knight1
        self.knight2 = knight2
        self.knight3 = knight3
        self.knight4 = knight4
        self.knights = [knight1, knight2, knight3, knight4]

    def to_battle(self):
        for knight in self.knights:
            if knight.potion is not None:
                if "power" in knight.potion.effect:
                    knight.power += knight.potion.effect["power"]

                if "protection" in knight.potion.effect:
                    knight.protection += knight.potion.effect["protection"]

                if "hp" in knight.potion.effect:
                    knight.hp += knight.potion.effect["hp"]

        # -------------------------------------------------------------------------------
        # BATTLE:

        # 1 Lancelot vs Mordred:
        self.knight1.hp -= self.knight2.power - self.knight1.protection
        self.knight2.hp -= self.knight1.power - self.knight2.protection
        self.knight3.hp -= self.knight4.power - self.knight3.protection
        self.knight4.hp -= self.knight3.power - self.knight4.protection

        # check if someone fell in battle
        if self.knight1.hp <= 0:
            self.knight1.hp = 0

        if self.knight2.hp <= 0:
            self.knight2.hp = 0

        if self.knight3.hp <= 0:
            self.knight3.hp = 0

        if self.knight4.hp <= 0:
            self.knight4.hp = 0

        # Return battle results:
        return {
            self.knight1.name: self.knight1.hp,
            self.knight3.name: self.knight3.hp,
            self.knight2.name: self.knight2.hp,
            self.knight4.name: self.knight4.hp,

        }
