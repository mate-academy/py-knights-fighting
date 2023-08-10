from app.Knights import Knight


class Battle:
    @staticmethod
    def make_ready_2_battle(knights_dic: dict[Knight]) -> None:
        for knight in knights_dic.values():
            if knight.potion:
                knight.potion_effect()
            knight.apply_armour()
            knight.add_weapon(knight.weapon)
            knight.apply_weapon()

    @staticmethod
    def make_fight(knights: dict[Knight]) -> dict:
        # 1 Lancelot vs Mordred:
        knights["Lancelot"].hp -= (
            knights["Mordred"].power - knights["Lancelot"].protection
        )
        knights["Mordred"].hp -= (
            knights["Lancelot"].power - knights["Mordred"].protection
        )

        # 2 Arthur vs Red Knight:
        knights["Arthur"].hp -= (
            knights["Red Knight"].power - knights["Arthur"].protection
        )
        knights["Red Knight"].hp -= (
            knights["Arthur"].power - knights["Red Knight"].protection
        )

    @staticmethod
    def is_anyone_alive(knights: dict[Knight]) -> None:
        for fighter in knights.values():
            if fighter.hp <= 0:
                fighter.hp = 0

    @staticmethod
    def return_result(knights: dict[Knight]) -> dict:
        return {
            "Lancelot": knights["Lancelot"].hp,
            "Arthur": knights["Arthur"].hp,
            "Mordred": knights["Mordred"].hp,
            "Red Knight": knights["Red Knight"].hp,
        }
