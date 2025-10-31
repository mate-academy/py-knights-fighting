from app.gameplay.knight import Knight


class Logic:

    @staticmethod
    def fight(fighter: Knight, second_fighter: Knight) -> None:
        damage = second_fighter.power - fighter.protection
        if damage > 0:
            fighter.hp -= damage

        damage = fighter.power - second_fighter.protection
        if damage > 0:
            second_fighter.hp -= damage

        if fighter.hp <= 0:
            fighter.hp = 0

        if second_fighter.hp <= 0:
            second_fighter.hp = 0

    @staticmethod
    def prepare_to_battle(fighter: Knight) -> None:
        fighter.apply_armour()
        fighter.apply_weapon()
        fighter.apply_potion()
