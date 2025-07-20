class Arena:

    @staticmethod
    def fight(knights: list, fighters_pair: tuple) -> dict:
        knight1 = next(knight for knight in knights
                       if knight.name == fighters_pair[0])
        knight2 = next(knight for knight in knights
                       if knight.name == fighters_pair[1])

        knight1_hp = max(0, knight1.hp - max(0, (knight2.power - knight1.protection)))
        knight2_hp = max(0, knight2.hp - max(0, (knight1.power - knight2.protection)))

        return {
            knight1.name: knight1_hp,
            knight2.name: knight2_hp
        }

    @staticmethod
    def get_results(knights: list, fighters: list) -> dict:
        results = {}
        for fighters_pair in fighters:
            results.update(Arena.fight(knights, fighters_pair))

        return results
