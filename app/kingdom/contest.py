from datetime import date

from app.people.knight import Knight


class Contest:
    def __init__(self, date: date, king: str, knights: dict) -> None:
        self.date = date
        self.king = king
        self.knights = knights
        print(f"On the {date} Fight contest of {len(knights)} "
              f"knights was created by King {king}")

    def prepare_for_battle(self) -> None:
        for fighter in self.knights.values():
            fighter.protection = 0
            for arm in fighter.armour:
                fighter.protection += arm["protection"]
            fighter.power += fighter.weapon["power"]
            if fighter.potion is not None:
                if "power" in fighter.potion["effect"]:
                    fighter.power += fighter.potion["effect"]["power"]

                if "protection" in fighter.potion["effect"]:
                    fighter.protection +=\
                        fighter.potion["effect"]["protection"]

                if "hp" in fighter.potion["effect"]:
                    fighter.hp += fighter.potion["effect"]["hp"]

            print(f"Knight {fighter.name} is ready to battle.")

    def battle(self, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        print(f"Knight {knight1.name} and Knight {knight2.name} are fighting")

        # check if someone fell in battle
        if knight1.hp <= 0:
            knight1.hp = 0
            print(knight1.name, "is dead.")

        if knight2.hp <= 0:
            knight2.hp = 0
            print(knight2.name, "is dead.")

    def get_battle_results(self) -> dict:
        results = dict()
        for fighter in self.knights.values():
            print(fighter.name, fighter.hp)
            results[fighter.name] = fighter.hp

        return results
