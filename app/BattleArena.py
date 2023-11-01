

class BattleArena:

    @staticmethod
    def check_hp(warriors: list) -> None:
        for warrior in warriors:
            if warrior.hp <= 0:
                print(f"{warrior.name} was defeated!")
                warrior.hp = 0

    @staticmethod
    def fight(warriors: list) -> dict:
        for warrior in warriors:
            warrior.get_ready_to_battle()

        warriors[0].hp -= warriors[1].power - warriors[0].protection
        warriors[1].hp -= warriors[0].power - warriors[1].protection
        warriors[2].hp -= warriors[3].power - warriors[2].protection
        warriors[3].hp -= warriors[2].power - warriors[3].protection

        BattleArena.check_hp(warriors)

        return {
            warriors[0].name: warriors[0].hp,
            warriors[1].name: warriors[1].hp,
            warriors[2].name: warriors[2].hp,
            warriors[3].name: warriors[3].hp,
        }
