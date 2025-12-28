from app.fighters.knights import Knights


class BattleAction:

    @staticmethod
    def battle_preparations(knights_instances: list[Knights]) -> None:
        for knight in knights_instances:
            knight.protection = knight.armour
            knight.power += knight.weapon["power"]
            if knight.potion:
                if knight.potion["effect"].get("hp"):
                    knight.hp += knight.potion["effect"]["hp"]
                if knight.potion["effect"].get("power"):
                    knight.power += knight.potion["effect"]["power"]
                if knight.potion["effect"].get("protection"):
                    knight.protection += knight.potion["effect"]["protection"]

    @staticmethod
    def knights_fight(knights_1: Knights, knights_2: Knights) -> None:
        knights_1.hp -= knights_2.power - knights_1.protection
        knights_2.hp -= knights_1.power - knights_2.protection
        if knights_1.hp <= 0:
            knights_1.hp = 0
        if knights_2.hp <= 0:
            knights_2.hp = 0

    @staticmethod
    def battle_result(knights: list[Knights]) -> dict:
        return {
            knight.name: knight.hp
            for knight in knights
        }
