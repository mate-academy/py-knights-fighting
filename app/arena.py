from app.knight import Knight


class Arena(Knight):
    __knights = {}

    @classmethod
    def fighting(cls, pair: list | tuple) -> None:
        name1, name2 = pair
        knight1 = cls.__knights[name1]
        knight2 = cls.__knights[name2]

        if knight1.hp > 0 and knight2.hp > 0:
            knight1.hp = max(
                knight1.hp - (knight2.power - knight1.protection), 0
            )
            knight2.hp = max(
                knight2.hp - (knight1.power - knight2.protection), 0
            )
        else:
            print("Dead knights can't fight!")

    @classmethod
    def equip_knights(cls, knights_config: dict) -> dict:
        cls.__knights = {
            name: Knight(config)
            for name, config
            in knights_config.items()
        }
        return cls.__knights
