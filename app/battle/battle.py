from app.human.knight import Knight


class Battle:
    start = "let the battle begin!!!"


    @staticmethod
    def lancelot_vs_mordred(lancelot: "Knight", mordred: "Knight"):
        lancelot.hp -= mordred.power - lancelot.armor.power
        if lancelot.hp <= 0:
            lancelot.hp = 0
        if mordred.hp <= 0:
            mordred.hp = 0


    @staticmethod
    def arthur_vs_red_knight(arthur: "Knight", red_knight: "Knight"):
        arthur.hp -= red_knight.power - arthur.armor.power
        if arthur.hp <= 0:
            arthur.hp = 0
        if red_knight.hp <= 0:
            red_knight.hp = 0
