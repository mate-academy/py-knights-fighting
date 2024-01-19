from app.knight import Knight


class Arena(Knight):
    __knights = {}

    @classmethod
    def battling(cls, pair: list | tuple) -> None:
        name1, name2 = pair
        knight1 = cls.__knights[name1]
        knight2 = cls.__knights[name2]

        knight1.hit(knight2)
        knight2.hit(knight1)

    @classmethod
    def equip_knights(cls, knights_config: dict) -> dict:
        cls.__knights = {
            name: Knight(config)
            for name, config
            in knights_config.items()
        }
        return cls.__knights

    @classmethod
    def get_statistics(cls) -> dict:
        return {
            config.name: config.hp
            for config in cls.__knights.values()
        }
