from app.knight.main import Knight


class Battle:
    results = {}

    def __init__(self) -> None:
        pass

    @classmethod
    def start_battle(cls, knight1: Knight, knight2: Knight) -> None:
        knight1.take_hit(knight2.power)
        knight2.take_hit(knight1.power)
        cls.results[knight1.name] = knight1.hp
        cls.results[knight2.name] = knight2.hp

    @classmethod
    def get_results(cls) -> dict:
        return cls.results
