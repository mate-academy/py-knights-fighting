from app.khight_module.khight import Knight


class Battle:

    result_of_all_battle = {}

    def __init__(self, fighter_one: Knight, fighter_two: Knight) -> None:
        self.fighter_one = Knight(fighter_one)
        self.fighter_two = Knight(fighter_two)
        self.fighter_one.get_ready_to_battle()
        self.fighter_two.get_ready_to_battle()

    def battle_begins(self) -> None:
        self.fighter_one.hp -= (
            self.fighter_two.power
            - self.fighter_one.protection
        )
        self.fighter_two.hp -= (
            self.fighter_one.power
            - self.fighter_two.protection
        )
        if self.fighter_one.hp <= 0:
            self.fighter_one.hp = 0
        elif self.fighter_two.hp <= 0:
            self.fighter_two.hp = 0

        for fighter in [self.fighter_one, self.fighter_two]:
            Battle.result_of_all_battle[fighter.name] = fighter.hp
