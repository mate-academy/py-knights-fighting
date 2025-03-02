from .fighter import Fighter


class Battle:
    def __init__(self, fighter: "Fighter", opponent: "Fighter") -> None:
        self.fighter = fighter
        self.opponent = opponent

    def fight(self) -> None:
        self.fighter.hp -= max(
            0, self.opponent.power - self.fighter.protection
        )
        self.opponent.hp -= max(
            0, self.fighter.power - self.opponent.protection
        )

        # check if someone fell in knight_fighting
        if self.fighter.hp < 0:
            self.fighter.reset_health_points()

        if self.opponent.hp < 0:
            self.opponent.reset_health_points()
