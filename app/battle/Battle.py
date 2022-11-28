from app.models.Knight import Knight


class Battle:

    @classmethod
    def battle(cls, knights_config: dict) -> dict:
        lancelot = Knight(knights_config["lancelot"]).knight_adjusting()
        arthur = Knight(knights_config["arthur"]).knight_adjusting()
        mordred = Knight(knights_config["mordred"]).knight_adjusting()
        red_knight = Knight(knights_config["red_knight"]).knight_adjusting()

        # -------------------------------------------------------------------------------
        # BATTLE:

        # 1 Lancelot vs Mordred:
        lancelot.hp -= mordred.power - lancelot.protection
        mordred.hp -= lancelot.power - mordred.protection
        # check if someone fell in battle
        if lancelot.hp <= 0:
            lancelot.hp = 0
        if mordred.hp <= 0:
            mordred.hp = 0

        # 2 Arthur vs Red Knight:
        arthur.hp -= red_knight.power - arthur.protection
        red_knight.hp -= arthur.power - red_knight.protection

        # check if someone fell in battle
        if arthur.hp <= 0:
            arthur.hp = 0
        if red_knight.hp <= 0:
            red_knight.hp = 0

        # Return battle results:
        return {
            lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp,
        }
