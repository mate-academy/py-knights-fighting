class Knight:
    def __init__(self, hp: int, power: int, protection: int) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection


def check_loser(fighter_hp: int) -> int:
    if fighter_hp <= 0:
        fighter_hp = 0
    return fighter_hp


def fight(fighter_1: Knight, fighter_2: Knight) -> None:
    fighter_1.hp -= fighter_2.power - fighter_1.protection
    fighter_2.hp -= fighter_1.power - fighter_2.protection

    fighter_1.hp = check_loser(fighter_1.hp)
    fighter_2.hp = check_loser(fighter_2.hp)
