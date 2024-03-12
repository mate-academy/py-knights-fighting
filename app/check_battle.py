class Knight:
    def __init__(self, hp: int, power: int, protection: int):
        self.hp = hp
        self.power = power
        self.protection = protection


def check_loser(fighter_hp: int) -> int:
    if fighter_hp <= 0:
        fighter_hp = 0
    return fighter_hp


def fight(first_fighter: Knight, second_fighter: Knight) -> None:
    first_fighter.hp -= second_fighter.power - first_fighter.protection
    second_fighter.hp -= first_fighter.power - second_fighter.protection

    first_fighter.hp = check_loser(first_fighter.hp)
    second_fighter.hp = check_loser(second_fighter.hp)
