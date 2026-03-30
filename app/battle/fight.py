from app.fighters.perks import Perk
from app.fighters.knight import Knight


class Fight:
    @staticmethod
    def fight(first_fighter: Knight, second_fighter: Knight) -> None:
        print("Fighters stat:")
        print(
            f"{first_fighter.name} hp: {first_fighter.hp}, "
            f"power: {first_fighter.power}, "
            f"protection: {first_fighter.protection}"
        )
        print(
            f"{second_fighter.name} hp: {second_fighter.hp}, "
            f"power: {second_fighter.power}, "
            f"protection: {second_fighter.protection}"
        )
        print("---")

        Perk.apply_all_perks(first_fighter)
        Perk.apply_all_perks(second_fighter)

        first_fighter.hp -= second_fighter.power - first_fighter.protection
        second_fighter.hp -= first_fighter.power - second_fighter.protection

        if first_fighter.hp <= 0:
            first_fighter.hp = 0
        if second_fighter.hp <= 0:
            second_fighter.hp = 0

        print("BATTLE RESULT:")
        if first_fighter.hp > second_fighter.hp:
            print(f"{first_fighter.name.upper()} win!")
        elif first_fighter.hp < second_fighter.hp:
            print(f"{second_fighter.name.upper()} win!")
        else:
            print("draw!")
        print("------------------")
